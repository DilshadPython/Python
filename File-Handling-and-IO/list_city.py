from pathlib import Path

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

'''

# create the folder
create_dir = Path('TextFolder')

# defile the path of text file inside the folder
txt_file = Path(create_dir, "cities.txt")

with open(txt_file, 'r') as f:
    for line in f:
        print('Hello,', line.rstrip())
