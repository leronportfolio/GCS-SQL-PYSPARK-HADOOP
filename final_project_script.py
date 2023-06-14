import json
import os
from pathlib import Path

# Define input and output file paths
input_file = Path("yelp_academic_dataset_user.json")
output_dir = Path("user_chunks")

# Create output directory if it doesn't exist
if not output_dir.exists():
    output_dir.mkdir()

# Define chunk size in bytes
chunk_size = 500000000  # 0.5 GB

with input_file.open(encoding='utf8') as f:
    current_chunk = None
    current_chunk_size = 0
    chunk_num = 0
    for line in f:
        if current_chunk is None or current_chunk_size + len(line) > chunk_size:
            if current_chunk:
                current_chunk.close()
            chunk_num += 1
            current_chunk_size = 0
            current_chunk = open(output_dir / f"chunk_{chunk_num}.json", "w", encoding='utf8')
        current_chunk.write(line)
        current_chunk_size += len(line)

    if current_chunk:
        current_chunk.close()
