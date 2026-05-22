

// 1. Definición del texto de entrada en formato Markdown sencillo
const texto = `# Título del Proyecto

## Subtítulo Técnico

Este es un **texto plano** de prueba para validar el comportamiento del script en la consola.

- Primer elemento de la lista
- Segundo elemento con **negrita interna**
- Tercer componente del bloque

Texto finalizado de manera correcta.`;

// 2. Función conversora de Markdown a HTML con estilos en línea
function transformarMarkdownAHtml(markdown) {
    // Separar el texto por líneas individuales
    const lineas = markdown.split('\n');
    let htmlResultado = [];
    let enLista = false;

    for (let i = 0; i < lineas.length; i++) {
        let linea = lineas[i].trim();

        // Caso de uso: Línea vacía
        if (linea === '') {
            if (enLista) {
                htmlResultado.push('</ul>');
                enLista = false;
            }
            continue;
        }

        // Procesar primero las negritas globales (**texto**) en la línea
        linea = linea.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

        // Caso de uso: Encabezado H1 (#) -> 22px
        if (linea.startsWith('# ')) {
            if (enLista) { htmlResultado.push('</ul>'); enLista = false; }
            const contenido = linea.replace('# ', '');
            htmlResultado.push(`<h1 style="font-size: 22px; font-family: Arial, sans-serif;">${contenido}</h1>`);
        }
        // Caso de uso: Encabezado H2 (##) -> 18px
        else if (linea.startsWith('## ')) {
            if (enLista) { htmlResultado.push('</ul>'); enLista = false; }
            const contenido = linea.replace('## ', '');
            htmlResultado.push(`<h2 style="font-size: 18px; font-family: Arial, sans-serif;">${contenido}</h2>`);
        }
        // Caso de uso: Elementos de lista (- item)
        else if (linea.startsWith('- ')) {
            if (!enLista) {
                htmlResultado.push('<ul style="font-size: 16px; font-family: Arial, sans-serif;">');
                enLista = true;
            }
            const contenido = linea.replace('- ', '');
            htmlResultado.push(`  <li>${contenido}</li>`);
        }
        // Caso de uso: Texto plano -> 16px
        else {
            if (enLista) { htmlResultado.push('</ul>'); enLista = false; }
            htmlResultado.push(`<p style="font-size: 16px; font-family: Arial, sans-serif; margin: 0">${linea}</p>`);
        }
    }

    // Cierre de seguridad si el documento finaliza dentro de una lista
    if (enLista) {
        htmlResultado.push('</ul>');
    }

    // Retorna el string HTML unificado por saltos de línea
    return htmlResultado.join('\n');
}

// 3. Ejecución y almacenamiento en la variable global
const htmlFinal = transformarMarkdownAHtml(texto);

// Mostrar el resultado limpio en la consola
console.log(htmlFinal);