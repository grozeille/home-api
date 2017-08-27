.PHONY: init_venv clean_venv

VIRTUALENV_EXISTS := $(shell which virtualenv 2> /dev/null)
PYBUILDER_EXISTS := $(shell which pyb 2> /dev/null)
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: init_venv
	PYTHONPATH=venv ; \
	. venv/bin/activate && \
	pyb install_dependencies && \
	pyb clean package publish && \
	venv/bin/pip install $$(find target -type f -name "*.whl") --upgrade

clean:
	PYTHONPATH=venv ; \
	. venv/bin/activate && \
	pyb clean

run:
	$(ROOT_DIR)/venv/bin/home_api

init_venv: check-prerequisites
	if [ ! -e "venv/bin/activate_this.py" ] ; then PYTHONPATH=venv ; virtualenv --clear venv ; fi

check-prerequisites: check-virtualenv check-pybuilder

check-virtualenv:
	@virtualenv --version >/dev/null 2>&1

check-pybuilder:
	@pyb --version >/dev/null 2>&1

clean_venv:
	rm -rf venv