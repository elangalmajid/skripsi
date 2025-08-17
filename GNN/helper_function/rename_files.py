import os

def rename_files(directory, category):
    print(f"Renaming files in directory: {directory}")
    
    # Counter for renaming files
    count = 1
    
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.jpg'):
            # New filename with category and count
            new_name = f"{category}_{count}.jpg"
            src = os.path.join(directory, filename)
            dst = os.path.join(directory, new_name)
            os.rename(src, dst)
            print(f"Renamed {src} to {dst}")
            
            # Increment the counter
            count += 1

# Directory containing the images
directory_path = './dataset3/benchpress2'

# Category to rename
category_name = 'benchTambahan3'

# Rename files
rename_files(directory_path, category_name)
