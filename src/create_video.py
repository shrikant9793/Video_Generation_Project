import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
from pydub import AudioSegment

path = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\voice_recording.wav"


# === Configuration ===
PHOTO_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\photo.png"
VOICE_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\voice_recording.wav"
TEXT_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\intro_text.txt"
OUTPUT_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\output\new_firstname_lastname_intro.mp4"
VIDEO_SIZE = (1280, 720)  # HD resolution
FONT_SIZE = 40
FONT_COLOR = "white"
FONT_PATH = "arial.ttf"  # default Windows font

audio_clip = AudioFileClip(VOICE_PATH)

# ====================== Functions ======================
def load_intro_text(file_path):
    """Read intro text from file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def make_text_image(text, size=VIDEO_SIZE, fontsize=FONT_SIZE, fontcolor=FONT_COLOR, font_path=FONT_PATH):
    """Create an image with text using Pillow"""
    img = Image.new("RGBA", size, (0, 0, 0, 0))  # transparent background
    draw = ImageDraw.Draw(img)

    # Try to load the font
# Try to load the font
try:
    font = ImageFont.truetype(font_path, fontsize)
except:
    font = ImageFont.load_default()

# Helper function to get text size
def get_text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

    lines = []
    words = text.split()
    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        w, h = get_text_size(draw, test_line, font)
        if w <= size[0] - 40:  # 20px margin
            line = test_line
        else:
            lines.append(line)
            line = word
    lines.append(line)

    # Draw lines centered vertically
    total_h = sum([get_text_size(draw, l, font)[1] for l in lines])
    current_h = (size[1] - total_h) // 2
    for l in lines:
        w, h = get_text_size(draw, l, font)
        draw.text(((size[0]-w)//2, current_h), l, font=font, fill=fontcolor)
        current_h += h


# ====================== Main ======================
def main():
    # Load voice
    audio_clip = AudioFileClip(VOICE_PATH)
    audio_duration = audio_clip.duration

    # Load photo and apply slow zoom (Ken Burns effect)
    image_clip = ImageClip(PHOTO_PATH).set_duration(audio_duration)
    image_clip = image_clip.resize(height=VIDEO_SIZE[1])
    image_clip = image_clip.fx(lambda clip: clip.resize(lambda t: 1 + 0.05 * t / audio_duration))

    # Load intro text
    intro_text = load_intro_text(TEXT_PATH)

    # Create text image clip
    text_clip = make_text_image(intro_text, size=image_clip.size)
    text_clip = text_clip.set_duration(audio_duration).set_position("center")

    # Combine photo + text + audio
    final_clip = CompositeVideoClip([image_clip, text_clip])
    final_clip = final_clip.set_audio(audio_clip)

    # Ensure output folder exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # Export video
    final_clip.write_videofile(OUTPUT_PATH, fps=24)

    print(f"✅ Video exported successfully at {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
