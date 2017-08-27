VIRTUALENV_EXISTS := $(shell which virtualenv 2> /dev/null)
PYBUILDER_EXISTS := $(shell which pyb 2> /dev/null)
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

build: venv
	( \
		source venv/bin/activate; \
		pyb install_dependencies; \
		pyb clean package publish; \
		venv/bin/pip install $$(find target -type f -name "*.whl") --upgrade; \
	)

.PHONY: build

run:
	$(ROOT_DIR)/venv/bin/home_api

venv: venv/bin/activate

venv/bin/activate: check-prerequisites
	virtualenv venv

check-prerequisites: check-virtualenv check-pybuilder

check-virtualenv:
	@type shell virtualenv --version >/dev/null 2>&1

check-pybuilder:
	@type shell pyb --version >/dev/null 2>&1
