import os
import shutil
cworkingdirectory = os.getcwd()

def pdf_copy():   
    folder_path = os.path.join("Downloads")
    for root, dirs, files in os.walk(folder_path):
        for d_index in range(len(dirs)):
            for f_index in range(len(files)):
                if files[f_index].endswith(".pdf"):
                    file_path = os.path.join(root,str(files[f_index])) 
                    cwd = os.path.join(".") 
                    shutil.copy(file_path,cwd)
pdf_copy()