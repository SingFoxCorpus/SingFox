import os
from pydub import AudioSegment

# files = ["ar", "bn", "de", "en", "es", "fr", "hi", "id", "it", "ja", "ko", "mr", "pa", "pt", "ru", "ta", "te", "tr", "vi", "zh"]
# folders = ["Standard Arabic", "Bengali", "German", "English", "Spanish", "French", "Hindi", "Indonesian", "Italian", "Japanese", "Korean", "Marathi", "Punjabi", "Portuguese", "Russian", "Tamil", "Telugu", "Turkish", "Vietnamese", "Mandarin Chinese"]

files = ["flute", "guitar", "tabla", "piano", "violin"]
folders = ["Flute", "Guitar", "Tabla", "Piano", "Violin"]

for i in range(len(files)):
    # Input: one WAV file
    input_wav = fr"D:\Devanshi_Himanshi_SingFox\Single_File\Music\{files[i]}.wav"

    # Output folder for chunks
    output_dir = fr"D:\Devanshi_Himanshi_SingFox\Folder_Datasets\Music\{folders[i]}"
    os.makedirs(output_dir, exist_ok=True)

    # Load the WAV file
    audio = AudioSegment.from_wav(input_wav)
    chunk_length_ms = 2000  # 2 seconds

    # Base name without extension
    base_name = os.path.splitext(os.path.basename(input_wav))[0]

    # Split into chunks
    total_chunks = len(audio) // chunk_length_ms + (1 if len(audio) % chunk_length_ms != 0 else 0)

    for i in range(total_chunks):
        start = i * chunk_length_ms
        end = min(start + chunk_length_ms, len(audio))
        chunk = audio[start:end]
        chunk_filename = f"{base_name}_{i+1}.wav"
        chunk_path = os.path.join(output_dir, chunk_filename)
        chunk.export(chunk_path, format="wav")

    print(f"✅ Done! Saved {total_chunks} chunks to {output_dir}")
