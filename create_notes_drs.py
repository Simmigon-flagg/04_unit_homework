import os
def main():
    print()
    if os.path.exists("CyberSecurity-Notes") == False:
        os.mkdir('CyberSecurity-Notes')
        print("Create New Folder")

    for index in range(1, 25):
        file_path = os.path.join("CyberSecurity-Notes")
        week = "Week " + str(index)
        if os.path.exists(file_path + "/" + week) == False:
            os.mkdir(file_path + "/" + week)
            for day_index in range(1,4):
                day = "Day " + str(day_index)
                print(day)
                if os.path.exists(file_path + "/" + week + "/" + day) == False:
                    os.mkdir(file_path + "/" + week + "/" + day)

        


main()

    