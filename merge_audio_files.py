import os
from pydub import AudioSegment
from tqdm import tqdm

# Path to the normalized dataset directory
input_root = r"D:\Devanshi_Himanshi_SingFox\Resampled_wav_Audio\Songs\Vietnamese"  # or wherever your normalized files are

# Output file path
output_path = r"D:\Devanshi_Himanshi_SingFox\Single_File\Songs\vi.wav"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Initialize an empty AudioSegment
merged_audio = AudioSegment.empty()

# Walk through all files and merge .wav files
for folder, _, files in os.walk(input_root):
    wav_files = sorted([f for f in files if f.lower().endswith(".wav")])  # sorted for consistent order
    for file in tqdm(wav_files, desc=f"Merging from {folder}"):
        file_path = os.path.join(folder, file)
        try:
            audio = AudioSegment.from_wav(file_path)
            if len(audio) > 0:
                merged_audio += audio # + AudioSegment.silent(duration=200)  # optional: 200ms silence between files
        except Exception as e:
            print(f"❌ Error with {file_path}: {e}")

# Export the merged file
merged_audio.export(output_path, format="wav")
print(f"\n✅ Merged audio saved to: {output_path}")
