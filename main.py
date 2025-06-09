import os
import shutil
import argparse
from datetime import datetime

def organize_by_type(folder_path):
    pdf_folder = os.path.join(folder_path, "PDFs")
    image_folder = os.path.join(folder_path, "Images")
    os.makedirs(pdf_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.lower().split('.')[-1]
            if ext == 'pdf':
                shutil.move(file_path, os.path.join(pdf_folder, filename))
                print(f"Moved PDF: {filename}")
            elif ext in ['jpg', 'jpeg', 'png']:
                shutil.move(file_path, os.path.join(image_folder, filename))
                print(f"Moved Image: {filename}")

def organize_by_date(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            mod_date = datetime.fromtimestamp(mod_time)
            date_folder = f"{mod_date.year}_{mod_date.strftime('%B')}"
            dest_folder = os.path.join(folder_path, date_folder)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"Moved: {filename} → {date_folder}/")

def organize_by_type_and_date(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.lower().split('.')[-1]
            if ext in ['pdf', 'jpg', 'jpeg', 'png']:
                type_folder = "PDFs" if ext == 'pdf' else "Images"
                mod_time = os.path.getmtime(file_path)
                mod_date = datetime.fromtimestamp(mod_time)
                date_folder = f"{mod_date.year}_{mod_date.strftime('%B')}"
                dest_folder = os.path.join(folder_path, type_folder, date_folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} → {type_folder}/{date_folder}/")

def main():
    parser = argparse.ArgumentParser(description="Organize files by type, date, or both.")
    parser.add_argument("--path", required=True, help="Path to folder (e.g. ~/Downloads)")
    parser.add_argument("--mode", required=True, choices=["type", "date", "type_date"],
                        help="Sorting mode: type, date, or type_date")

    args = parser.parse_args()
    folder = os.path.expanduser(args.path)

    if args.mode == "type":
        organize_by_type(folder)
    elif args.mode == "date":
        organize_by_date(folder)
    elif args.mode == "type_date":
        organize_by_type_and_date(folder)

if __name__ == "__main__":
    main()
