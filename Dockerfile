FROM python:3.10-slim

# Actualizar el sistema e instalar las dependencias necesarias de una sola vez
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    bash \
    ffmpeg \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements primero para aprovechar la caché de Docker
COPY requirements.txt .

RUN pip3 install --no-cache-dir wheel && \
    pip3 install --no-cache-dir -U -r requirements.txt

# Copiar el resto del código del proyecto
COPY . .

# Comando de inicio
CMD flask run -h 0.0.0.0 -p 8000 & python3 -m devgagan
