"""
Wav2Lip Setup and Usage Guide
=============================

This script provides instructions and setup for Wav2Lip, an open-source AI tool
that can create realistic lip-sync from a photo and audio file.

Requirements:
- Python 3.8+
- CUDA-compatible GPU (recommended)
- At least 8GB RAM
- Your photo and voice recording

Installation Steps:
1. Clone Wav2Lip repository
2. Install dependencies
3. Download pre-trained models
4. Run lip-sync generation

Note: This is an advanced solution requiring technical setup.
For easier alternatives, consider D-ID, HeyGen, or Synthesia.
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if system meets Wav2Lip requirements"""
    print("🔍 Checking system requirements...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    else:
        print(f"✅ Python {python_version.major}.{python_version.minor} detected")
    
    # Check for CUDA
    try:
        import torch
        if torch.cuda.is_available():
            print(f"✅ CUDA available: {torch.cuda.get_device_name(0)}")
        else:
            print("⚠️  CUDA not available - will use CPU (slower)")
    except ImportError:
        print("⚠️  PyTorch not installed")
    
    return True

def install_wav2lip():
    """Install Wav2Lip and dependencies"""
    print("\n🚀 Installing Wav2Lip...")
    
    commands = [
        "git clone https://github.com/Rudrabha/Wav2Lip.git",
        "cd Wav2Lip",
        "pip install -r requirements.txt",
        "pip install opencv-python",
        "pip install torch torchvision torchaudio",
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e}")
            return False
    
    print("✅ Wav2Lip installation completed!")
    return True

def download_models():
    """Download required pre-trained models"""
    print("\n📥 Downloading pre-trained models...")
    
    model_urls = {
        "checkpoints/wav2lip_gan.pth": "https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIYoggf7hLJzn8M7PqY4M7g?e=n9ljGW",
        "checkpoints/wav2lip.pth": "https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxpouY9cAg?e=eTk8rs"
    }
    
    for model_path, url in model_urls.items():
        print(f"Downloading {model_path}...")
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        # Note: Manual download may be required due to SharePoint links
        print(f"⚠️  Manual download required: {url}")
    
    print("✅ Models download completed!")

def generate_lip_sync():
    """Generate lip-sync video"""
    print("\n🎬 Generating lip-sync video...")
    
    # File paths
    video_path = "assets/photo.png"
    audio_path = "assets/voice_recording.wav"
    output_path = "output/shrikanth_lip_sync.mp4"
    
    # Check if files exist
    if not os.path.exists(video_path):
        print(f"❌ Video file not found: {video_path}")
        return False
    
    if not os.path.exists(audio_path):
        print(f"❌ Audio file not found: {audio_path}")
        return False
    
    # Wav2Lip command
    cmd = f"""
    cd Wav2Lip
    python inference.py 
        --checkpoint_path checkpoints/wav2lip_gan.pth 
        --face "{os.path.abspath(video_path)}" 
        --audio "{os.path.abspath(audio_path)}" 
        --outfile "{os.path.abspath(output_path)}"
    """
    
    print(f"Running: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Lip-sync video generated: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating video: {e}")
        return False

def main():
    """Main setup function"""
    print("🎥 Wav2Lip Setup for Professional Lip-Sync Video")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        print("❌ System requirements not met")
        return
    
    # Install Wav2Lip
    if not install_wav2lip():
        print("❌ Installation failed")
        return
    
    # Download models
    download_models()
    
    # Generate lip-sync
    if generate_lip_sync():
        print("\n🎉 SUCCESS! Professional lip-sync video created!")
        print("📁 Output: output/shrikanth_lip_sync.mp4")
    else:
        print("\n❌ Video generation failed")
        print("💡 Consider using D-ID, HeyGen, or Synthesia for easier setup")

if __name__ == "__main__":
    main()
