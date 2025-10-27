#!/usr/bin/env python3
"""firedown.py — YouTube Video & Audio Downloader using yt-dlp.
"""

import argparse
import sys
import os
from yt_dlp import YoutubeDL
from tqdm import tqdm

class ProgressDisplay:
    def __init__(self):
        self.pbar = None
        self.last_bytes = 0

    def hook(self, d):
        status = d.get('status')
        if status == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            done = d.get('downloaded_bytes', 0)
            if total:
                if not self.pbar:
                    self.pbar = tqdm(total=total, unit='B', unit_scale=True, desc=d.get('filename', 'Downloading'))
                self.pbar.n = done
                self.pbar.refresh()
            else:
                if not self.pbar:
                    self.pbar = tqdm(unit='B', unit_scale=True, desc=d.get('filename', 'Downloading'))
                self.pbar.update(done - self.last_bytes)
            self.last_bytes = done
        elif status == 'finished':
            if self.pbar:
                self.pbar.close()
                self.pbar = None
            print("✅ Download finished, post-processing...")
        elif status == 'error':
            if self.pbar:
                self.pbar.close()
            print("❌ Download error:", d)

def make_opts(args):
    outtmpl = args.output or os.path.join(args.output_dir, '%(title)s.%(ext)s')
    postprocessors = []
    if args.audio:
        postprocessors.append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': args.audio_format,
            'preferredquality': str(args.audio_quality),
        })

    class Logger:
        def debug(self, msg): 
            if args.verbose: print(msg)
        def warning(self, msg): print("[WARN]", msg)
        def error(self, msg): print("[ERROR]", msg)

    opts = {
        'format': 'best' if not args.audio else 'bestaudio/best',
        'outtmpl': outtmpl,
        'ignoreerrors': True,
        'quiet': True,
        'retries': args.retries,
        'continuedl': args.resume,
        'logger': Logger(),
        'progress_hooks': [ProgressDisplay().hook],
        'postprocessors': postprocessors,
    }
    return opts

def download(urls, args):
    opts = make_opts(args)
    with YoutubeDL(opts) as ydl:
        for url in urls:
            try:
                print(f"\n▶️  Downloading: {url}")
                ydl.download([url])
            except Exception as e:
                print("Error:", e)

def parse_args():
    p = argparse.ArgumentParser(description="Simple YouTube downloader (yt-dlp backend)")
    p.add_argument('urls', nargs='+', help='Video or playlist URLs')
    p.add_argument('-o', '--output', help='Custom filename template')
    p.add_argument('-d', '--output-dir', default='downloads', help='Output directory')
    p.add_argument('--audio', action='store_true', help='Download audio only')
    p.add_argument('--audio-format', default='mp3', choices=['mp3','aac','m4a','wav','flac'])
    p.add_argument('--audio-quality', type=int, default=192)
    p.add_argument('--retries', type=int, default=3)
    p.add_argument('--resume', action='store_true')
    p.add_argument('--verbose', action='store_true')
    return p.parse_args()

if __name__ == '__main__':
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    download(args.urls, args)
