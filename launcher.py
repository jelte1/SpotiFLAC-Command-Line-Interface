#!/usr/bin/env python3
"""
Launcher script for SpotiFLAC
"""
import argparse
import sys
import os

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, application_path)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Spotify URL")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument(
        "--service",
        choices=["tidal", "deezer", "qobuz", "amazon"],
        nargs="+",
        default=["tidal"],
        help="One or more services to try in order (e.g. --service tidal deezer qobuz amazon)",
    )
    parser.add_argument("--filename-format", choices=["title_artist","artist_title","title_only"], default="title_artist")
    parser.add_argument("--use-track-numbers", action="store_true")
    parser.add_argument("--use-artist-subfolders", action="store_true")
    parser.add_argument("--use-album-subfolders", action="store_true")
    parser.add_argument("--loop", type=int, help="Loop delay in minutes")
    return parser.parse_args()

# Now import and run the main SpotiFLAC module
if __name__ == '__main__':
    from SpotiFLAC.SpotiFLAC import SpotiFLAC

    args = parse_args()
    SpotiFLAC(args.url, args.output_dir, args.service, args.filename_format, args.use_track_numbers, args.use_artist_subfolders, args.use_album_subfolders, args.loop)
