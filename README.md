# FireDownloader
Download Youtube videos or playlists

A minimal Python command-line tool for downloading YouTube videos or extracting audio, built on [yt-dlp](https://github.com/yt-dlp/yt-dlp).

---

## ✨ Features
- Download videos or full playlists  
- Audio-only mode (MP3, M4A, FLAC, etc.)  
- Resumable downloads  
- Clean progress bar using `tqdm`  
- Works cross-platform  

---

## 🛠️ Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/thewaleogun/FireDownloader.git
cd ytfetch
```
### 2️⃣ (Optional) Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Install FFmpeg (for audio conversion)
```bash
Linux
sudo apt install ffmpeg

macOs
brew install ffmpeg

Windows
Download and install from ffmpeg.org/download
```
### 🚀 Usage Examples
```bash
🎬 Download a YouTube Video
python firedown.py "https://www.youtube.com/watch?v=VIDEO_ID"

🎧 Extract Audio Only
python firedown.py "https://www.youtube.com/watch?v=VIDEO_ID" --audio

📜 Download Playlist
python firedown.py "https://www.youtube.com/playlist?list=YOUR_LIST_ID" --playlist

💾 Save to Custom Folder
python firedown.py "https://youtu.be/abcd1234" -d ./downloads

⚙️ Options and Flags
Flag	Description
--audio	Download audio only
--audio-format	Audio format (mp3, m4a, flac, etc.)
--audio-quality	Audio bitrate (default: 192)
--output	Custom filename template
--resume	Resume partial downloads
--verbose	Enable debug logs

