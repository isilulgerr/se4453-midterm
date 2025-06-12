#!/bin/sh
/usr/sbin/sshd
gunicorn app:app --bind 0.0.0.0:8000
