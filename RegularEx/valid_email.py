# importing regular expression
import re
'''
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
'''
email = input("Enter your email: ").strip()

# [^@] means accept any characters except @
# .* it means 0 or other characters
# \. means exactly enden with .com because \ don't allowed . work as any characters
# The ^ and & added to match the exact email required
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
# if re.search(r"^\w+@\w+\.com$", email):
# if re.search(r"^[^@]+@[^@]+\.com$", email):

# if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
# re.IGNORECASE allowed the user to enter uppercase or lowercase the email address
# if re.search(r"^\w+@\w+\.(com|net|co.uk|gov|org|de)$", email, re.IGNORECASE):
# ? mean or can be extra . after @
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid Email")
else:
    print("Invalid Email")