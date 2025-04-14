import os
import requests
import datetime
import shutil


firstname = "Adjei"
lastname = "Mensah"

folder_name = f"{firstname}_{lastname}"
filename = f"{firstname}_{lastname}.txt"

url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

if os.path.exists(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"Folder '{folder_name}' has been deleted")
    except:
        print(f"Error deleting folder '{folder_name}'")


try:
    os.mkdir(folder_name)
    print(f"folder '{folder_name}' has been created")
except:
    print(f"folder '{folder_name}' could not be created")


local_file_path = os.path.join(folder_name, filename)


response = requests.get(url)

if response.status_code ==200:
    print("File downloaded")

    with open(local_file_path, "wb") as file:
        file.write(response.content)

    print("File saved")

else:
    print("download failed")

user_input1 = input("Describe what you have learned so far in a sentence.:")

current_date = datetime.datetime.now().timestamp()

with open(local_file_path, "w") as file:
    file.write(user_input1 + "\n")
    file.write( f"last modified on {current_date}")


with open(local_file_path, "r") as file:
    print("File contains: /n")
    print(file.read())
