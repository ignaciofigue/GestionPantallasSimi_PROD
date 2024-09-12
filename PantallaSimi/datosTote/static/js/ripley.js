function alertaProductosRestantes(cantidad) {
    if (cantidad < 5) {
        alert("Quedan menos de 5 productos.");
        var audio = new Audio('{% static "audio/alert.mp3" %}');
        audio.play();
    }
}

function reportarObjetoPerdido() {
    var codigo = document.getElementById("codigoObjetoPerdido").value;
    alert("Se ha reportado el objeto con código: " + codigo);
    // Aquí puedes agregar la lógica para enviar el reporte a tu backend
    document.getElementById("codigoObjetoPerdido").value = '';  // Limpiar el input después de reportar
}

// Función para filtrar la tabla por el SKU ingresado
function filterTable() {
    var input = document.getElementById("codigoFilter").value.toUpperCase();
    var table = document.querySelector("table tbody");
    var rows = table.getElementsByTagName("tr");

    for (var i = 0; i < rows.length; i++) {
        var codigo = rows[i].getElementsByTagName("td")[0].textContent.toUpperCase();
        if (codigo.indexOf(input) > -1) {
            rows[i].style.display = "";  // Mostrar la fila si coincide con el filtro
        } else {
            rows[i].style.display = "none";  // Ocultar la fila si no coincide
        }
    }
}

// Función para limpiar la tabla cuando se despachan todos los productos del SKU
function limpiarTabla() {
    var tableBody = document.querySelector("table tbody");
    tableBody.innerHTML = "";  // Limpiar todas las filas de la tabla
}

// Ejemplo de uso de `limpiarTabla` después de que se despachen los productos
function procesarDespacho() {
    var cantidadTotal = parseInt(document.getElementById("countdown-timer").textContent.split(":")[1].trim());
    if (cantidadTotal === 0) {
        limpiarTabla();  // Llamar a la función para limpiar la tabla cuando no haya más productos
    }
}
