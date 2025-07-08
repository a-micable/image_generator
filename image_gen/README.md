# Image Generator with Style Transfer
![ss](./ss.JPG)
This Streamlit app generates unique images based on a text prompt and an optional style image, using the `kandinsky-community/kandinsky-2-2-decoder` model from Hugging Face. The model combines text-guided generation with image-to-image transformations, allowing users to create art with custom styles and themes.

## Features

- **Text-Guided Image Generation**: Enter a description, and the app generates an image based on the prompt.
- **Style Transfer with Optional Initial Image**: Upload an initial image to guide the style of the generated image, or use the default style provided by the app.
- **Streamlit Interface**: Simple and intuitive interface for interactive image generation.

## How It Works

1. **Load the Model**: The app uses `AutoPipelineForImage2Image` from the Hugging Face `diffusers` library to load the pre-trained model `kandinsky-2-2-decoder`. Model resources are managed with CPU offload for efficiency.
2. **User Input**: A text prompt describes the image concept. Optionally, users can upload an initial style image.
3. **Generate Image**: Upon clicking "Generate Image," the app runs the text prompt through the model, applying the style of the initial image if provided.
4. **Display**: Both the initial (style) and generated images are displayed in a grid layout.

## Installation

1. Clone the repository and navigate to the project directory.
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```
2. Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app with Streamlit.
    ```bash
    streamlit run app.py
    ```

## Usage

1. Start the app by running the command above. The interface should open in your default web browser.
2. Enter a descriptive prompt for the image you want to generate.
3. Optionally, upload a style image to guide the style of the generated image.
4. Click "Generate Image" to see the results.

## Requirements

Dependencies in `requirements.txt`:

```text
streamlit
torch
transformers
diffusers
Pillow
