#!/usr/bin/env bash
virtualenv venv
source venv/bin/activate
pyb_ install_dependencies

pyb_ clean package install
pip install $(find target -type f -name "*.whl") --upgrade

home_api