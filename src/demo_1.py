from moviepy.editor import VideoClip, TextClip, CompositeVideoClip

# Video settings
duration = 5  # seconds
video_size = (640, 360)
bg_color = (30, 144, 255)  # Dodger Blue

# Create a background clip
background = VideoClip(lambda t: bg_color, duration=duration).set_duration(duration).set_fps(24).set_size(video_size)

# Create a moving text clip
def make_text(t):
    txt = TextClip(f"Hello, World! {int(t)}s", fontsize=50, color='white', font='Arial-Bold')
    txt = txt.set_position(('center', int(100 + 100*t)))  # move downward over time
    txt = txt.set_duration(duration)
    return txt

text_clips = [make_text(t) for t in range(duration)]

# Combine background and text
final = CompositeVideoClip([background] + text_clips).set_duration(duration)

# Write to a file
final.write_videofile("output_video.mp4", codec="libx264", fps=24)