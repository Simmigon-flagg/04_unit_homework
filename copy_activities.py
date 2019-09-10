import shutil
import os

def stu_activities():
    folder_path = os.path.join("Downloads")
    des = os.path.join("new")
    for root, dirs, files in os.walk(folder_path): 
        for index in range(len(dirs)):
            if dirs[index].startswith("Stu_"):
                print("Found!")
                print(root +" and folder is " + dirs[index]) 
                current_file_path = os.path.join(root,str(dirs[index]))
                print(current_file_path)
                shutil.copytree(current_file_path,str(dirs[index]))
stu_activities()