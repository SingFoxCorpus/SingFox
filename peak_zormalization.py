import os
from pydub import AudioSegment
from tqdm import tqdm

def match_target_amplitude(sound, target_dBFS):
    """Normalize given AudioSegment to target dBFS"""
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def normalize_audio_dataset(input_dir, output_dir=None, target_dBFS=-1.0):
    """
    Normalizes volume of all audio files in a dataset to target_dBFS.
   
    Args:
        input_dir (str): Path to dataset (all should be .wav ideally).
        output_dir (str): If None, overwrites original. Else saves to this path.
        target_dBFS (float): Target loudness (e.g., -1.0 dBFS).
    """
    valid_ext = ('.wav', '.mp3', '.flac', '.aac', '.m4a', '.ogg')

    for foldername, _, filenames in os.walk(input_dir):
        for filename in tqdm(filenames, desc=f"Normalizing {foldername}"):
            if filename.lower().endswith(valid_ext):
                input_path = os.path.join(foldername, filename)
                try:
                    audio = AudioSegment.from_file(input_path)
                    normalized_audio = match_target_amplitude(audio, target_dBFS)

                    relative = os.path.relpath(foldername, input_dir)
                    output_base = output_dir if output_dir else input_dir
                    output_folder = os.path.join(output_base, relative)
                    os.makedirs(output_folder, exist_ok=True)
                    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.wav')

                    normalized_audio.export(output_path, format='wav')
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

# 🔁 Apply on your resampled dataset
resampled_path = r"D:\Devanshi_Himanshi_SingFox\Resampled_Audio\Music"
# Optional: set output path if you don't want to overwrite
# normalized_output_path = r"D:\Devanshi_Himanshi_singfake\Raw_Data\Songs\Normalized"

normalize_audio_dataset(resampled_path, target_dBFS=-1.0)
