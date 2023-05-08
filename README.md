# lux

This repository contains a program designed to have aesthetic light animations for these lights to be mounted on a porch.

## Installation

```
# clone the repo
git clone git@github.com:nohumanman/lux.git
# cd into the repo
cd lux
# make shell files runnable
chmod u+x start.sh && chmod u+x add-to-cron.sh
# add to crontab
./add-to-cron.sh "@reboot sleep 20; $(pwd)/start.sh;"
# run the program
./start.sh
```
