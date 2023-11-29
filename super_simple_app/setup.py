from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Food Fetcher Wrapper'
LONG_DESCRIPTION = 'A package that allows you to fetch food data from the USDA Food Composition Databases API'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="food_fetcher",
    version=VERSION,
    author="Tomislav Ignjatov",
    author_email="tomislavignjatov@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=['requests'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'food', 'fetcher', 'usda', 'api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
