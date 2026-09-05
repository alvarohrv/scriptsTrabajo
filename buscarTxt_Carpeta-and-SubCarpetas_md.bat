@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Buscador en archivos .md (Incluye Subcarpetas)
echo ========================================
echo.

set /p "buscar=Ingresa el texto a buscar: "

if "%buscar%"=="" (
    echo No ingresaste ningun texto.
    pause
    exit /b
)

echo.
echo Buscando "%buscar%" en archivos .md y sus subcarpetas...
echo.

set "encontrado=0"
set "salida=resultado_busqueda.txt"

echo Resultados de busqueda de "%buscar%" > "%salida%"
echo. >> "%salida%"

:: El parámetro /R busca recursivamente en subcarpetas
:: 1. 'for /R' busca de manera recursiva (en la carpeta actual y en todas sus subcarpetas)
::    y va guardando temporalmente la ruta de cada archivo '.md' que encuentra en la variable '%%f'.

for /R %%f in (*.md) do (
    :: Evitamos que el buscador intente leer el propio archivo de salida si tuviera extensión .md por error (evita un bucle infinito)
    if not "%%f"=="%cd%\%salida%" (
        ::    '/i' ignora mayúsculas/minúsculas. '/c:"..."' busca la frase exacta.
        ::    nul oculta la salida de la búsqueda en la consola para que no se vea desordenado con textos extractos.
        findstr /i /c:"%buscar%" "%%f" >nul
        if !errorlevel! == 0 (
            :: Muestra en la pantalla de la consola que lo encontró y en qué archivo.
            echo [✅] Encontrado en: %%f
            :: El símbolo '>>' escribe (anexa) esa misma línea al final del archivo de reporte '%salida%'.
            echo [✅] Encontrado en: %%f >> "%salida%"
            :: Cambia esta variable a '1' para que el script sepa que al menos hubo una coincidencia.
            set "encontrado=1"
        )
    )
)


echo. >> "%salida%"
echo Busqueda completada. >> "%salida%"

echo.
if !encontrado! == 0 (
    echo [❌] No se encontro "%buscar%" en ningun archivo .md.
    echo No se encontro el texto >> "%salida%"
) else (
    echo [✅] Busqueda completada. Revisa el archivo %salida%
)

pause