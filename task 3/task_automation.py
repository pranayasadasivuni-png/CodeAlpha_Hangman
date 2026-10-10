import os
import shutil

# Source and destination folders
source_folder = "source_images"
destination_folder = "jpg_images"

# Create folders if they do not exist
os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)

# Move all JPG files
moved_count = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
        moved_count += 1

print(f"\nTask completed! Total JPG files moved: {moved_count}")