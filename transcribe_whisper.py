import os
import platform
import subprocess
import sys
import whisper

def check_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_os_specific_instructions():
    current_os = platform.system()
    instructions = {
        "Darwin": "\n\033[94mBrew install command:\nbrew install ffmpeg\033[0m",
        "Windows": "\n\033[94mChocolatey install command:\nchoco install ffmpeg\n\nScoop install command:\nscoop install ffmpeg\033[0m",
        "Linux": "\n\033[94mAPT install command:\nsudo apt install ffmpeg\033[0m"
    }
    return instructions.get(current_os, "Please install FFmpeg for your operating system")

def format_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    msecs = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{msecs:03}"

def validate_file_path(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    if not file_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.mp3', '.wav', '.flac')):
        raise ValueError("Unsupported file format. Please provide a video or audio file")

def main():
    try:
        # Detect operating system
        current_os = platform.system()
        print(f"\033[1mDetected operating system: {current_os}\033[0m")

        # Check FFmpeg installation
        if not check_ffmpeg_installed():
            print("\033[91mFFmpeg is not installed or not in system PATH\033[0m")
            print(get_os_specific_instructions())
            return

        # Load Whisper Turbo model
        print("\n\033[93mLoading Whisper Turbo model... (Initial download may take several minutes)\033[0m")
        model = whisper.load_model("turbo")
        
        # Get input file path
        file_path = input("\n\033[1mEnter path to media file: \033[0m").strip()
        validate_file_path(file_path)

        # Transcribe content
        print("\n\033[96mStarting transcription...\033[0m")
        result = model.transcribe(file_path, task='transcribe')

        # Save results as SRT subtitles
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = f"{base_name}.srt"
        with open(output_file, "w", encoding="utf-8") as f:
            for i, segment in enumerate(result.get("segments", []), start=1):
                start = format_timestamp(segment["start"])
                end = format_timestamp(segment["end"])
                text = segment["text"].strip()
                f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

        print(f"\n\033[1;92mTranscription complete! Saved to:\033[0m {output_file}")
        print(f"\033[95mProcessing time: {result['segments'][-1]['end']:.1f}s\033[0m")

    except Exception as e:
        print(f"\n\033[91mError: {str(e)}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
