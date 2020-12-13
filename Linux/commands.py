lnx_list = {
    'cd': 'Change directory',
    'alias': 'You can create your own command or change the command',
    'cat': 'Short for concatenate, display the content of the file or concatenate files and print on the standard output',
    'cd': 'Change directory',
    'cd "My File"': 'If you have directory with two words with empty space or use cd "My\ file"',
    'cat -b file.html': 'Show the content with the number except the empty line',
    'cat -n file.html': 'Add number for the empty line',
    'cat -s file.txt': 'In this file there many empty lines will set the empty lines to one empty line and remove the rest',
    'cat -E file.text': 'Add $ to the end of each lines and empty lines on the shell not in the file',
    'chmod': 'Allow user to sets the file permissions flags Like Read, Write and Execute between 0-7 "\n" \
    		chmod -R 756 filename.txt "\n" \
    		0: No permission "\n" \
			1: Execute permission "\n" \
			2: Write permission "\n" \
			3: Write and execute permissions "\n" \
			4: Read permission "\n" \
			5: Read and execute permissions "\n" \
			6: Read and write permissions "\n" \
			7: Read, write and execute permissions',
    'chown': 'The chown command allows you to change the owner and group owner of a file "\n" \
    		sudo chown dave:mary example.txt ',
    'curl': 'This command is a tool to retrieve information and files from Uniform Resource "\n" \
            curl https://linkedin.com/dilshad',
    'ls': 'Display list of directory and files in current folder',
    'ls -a': 'Display files, folders with hidden files and folders ',
    'ls -l': 'Display folders files permissions include size',
    'ls -la': 'Display folders files permissions include size and hidden files and folder with total number',
    'ls -lS': 'Display folder and files by sortting from largest size to smallest',
    'ls -lS > file.html': 'Create the file.html for you in current folder copy every files, folder to file.html created include permissions and size',
    'ls -d */': 'Display only the directories in current folder or location',
    'wc': 'print newline, word, and byte counts for each file',
    'wc file.html': '5 == newline 38 == words 229 == size by byte of the file.html',
    
    'mkdir': 'Create directory in current folder',
    'touch': 'Create file',
    'curl': 'The curl command is a tool to retrieve information and files from Uniform Resource',
    'mkdir -p names/dilmac': 'Create two directories first called name and second dilmac the -p is helpes to create subdirectory in parents directory',
    'mkdir -p test/{one,two,three}': 'Create test directory and 3 other directories inside test but don\'t put space between the dir names'
    'rm': 'Remove the file',
    'rmdir': 'Remove the directory',
    'rm -r': 'Remove the directory if the directory is not empty',
    'ls -R': 'Display the main directory including all other directories inside the main directory',
    'rmdir test/a/b/c': 'Remove only the c directory not other',
    'rmdir -p test/a/b/c': 'Remove all directories inside each other.',
    'rmdir -pv a/b/c/d/e/f/h': "rmdir: removing directory, 'a/b/c/d/e/f/h' \
                                rmdir: removing directory, 'a/b/c/d/e/f' \
                                rmdir: removing directory, 'a/b/c/d/e' \
                                rmdir: removing directory, 'a/b/c/d' \
                                rmdir: removing directory, 'a/b/c' \
                                rmdir: removing directory, 'a/b' \
                                rmdir: removing directory, 'a' \
                                                            ",
    'cp': 'Copy file to where you want',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
}
