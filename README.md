# Package Manager Demo

## Description
This is a demo that shows how to publish a package using the bare minimum such as pip without any fancy package managers

## 1. Create the virtual enviroment
python -m venv path_to_virtual_enviroment -- to create it with pip

conda create --name package-manager-enviroment python=3.11  -- to create it with conda

pipenv install

## 2. Build the package with the setup script
python setup.py sdist bdist_wheel

## 3. Upload the package to pypi or some local pypi clone 
twine upload dist/*
