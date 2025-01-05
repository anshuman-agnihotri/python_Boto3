import os
folders = input ("provide valid folder:")
for folder in folders:
    try: 
        files = os.listdir(folder)
    except FileNotFoundError:
     break 
    print ("provide valid dir:" +folder)
  
    print (files)