# PythonLibrary-Tutorial
This is a tutorial project for publishing your own python library on PyPi.

## Requirments

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the requirements.
Just follow the commands below:

Upgrade Setuptoos:
```bash
python -m pip install --upgrade twine setuptools
```

Install Wheel:
```bash
pip install wheel
```

Make a build for your Library/Package:
```bash
python setup.py sdist bdist_wheel
```

Install twine:
```bash
pip install twine
```

Upload Your Library:
```bash
twine upload dist/*
```

If the above command fail to upload:
```bash
python -m twine upload dist/*
```


Congratulations your Library/Package is Published Successfully!! You might also got a link like this:
https://pypi.org/project/AreaOfFigs/


If you want to upload through Git repo,
Add this code after import statements
```python
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
```
After add this code you have to add an Readme.md file and the just follow the commands above.

## Usage
Watch the full [tutorial](https://youtu.be/43VD7zH5iPY) on our youtube channel to know the complete setup. 
YT Channel: [Developer Gautam](https://www.youtube.com/c/DeveloperGautam)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
