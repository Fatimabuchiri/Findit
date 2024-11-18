#Convert music files to .wav format and store in the same folder

from pydub import AudioSegment # type: ignore
import os

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    """
    Convert an MP3 file to WAV format.
    :param mp3_file_path: Path to the input MP3 file.
    :param wav_file_path: Path to save the output WAV file.
    """
    try:
        # Load the MP3 file
        audio = AudioSegment.from_mp3(mp3_file_path)
        
        # Export the audio as a WAV file
        audio.export(wav_file_path, format="wav")
        print(f"Conversion successful! WAV file saved at: {wav_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    mp3_path = "Findit/test/93 - Adh-Dhuha (the Forenoon).mp3"  # Replace with your MP3 file path
    wav_path = "Findit/test/93 - Adh-Dhuha (the Forenoon).wav"  # Replace with your desired WAV file path
    convert_mp3_to_wav(mp3_path, wav_path)

