# 🎵 How to Download YouTube Playlist as MP3 (Step by Step Guide)

This guide will help **any beginner**, even if you are new to
computers.\
We will use **Google Colab** (free online tool) to download songs from a
YouTube playlist and save them as MP3.

------------------------------------------------------------------------

## ✅ What You Need

-   A **Google account** (to use Colab).
-   A **YouTube playlist link** (with songs you want to download).

------------------------------------------------------------------------

## 🚀 Steps

### 1. Open Google Colab

1.  Go to [Google Colab](https://colab.research.google.com/).
2.  Click on **New Notebook**.

------------------------------------------------------------------------

### 2. Install Tools in Colab

Copy & paste the code below into the first cell of Colab and run it
(press `Shift + Enter`):

``` python
!pip install yt-dlp
!pip install pydub
```

This installs the tools needed to download music.

------------------------------------------------------------------------

### 3. Add Playlist Link

In the next cell, paste this code:

``` python
import os

# 🔗 Put your YouTube playlist link here
playlist_url = "YOUR_YOUTUBE_PLAYLIST_LINK"

# Create a folder for downloads
os.makedirs("downloads", exist_ok=True)

# Download all videos as high-quality MP3
!yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 -o "downloads/%(title)s.%(ext)s" {playlist_url}
```

👉 Replace **YOUR_YOUTUBE_PLAYLIST_LINK** with your real playlist link.

------------------------------------------------------------------------

### 4. Zip All Songs

Now we will zip all MP3 files into one file:

``` python
!zip -r songs.zip downloads
```

------------------------------------------------------------------------

### 5. Download to Your Computer

Run this code to download the ZIP file:

``` python
from google.colab import files
files.download("songs.zip")
```

This will give you a ZIP file with all songs in MP3 format.

------------------------------------------------------------------------

## 🎧 Notes

-   Audio quality depends on the original upload on YouTube.
-   Using MP3 is good enough for most listeners (high quality with
    smaller file size).
-   Use **royalty-free music** if you want to upload to YouTube without
    copyright issues.

------------------------------------------------------------------------

## 🎵 Where to Find Royalty-Free Music?

-   [YouTube Audio Library](https://www.youtube.com/audiolibrary/music)
-   [Pixabay Music](https://pixabay.com/music/)
-   [Free Music Archive](https://freemusicarchive.org/)

------------------------------------------------------------------------

✅ Done! Now you can easily download and enjoy your music.
