# Formulae

## Intro

This is a simple tool that processes a png image (ideally a screenshot of a mathematical formula) and returns the markdown text.
The base model is Nougat, first proposed in [Nougat: Neural Optical Understanding for Academic Documents](https://doi.org/10.48550/arXiv.2308.13418) and accessible via [HuggingFace](https://huggingface.co/) `transformers`.

## Usage guide

First clone git repo in a directory of your choice,
```bash
git clone https://github.com/apiraccini/formulae.git
cd formulae
```

then you can either set up the app from terminal
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

or build a docker image and run it in a container
```bash
docker build -t formulae_app .
docker run -p 7860:7860 formulae_app
```

and paste the URL printed in the terminal in your browser.

## Base utilities

You can also use the base utilities provided for handling files directly from python code.
Inside the cloned repository, in a python shell, you can do
```python
from utils.app_utils import process_formula, process_folder

text = process_formula('your_image_folder/your_image.png')
print(text)

process_folder('your_image_folder')
```
