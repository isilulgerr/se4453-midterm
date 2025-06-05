#!/bin/bash

# SSH başlat
service ssh start

# Flask uygulamasını başlat (gunicorn ile)
exec gunicorn app:app --bind 0.0.0.0:8000
