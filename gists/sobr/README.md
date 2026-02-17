[Check other gists](../..)

# sobr - Tiny sound browser

A tiny sound browser TUI (terminal user interface) made with Python and [Textual](https://textual.textualize.io/).

![sobr screenshot](https://i.imgur.com/dsZmxiB.png)

https://github.com/user-attachments/assets/a897eb7e-d2c6-407e-8f83-87bbe05224db


## Requirements

There are 02 requirements.

The first one is Python's third-party library [Textual](https://textual.textualize.io/).

```
pip install textual
```

If you want, [check this](https://textual.textualize.io/getting_started/#installation) for more options and other installation instructions.

The second requirement is a command line utility from your system to play the audio files. In my GNU/Linux system I use `paplay`. Please, search the web for a command line utility on your system that can be used to play audio. Once you have its name, you just have to replace `paplay`'s name inside the [sobr.py](./sobr.py) script with the name of the tool you want to use. Of course, you'll likely need to update the parts where the volume is updated as well, depending on how the utility you pick handles volume (or whether it allows such control at all), so play close attention to this as well.


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

Within the [sobr.py](./sobr.py) script, you can also change the extensions recognized as sound files.

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
