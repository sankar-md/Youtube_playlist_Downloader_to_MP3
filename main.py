# Install yt-dlp and ffmpeg
!pip install yt-dlp
!apt-get install ffmpeg -y

import os, zipfile
import yt_dlp

# Playlist URL
PLAYLIST_URL = "https://www.youtube.com/watch?v=3TVvRETczto&list=PLtQZNXwCeuXSZ3NOUkhenPHsU3cZkRRnz"

# Output directory & zip file
OUTPUT_DIR = "yt_playlist_downloads"
ZIP_FILE = "playlist_songs.zip"

def download_playlist(url, outdir):
    """Download YouTube playlist as MP3"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{outdir}/%(title)s.%(ext)s',
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    os.makedirs(outdir, exist_ok=True)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def zip_files(directory, zip_name):
    """Zip all MP3 files in directory"""
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".mp3"):
                    zipf.write(os.path.join(root, file), file)

print("⬇️ Downloading playlist...")
download_playlist(PLAYLIST_URL, OUTPUT_DIR)

print("📦 Creating ZIP file...")
zip_files(OUTPUT_DIR, ZIP_FILE)

print(f"✅ Done! All songs saved in {ZIP_FILE}")
