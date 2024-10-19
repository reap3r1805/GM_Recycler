document.addEventListener('DOMContentLoaded', function() {
    const buscarClienteInput = document.getElementById('buscar_cliente');
    const resultadosBusqueda = document.querySelector('resultados-busqueda');
    const clienteSelect = document.getElementById('id_cliente');
    const addDetalleButton = document.getElementById('add-detalle');
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
        const newIndex = parseInt(totalForms.value);
        const template = documnet.querySelector('.detalle-form').cloneNode(true);

        template.innerHTML = template.innerHTML.replace(/detalles-\d+/, `detalles-${newIndex}`);
        template.querySelectorAll('input, select').forEach(input => {
            input.value = '';
            input.id = input.id.replace(/detalles-\d+/, `detalles-${newIndex}`);
        });

        detallesContainer.appendChild(template);
        totalForms.value = newIndex + 1;
    });

    detallesContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('remove-detalle')) {
            e.target.closest('.detalle-form').remove();
        }
    });
    

});