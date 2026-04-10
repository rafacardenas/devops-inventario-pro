#!/bin/bash

echo "Actualizando sistema..."
sudo apt update -y

echo "Instalando herramientas..."
sudo apt install -y git docker.io python3 python3-pip

echo "Instalación completada"

