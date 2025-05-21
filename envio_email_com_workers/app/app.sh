#! /bin/sh
apt-get update && apt-get install -y netcat
# Espera o banco responder na porta 5432
echo "Aguardando o banco de dados ficar disponível..."
while ! nc -z db 5432; do
  sleep 2
done

pip install bottle==0.12.13 psycopg2==2.7.3.2 redis==2.10.5
python -u sender.py