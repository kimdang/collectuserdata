#!/usr/bin/env bash
gunicorn collectuserinfo.wsgi --bind 0.0.0.0:8080 --workers 3
