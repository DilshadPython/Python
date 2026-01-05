First: Go to setting install
https://docs.astral.sh/uv/#projects

Using Numpy, Pandas, Matplotlib and Sklearn

I installed uv in My linux mint as first:
uv?
An extremely fast python package and project manager and much better and faster than pip.
https://docs.astral.sh/uv/

https://scikit-learn.org/stable/install.html

What is the reason:
Much faster than pip
Same functionality but less  codes
It's a single tool replace poetry, pyenv, etc

To use uv:
uv run main.py  instated of python main.py
uv add -r requirements.txt instead of pip install -r requirements.txt
uv sync instead of python -m venv .venv

Captured automatic for pip freeze > requirements.txt

Installation and using uuv init --app --python$(which python3)v:
https://docs.astral.sh/uv/#highlights
- install uv run:
  - curl -LsSf https://astral.sh/uv/install.sh | sh
  - uv and uvx automatically install
- Create new project use uv
  - cd Python/ML 
    - uv init --no-workspace
    - Initialized project `ml`

  Tips:
 total 32
drwxrwxr-x   2 monika monika 4096 Jan  3 13:15 .
drwxrwxr-x 146 monika monika 4096 Nov 21 02:28 ..
-rw-rw-r--   1 monika monika   80 Jan  3 13:14 main.py
-rw-rw-r--   1 monika monika  148 Jan  3 13:14 pyproject.toml
-rw-rw-r--   1 monika monika    5 Jan  3 13:14 .python-version
-rw-rw-r--   1 monika monika    0 Jan  3 13:14 README.md
- Add dependencies
  - uv add numpy
  - uv add pandas
  - uv add matplotlib
  - uv add scikit-learn
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Resolved 2 packages in 684ms
Prepared 1 package in 5.87s
Installed 1 package in 23ms
 + numpy==2.4.0

# When installed first package automatically add .venv and install the package
/Devel/Python/ML$ ls -la
total 48
drwxrwxr-x   3 monika monika  4096 Jan  3 13:20 .
drwxrwxr-x 146 monika monika  4096 Nov 21 02:28 ..
-rw-rw-r--   1 monika monika    80 Jan  3 13:14 main.py
-rw-rw-r--   1 monika monika   169 Jan  3 13:20 pyproject.toml
-rw-rw-r--   1 monika monika     5 Jan  3 13:14 .python-version
-rw-rw-r--   1 monika monika  1485 Jan  3 13:20 README.md
-rw-rw-r--   1 monika monika 17302 Jan  3 13:20 uv.lock
drwxrwxr-x   4 monika monika  4096 Jan  3 13:20 .venv

Next add the numpy to pyproject.toml file