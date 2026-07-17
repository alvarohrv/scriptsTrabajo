
# 📁 Creador Automatizado de Carpetas para Tickets

Script en Python que automatiza la creación de carpetas estructuradas para tickets, copiando y modificando plantillas de manera consistente.

## 📋 Requisitos

- Python 3.6 o superior
- Módulos estándar (no requiere instalaciones adicionales):
  - `os`, `re`, `shutil`, `sys`, `datetime`, `pathlib`
- Las plantillas base en una carpeta llamada `Base_MiTicket/` ubicada junto al script.
- Estructura inicial 📂
```
proyecto/
├── Base_MiTicket/
│   ├── MT.md          # Plantilla Markdown
│   └── index.sql      # Plantilla SQL
├── crear_carpeta_v2mm.py
├── runCreateFolder.bat
└── README.md
```
Nota: En ambas plantillas (`MT.md` e `index.sql`) de contener la palabra `Ticket` en algún lugar, será reemplazada por el nombre completo de la carpeta destino al ejecutar el script.

## 🛠️  Uso - Modo interactivo

Doble click sobre `crear_carpeta.bat` (o ejecutar `python crear_carpeta_v2MinMax.py` desde consola) y escribir el input cuando lo pida.
Ejemplo de formato de entrada: "MiTicket-22859 AguasManizales 10444"
De la forma "ticket entidad ticketid"

- **Ticket**: texto con guion y número al final, por ejemplo `MiTicket-22859`.
- **entidad**: nombre del cliente o ubicación, por ejemplo `AguasManizales`.
- **ticketid**: solo dígitos, por ejemplo `10444`.

nota: modo argumentos es opcional.

## 🔄 Flujo

- **Creación automatizada** de carpetas con formato `Ticket-Fecha-Cliente-Código`
- **Copia de plantillas** (Markdown y SQL) desde una carpeta base
- **Reemplazo inteligente** de marcador usando expresiones regulares
- **Crear subcarpeta** para archivos axuliares
- **Generación de archivos** de ticket con contenido informativo
- **Soporte para entrada interactiva** o por argumentos de línea de comandos


## 📁 Estructura de la Carpeta Creada

```
MiTicket-22859-260715-AguasManizales-10444/
├── MT-10444.md                    # Plantilla Markdown personalizada
├── index-10444.sql                # Plantilla SQL personalizada
└── adjuntos/
    └── MITICKET-22859.txt         # Archivo de ticket con información
```

## 📄 Licencia

Proyecto personal, pero puede ser modificado y usado con fines academicos.
