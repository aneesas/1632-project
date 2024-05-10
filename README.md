# Swing-up Control of the Acrobot

(Source: https://github.com/aneesas/1632-project)

This repository contains code to find an optimal controller for the acrobot swing-up problem using pseudospectral methods. To learn more about the acrobot, please see the references at the bottom of the project notebook.

## Contents
All of the project code lives in the iPython notebook titled `acrobot.ipynb`. There is explanatory text within the notebook describing each section's purpose. The core of the optimization is in the function `acrobot_swing_up`, which takes in boundary conditions and references to dynamics and cost functions (for which multiple options are defined in the notebook).

## Requirements
Required packages found on [PyPI](https://pypi.org/) are listed in `requirements.txt` and can be installed via `pip` or similar. Additionally, the following tools are needed to run the included iPython notebook:

- YAPSS v1.0.0-alpha.1
- ffmpeg (for generating acrobot animations only)

### Installing ffmpeg
MacOSX does not ship with ffmpeg installed by default. The easiest way to get ffmpeg is via [Homebrew](https://brew.sh/):

```bash
brew install ffmpeg
```

If on Linux, similarly use apt:

```bash
sudo apt install ffmpeg
```

The notebook kernel may need to be restarted after installation.
