import yt_dlp
import os
import sys
from subprocess import run

def download_and_convert(url):
    # Create a yt-dlp options dictionary
    ydl_opts = {
        'format': 'bestvideo[ext=?vp9][height>=?1080]+bestaudio[ext=opus]/bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge-output-chapters': True,
        'merge-output-metadata': True
    }

    # Create a yt-dlp instance
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the video
        ydl.download([url])

    # Get the downloaded file name
    info = ydl.extract_info(url, download=False)
    video_filename = ydl.prepare_filename(info)

    # Prompt the user for output format
    print("Choose the output format:")
    print("1. Leave as is")
    print("2. MP4")
    print("3. MOV")
    print("4. MKV")
    print("5. AVI")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(f"Video downloaded: {video_filename}")
    elif choice == "2":
        # Transcode the downloaded video to MP4 format

        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

        # Construct the full path to presetCustom.json
        preset_file_path = os.path.join(script_dir, 'config', 'presetCustom.json')


        output_extension = "mp4"
        output_filename = os.path.join(os.getcwd(), f'{os.path.splitext(os.path.basename(video_filename))[0]}.{output_extension}')
        handbrake_cmd = f'HandBrakeCLI -i "{video_filename}" -o "{output_filename}" --preset-import-file "{preset_file_path}" -Z "maximumQualityMP4"'
        run(handbrake_cmd, shell=True)
        print(f'Video downloaded and converted: {output_filename}')
    elif choice == "3":
        # Transcode the downloaded video to QuickTime MOV format
        output_extension = "mov"
        output_filename = os.path.join(os.getcwd(), f'{os.path.splitext(os.path.basename(video_filename))[0]}.{output_extension}')
        transcode_cmd = f'ffmpeg -i "{video_filename}" -c:v libx264 -crf 18 -c:a aac -b:a 192k -movflags faststart "{output_filename}"'
        run(transcode_cmd, shell=True)
        print(f'Video downloaded and transcoded to QuickTime MOV: {output_filename}')
    elif choice == "4":
        # Convert the downloaded video to MKV format
        output_extension = "mkv"
        output_filename = os.path.join(os.getcwd(), f'{os.path.splitext(os.path.basename(video_filename))[0]}.{output_extension}')
        convert_cmd = f'ffmpeg -i "{video_filename}" -map 0 -c copy "{output_filename}"'
        run(convert_cmd, shell=True)
        print(f'Video downloaded and converted to MKV: {output_filename}')
    elif choice == "5":
        # Transcode the downloaded video to AVI format
        output_extension = "avi"
        output_filename = os.path.join(os.getcwd(), f'{os.path.splitext(os.path.basename(video_filename))[0]}.{output_extension}')
        transcode_cmd = f'ffmpeg -i "{video_filename}" -c:v libxvid -qscale:v 3 -c:a aac -b:a 192k "{output_filename}"'
        run(transcode_cmd, shell=True)
        print(f'Video downloaded and transcoded to AVI: {output_filename}')
    else:
        print(f"Invalid choice. Video not Converted. Video Saved: {video_filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python code.py <video_link>")
        sys.exit(1)
    youtube_url = sys.argv[1]
    download_and_convert(youtube_url)
