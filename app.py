import gradio as gr
from utils.app_utils import process_formula

with gr.Blocks(theme=gr.themes.Monochrome()) as demo:

    gr.Markdown('# Formulae 🤗📑\nTired of writing long markdown formulas for \LaTex? ')

    image = gr.Image(label='Load the screenshot of your formula here', source='upload', type='filepath')
    btn = gr.Button(label='Process', size='sm')
    formula = gr.Textbox(label='Your formula', placeholder='When in doubt, 42 is a good answer.')

    btn.click(fn=process_formula, inputs=image, outputs=formula, api_name='process_formula')

if __name__ == '__main__':
    demo.launch()