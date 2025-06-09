import os
import librosa
import soundfile as sf
from tqdm import tqdm

def resample_all_languages(base_input_dir, base_output_dir, target_sr=16000):
    """
    Resamples audio files in all subfolders (each language) of base_input_dir.
   
    Args:
        base_input_dir (str): Main dataset path with language folders.
        base_output_dir (str): Output path to store resampled files.
        target_sr (int): Target sample rate (e.g., 16000).
    """
    for language_folder in os.listdir(base_input_dir):
        input_language_path = os.path.join(base_input_dir, language_folder)
        output_language_path = os.path.join(base_output_dir, language_folder)

        if not os.path.isdir(input_language_path):
            continue  # Skip non-folder items

        os.makedirs(output_language_path, exist_ok=True)

        for root, _, files in os.walk(input_language_path):
            for file in tqdm(files, desc=f"Resampling {language_folder}"):
                if file.lower().endswith(('.wav', '.mp3', '.flac')):
                    input_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(root, input_language_path)
                    output_subdir = os.path.join(output_language_path, relative_path)
                    os.makedirs(output_subdir, exist_ok=True)
                    output_file_path = os.path.join(output_subdir, os.path.splitext(file)[0] + '.wav')

                    try:
                        y, sr = librosa.load(input_file_path, sr=None)
                        y_resampled = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
                        sf.write(output_file_path, y_resampled, target_sr)
                    except Exception as e:
                        print(f"Error with {input_file_path}: {e}")

# 🗂️ Input and Output Paths
input_root = r"D:\Devanshi_Himanshi_SingFox\Raw_Data\Music"
output_root = r"D:\Devanshi_Himanshi_SingFox\Resampled_wav_Audio\Music"

# ▶️ Run the Resampling
resample_all_languages(input_root, output_root, target_sr=16000)
