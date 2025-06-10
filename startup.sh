#!/bin/bash
service ssh start
exec gunicorn app:app --bind 0.0.0.0:8000
