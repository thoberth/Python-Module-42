python3 -m pip install --upgrade pip build setuptools wheel
python3 setup.py sdist bdist_wheel bdist_egg
pip install ./dist/my_minipack-0.0.1-py3-none-any.whl
