@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Buscador en archivos .md
echo ========================================
echo.

set /p "buscar=Ingresa el texto a buscar: "

if "%buscar%"=="" (
    echo No ingresaste ningun texto.
    pause
    exit /b
)

echo.
echo Buscando "%buscar%" en archivos .md...
echo.

set "encontrado=0"
set "salida=resultado_busqueda.txt"

echo Resultados de busqueda de "%buscar%" > "%salida%"
echo. >> "%salida%"

for %%f in (*.md) do (
    findstr /i /c:"%buscar%" "%%f" >nul
    if !errorlevel! == 0 (
        echo [✅] Encontrado en: %%f
        echo [✅] Encontrado en: %%f >> "%salida%"
        set "encontrado=1"
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