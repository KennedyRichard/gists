[Check other gists](../..)

# sobr - Tiny sound browser

A tiny sound browser TUI (terminal user interface) made with Python and [Textual](https://textual.textualize.io/).

![sobr screenshot](https://i.imgur.com/dsZmxiB.png)


## Requirements

Python's third-party library [Textual](https://textual.textualize.io/).

```
pip install textual
```

If you want, [check this](https://textual.textualize.io/getting_started/#installation) for more options and other installation instructions.


## Usage

To learn how to use `sobr`, just execute `sobr -h` in your terminal. The following message will appear:

```
usage: sobr [-h] [--volume VOLUME] [--columns COLUMNS]

sobr - sound browser to play sound files from current folder

options:
  -h, --help         show this help message and exit
  --volume VOLUME
  --columns COLUMNS
```

## Setup

Please, search the web to learn how to set this Python script/app for your operating system.

On my system, Xubuntu (a Ubuntu GNU/Linux distro), it is as simple as placing it in a folder where the terminal can see it and adding a line similar to the next one to the top of the script, which tells it where to find the Python interpreter:

```
#! /usr/bin/env python3
```

In my case, I usually point to the exact Python interpreter instance from the virtual environment I use (which has Textual installed). Something similar to this:

```
#! /path/to/venv/bin/python3
```
