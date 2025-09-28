# 🎬 Step-by-Step D-ID Guide

## Current Status
❌ Error: `shrikanth_lip_sync_base.mp4` not found
✅ Solution: Create lip-sync video using D-ID first

## 📋 **Step-by-Step Instructions**

### **Step 1: Go to D-ID**
1. Open browser and go to: **https://www.d-id.com**
2. Click "Sign Up" (free account)
3. Use your email to create account

### **Step 2: Upload Your Photo**
1. Click "Create Video"
2. Choose "Photo + Audio" option
3. Upload your photo: `C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\photo.png`
4. Wait for photo to process

### **Step 3: Upload Your Voice**
1. Upload your audio: `C:\Users\hp\Video_Generation_Project\Video_Generation_Project\assets\voice_recording.wav`
2. Click "Generate Video"
3. Wait 3-5 minutes for AI processing

### **Step 4: Download Result**
1. When ready, download the video
2. **IMPORTANT:** Save it as: `shrikanth_lip_sync_base.mp4`
3. Place it in: `C:\Users\hp\Video_Generation_Project\Video_Generation_Project\output\`

### **Step 5: Run Enhancement Script**
```bash
cd C:\Users\hp\Video_Generation_Project\Video_Generation_Project
python src/enhance_ai_video.py
```

## 🎯 **Expected Result**
- Perfect lip-sync video where your lips move with your voice
- Professional visual effects added
- Final video: `shrikanth_professional_intro.mp4`

## ⏱️ **Total Time: 15 minutes**
- D-ID setup: 5 minutes
- AI processing: 5 minutes  
- Enhancement: 5 minutes

## 🆘 **If D-ID Doesn't Work**
Try these alternatives:
1. **HeyGen:** https://www.heygen.com
2. **Synthesia:** https://www.synthesia.io
3. **Wav2Lip:** Free but technical (see setup_wav2lip.py)
