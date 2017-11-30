# BSTSB
Bot Script the Script Bot

## Installation
Requires the slackclient python module.

`python setup.py install`

Note the installation will edit `~/.bashrc` and it must therefore be sourced by your shell.
For MacOS and some other systems it is necessary to source `~/.bashrc` from `~/.bash_profile`.
During installation you will be prompted if you want this to be done automatically.
To do so manually add the following to `~/.bash_profile`:
```
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

## Configuration
During installation you will be prompted to configure your slack account.
If you choose not to during installation you may add the following to `~/.bashrc` afterwards:
```
export SLACK_USERNAME=your username here
export SLACK_BOT_TOKEN=api token here
```
## Usage
To run something in the foreground:
`bstsb command here`

To run something in the background:
`bstsb -bg command here`

### Example
If you want to run a long python script and don't want to sit around for a while you could do the following:

`bstsb -bg python long_script.py`
