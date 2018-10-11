# pipy

A Raspberry Pi Python Installer.

No fuss, simple Python installer.

`python -m pipy [--all (install dependencies)] [--run (run generated bash script)] <python_version>`

## Usage

pipy will only generate a bash script when you run it.
This bash script will perform the following:

 - wget the .tgz for that python version
 - use tar to unpack it into a directory
 - run configure.sh, make and make altinstall
 - remove unpacked directory and clean up

## Example

- Installing Python 3.7.0 with all the dependencies.
```
python -m pipy --all --run 3.7.0
```
