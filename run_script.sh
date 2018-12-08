#!/usr/bin/env bash
export SLAMBOOK_DEV=dev
python manage.py db upgrade
python manage.py server