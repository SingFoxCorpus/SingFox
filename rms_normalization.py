import os
from pydub import AudioSegment
from tqdm import tqdm

# Input directory (also output directory now)
input_root = r"D:\Devanshi_Himanshi_SingFox\Single_File\New folder"

# Normalization targets
peak_target_dBFS = -1.0
rms_target_dBFS = -20.0
fallback_threshold_peak = -10.0  # if peak is below this
fallback_threshold_rms = -30.0  # and RMS is also low

# Start normalization
for folder, _, files in os.walk(input_root):
    for file in tqdm(files, desc=f"Normalizing {folder}"):
        if file.lower().endswith(".wav"):
            input_path = os.path.join(folder, file)

            try:
                audio = AudioSegment.from_wav(input_path)

                if len(audio) == 0 or audio.max_dBFS == float('-inf'):
                    print(f"⚠️ Skipped (empty or silent): {input_path}")
                    continue

                # Normalize by peak
                peak_gain = peak_target_dBFS - audio.max_dBFS
                normalized_audio = audio.apply_gain(peak_gain)

                # Check if still too soft (instruments, etc.)
                if audio.max_dBFS < fallback_threshold_peak and audio.dBFS < fallback_threshold_rms:
                    rms_gain = rms_target_dBFS - audio.dBFS
                    normalized_audio = audio.apply_gain(rms_gain)
                    print(f"🎻 RMS Fallback used for: {file} (gain: {round(rms_gain, 2)} dB)")

                # Export to same path (overwrite original)
                normalized_audio.export(input_path, format="wav")

            except Exception as e:
                print(f"❌ Error with {input_path}: {e}")
