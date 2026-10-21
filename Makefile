PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PYTHON_VENV := $(VENV)/bin/python

setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

demo:
	$(PYTHON_VENV) examples/lane_following/demo.py

run:
	$(PYTHON_VENV) examples/lane_following/demo.py

.PHONY: setup demo run
