# Escape
![logo](https://www.qaviton.com/wp-content/uploads/logo-svg.svg)  
[![version](https://img.shields.io/pypi/v/pyescape.svg)](https://pypi.python.org/pypi)
[![license](https://img.shields.io/pypi/l/pyescape.svg)](https://pypi.python.org/pypi)
[![open issues](https://img.shields.io/github/issues/qaviton/escape)](https://github/issues-raw/qaviton/escape)
[![downloads](https://img.shields.io/pypi/dm/pyescape.svg)](https://pypi.python.org/pypi)
![code size](https://img.shields.io/github/languages/code-size/qaviton/escape)
-------------------------  
  
Escape  
is a package handling characters  
that should be escaped such as: '" \\n\t.  
  
## Installation  
```sh  
pip install pyescape -U
```  

### Requirements
- Python 3.6+  
  
## Features  
* Escape class
  
## Usage  
  
```python
from os import system
from escape import Escape
from sys import executable

escape = Escape('"\' ')
executable = '"'+executable+'"'  # python executable with special characters

system(executable+' -c "print(\'hello world\')"')
```  
