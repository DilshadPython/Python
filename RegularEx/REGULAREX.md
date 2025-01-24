https://docs.python.org/3/library/re.html

. any character except a newline (any characters uppercase or lowercase except newline)
* 0 or more repetitions (any number from 0 to whatever enter)
+ 1 or more repetitions (number from 1 to whatever enter)
? 0 or 1 repetition (after you enter ? you can enter 0 char or 1 char)
{m} m repetition (m stand for number of repetitions)
{m,n} m-n repetition (m any number and n you mean between m and n) number of repetitions
^ matches the start of the string
$ matches the end of the string just before the newline at the end of the string
[] set of characters
[^] complementing the set of characters
\d decimal digit
\D not a decimal digit
\s whitespace character
\S not a whitespace character
\w word character ... as well as numbers and the underscore
\W not a word character
| means or
A|B either A or B
(...) a group
(?:...) mom-capturing version

re.IGNORECASE  = This is use when the user enter uppercase or lowercase will ignored and accept
re.MULTILINE
re.DOTALL

re.search(pattern, string, flags=0)
re.match(pattern, string, flags=0)
re.fullmatch(pattern, string, flags=0)
re.findall(pattern, string, flags=0)
re.sub(pattern, repl, string, count=0, flags=0)
pattern = is want you search for
string = is what you searching for which user enter
flags = parameter you put in

# username, domain = email.split("@")

# re.search(pattern, string, flags=0)

# below adding empty space
if re.search(r"^[a-zA-Z0-9_ ]+@\w+\.com$", email):
if re.search(r"^(\w|\s)+@\w+\.com$", email):

# if re.search(r"[^@]+@[^@]+\.[^@]+", email):
# if re.search('@', email):
# . any char
# time = 8.55
start ---> q1 ----@----> q2
