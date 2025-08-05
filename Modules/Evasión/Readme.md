**Técnicas de Evasión Avanzada**  

*Módulos para evadir EDRs, AVs y análisis forense. Escrito en Python y C para máxima eficiencia.*  

```bash
modules/evasion/
├── bypass_av.py           # Bypass de Antivirus (XOR, sandbox checks)
├── process_injection.py   # Inyección en memoria (Reflective DLL, Process Hollowing)
└── syscalls/              # Llamadas directas a APIs/Syscalls (Opcional)
```

---

## **🔍 Módulos Disponibles**  

### **1. `bypass_av.py`**  
**Técnicas Implementadas**:  
- **XOR Encryption**: Ofuscación dinámica de payloads.  
- **Sandbox Detection**: Verifica si se ejecuta en un entorno virtualizado.  
- **Polymorphic Code**: Genera variantes únicas del shellcode.  

**Uso**:  
```python
from evasion.bypass_av import AVBypass

payload = b"\x90\x90\x90"  # Shellcode ejemplo
encrypted_payload = AVBypass.xor_encrypt(payload, key=0x3A)
```

---

### **2. `process_injection.py`**  
**Técnicas Implementadas**:  
- **Reflective DLL Injection**: Carga DLLs directamente en memoria (sin tocar disco).  
- **Process Hollowing**: Reemplaza código de procesos legítimos (ej: `explorer.exe`).  

**Requisitos**:  
- Windows 10/11.  
- Privilegios administrativos.  

**Ejemplo**:  
```python
from evasion.process_injection import reflective_dll_injection

dll_bytes = open("evil.dll", "rb").read()
reflective_dll_injection(pid=1337, dll_bytes=dll_bytes)
```

---

## **⚡ Casos de Uso Típicos**  
1. **Evadir Windows Defender**:  
   ```python
   from evasion.bypass_av import AVBypass
   payload = AVBypass.generate_poly_shellcode(shellcode)
   ```  
2. **Inyectar en `lsass.exe`**:  
   ```python
   inject_to_process("lsass.exe", "spoofed.dll")
   ```  

---

## **🛠️ Requisitos**  
- **Python 3.10+** (para módulos base).  
- **ctypes** (para interacción con APIs de Windows).  
- **DLLs compiladas** (para inyección, usa [msfvenom](https://github.com/rapid7/metasploit-framework/wiki)).  

---

## **📌 Mejoras Planeadas**  
- [ ] Integrar **syscalls directos** (via [Hell's Gate](https://github.com/am0nsec/HellsGate)).  
- [ ] Añadir **inyección en kernel-mode** (requiere drivers).  
- [ ] Soporte para **Linux** (eBPF, LD_PRELOAD hijacking).  

---

## **⚠️ Advertencia**  
Estas técnicas son **fácilmente detectables** si se usan sin modificaciones. Siempre:  
1. **Personaliza** el código (cambia firmas estáticas).  
2. **Combina** múltiples técnicas (ej: XOR + Process Hollowing).  
3. **Prueba** en entornos controlados antes de operaciones reales.  

---

## **📚 Recursos Recomendados**  
- [MITRE ATT&CK: Defense Evasion](https://attack.mitre.org/tactics/TA0005/)  
- [Malware Development Books](https://maldevacademy.com/)  
- [Awesome AV Evasion](https://github.com/rootkit-io/awesome-malware-development)  

---

```markdown
¿Problemas? Abre un *issue* o contribuye con nuevas técnicas via *pull request*!  
```  

--- 
