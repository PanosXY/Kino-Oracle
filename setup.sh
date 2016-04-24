#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

cmd=`which pip`
if [ $? != 0 ]; then
    echo "Installing basic modules...(This may take a while)"
    (apt-get install -y python-pip && pip install setuptools) > /dev/null
fi

current_path=`pwd`
cmd=`pip list | grep ansicolors | wc -l`
if (($cmd == 0)); then
    echo "You don't have 'ansicolors' python module installed."
    echo "Cloning git repo at /tmp/ansicolors/..."
    git clone https://github.com/verigak/colors.git /tmp/ansicolors/
    echo "Installing module..."
    cd /tmp/ansicolors/
    python setup.py install > /dev/null
    echo "Cleaning up..."
    rm -rf /tmp/ansicolors
    cd $current_path
fi

echo "Installing script..."
python setup.py install > /dev/null && echo "Installation Succesful!!"
exit 0
