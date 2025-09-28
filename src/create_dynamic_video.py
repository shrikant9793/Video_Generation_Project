import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import cv2

# === Configuration ===
PHOTO_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\photo.png"
VOICE_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\voice_recording.wav"
TEXT_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\intro_text.txt"
OUTPUT_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\output\shrikanth_intro.mp4"
VIDEO_SIZE = (1280, 720)  # HD resolution
FONT_SIZE = 48
FONT_COLOR = "white"
FONT_PATH = "arial.ttf"

def load_intro_text(file_path):
    """Read intro text from file and split into sentences"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    # Split by sentences for better timing
    sentences = [s.strip() for s in text.replace('\n', ' ').split('.') if s.strip()]
    return sentences

def create_animated_text_clip(text, duration, start_time, position="center", fontsize=FONT_SIZE):
    """Create animated text using PIL-generated images"""
    # Create text image using PIL
    text_img = create_text_image_pil(text, fontsize=fontsize, color='white')
    text_array = np.array(text_img)
    
    # Create ImageClip from numpy array
    txt_clip = ImageClip(text_array, transparent=True)
    txt_clip = txt_clip.set_start(start_time).set_duration(duration)
    txt_clip = txt_clip.set_position(position)
    
    # Add fade effects
    fade_duration = 0.5
    txt_clip = txt_clip.fadein(fade_duration).fadeout(fade_duration)
    
    return txt_clip

def create_text_image_pil(text, fontsize=FONT_SIZE, color='white'):
    """Create text image using PIL"""
    # Create transparent image
    img = Image.new("RGBA", (VIDEO_SIZE[0]-100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Try to load font
    try:
        font = ImageFont.truetype("arial.ttf", fontsize)
    except:
        font = ImageFont.load_default()
    
    # Get text size and center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, font=font, fill=color)
    
    return img

def create_background_clip(duration):
    """Create animated background with gradient effect"""
    # Create a gradient background that changes over time
    def make_frame(t):
        # Create gradient from dark blue to lighter blue
        gradient = np.zeros((VIDEO_SIZE[1], VIDEO_SIZE[0], 3), dtype=np.uint8)
        
        # Animate gradient based on time
        progress = t / duration
        blue_intensity = int(30 + progress * 50)  # 30 to 80
        
        for y in range(VIDEO_SIZE[1]):
            # Create vertical gradient
            intensity = int(blue_intensity * (1 - y / VIDEO_SIZE[1]))
            gradient[y, :] = [intensity//3, intensity//2, intensity]
        
        return gradient
    
    return VideoClip(make_frame, duration=duration)

def create_photo_animation_clip(photo_path, duration):
    """Create dynamic photo animation with zoom and pan effects"""
    # Load photo
    photo_clip = ImageClip(photo_path)
    
    # Resize to fit video while maintaining aspect ratio
    photo_clip = photo_clip.resize(height=VIDEO_SIZE[1])
    
    # Create Ken Burns effect (zoom + pan)
    def zoom_effect(get_frame, t):
        frame = get_frame(t)
        zoom_factor = 1 + 0.1 * (t / duration)  # Gradual zoom from 1.0 to 1.1
        
        # Calculate new dimensions
        h, w = frame.shape[:2]
        new_h, new_w = int(h * zoom_factor), int(w * zoom_factor)
        
        # Resize frame
        frame_resized = cv2.resize(frame, (new_w, new_h))
        
        # Crop to original size (pan effect)
        start_y = (new_h - h) // 2
        start_x = (new_w - w) // 2
        
        return frame_resized[start_y:start_y+h, start_x:start_x+w]
    
    photo_clip = photo_clip.fl(zoom_effect)
    photo_clip = photo_clip.set_duration(duration)
    
    # Position photo (offset to one side to make room for text)
    photo_clip = photo_clip.set_position(('left', 'center'))
    
    return photo_clip

def create_title_clip(text, duration, start_time):
    """Create animated title with special effects using PIL"""
    # Create title image with special styling
    title_img = create_text_image_pil(text, fontsize=72, color='#FFD700')
    title_array = np.array(title_img)
    
    title_clip = ImageClip(title_array, transparent=True)
    title_clip = title_clip.set_start(start_time).set_duration(duration)
    title_clip = title_clip.set_position(('center', 100))
    
    # Add special effects
    title_clip = title_clip.fadein(1.0).fadeout(0.5)
    
    return title_clip

def create_bouncing_element(text, duration, start_time, bounce_position):
    """Create bouncing animated element using PIL"""
    def bounce_position_func(t):
        # Create bouncing effect
        bounce_cycle = 2  # seconds per bounce
        phase = (t % bounce_cycle) / bounce_cycle * 2 * np.pi
        bounce_offset = 20 * np.sin(phase)
        return ('center', bounce_position + bounce_offset)
    
    # Create text image using PIL
    bounce_img = create_text_image_pil(text, fontsize=36, color='#00FF00')
    bounce_array = np.array(bounce_img)
    
    bounce_clip = ImageClip(bounce_array, transparent=True)
    bounce_clip = bounce_clip.set_start(start_time).set_duration(duration)
    bounce_clip = bounce_clip.set_position(bounce_position_func)
    
    return bounce_clip

def main():
    print("🎬 Creating dynamic intro video...")
    
    # Load voice and get duration
    audio_clip = AudioFileClip(VOICE_PATH)
    audio_duration = audio_clip.duration
    print(f"📊 Audio duration: {audio_duration:.2f} seconds")
    
    # Load and parse intro text
    sentences = load_intro_text(TEXT_PATH)
    print(f"📝 Loaded {len(sentences)} sentences")
    
    # Create background
    background = create_background_clip(audio_duration)
    
    # Create photo animation
    photo_clip = create_photo_animation_clip(PHOTO_PATH, audio_duration)
    
    # Create title
    title = create_title_clip("Hello! I'm Shrikanth", 3.0, 0)
    
    # Create animated text clips for each sentence
    text_clips = []
    time_per_sentence = (audio_duration - 4) / len(sentences)  # Leave time for title
    
    for i, sentence in enumerate(sentences):
        start_time = 3.5 + i * time_per_sentence
        duration = time_per_sentence - 0.5  # Small gap between sentences
        
        # Create animated text
        text_clip = create_animated_text_clip(
            sentence, duration, start_time, 
            position=('center', 200 + i * 80)
        )
        text_clips.append(text_clip)
    
    # Create bouncing skill elements
    skills = ["Python Developer", "Data Analysis", "Machine Learning", "Cloud Technologies"]
    skill_clips = []
    
    for i, skill in enumerate(skills):
        start_time = 8 + i * 1.5
        skill_clip = create_bouncing_element(
            f"• {skill}", 1.0, start_time, 
            bounce_position=500 + i * 40
        )
        skill_clips.append(skill_clip)
    
    # Create closing message
    closing = create_animated_text_clip(
        "Thank you for watching!", 2.0, 
        audio_duration - 2.5, 
        position=('center', 600),
        fontsize=56
    )
    
    # Combine all clips
    all_clips = [background, photo_clip, title] + text_clips + skill_clips + [closing]
    
    # Create final composite
    final_clip = CompositeVideoClip(all_clips, size=VIDEO_SIZE)
    final_clip = final_clip.set_audio(audio_clip)
    final_clip = final_clip.set_fps(24)
    
    # Ensure output folder exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    print("🎥 Rendering video...")
    # Export video with high quality
    final_clip.write_videofile(
        OUTPUT_PATH, 
        fps=24, 
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True
    )
    
    print(f"✅ Dynamic video created successfully!")
    print(f"📁 Output: {OUTPUT_PATH}")
    print(f"⏱️  Duration: {audio_duration:.2f} seconds")
    print(f"📐 Resolution: {VIDEO_SIZE[0]}x{VIDEO_SIZE[1]}")

if __name__ == "__main__":
    main()
