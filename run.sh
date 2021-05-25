#!/usr/bin/env bash
mkdir static
gunicorn collectuserinfo.wsgi --bind 0.0.0.0:8080 --workers 3
