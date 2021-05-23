#!/usr/bin/env bash
mkdir -p /collectuserinfo/collect_app/static
python3 manage.py collectstatic
gunicorn collectuserinfo.wsgi --bind 0.0.0.0:8080 --workers 3
