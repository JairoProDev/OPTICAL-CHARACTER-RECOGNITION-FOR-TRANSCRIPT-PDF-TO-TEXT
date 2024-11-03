import gradio as gr
import PyPDF2

def generate(file, num_page):
    """
    Extrae texto de un archivo PDF.

    Args:
        file (UploadedFile): Archivo PDF subido por el usuario.
        num_page (int): Número de páginas a extraer.

    Returns:
        str: Texto extraído del PDF o mensaje de error.
    """
    num_page = int(num_page)
    try:
        # Crear un objeto PdfReader
        reader = PyPDF2.PdfReader(file.name)
        text = ""
        # Iterar sobre el número de páginas especificado
        for page_num in range(min(num_page, len(reader.pages))):
            page = reader.pages[page_num]
            # Extraer texto de cada página
            text += page.extract_text()
        return text if text else "No se pudo extraer texto del PDF."
    except Exception as e:
        # Manejar excepciones y devolver un mensaje de error
        return f"Error al procesar el archivo: {e}"

# Configurar la interfaz de Gradio
iface = gr.Interface(
    fn=generate,
    inputs=[
        gr.File(label="Sube tu archivo PDF"),
        gr.Number(label="Número de páginas", value=5, precision=0)
    ],
    outputs=gr.Textbox(),
    title="Convertidor de PDF a Texto",
    description="Sube un archivo PDF y especifica el número de páginas que deseas convertir a texto."
)

if __name__ == "__main__":
    # Iniciar la aplicación
    iface.launch()