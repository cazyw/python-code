# File Backup With Python

A simple application for comparing and backing up files

<img src="https://cazyw.github.io/img/backup-0.jpg" width="450">

It's been a while, still works (on my Windows 10 machine), but it's time to review the code.

## Environment and System Configuration

Built in Windows 7 with Python 3. Only tested in a windows environment. There may be issues in other environments due to the '/' and '\\' difference between Windows and Unix based systems.

Python 3 can be downloaded from https://www.python.org/
The GUI was built using the Tkinter package which is included in the Windows python download.

## Application Installation Instructions

Clone or download this repository

## Operating Instructions

Navigate to the backup folder in the repository. There should be one file `backup.py`. Run it with:

```
$ python3 backup.py
```
This will open a graphical interface and users can select a `Source` and `Destination` folder and choose to:
* `List` Outputs the list of files in the source folder
* `Compare` Compare the files in the source and destination folders and outputs a list of the files in the Source folder, flagging the ones that are not in the destination folder and therefore need to be backed up
* `Copy` Compare the files in the source and destination folders and if the source folder has a newer copy of a file (or the file doesn't exist in the destination folder), copy the file from the source folder to the destination folder and also output a log 

<img src="https://cazyw.github.io/img/backup-1.jpg" width="450">

Logs are output to `stdout` and time-stamped text files a `copy_log` folder

<img src="https://cazyw.github.io/img/backup-2.jpg" width="450">

## Overview and Discussion

This was a personal project both to learn and use Python but also because I had wanted a file-copy/backup program that did exactly what I wanted. Most of the programs available had a lot of extra features I did not need. Building this project I learnt about manipulating file systems, GUI interfaces in python and classes. I use this to compare and backup files from my laptop to external storage.

It compares files based on file names and the time it was last modified. I have not tried using this for large sets of files.

## Contributing
Carol Wong

