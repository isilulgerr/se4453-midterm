FROM python:3.10-slim

# Sistem paketleri
RUN apt-get update && apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# SSH için parola belirle
RUN echo 'root:rootpassword' | chpasswd

# Flask app'ini kopyala
WORKDIR /app
COPY . /app

# Gerekli paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Portları aç
EXPOSE 22 8000

# SSH ve gunicorn başlat
CMD ["/bin/bash", "startup.sh"]
