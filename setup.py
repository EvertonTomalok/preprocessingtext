from setuptools import setup, find_packages
from preprocessingtext import name, __version__

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name=name,
    packages=find_packages(),
    version=__version__,
    author="Everton Tomalok",
    author_email="evertontomalok123@gmail.com",
    description="A series of methods to help you work pre processing of text in general, like stem, tokenizer and others.",
    long_description=long_description.replace('<br>', ' '),
    url="https://github.com/EvertonTomalok/preprocessingtext",
    download_url='https://github.com/EvertonTomalok/preprocessingtext/archive/master.zip',
    keywords=['pre-processing text'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['textblob', 'nltk'],
    license="MIT",
)
