---

# YouTube Video Downloader and Converter

This Python script allows you to download YouTube videos in the highest available quality and convert them to various formats using different encoding options. It utilizes the `yt_dlp` library for downloading videos and supports conversion to MP4, MOV, MKV, and AVI formats.

## Requirements

- **yt_dlp**: A fork of youtube-dl with additional features and fixes.
- **ffmpeg**: A multimedia framework for handling audio, video, and other multimedia files.
- **HandBrakeCLI**: Command-line interface for HandBrake, a video transcoder.

## Installation

1. **yt_dlp**:

   You can install `yt_dlp` using pip:

   ```
   pip install yt-dlp
   ```

2. **ffmpeg**:

   - **Linux**: ffmpeg may be available in your package manager. For example, on Ubuntu:
   
     ```
     sudo apt-get install ffmpeg
     ```

   - **macOS**: You can install ffmpeg using Homebrew:
   
     ```
     brew install ffmpeg
     ```

   - **Windows**: Download the binary from the [official website](https://ffmpeg.org/download.html) and add it to your system's PATH environment variable.

3. **HandBrakeCLI**:

   - **Linux**: HandBrakeCLI may be available in your package manager. For example, on Ubuntu:
   
     ```
     sudo apt-get install handbrake-cli
     ```

   - **macOS**: You can install HandBrakeCLI using Homebrew:
   
     ```
     brew install handbrake
     ```

   - **Windows**: Download the binary from the [official website](https://handbrake.fr/downloads2.php) and add it to your system's PATH environment variable.

4. Clone the repository to your local machine:

   ```
   git clone https://github.com/yourusername/youtube-video-downloader.git
   ```

5. Navigate to the project directory:

   ```
   cd youtube-video-downloader
   ```

6. (Optional) If you prefer to use the executable, add the directory containing `grab.exe` to your system's PATH environment variable.

## Usage

Run the script from the command line with the following syntax:

```
python grab.py <video_link>
```

or using the executable (if added to PATH):

```
grab <video_link>
```

Replace `<video_link>` with the URL of the YouTube video you want to download.

Follow the prompts to select the desired output format and encoding options.

## Example

```
python grab.py https://www.youtube.com/watch?v=videoid
```

This command will download the YouTube video with the specified ID (`videoid`) in the highest available quality and prompt you to choose a format for conversion.

## Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
