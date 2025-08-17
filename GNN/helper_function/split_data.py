import os
import shutil
from sklearn.model_selection import train_test_split

# Define the paths
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_dir, 'dataset')
train_dir = os.path.join(data_dir, 'train')
test_dir = os.path.join(data_dir, 'test')

# Define classes
classes = ['Benchpress', 'Squat', 'Deadlift']

# Create train and test directories if they don't exist
for cls in classes:
    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(test_dir, cls), exist_ok=True)

# Function to split the dataset and print totals
def split_data(data_dir, train_dir, test_dir, classes, test_size=0.1):
    for cls in classes:
        cls_dir = os.path.join(data_dir, cls)
        images = os.listdir(cls_dir)
        
        # Filter and create full paths for images
        images = [os.path.join(cls_dir, img) for img in images if img.endswith(('jpg', 'png', 'jpeg', 'JPG'))]
        
        # Print total images before split
        total_images = len(images)
        print(f"Class '{cls}':")
        print(f"  Total images before split: {total_images}")
        
        if total_images == 0:
            print(f"  No images found in '{cls}' directory. Skipping...")
            continue
        
        # Split the data
        train_images, test_images = train_test_split(images, test_size=test_size, random_state=42)
        
        # Copy files to respective directories
        for img in train_images:
            shutil.copy(img, os.path.join(train_dir, cls))
        
        for img in test_images:
            shutil.copy(img, os.path.join(test_dir, cls))
        
        # Print totals after split
        print(f"  Training images: {len(train_images)}")
        print(f"  Testing images: {len(test_images)}")

# Perform the split
split_data(data_dir, train_dir, test_dir, classes)

print("Data splitting completed!")