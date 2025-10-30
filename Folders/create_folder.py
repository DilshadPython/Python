from pathlib import Path
# created folder where we save and create the text file 
test_folder = Path("TextFolder")

# if the folder not exist create it
test_folder.mkdir(exist_ok=True)

print("Folder created successfully.")