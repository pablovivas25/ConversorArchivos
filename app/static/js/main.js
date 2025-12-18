const form = document.getElementById("convertForm");
const statusDiv = document.getElementById("status");
const fileInput = document.getElementById("file");
const formatSelect = document.getElementById("target_format");

// Cuando se selecciona un archivo → pedir formatos al backend
fileInput.addEventListener("change", async () => {
  const file = fileInput.files[0];
  if (!file) return;

  const extension = file.name.split(".").pop().toLowerCase();

  formatSelect.innerHTML = "<option>Cargando formatos...</option>";

  try {
    const response = await fetch(`/formats/${extension}`);
    const data = await response.json();

    formatSelect.innerHTML = "<option value=''>Formato destino</option>";

    if (data.outputs.length === 0) {
      const option = document.createElement("option");
      option.textContent = "No hay conversiones disponibles";
      option.disabled = true;
      formatSelect.appendChild(option);
      return;
    }

    data.outputs.forEach((format) => {
      const option = document.createElement("option");
      option.value = format;
      option.textContent = format.toUpperCase();
      formatSelect.appendChild(option);
    });
  } catch (error) {
    formatSelect.innerHTML =
      "<option disabled>Error al cargar formatos</option>";
  }
});

// Envío del formulario
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const file = fileInput.files[0];
  const targetFormat = formatSelect.value;

  if (!file || !targetFormat) {
    statusDiv.innerText = "Seleccioná archivo y formato";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("target_format", targetFormat);

  statusDiv.innerText = "Convirtiendo...";

  try {
    const response = await fetch("/convert", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Error en la conversión");
    }

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = `archivo_convertido.${targetFormat}`;
    a.click();

    statusDiv.innerText = "Conversión exitosa ✔";
  } catch (error) {
    statusDiv.innerText = "Error al convertir ❌";
  }
});
