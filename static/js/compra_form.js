document.addEventListener('DOMContentLoaded', function() {
    const buscarClienteInput = document.getElementById('buscar_cliente');
    const resultadosBusqueda = document.querySelector('resultados-busqueda');
    const clienteSelect = document.getElementById('id_cliente');
    const addDetalleButton = document.getElementById('add-detalle');
    if (!addDetalleButton) {
        console.error('El botón de agregar detalle no se encontró');
        return;
    }
    const detallesContainer = document.getElementById('detalles-container');

    buscarClienteInput.addEventListener('input', function() {
        const query = this.value;
        if (query.length > 2) {
            fetch(`/compra/buscar-cliente/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    resultadosBusqueda.innerHTML = '';
                    data.forEach(cliente => {
                        const div = document.createElement('div');
                        div.textContent = `${cliente.nombre} - ${cliente.telefono}`;
                        div.addEventListener('click', function() {
                            clienteSelect.value = cliente.id;
                            buscarClienteInput.value = cliente.nombre;
                            resultadosBusqueda.innerHTML = '';
                        });
                        resultadosBusqueda.appendChild(div);
                    });
                });
        }else{
            resultadosBusqueda.innerHTML = '';
        }
    });

    addDetalleButton.addEventListener('click', function() {
        const totalForms = document.querySelector('#id_detalles-TOTAL_FORMS');
        if (!totalForms) {
            console.error('El campo de total de formularios no se encontró');
            return;
        }
        const newIndex = parseInt(totalForms.value);
        const templateElement = document.querySelector('.detalle-form');
        if (!templateElement) {
            console.error('El template de detalle no se encontró');
            return;
        }
        const template = templateElement.cloneNode(true);
        //const template = document.querySelector('.detalle-form').cloneNode(true);

        template.innerHTML = template.innerHTML.replace(/detalles-\d+/, `detalles-${newIndex}`);
        template.querySelectorAll('input, select').forEach(input => {
            input.value = '';
            input.id = input.id.replace(/detalles-\d+/, `detalles-${newIndex}`);
        });

        detallesContainer.appendChild(template);
        totalForms.value = newIndex + 1;
        showNotification('Producto agregado correctamente');
    });

    detallesContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('remove-detalle')) {
            e.target.closest('.detalle-form').remove();
        }
    });

    function showNotification(message, type = 'success') {
        Toastify({
            text: message,
            duration: 3000,
            close: true,
            gravity: "top", 
            position: "right", 
            backgroundColor: type === 'success' ? "linear-gradient(to right, #00b09b, #96c93d)" : 
                             type === 'error' ? "linear-gradient(to right, #ff5f6d, #ffc371)" :
                             "linear-gradient(to right, #00b09b, #96c93d)",
        }).showToast();
    }

    document.querySelector('form').addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Asumiendo que estás usando fetch para enviar el formulario
        fetch(this.action, {
            method: 'POST',
            body: new FormData(this),
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                showNotification('Compra guardada correctamente');
                // Redirigir o actualizar la página según sea necesario
            } else {
                showNotification('Error al guardar la compra', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showNotification('Error al procesar la solicitud', 'error');
        });
    });
    

});