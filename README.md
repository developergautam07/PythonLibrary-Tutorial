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


## Usage
Watch the full [tutorial](https://youtu.be/BiQwZA6CGrk) on our youtube channel to know the complete setup. 
YT Channel: [Developer Gautam](https://www.youtube.com/c/DeveloperGautam)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
