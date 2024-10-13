import whisper
import os
import subprocess

# Function to extract audio using ffmpeg
def extract_audio(video_file, audio_file):
    # Use ffmpeg to extract audio from the video
    command = f"ffmpeg -i {video_file} -q:a 0 -map a {audio_file} -y"
    subprocess.run(command, shell=True, check=True)
    print(f"Audio extracted: {audio_file}")

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file, output_text_file):
    # Load the Whisper model
    model = whisper.load_model("base")  # You can change "base" to "small", "medium", "large", or "large-v2"
    
    # Transcribe the audio file
    result = model.transcribe(audio_file)
    transcript = result["text"]
    
    # Write the transcription to a text file
    with open(output_text_file, 'w') as f:
        f.write(transcript)
    print(f"Transcription saved: {output_text_file}")

def main():
    # Ask the user how many videos they want to transcribe
    num_videos = int(input("How many videos do you want to transcribe? "))

    # Loop through the number of videos
    for i in range(num_videos):
        # Get the video file name from the user
        video_file = input(f"Enter the name of video file {i + 1} (with extension, e.g., 'video1.mp4'): ")
        
        # Create the corresponding audio file name
        audio_file = os.path.splitext(video_file)[0] + ".mp3"
        
        # Extract audio from the video
        extract_audio(video_file, audio_file)
        
        # Define the output text file for the transcription
        output_text_file = os.path.splitext(video_file)[0] + "_transcribed.txt"
        
        # Transcribe the extracted audio and save it
        transcribe_audio(audio_file, output_text_file)

if __name__ == "__main__":
    main()
