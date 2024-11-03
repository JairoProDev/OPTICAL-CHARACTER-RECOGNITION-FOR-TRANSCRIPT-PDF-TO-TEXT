---
title: Pdf To Text
emoji: 🦾
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# Convertidor de PDF a Texto

Aplicación web sencilla para convertir archivos PDF a texto utilizando Gradio y PyPDF2.

## Descripción

Esta aplicación permite subir un archivo PDF y extraer el texto de un número especificado de páginas.

## Características

- **Extracción de texto:** Utiliza `PyPDF2` para extraer texto de archivos PDF.
- **Interfaz web intuitiva:** Gracias a `Gradio`, ofrece una interfaz fácil de usar.
- **Personalización:** Selecciona el número de páginas a convertir.

## Requisitos previos

- Python 3.x instalado en tu máquina.

## Instalación

1. **Clona este repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/convertidor-pdf-texto.git
   cd convertidor-pdf-texto