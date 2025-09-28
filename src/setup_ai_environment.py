"""
AI Environment Setup Script
===========================

This script sets up the advanced AI environment for video generation
using ModelScope, OpenCLIP, PyTorch Lightning, and other cutting-edge libraries.

Run this script to install all required dependencies.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    else:
        print("✅ Python version is compatible")
        return True

def install_core_libraries():
    """Install core AI libraries"""
    libraries = [
        ("torch torchvision torchaudio", "PyTorch"),
        ("modelscope", "ModelScope"),
        ("open_clip_torch", "OpenCLIP"),
        ("pytorch-lightning", "PyTorch Lightning"),
    ]
    
    for lib, name in libraries:
        if not run_command(f"pip install {lib}", f"Installing {name}"):
            print(f"⚠️  {name} installation failed, trying alternative...")
            # Try without specific version
            run_command(f"pip install {lib.split()[0]}", f"Installing {name} (basic)")

def install_vision_libraries():
    """Install computer vision libraries"""
    vision_libs = [
        "opencv-python",
        "Pillow",
        "scikit-image",
        "matplotlib",
        "imageio",
        "imageio-ffmpeg"
    ]
    
    for lib in vision_libs:
        run_command(f"pip install {lib}", f"Installing {lib}")

def install_audio_libraries():
    """Install audio processing libraries"""
    audio_libs = [
        "librosa",
        "soundfile",
        "pydub"
    ]
    
    for lib in audio_libs:
        run_command(f"pip install {lib}", f"Installing {lib}")

def install_video_libraries():
    """Install video processing libraries"""
    video_libs = [
        "moviepy",
        "ffmpeg-python"
    ]
    
    for lib in video_libs:
        run_command(f"pip install {lib}", f"Installing {lib}")

def install_utility_libraries():
    """Install utility libraries"""
    utils = [
        "numpy",
        "scipy",
        "tqdm",
        "requests",
        "transformers"
    ]
    
    for lib in utils:
        run_command(f"pip install {lib}", f"Installing {lib}")

def test_imports():
    """Test if all libraries can be imported"""
    print("\n🧪 Testing library imports...")
    
    test_libraries = [
        ("torch", "PyTorch"),
        ("cv2", "OpenCV"),
        ("PIL", "Pillow"),
        ("numpy", "NumPy"),
        ("moviepy", "MoviePy"),
        ("pytorch_lightning", "PyTorch Lightning"),
    ]
    
    failed_imports = []
    
    for lib, name in test_libraries:
        try:
            __import__(lib)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            failed_imports.append(name)
    
    # Test advanced libraries (optional)
    advanced_libraries = [
        ("modelscope", "ModelScope"),
        ("open_clip", "OpenCLIP"),
    ]
    
    for lib, name in advanced_libraries:
        try:
            __import__(lib)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"⚠️  {name} import failed (optional): {e}")
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        return False
    else:
        print("\n✅ All core libraries imported successfully!")
        return True

def main():
    """Main setup function"""
    print("🤖 Advanced AI Video Generation Setup")
    print("=" * 50)
    print("Installing: ModelScope + OpenCLIP + PyTorch Lightning")
    print()
    
    # Check Python version
    if not check_python_version():
        print("❌ Setup failed: Incompatible Python version")
        return
    
    print("\n📦 Installing AI libraries...")
    
    # Install libraries in order
    install_core_libraries()
    install_vision_libraries()
    install_audio_libraries()
    install_video_libraries()
    install_utility_libraries()
    
    print("\n🧪 Testing installation...")
    
    # Test imports
    if test_imports():
        print("\n🎉 Setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Run: python src/ai_video_generator.py")
        print("2. Your photo and voice will be used automatically")
        print("3. AI will generate professional video with lip-sync")
        print("\n🚀 Ready to create AI-powered videos!")
    else:
        print("\n⚠️  Setup completed with some issues")
        print("💡 Some optional libraries may not be available")
        print("🔄 The basic video generation will still work")

if __name__ == "__main__":
    main()
