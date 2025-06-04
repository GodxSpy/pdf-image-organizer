import os
import shutil
from datetime import datetime

def organize_files_by_type_and_date(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_ext = filename.lower().split('.')[-1]

            if file_ext in ['pdf', 'jpg', 'jpeg', 'png']:
                # Type-based folder
                type_folder = "PDFs" if file_ext == 'pdf' else "Images"

                # Date-based folder
                modified_time = os.path.getmtime(file_path)
                mod_date = datetime.fromtimestamp(modified_time)
                date_folder = f"{mod_date.year}_{mod_date.strftime('%B')}"

                # Create final destination
                destination_folder = os.path.join(folder_path, type_folder, date_folder)
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved: {filename} → {type_folder}/{date_folder}/")

# Test
folder = os.path.expanduser('~/Downloads')
organize_files_by_type_and_date(folder)
