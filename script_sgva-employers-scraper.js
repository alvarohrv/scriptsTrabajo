(async () => {
  const tarjetas = document.querySelectorAll('.divSolicitudRequeridaCasillaContenedor');
  const resultados = [];

  for (let i = 0; i < tarjetas.length; i++) {
    const tarjeta = tarjetas[i];

    // Nombre de la empresa
    const nombreEmpresa = tarjeta.querySelector('.aprendizLabelTituloSolicitudesBA')?.innerText.trim();

    // Simular clic en el botón "Ver - Aplicar"
    const boton = tarjeta.querySelector('button#solicitud_aplicar');
    boton.click();

    // Esperar a que se abra el modal
    await new Promise(resolve => setTimeout(resolve, 800)); // puedes ajustar el tiempo si el modal tarda más

    // Modal activo
    const modal = document.querySelector('.modal-content.aprendizModal');

    const personaContacto = modal.querySelector('#lbl_modal_solicitud_contacto')?.innerText.trim();
    const direccion = modal.querySelector('#lbl_modal_solicitud_direccion')?.innerText.trim();
    const telefono = modal.querySelector('#lbl_modal_solicitud_telefono')?.innerText.trim();
    const email = modal.querySelector('#lbl_modal_solicitud_email')?.innerText.trim();
    const perfil = modal.querySelector('#lbl_modal_solicitud_perfiln')?.innerText.trim();
    const funciones = modal.querySelector('#lbl_modal_solicitud_funciones')?.innerText.trim();

    resultados.push({
      empresa: nombreEmpresa,
      contacto: personaContacto,
      direccion: direccion,
      telefono: telefono,
      email: email,
      perfil: perfil,
      funciones: funciones
    });

    // Cerrar el modal
    const btnCerrar = modal.querySelector('.close');
    btnCerrar.click();

    // Esperar a que se cierre el modal antes de continuar
    await new Promise(resolve => setTimeout(resolve, 500));
  }

  console.log(resultados);
  console.log(JSON.stringify(resultados, null, 2));
})();
