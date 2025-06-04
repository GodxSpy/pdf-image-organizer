import os
import shutil

def oraganize_files_by_type(folder_path):
    pdf_folder=os.path.join(folder_path,"PDFs")
    image_folder=os.path.join(folder_path,"Images")

    os.makedirs(pdf_folder,exist_ok=True)
    os.makedirs(image_folder,exist_ok=True)
    for filename in os.listdir(folder_path):
        file_path=os.path.join(folder_path,filename)

        if os.path.isfile(file_path):
            if filename.lower().endswith('.pdf'):
                shutil.move(file_path,os.path.join(pdf_folder,filename))
                print(f"Moved PDF :{filename}")
            elif filename.lower().endswith(('.jpeg', '.png', '.jpg')):
                shutil.move(file_path,os.path.join(image_folder,filename))
                print(f"Moved Image : {filename}")

# Test
folder = os.path.expanduser('~/Downloads')
oraganize_files_by_type(folder)
