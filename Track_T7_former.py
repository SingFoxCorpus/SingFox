import os
import random
from pydub import AudioSegment
from pathlib import Path
from tqdm import tqdm

# Input folders
songs_dir = r"G:\Devanshi_Himanshi_SingFox\track 3 and track 6\T6"
music_dir = r"D:\Devanshi_Himanshi_SingFox\SingFox_ICASSP\T3"

# Output folder
output_dir = r"D:\Devanshi_Himanshi_SingFox\SingFox_ICASSP\T7"

splits = ["train", "test", "val"]
classes = {
    "class1_realSong_realMusic": ("real", "real"),
    "class2_fakeSong_realMusic": ("fake", "real"),
    "class3_fakeSong_fakeMusic": ("fake", "fake"),
}

def load_audio_paths(base_dir):
    return {
        split: {
            label: list(Path(base_dir, split, label).glob("*.wav"))
            for label in ["real", "fake"]
        } for split in splits
    }

def mix_and_save(song_path, music_path, out_path):
    try:
        song = AudioSegment.from_file(song_path)
        music = AudioSegment.from_file(music_path)
        mixed = song.overlay(music[:len(song)])
        mixed.export(out_path, format="wav")
    except Exception as e:
        print(f"❌ Error mixing {song_path.name} with {music_path.name}: {e}")

def create_dataset(songs_paths, music_paths):
    for split in splits:
        for class_name, (song_type, music_type) in classes.items():
            song_list = songs_paths[split][song_type]
            music_list = music_paths[split][music_type]
            out_dir = Path(output_dir, split, class_name)
            out_dir.mkdir(parents=True, exist_ok=True)

            print(f"🔄 Processing {split}/{class_name} - {len(song_list)} files")
            for i, song_path in enumerate(tqdm(song_list)):
                music_path = random.choice(music_list)
                new_filename = f"{song_path.stem}__{music_path.stem}.wav"
                mix_and_save(song_path, music_path, out_dir / new_filename)

songs_paths = load_audio_paths(songs_dir)
music_paths = load_audio_paths(music_dir)

create_dataset(songs_paths, music_paths)
