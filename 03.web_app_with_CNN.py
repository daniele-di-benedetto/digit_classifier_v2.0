import numpy as np
from gradio import Interface
from gradio.components import Image
from gradio.components import Label
from tensorflow.keras.models import load_model
from src.utils import *


model = load_model('.\model\CNN_Model.h5')
input_image = Image(image_mode="L", invert_colors=True, source="canvas", label="INPUT DIGIT")
output_labels = Label(label="MODEL PREDICTION")
title = "Digit classifier with Deep Learning"
description = "<center>This project is a demo for handwritten digits recognition.</center>"


def predict_image(image):
    labels = np.arange(start=0, stop=10, dtype=int).astype(str)
    resized_image = canvas_to_28x28(source=image)
    processed_image = (resized_image / 255).reshape(-1,28,28,1)
    probas = model.predict(processed_image)[0].astype(object)
    result = {label: proba for label, proba in zip(labels, probas)}
    return result


interface = Interface(
    fn=predict_image,
    inputs=input_image,
    outputs=output_labels,
    title=title,
    description=description,
    allow_flagging="never"
    )
interface.launch(share=True)
