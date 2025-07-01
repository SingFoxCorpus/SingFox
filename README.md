# SingFox

mp3_to_wav.py	--> Converts MP3 audio files to WAV format for consistent processing.

resampling.py	--> Resamples all WAV files to a target sample rate (e.g., 16 kHz) for uniformity.

peak_zormalization.py -->	Applies peak normalization to adjust audio levels so the loudest peak reaches a target dBFS.

rms_normalization.py --> Applies RMS normalization to ensure consistent perceived loudness across files.

check_normatization.py --> Verifies whether files are properly normalized (checks peak and RMS levels).

merge_audio_files.py --> Merges all WAV files into a single long WAV file, with optional silence between clips.

divide_audio_file.py --> Splits each WAV file into fixed-length segments (e.g., 2 seconds) and saves them with consistent naming.

distribute_dataset_chunks.py – Splits audio files by language and type into fixed-size chunks across multiple organized directories for singfake generation.

dataset_from_dirs_code.ipynb - If the structure is like 2 folders with n (n=number of directories) subdirectories, and each subdirectory has language folder which contains audios, then the code will make a dataset we want in base form.
