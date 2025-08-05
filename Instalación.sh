#!/bin/bash

# ██████╗ ███████╗██████╗ ████████╗███████╗ █████╗ ███╗   ███╗
# ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
# ██████╔╝█████╗  ██║  ██║   ██║   █████╗  ███████║██╔████╔██║
# ██╔══██╗██╔══╝  ██║  ██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
# ██║  ██║███████╗██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
# ╚═╝  ╚═╝╚══════╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

# Colores para mensajes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar si es root
if [ "$(id -u)" != "0" ]; then
    echo -e "${RED}[!] Este script debe ejecutarse como root.${NC}" >&2
    exit 1
fi

# Banner de inicio
echo -e "${YELLOW}"
cat << "EOF"
  ____           __  __         _____  _                         
 |  _ \ ___  ___|  \/  |_   _  |___ / / \   _ __ ___   ___ _ __ 
 | |_) / _ \/ __| |\/| | | | |   |_ \/ _ \ | '_ ` _ \ / _ \ '__|
 |  _ <  __/\__ \ |  | | |_| |  ___) / ___ \| | | | | |  __/ |   
 |_| \_\___||___/_|  |_|\__, | |____/_/   \_\_| |_| |_|\___|_|   
                        |___/                                    
EOF
echo -e "${NC}"

# Actualizar repositorios
echo -e "${GREEN}[+] Actualizando paquetes del sistema...${NC}"
apt-get update -qq || { echo -e "${RED}[!] Fallo al actualizar.${NC}"; exit 1; }

# Instalar dependencias básicas
echo -e "${GREEN}[+] Instalando dependencias...${NC}"
apt-get install -y -qq git python3 python3-pip nmap metasploit-framework || {
    echo -e "${RED}[!] Fallo al instalar dependencias críticas.${NC}";
    exit 1;
}

# Clonar repositorios adicionales (ejemplo: Impacket)
echo -e "${GREEN}[+] Clonando Impacket para ataques de red...${NC}"
git clone --quiet https://github.com/SecureAuthCorp/impacket.git /opt/impacket || {
    echo -e "${YELLOW}[!] Fallo al clonar Impacket (puede instalarlo manualmente después).${NC}";
}

# Instalar requisitos de Python
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}[+] Instalando módulos de Python...${NC}"
    pip3 install -q -r requirements.txt || {
        echo -e "${YELLOW}[!] Algunos módulos de Python fallaron (verifique manualmente).${NC}";
    }
fi

# Configurar permisos
echo -e "${GREEN}[+] Configurando permisos...${NC}"
chmod +x redteamxtreme.py  # Asegura que el script principal sea ejecutable

# Mensaje final
echo -e "\n${GREEN}[✔] Instalación completada. Ejecuta: ./redteamxtreme.py --help${NC}"
echo -e "${YELLOW}[!] ¡Recomendación! Configura tus API keys en config/default.conf${NC}"
