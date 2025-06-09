import os
from pydub import AudioSegment
from tqdm import tqdm

def convert_to_wav(root_dir, output_dir=None):
    """
    Converts all audio files in root_dir to WAV format and saves in output_dir.
    If output_dir is None, it replaces files in-place.

    Args:
        root_dir (str): Path to the base folder containing audio files.
        output_dir (str): Destination root folder for converted files.
    """
    supported_ext = ('.mp3', '.flac', '.aac', '.ogg', '.m4a', '.wav')

    for foldername, _, filenames in os.walk(root_dir):
        for filename in tqdm(filenames, desc=f"Processing {foldername}"):
            if filename.lower().endswith(supported_ext):
                src_path = os.path.join(foldername, filename)

                # Load using pydub
                try:
                    audio = AudioSegment.from_file(src_path)
                except Exception as e:
                    print(f"Failed to load {src_path}: {e}")
                    continue

                # Define output path
                relative_path = os.path.relpath(foldername, root_dir)
                base_output = output_dir if output_dir else root_dir
                dest_folder = os.path.join(base_output, relative_path)
                os.makedirs(dest_folder, exist_ok=True)
                dest_filename = os.path.splitext(filename)[0] + ".wav"
                dest_path = os.path.join(dest_folder, dest_filename)

                # Export to WAV
                try:
                    audio.export(dest_path, format="wav")
                except Exception as e:
                    print(f"Failed to export {dest_path}: {e}")

# 🗂️ Apply on Resampled Dataset
resampled_path = r"D:\Devanshi_Himanshi_SingFox\Single_File\New folder"
# Optional: convert and save to a new folder
# output_path = r"D:\Devanshi_Himanshi_singfake\Raw_Data\Songs\WAV_Format"

convert_to_wav(resampled_path)
