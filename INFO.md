# All installed models are store in python(version) folder/lib
# All internale models are stor in builtin 
# All external models or third party models are store in package manager \
	site-package


# ctrl + shift and P
	Install package
	Predawan >> color
	Material Theame
	SidebarEnhancements

<!--
https://www.youtube.com/watch?v=xFciV6Ew5r4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=10&ab_channel=CoreySchafer
	https://github.com/CoreyMSchafer/dotfiles/blob/master/settings/Preferences.sublime-settings
-->

$ pip list --outdated
Package    Version Latest Type
---------- ------- ------ -----
Django     3.2     4.0.2  wheel
setuptools 60.3.1  60.7.1 wheel

$ pip freeze --local | grep -v "^\-e" | cut -d = -f 1
asgiref
Django
pytz
sqlparse

# Upgrate all packegs has new version and need to be upgrate:
$ pip freeze --local | grep -v "^\-e" | cut -d = -f 1 | xargs -n1 pip install -U
asgiref
Django
pytz
sqlparse

$ pip list
Package    Version
---------- -------
asgiref    3.5.0
Django     3.2
pip        22.0.3
pytz       2021.3
setuptools 60.3.1
sqlparse   0.4.2
wheel      0.37.1
