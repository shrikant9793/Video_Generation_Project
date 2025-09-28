from moviepy.editor import ColorClip, CompositeVideoClip
import numpy as np

# Video settings
duration = 5  # seconds
video_size = (640, 360)
bg_color = (30, 144, 255)  # Dodger Blue

# Create a background clip
background = ColorClip(size=video_size, color=bg_color, duration=duration)

# Create a simple moving rectangle instead of text (to avoid ImageMagick dependency)
def make_moving_shape(t):
    # Create a simple colored rectangle that moves
    shape_clip = ColorClip(size=(200, 50), color=(255, 255, 255), duration=1)
    shape_clip = shape_clip.set_position(('center', int(100 + 100*t)))
    shape_clip = shape_clip.set_start(t)
    return shape_clip

moving_shapes = [make_moving_shape(t) for t in range(duration)]

# Combine background and shapes
final = CompositeVideoClip([background] + moving_shapes).set_duration(duration)

# Write to a file
final.write_videofile("output_video.mp4", codec="libx264", fps=24)