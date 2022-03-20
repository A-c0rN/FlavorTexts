![PyPI](https://img.shields.io/pypi/v/FlavorTexts?label=Version&style=flat-square) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/A-c0rN/FlavorTexts/CodeQL?style=flat-square) ![PyPI - Downloads](https://img.shields.io/pypi/dm/FlavorTexts?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/A-c0rN/FlavorTexts?style=flat-square) ![GitHub](https://img.shields.io/github/license/A-c0rN/FlavorTexts?style=flat-square)

You can't spell FlavorText without Vortex.

## Features
> - [x] Fast generation
> - [x] Buffered print library
> - [x] Clearscreen funtion
> - [x] Absolute Insanity
> - [x] Patreon Specific flag included!

## Installation
This package should be installable through Pip.

On a Debian Based Linux OS:
```
sudo apt update
sudo apt install python3 python3-pip
pip3 install FlavorTexts
```


On Windows:

[Install Python](https://www.python.org/downloads/)

In CMD:
```
python -m pip install FlavorTexts
```


## Usage
To confuse yourself:
```python
from FlavorTexts import FlavorTexts
from FlavorTexts import BufferedText
from time import sleep

try:
    ## Define a FlavorText Generator
    generator= FlavorTexts(patreon=False)

    while True:

        ## Generate a random True/False
        constructive = bool(generator._random(1))

        ## Generate a random text string with a random Constructive/Destructive flag.
        textList = generator.generateText(constructive=constructive)

        ## Write the random text to the buffered text manager, and print a newline
        BufferedText.bufferedWrite(textList)
        print()

        ## Sleep for 1/2 second
        sleep(0.5)

## Exit smoothly on a CTRL+C
except KeyboardInterrupt:
    exit(0)
```


I am so sorry...