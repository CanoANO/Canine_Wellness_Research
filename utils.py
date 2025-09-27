import os
import kagglehub
import shutil

class Utils:
    def __init__(self):
        self.file_full_path = './data/canine-wellness-dataset-synthetic-10k-samples/1/synthetic_dog_breed_health_data.csv'
        self.file_download_folder = './data/canine-wellness-dataset-synthetic-10k-samples'
        self.file_download_path = "aaronisomaisom3/canine-wellness-dataset-synthetic-10k-samples"
        
    def download_csv(self):
        if not os.path.exists(self.file_full_path):
            # Download latest version
            path = kagglehub.dataset_download(self.file_download_path)
            # move file to /data/canine-wellness-dataset-synthetic-10k-samples
            os.makedirs(self.file_download_folder, exist_ok=True)
            shutil.move(path, self.file_download_folder)
            print(f"File downloaded and moved to {self.file_download_folder}")
        else:
            print(f"File already exists in {self.file_download_folder}")
        return self.file_full_path
