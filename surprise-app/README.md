# Surprise App

A small desktop app written in Python with a graphical interface.
It shows a series of screens with compliments and two answer buttons.
The "wrong" button runs away from the mouse cursor, and at the end
a heart is drawn on the screen while little hearts fall down.

![Screenshot](screenshot.png)

## Features

- Multiple screens generated from a list of questions
- A button that jumps away when the cursor touches it
- Animation: the heart is drawn line by line
- Falling hearts with random sizes, colors and speeds

## Getting started

Install Python 3, then install the dependency:

```
pip install customtkinter
```

Run the app:

```
python surprise.py
```

## Build an executable (Windows)

```
pip install pyinstaller
py -m PyInstaller --onefile --windowed --collect-all customtkinter surprise.py
```

The result will be in the `dist` folder.

## What I learned

- Building a GUI with customtkinter: widgets, events, `command` and `bind`
- Lists of dictionaries, functions with parameters, `lambda`
- Animation with `after()`
- Drawing on a `Canvas`
- Packaging a Python app into an `.exe` with PyInstaller

## Tech stack

Python, customtkinter, tkinter

