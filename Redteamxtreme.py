#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔥 RedTeam-Xtreme Core 🔥
Framework modular para operaciones de Red Team en Linux.
"""

import argparse
import sys
import os
from time import sleep
from modules.scanner import NetworkScanner
from modules.exploiter import ExploitEngine
from modules.persistence import PersistenceManager

# Configuración de colores (para mensajes estilo hacker)
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    END = "\033[0m"

# Banner ASCII art
BANNER = f"""
{Colors.RED}
  _____           ______      __  __         _____  _                         
 |  __ \ ___  ___|  ____|    |  \/  |_   _  |___ / / \   _ __ ___   ___ _ __ 
 | |__) / _ \/ __| |__ ______| |\/| | | | |   |_ \/ _ \ | '_ ` _ \ / _ \ '__|
 |  _ <  __/\__ \  __|______| |  | | |_| |  ___) / ___ \| | | | | |  __/ |   
 |_| \_\___||___/_|         |_|  |_|\__, | |____/_/   \_\_| |_| |_|\___|_|   
                                    |___/                                    
{Colors.END}
{Colors.CYAN}>> Versión 1.0 - By @YourHandle <<{Colors.END}
"""

def print_banner():
    """Muestra el banner de inicio."""
    print(BANNER)
    sleep(1)

def parse_args():
    """Configura los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description=f"{Colors.YELLOW}RedTeam-Xtreme: Framework para operaciones avanzadas.{Colors.END}",
        epilog=f"{Colors.PURPLE}Ejemplo: ./redteamxtreme.py --scan 192.168.1.0/24 --stealth{Colors.END}"
    )
    
    # Grupo principal de comandos
    group = parser.add_argument_group("Opciones principales")
    group.add_argument(
        "--scan", 
        metavar="IP/Rango", 
        help="Escaneo de red (nmap + OSINT integrado)"
    )
    group.add_argument(
        "--exploit", 
        metavar="CVE", 
        help="Ejecuta un exploit (ej: CVE-2023-1234)"
    )
    group.add_argument(
        "--persist", 
        action="store_true", 
        help="Establece persistencia en el sistema objetivo"
    )
    
    # Opciones avanzadas
    advanced = parser.add_argument_group("Opciones avanzadas")
    advanced.add_argument(
        "--stealth", 
        action="store_true", 
        help="Modo sigiloso (evita detección)"
    )
    advanced.add_argument(
        "--output", 
        metavar="FILE", 
        default="results.txt", 
        help="Guardar resultados en un archivo"
    )
    
    return parser.parse_args()

def main():
    """Función principal."""
    print_banner()
    args = parse_args()
    
    try:
        if args.scan:
            print(f"{Colors.GREEN}[+] Iniciando escaneo en {args.scan}...{Colors.END}")
            scanner = NetworkScanner(target=args.scan, stealth=args.stealth)
            scanner.run()
            
        elif args.exploit:
            print(f"{Colors.GREEN}[+] Explotando {args.exploit}...{Colors.END}")
            exploiter = ExploitEngine(cve_id=args.exploit)
            exploiter.execute()
            
        elif args.persist:
            print(f"{Colors.GREEN}[+] Configurando persistencia...{Colors.END}")
            persistence = PersistenceManager()
            persistence.install()
            
        else:
            print(f"{Colors.RED}[!] No se especificó una acción. Usa --help.{Colors.END}")
            
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Interrupción del usuario. Saliendo...{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[!] Error crítico: {str(e)}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
