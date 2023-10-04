# Intro

This is a simple tool that processes a png image (ideally a screenshot of a mathematical formula) and returns the markdown text.
The base model is Nougat, first proposed in [Nougat: Neural Optical Understanding for Academic Documents](https://doi.org/10.48550/arXiv.2308.13418) and accessible via [HuggingFace](https://huggingface.co/) `transformers`.

# Usage guide

Clone git repo:
```git clone git@github.com:apiraccini/formulae.git```

Go to cloned repo:
```cd formulae```

Create virtual environment:
```python -m venv venv```

Activate virtual environment>
```venv\Scripts\activate```

Install requirements:
```pip install -r requirements.txt```

Run application:
```python app.py```
