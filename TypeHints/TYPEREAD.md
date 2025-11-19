for this tutorial I am using VisualStudio
create python3 -m pip typenv

To make the code running using following packages to run the codes correct

python3 -m pip install pydantic-settings
OR
python3 -m pip install pydantic

Using pydantic here only to help use validate_call

To do manual type check you can comment from pydantic import validate_call, using if not isinstance 
