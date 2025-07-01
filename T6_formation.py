import os
import shutil
import random
from pathlib import Path
from tqdm import tqdm

def create_subset(source_root, dest_root, subset_ratio=0.33):
    splits = ['train', 'test', 'val']
    for split in splits:
        split_src = os.path.join(source_root, split)
        split_dst = os.path.join(dest_root, split)
        
        if not os.path.exists(split_dst):
            os.makedirs(split_dst)
        
        class_names = os.listdir(split_src)
        for class_name in class_names:
            class_src = os.path.join(split_src, class_name)
            class_dst = os.path.join(split_dst, class_name)
            os.makedirs(class_dst, exist_ok=True)

            files = [f for f in os.listdir(class_src) if os.path.isfile(os.path.join(class_src, f))]
            subset_count = max(1, int(len(files) * subset_ratio))  # at least 1 file
            subset_files = random.sample(files, subset_count)

            for file in subset_files:
                shutil.copy2(os.path.join(class_src, file), os.path.join(class_dst, file))

# Example usage
source_dataset = r"D:\Devanshi_Himanshi_SingFox\SingFox_ICASSP\T5 - Copy"
subset_dataset = r"D:\Devanshi_Himanshi_SingFox\SingFox_ICASSP\T6"

create_subset(source_dataset, subset_dataset, subset_ratio=0.33)
