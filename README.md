# digit_classifier_v2.0 <br> <text style="font-size:2vw">*see also [digit_classifier_v1.0](https://github.com/andrea-cadeddu/digit_classifier)*</text>

*Image Classification*

This project shows how to use deep learning to analyze digit images. <br> In addition, an extra part has been added where it is shown how you can create an interactive demo to show the model using [Gradio](https://github.com/gradio-app/gradio).  

<center>
<img src="https://www.researchgate.net/profile/Steven-Young-5/publication/306056875/figure/fig1/AS:393921575309346@1470929630835/Example-images-from-the-MNIST-dataset.png" class="center"  width="85%" height="auto">
</center>   
<p align="center" style="font-style: italic; font-size:2vw">
Example images from the MNIST dataset.<br>
</p>

---
## Content of the notebooks
1. [Explorative data analysis](https://github.com/daniele-di-benedetto/digit_classifier_v2.0/blob/main/01.explorative_data_analysis.ipynb)
2. [Model training](https://github.com/daniele-di-benedetto/digit_classifier_v2.0/blob/main/02.train_CNN_Model.ipynb)
3. [Web app creation](https://github.com/daniele-di-benedetto/digit_classifier_v2.0/blob/main/03.web_app_with_CNN.py)

---

## Project requirements
* Python >= 3.10
* A virtual environment with the following libraries installed:
    * gradio
    * matplotlib
    * numpy
    * opencv-python
    * scikit-learn
    * tensorflow
---

## Install requirements
To install the project requirements, it is advisable to create a virtual environment to isolate dependencies and avoid errors with your Python system installation.  
To create a virtual environment, you can use [this guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) directly from the official documentation of Python.  
Once the virtual environment has been set up, to install the required project packages one has to run the following instruction from the terminal:
```shell
pip install -r requirements.txt
```
---

## Use notebooks online
Thanks to [Binder](https://mybinder.org/), it is possible to interact and run these notebooks online