/*v260703*/
async function buscar(cuentasInput, fechaInteres, ignorarInput) {
    if (!cuentasInput || cuentasInput.trim() === '') {
        console.error('❌ Debes proporcionar al menos una cuenta');
        return;
    }
    const cuentasRegex = /^[\d,\s]+$/;
    if (!cuentasRegex.test(cuentasInput)) {
        console.error(`❌ Formato inválido: "${cuentasInput}". Solo se permiten números y comas (vale, se te puede ir un espacios).`);
        return;
    }
    const cuentas = cuentasInput.split(',').map(c => c.trim()).filter(c => c !== '');
    if (!fechaInteres) {
        console.error('❌ Debes proporcionar un segundo parametro, una fecha mes/dia/año segun log');
        return;
    }
    let ignorar = [];
    if (ignorarInput) {
        ignorar = ignorarInput.split(',')
            .map(i => i.trim())
            .filter(i => i !== '')
            .map(i => i.replace(/\.txt$/i, '')); 
    }
    
    
    

    
    
    
    /* NODO:::::::::::::::::
        " 6/25/2026  8:14 AM         1476 "
    <a href="/applogs/Mod_Admin/FNA/PAG_10020_20260624_081300.TXT">PAG_10020_20260624_081300.TXT</a>
    */

    const resumenExistente = document.querySelector('#resumen-busqueda');
        if (resumenExistente) {
            resumenExistente.remove();
    }


    
    const todosLosEnlaces = document.querySelectorAll('a[href$=".TXT"]');
    const enlacesPAGgeneral = Array.from(todosLosEnlaces).filter(a => {
        const href = a.getAttribute('href');
        return href && href.includes('/PAG_');
    });
    if (enlacesPAGgeneral.length === 0) {
        console.warn('⚠️ No se encontraron archivos PAG_ en esta página.');
        return;
    }

    
    const enlacesFiltrados = [];
    for (let enlace of enlacesPAGgeneral) {
        let nodoAnterior = enlace.previousSibling; 
        let textoConFechaInteres = ''; 
        while (nodoAnterior) {
            if (nodoAnterior.nodeType === Node.TEXT_NODE) {
                textoConFechaInteres = nodoAnterior.textContent.trim();
                break;
            }
            nodoAnterior = nodoAnterior.previousSibling; 
        }
        if (textoConFechaInteres.includes(fechaInteres)) { 
            const nombreArchivo = enlace.textContent.trim();
            
            if (!ignorar.some(ign => nombreArchivo.includes(ign))) { 
                enlacesFiltrados.push({
                    nombre: nombreArchivo,
                    url: enlace.href,
                    elemento: enlace
                });
            } else {
                
                enlace.style.color = 'gray';
                enlace.style.opacity = '0.8';
            }
        }
    }
    if (enlacesFiltrados.length === 0) {
        console.warn(`⚠️ No se encontraron archivos PAG_ para la fecha ${fechaInteres}.`);
        return;
    }
    console.log(`📁 ${enlacesFiltrados.length} archivos a revisar.`);

    
    
    const resultados = {};

    for (let archivo of enlacesFiltrados) {
        console.log(`📄 Leyendo: ${archivo.nombre} ...`);
        try {
            const response = await fetch(archivo.url);
            if (!response.ok) { 
                console.warn(`   ❌ Error al leer ${archivo.nombre}: ${response.status}`);
                continue;
            }
            const contenido = await response.text();
            
            const primeraLinea = contenido.split('\n')[0] || '';
            
            let cuentaEncontrada = false; 
            for (let cuenta of cuentas) {
                if (primeraLinea.includes(cuenta)) {
                    if (resultados[cuenta]) { 
                        if (Array.isArray(resultados[cuenta])) {
                            resultados[cuenta].push(archivo.nombre);
                        } else { 
                            resultados[cuenta] = [resultados[cuenta], archivo.nombre];
                        }
                    } else {
                        resultados[cuenta] = archivo.nombre;
                    }
                    
                    cuentaEncontrada = true;
                    
                }
            }
            

            archivo.elemento.style.color = 'black';
            archivo.elemento.style.opacity = '1';
            archivo.elemento.style.border = 'none';
            archivo.elemento.style.borderRadius = 'none';
            archivo.elemento.style.padding = '0px';
            archivo.elemento.style.backgroundColor = 'transparent';
            archivo.elemento.style.display = 'inline-block';

            if (!cuentaEncontrada) {
                
                archivo.elemento.style.color = '#141414';
                archivo.elemento.style.opacity = '0.8';   
                
            } else {
                
                archivo.elemento.style.color = 'green';
                archivo.elemento.style.border = '2px solid green';
                archivo.elemento.style.borderRadius = '4px';
                archivo.elemento.style.padding = '2px';
                archivo.elemento.style.backgroundColor = '#e6ffed';
                


                
                const cuentasEncontradasEnEsteArchivo = [];
                for (let cuenta of cuentas) {
                    if (primeraLinea.includes(cuenta)) {
                        cuentasEncontradasEnEsteArchivo.push(cuenta);
                    }
                }

                
                const cuentasTexto = ` 🔍${cuentasEncontradasEnEsteArchivo.join(', ')}`;
                archivo.elemento.insertAdjacentText('afterend', cuentasTexto);
            }

        } catch (error) {
            console.error(`   ❌ Error al leer ${archivo.nombre}:`, error.message);
        }
    }

    
    console.log('\n✅ === RESULTADOS DE LA BÚSQUEDA ===');
    if (Object.keys(resultados).length === 0) {
        console.log('❌ Ninguna cuenta fue encontrada en los archivos revisados.');
    } else {
        console.log(JSON.stringify(resultados, null, 2));
        
    }

    
    const resumenDiv = document.createElement('div');
    resumenDiv.id = 'resumen-busqueda';
    resumenDiv.style.cssText = 'position: fixed; bottom: 10px; right: 10px; background: white; border: 2px solid #333; padding: 15px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); z-index: 9999; max-width: 400px; font-family: monospace; font-size: 12px;';
    resumenDiv.innerHTML = `<strong>Resultados de búsqueda</strong><br><pre>${JSON.stringify(resultados, null, 2)}</pre>`;
    document.body.appendChild(resumenDiv);

    console.log('🎯 Script finalizado.');
};


