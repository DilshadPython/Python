Inatll poetry for python tutorials to avoid using virtualenv or virtualenwrapper

- Open terminal run: curl -sSL https://install.python-poetry.org | python3 -
- sudo apt install python3-poetry
- By Default automatically added: ~/.local/share/pypoetry on Linux
- poetry --version
# Here starting how to Use:
- poetry new poetry-pkg (you can name whatever you like we named here poetry-pkg)
- Activate run: poetry shell
- Output is:  (poetry-pkg-7Za_pVj1-py3.10) username of pc and roject name
- installing third-party package for each lessons need to run this:
	poetry add package_name ex. poetry add pickle-mixin for Serialization
- each package installed going to /poetry-pkg/pyproject.toml 