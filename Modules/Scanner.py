import nmap
import requests

class NetworkScanner:
    def __init__(self, target, stealth=False):
        self.target = target
        self.stealth = stealth
        self.nm = nmap.PortScanner()
        
    def run(self):
        """Ejecuta el escaneo con Nmap + consulta Shodan (si hay API key)."""
        try:
            print(f"[*] Escaneando {self.target} (Stealth: {self.stealth})...")
            scan_args = "-sS -T4" if self.stealth else "-A -T4"
            
            self.nm.scan(hosts=self.target, arguments=scan_args)
            for host in self.nm.all_hosts():
                print(f"\n[+] Host: {host}")
                for proto in self.nm[host].all_protocols():
                    print(f"  Protocolo: {proto}")
                    ports = self.nm[host][proto].keys()
                    for port in ports:
                        print(f"    Puerto {port}: {self.nm[host][proto][port]['state']}")
                        
        except Exception as e:
            raise Exception(f"Error en escaneo: {str(e)}")
