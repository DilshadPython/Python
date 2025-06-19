

mkvirtualenv imgchangenv
pip install numpy
pip install opencv-python

pip install uv

## create new .env 
# Reference: 
# https://www.techprofree.com/category/books/?fbclid=IwY2xjawLA2zxleHRuA2FlbQIxMABicmlkETB1TnM1alpPSWZJZ3BuUnpUAR4fthPmlUmeSTowCH-d4QnZ5sXYpR4feLLZelSIOVZwuXl56_l1nogQXXvhiQ_aem_pwoNbqGw_FcTYYIhuuaAYQ

uv init --no-workspace (name of .env you want)
# Example
uv init --no-workspace imgenv 

cd imgenv

# to run
uv run main.py
# Remove image background
# install rembg use
uv add rembg
