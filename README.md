# Video Generation Project

A Python-based system for creating dynamic intro videos with photo, voice, and animated text effects.

## 🎯 Project Overview

This project creates professional intro videos by combining:
- Personal photos with Ken Burns animation effects
- Voice recordings with synchronized visual elements
- Dynamic text animations with fade effects
- Animated backgrounds and bouncing elements

## 📁 Project Structure

```
Video_Generation_Project/
├── src/
│   ├── create_dynamic_video.py    # 🎬 Main video generator (RECOMMENDED)
│   ├── create_video.py            # 📸 Basic static version
│   └── demo_1.py                  # 🧪 Simple demo
├── assets/
│   ├── photo.png                  # 📷 Your personal photo
│   ├── voice_recording.wav        # 🎤 Voice narration
│   └── intro_text.txt             # 📝 Introduction text
├── output/
│   └── shrikanth_intro.mp4        # 🎥 Final video output
├── report/
│   └── project_report.md          # 📊 Detailed project report
└── requirements.txt               # 📦 Dependencies
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv myenv

# Activate environment (Windows)
myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Prepare Your Assets

Place your files in the `assets/` folder:
- `photo.png` - Your personal photo
- `voice_recording.wav` - Your voice recording
- `intro_text.txt` - Your introduction text

### 3. Run the Video Generator

```bash
# Generate dynamic video (RECOMMENDED)
python src/create_dynamic_video.py

# Or generate basic static video
python src/create_video.py
```

## 🎬 Features

### Dynamic Video (`create_dynamic_video.py`)
- ✅ **Animated Background:** Gradient background that changes over time
- ✅ **Ken Burns Effect:** Photo with zoom and pan animation
- ✅ **Dynamic Text:** Animated text with fade in/out effects
- ✅ **Title Animation:** Special title with golden styling
- ✅ **Bouncing Elements:** Animated skill highlights
- ✅ **Synchronized Timing:** All elements timed to match audio

### Basic Video (`create_video.py`)
- ✅ **Photo + Audio:** Simple combination with text overlay
- ✅ **Text Rendering:** PIL-based text generation
- ✅ **HD Output:** 1280x720 resolution

## 📋 Requirements

### Python Dependencies
```
moviepy>=1.0.3
pillow>=10.0.0
numpy>=1.24.0
opencv-python>=4.8.0
pydub>=0.25.1
```

### System Requirements
- Python 3.8+
- Windows/Linux/MacOS
- FFmpeg (automatically handled by MoviePy)

## 🎨 Customization

### Modify Video Settings
Edit the configuration section in `create_dynamic_video.py`:

```python
# === Configuration ===
VIDEO_SIZE = (1280, 720)  # HD resolution
FONT_SIZE = 48
FONT_COLOR = "white"
OUTPUT_PATH = "your_name_intro.mp4"
```

### Customize Text Animation
```python
# Modify timing for different effects
fade_duration = 0.5  # Fade in/out duration
bounce_cycle = 2     # Bouncing speed
```

### Add Your Own Effects
```python
def custom_effect(text, duration, start_time):
    # Your custom animation code here
    pass
```

## 🔧 Troubleshooting

### Common Issues

#### 1. ImageMagick Error
**Error:** `MoviePy Error: creation of None failed`

**Solution:** The code uses PIL instead of ImageMagick, so this shouldn't occur. If it does, check your MoviePy installation.

#### 2. Audio File Issues
**Error:** `AudioFileClip` fails to load

**Solution:** Ensure your audio file is in WAV format and not corrupted.

#### 3. Memory Issues
**Error:** Out of memory during rendering

**Solution:** Reduce video resolution or duration, or close other applications.

#### 4. Slow Rendering
**Issue:** Video takes too long to render

**Solution:** Reduce video quality or complexity of effects.

## 📊 Output Specifications

- **Resolution:** 1280x720 (HD)
- **Frame Rate:** 24 FPS
- **Audio Codec:** AAC
- **Video Codec:** H.264
- **Duration:** Matches your audio recording length

## 🎯 Project Requirements Met

This project fulfills all specified requirements:

1. ✅ **Personal Photo:** Uses your own photo with animation
2. ✅ **Real Voice:** Uses your recorded voice (not AI-generated)
3. ✅ **Intro Text:** Incorporates your introduction text
4. ✅ **Proper Video:** Dynamic motion and effects (not static image)
5. ✅ **Visual Effects:** Multiple animated elements
6. ✅ **Professional Quality:** HD output with smooth animations

## 🚀 Advanced Features

### Ken Burns Effect
The photo animation includes:
- Gradual zoom (1.0x to 1.1x)
- Pan movement for visual interest
- Maintains aspect ratio

### Text Animation
- Fade in/out effects
- Centered positioning
- Multiple font sizes and colors
- Sentence-by-sentence timing

### Background Animation
- Gradient color changes
- Time-based color transitions
- Professional color scheme

## 📈 Performance Tips

1. **Optimize Assets:**
   - Use compressed images (PNG/JPG)
   - Keep audio files under 30 seconds
   - Optimize text length

2. **Rendering Settings:**
   - Use lower FPS for faster rendering
   - Reduce video resolution for testing
   - Close other applications during rendering

3. **Memory Management:**
   - Process shorter video segments
   - Use efficient data types
   - Clear unused variables

## 🤝 Contributing

Feel free to contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review the project report
3. Ensure all dependencies are installed
4. Verify your asset files are correct

---

**Created by:** Shrikanth  
**Project Type:** Video Generation with Python  
**Status:** ✅ Completed Successfully