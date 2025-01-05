import os
folders = input("Please give folder name with space:").split()
for folder in folders:
    try:
       files = os.listdir(folder)
    except FileNotFoundError:
        print("provide valid folder name:" + folder)
        break
    except PermissionError:
        print("No access to this folder:"+folder)

    print(files)