# restrip() remove extra line show the reading more nice
# rstrip() remove extra line show the reading more nice
import sys

from pathlib import Path

# created folder where we save and create the text file 
create_dir = Path("TextFolder")

txt_file = Path(create_dir, "languages.txt")

enter_name = input("Enter language name or type 'exit' to quit: ")


openFile = open("languages.txt", "w")

openFile.write(txt_file)
openFile.close()
