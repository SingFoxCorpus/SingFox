import os
from pydub import AudioSegment
from tqdm import tqdm

def check_peak_dBFS(directory, threshold_dbfs=-1.0):
    report = []

    for folder, _, files in os.walk(directory):
        for file in tqdm(files, desc=f"Checking {folder}"):
            if file.lower().endswith(".wav"):
                file_path = os.path.join(folder, file)
                try:
                    audio = AudioSegment.from_wav(file_path)
                    peak_dBFS = audio.max_dBFS  # Closest to 0 dBFS
                    is_normalized = peak_dBFS >= threshold_dbfs - 0.1  # 0.1 tolerance
                    report.append((file_path, round(peak_dBFS, 2), is_normalized))
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")

    # Print summary
    for path, peak_db, norm in report:
        status = "✅ Normalized" if norm else "❌ Not Normalized"
        print(f"{path}: Peak {peak_db} dBFS → {status}")

    return report

# Example use
resampled_path = r"D:\Devanshi_Himanshi_SingFox\Resampled_wav_Audio\Music"
check_peak_dBFS(resampled_path)
