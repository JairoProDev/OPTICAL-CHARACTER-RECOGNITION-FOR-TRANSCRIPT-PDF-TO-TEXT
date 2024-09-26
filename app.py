import gradio as gr
from gradio_client import Client, handle_file

def generate(file, num_page):
	path_file = file.name if not isinstance(file, str) else file

	client = Client("k9lab/p_pdf_to_text")
	result = client.predict(
			file_name=handle_file(path_file),
			num_page=num_page,
			api_name="/predict"
	)
	return result

iface = gr.Interface(
    fn=generate,
    inputs=[
        gr.File(label="Sube tu archivo PDF"),
        gr.Number(label="Número de páginas", value=5)
    ],
	outputs=[gr.Markdown(), gr.File()],
    title="Convertidor de PDF a texto",
    description="Sube un archivo PDF y especifica el número de página que deseas convertir a texto."
)

iface.launch()