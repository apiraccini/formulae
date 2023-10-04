from PIL import Image, ImageOps
from transformers import AutoProcessor, VisionEncoderDecoderModel, StoppingCriteriaList
from .misc import  StoppingCriteriaScores
import torch


def process_formula(filepath_png):

    # open image with pillow      
    image = Image.open(filepath_png).convert('RGB')
    #image = get_a4(image_raw)

    # load model and processor
    processor = AutoProcessor.from_pretrained("facebook/nougat-small")
    model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-small")

    # move the model to GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    # prepare image for the model
    pixel_values = processor(images=image, data_format='channels_first', return_tensors="pt").pixel_values

    # autoregressively generate tokens, with custom stopping criteria (as defined by the Nougat authors)
    outputs = model.generate(
        pixel_values.to(device),
        min_length=1,
        max_length=3584,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
        return_dict_in_generate=True,
        output_scores=True,
        stopping_criteria=StoppingCriteriaList([StoppingCriteriaScores()]),
        )

    # decode the generated IDs back to text and postprocess the generation.
    generated = processor.batch_decode(outputs[0], skip_special_tokens=True)[0]
    markdown = processor.post_process_generation(generated, fix_markdown=False)

    return markdown