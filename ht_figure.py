import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load both audio files
file1 = r"C:\Users\admin\Downloads\ht_1.ogg"
file2 = r"C:\Users\admin\Downloads\ht_2.ogg"

y1, sr1 = librosa.load(file1, sr=None)
y2, sr2 = librosa.load(file2, sr=None)

# Ensure same sampling rate
assert sr1 == sr2, "Sampling rates must match!"

# Define replacement interval (4s to 6s)
start_sec = 4
end_sec = 6
start_sample = int(start_sec * sr1)
end_sample = int(end_sec * sr1)

# Store original for comparison
y1_original = y1.copy()

# Replace 4s–6s of y1 with same part from y2
y1[start_sample:end_sample] = y2[start_sample:end_sample]

# Plot original and modified
plt.figure(figsize=(14, 6))

# Original
plt.subplot(2, 1, 1)
librosa.display.waveshow(y1_original, sr=sr1)
plt.axvspan(start_sec, end_sec, color='red', alpha=0.3, label='Will be replaced')
# plt.title("Original Audio 1")
plt.ylabel("Amplitude")
plt.legend()

# Modified
plt.subplot(2, 1, 2)
librosa.display.waveshow(y1, sr=sr1)
plt.axvspan(start_sec, end_sec, color='green', alpha=0.3, label='Replaced Segment')
# plt.title("Modified Audio 1 (with segment from Audio 2)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
