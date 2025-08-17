from icrawler.builtin import GoogleImageCrawler
from PIL import Image
from pathlib import Path

# # Step 1: Download images with an offset
google_crawler = GoogleImageCrawler(storage={'root_dir': 'dataset3/squat3'})
google_crawler.crawl(keyword='barbell squat form jpg', max_num=200)  # Mulai dari hasil pencarian ke-50

# Step 2: Convert images to JPG
dataset_path = Path('./dataset3/AFIF')

# Iterate through all images in the dataset directory
for image_path in dataset_path.glob('*.*'):
    if image_path.suffix.lower() not in ['.jpg']:
        try:
            # Open an image file
            with Image.open(image_path) as img:
                # Convert the image to RGB mode if not already in it
                img = img.convert('RGB')
                # Save the image in JPG format, replacing the original file
                new_image_path = image_path.with_suffix('.jpg')
                img.save(new_image_path, 'JPEG')
                print(f"Converted {image_path} to {new_image_path}")
                
                # Remove the original file if the new file is created successfully
                image_path.unlink()
        except Exception as e:
            print(f"Could not convert {image_path}: {e}")

print("Image conversion complete.")
