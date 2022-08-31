# Fractal Art
Using L-systems and Python turtle graphics to create fractal art. 

<p align="center">
  <img style="white-space: pre" width="300" height="280" src="https://github.com/miaisakovic/fractal-art/blob/main/images/sierpinski_arrowhead_curve.png"/>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
  <img style="white-space: pre" width="300" height="280" src="https://github.com/miaisakovic/fractal-art/blob/main/images/l_system.png"/>
</p>

## Table of Contents
* [Setup](#setup)
  * [For Linux](#for-linux)
  * [For MacOS](#for-macos)
  * [After Installing Initial Requirements](#after-installing-initial-requirements)
* [Viewing the Fractal Art](#viewing-the-fractal-art)

## Setup 
### For Linux
If Python has not been previously installed, run the following:
```
$ sudo apt install python3.9
$ python3.9 --version
```

### For MacOS
If Homebrew has not been previously installed, follow the instructions listed [here](https://brew.sh/).

If Python has not been previously installed, run the following:
```
$ brew install python@3.9
$ python3.9 --version
```

### After Installing Initial Requirements
Clone this repository:
```
$ git clone <fractal-art URL>
``` 
When asked to enter credentials, input your username and personal access token.

## Viewing the Fractal Art
To view the Sierpiński arrowhead curve, run the following command:
```
$ python3.9 <relative path to sierpinski_arrowhead_curve.py>
```
To view fractal art generated by an L-system [LSystemBot 2.0](https://twitter.com/lsystembot?lang=en)  provided, run the following command
```
$ python3.9 <relative path to l_system.py>
```
