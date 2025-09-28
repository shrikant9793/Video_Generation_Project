"""
Enhanced AI Video Processor
==========================

This script enhances AI-generated lip-sync videos (from D-ID, HeyGen, etc.)
by adding professional effects, backgrounds, and styling.

Usage:
1. Generate lip-sync video using D-ID/HeyGen/Synthesia
2. Run this script to enhance it with professional effects
3. Get final professional intro video

Requirements:
- AI-generated lip-sync video (from D-ID, etc.)
- Original assets (photo, audio, text)
"""

import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import cv2

# === Configuration ===
AI_LIPSYNC_VIDEO = "output/shrikanth_lip_sync_base.mp4"  # From D-ID/HeyGen
PHOTO_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\photo.png"
VOICE_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\voice_recording.wav"
TEXT_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\intro_text.txt"
OUTPUT_PATH = r"C:\Users\hp\Video_Generation_Project\Video_Generation_Project\output\shrikanth_professional_intro.mp4"
VIDEO_SIZE = (1280, 720)  # HD resolution
FONT_SIZE = 48

def load_intro_text(file_path):
    """Load and parse intro text"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    sentences = [s.strip() for s in text.replace('\n', ' ').split('.') if s.strip()]
    return sentences

def create_text_image_pil(text, fontsize=FONT_SIZE, color='white'):
    """Create text image using PIL"""
    img = Image.new("RGBA", (600, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", fontsize)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2
    
    draw.text((x, y), text, font=font, fill=color)
    return img

def create_professional_background(duration):
    """Create professional animated background"""
    def make_frame(t):
        # Create professional gradient background
        frame = np.zeros((VIDEO_SIZE[1], VIDEO_SIZE[0], 3), dtype=np.uint8)
        
        # Professional color scheme
        progress = t / duration
        
        # Dark blue to lighter blue gradient
        for y in range(VIDEO_SIZE[1]):
            intensity = int(20 + (1 - y / VIDEO_SIZE[1]) * 60)
            frame[y, :] = [intensity//4, intensity//3, intensity]
        
        # Add subtle animation
        wave_offset = int(10 * np.sin(t * 0.5))
        frame = np.roll(frame, wave_offset, axis=1)
        
        return frame
    
    return VideoClip(make_frame, duration=duration)

def add_title_overlay(text, duration, start_time):
    """Add professional title overlay"""
    title_img = create_text_image_pil(text, fontsize=64, color='#FFD700')
    title_array = np.array(title_img)
    
    title_clip = ImageClip(title_array, transparent=True)
    title_clip = title_clip.set_start(start_time).set_duration(duration)
    title_clip = title_clip.set_position(('center', 50))
    
    # Add professional effects
    title_clip = title_clip.fadein(1.5).fadeout(0.8)
    
    return title_clip

def add_text_overlays(sentences, duration, start_time):
    """Add animated text overlays"""
    text_clips = []
    time_per_sentence = (duration - start_time - 3) / len(sentences)
    
    for i, sentence in enumerate(sentences):
        sentence_start = start_time + 3 + i * time_per_sentence
        sentence_duration = time_per_sentence - 0.5
        
        text_img = create_text_image_pil(sentence, fontsize=42, color='white')
        text_array = np.array(text_img)
        
        text_clip = ImageClip(text_array, transparent=True)
        text_clip = text_clip.set_start(sentence_start).set_duration(sentence_duration)
        text_clip = text_clip.set_position(('center', 150 + i * 60))
        
        # Professional fade effects
        text_clip = text_clip.fadein(0.8).fadeout(0.8)
        text_clips.append(text_clip)
    
    return text_clips

def add_skill_highlights(duration, start_time):
    """Add animated skill highlights"""
    skills = ["Python Developer", "Data Analysis", "Machine Learning", "Cloud Technologies"]
    skill_clips = []
    
    for i, skill in enumerate(skills):
        skill_start = start_time + 8 + i * 1.2
        skill_duration = 1.0
        
        # Create bouncing effect
        def bounce_pos(t):
            bounce_cycle = 1.5
            phase = (t % bounce_cycle) / bounce_cycle * 2 * np.pi
            bounce_offset = 15 * np.sin(phase)
            return ('center', 400 + i * 50 + bounce_offset)
        
        skill_img = create_text_image_pil(f"• {skill}", fontsize=36, color='#00FF99')
        skill_array = np.array(skill_img)
        
        skill_clip = ImageClip(skill_array, transparent=True)
        skill_clip = skill_clip.set_start(skill_start).set_duration(skill_duration)
        skill_clip = skill_clip.set_position(bounce_pos)
        skill_clips.append(skill_clip)
    
    return skill_clips

def add_closing_message(duration):
    """Add professional closing message"""
    closing_img = create_text_image_pil("Thank you for watching!", fontsize=56, color='#FFD700')
    closing_array = np.array(closing_img)
    
    closing_clip = ImageClip(closing_array, transparent=True)
    closing_clip = closing_clip.set_start(duration - 3).set_duration(3)
    closing_clip = closing_clip.set_position(('center', 600))
    
    # Professional entrance effect
    closing_clip = closing_clip.fadein(1.0).fadeout(1.0)
    
    return closing_clip

def enhance_ai_video():
    """Main function to enhance AI-generated lip-sync video"""
    print("🎬 Enhancing AI-generated lip-sync video...")
    
    # Check if AI lip-sync video exists
    if not os.path.exists(AI_LIPSYNC_VIDEO):
        print(f"❌ AI lip-sync video not found: {AI_LIPSYNC_VIDEO}")
        print("💡 Please generate lip-sync video using D-ID, HeyGen, or Synthesia first")
        print("📋 Save it as: {AI_LIPSYNC_VIDEO}")
        return False
    
    # Load AI lip-sync video
    print("📹 Loading AI lip-sync video...")
    lipsync_clip = VideoFileClip(AI_LIPSYNC_VIDEO)
    duration = lipsync_clip.duration
    
    print(f"⏱️  Video duration: {duration:.2f} seconds")
    
    # Resize to standard format
    lipsync_clip = lipsync_clip.resize(VIDEO_SIZE)
    
    # Create professional background
    print("🎨 Creating professional background...")
    background = create_professional_background(duration)
    
    # Load intro text
    sentences = load_intro_text(TEXT_PATH)
    print(f"📝 Loaded {len(sentences)} sentences")
    
    # Create overlays
    print("✨ Adding professional overlays...")
    
    # Title
    title = add_title_overlay("Hello! I'm Shrikanth", 4.0, 0)
    
    # Text overlays
    text_clips = add_text_overlays(sentences, duration, 4.0)
    
    # Skill highlights
    skill_clips = add_skill_highlights(duration, 4.0)
    
    # Closing message
    closing = add_closing_message(duration)
    
    # Combine all elements
    print("🎭 Compositing final video...")
    all_clips = [background, lipsync_clip, title] + text_clips + skill_clips + [closing]
    
    final_clip = CompositeVideoClip(all_clips, size=VIDEO_SIZE)
    final_clip = final_clip.set_fps(24)
    
    # Ensure output folder exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    # Export enhanced video
    print("🎥 Rendering enhanced video...")
    final_clip.write_videofile(
        OUTPUT_PATH,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True
    )
    
    print(f"✅ Enhanced video created successfully!")
    print(f"📁 Output: {OUTPUT_PATH}")
    print(f"🎯 Features: Lip-sync + Professional effects + Animated text")
    
    return True

def main():
    """Main function"""
    print("🤖 AI Video Enhancement Tool")
    print("=" * 40)
    print("This tool enhances AI-generated lip-sync videos with professional effects")
    print()
    
    if enhance_ai_video():
        print("\n🎉 SUCCESS! Professional intro video created!")
        print("📋 Next steps:")
        print("1. Review the enhanced video")
        print("2. Submit as your final project deliverable")
        print("3. Update your project report")
    else:
        print("\n❌ Enhancement failed")
        print("💡 Make sure you have generated a lip-sync video first using:")
        print("   - D-ID (recommended)")
        print("   - HeyGen")
        print("   - Synthesia")
        print("   - Wav2Lip")

if __name__ == "__main__":
    main()
