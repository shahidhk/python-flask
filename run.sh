#!/bin/sh
exec gunicorn --config /app/src/gunicorn_config.py server:app
