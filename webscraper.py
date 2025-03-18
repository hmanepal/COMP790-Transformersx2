from simple_image_download.simple_image_download import Downloader
import os
import shutil

def create_transformers_dataset():
    # Initialize the downloader
    downloader = Downloader()
    
    # List of Transformers characters with their search terms in quotes
    characters = {
        "Optimus_Prime": "'Optimus Prime'",  # Using single quotes instead
        "Bumblebee": "Bumblebee",
        "Megatron": "Megatron",
        "Starscream": "Starscream"
    }
    
    # Base directory for the dataset
    base_path = r"C:\Users\harsh\Downloads\Comp790 Final Project\Images\transformers_dataset"
    
    # Create the base directory if it doesn't exist
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    # Download images for each character in their respective folders
    for folder_name, search_term in characters.items():
        # Create character-specific folder
        character_path = os.path.join(base_path, folder_name)
        if not os.path.exists(character_path):
            os.makedirs(character_path)
        
        print(f"Downloading images for {search_term}...")
        
        try:
            # Download images
            downloader.download(search_term, limit=100)
            
            # Handle the default folder name (remove quotes for folder lookup)
            default_folder = f"simple_images/{search_term}"
            if os.path.exists(default_folder):
                # Get all files in the default folder
                files = os.listdir(default_folder)
                
                # Move each file to the character folder
                for file in files:
                    src = os.path.join(default_folder, file)
                    dst = os.path.join(character_path, file)
                    shutil.move(src, dst)
                
                # Remove the empty default folder
                shutil.rmtree(default_folder)
                
            print(f"Successfully downloaded images for {search_term}")
            
        except Exception as e:
            print(f"Error downloading images for {search_term}: {str(e)}")
        
        # Clean up any split folders that might have been created
        split_terms = search_term.replace("'", "").split()
        for term in split_terms:
            split_folder = f'simple_images/{term}'
            if os.path.exists(split_folder):
                shutil.rmtree(split_folder)
    
    print("\nDataset creation complete!")
    print(f"Dataset location: {base_path}")

if __name__ == "__main__":
    create_transformers_dataset()