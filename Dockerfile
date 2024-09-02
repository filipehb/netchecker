# Use uma imagem base do Python
FROM python:3.12-slim

# Instale as ferramentas necessárias: ping e traceroute
RUN apt-get update && apt-get install -y \
    iputils-ping \
    traceroute \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY requirements.txt requirements.txt
COPY netchecker.py netchecker.py
COPY domains.txt domains.txt

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Execute o script
CMD ["python", "netchecker.py"]
