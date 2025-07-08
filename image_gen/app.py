import streamlit as st
from diffusers import AutoPipelineForImage2Image
from diffusers.utils import make_image_grid, load_image
import torch
from PIL import Image

# Function to load and cache model
@st.cache_resource
def load_pipeline():
    pipeline = AutoPipelineForImage2Image.from_pretrained(
        "kandinsky-community/kandinsky-2-2-decoder",
        torch_dtype=torch.float16,
        use_safetensors=True
    )
    pipeline.enable_model_cpu_offload()
    return pipeline

# Set up Streamlit UI components
st.title("Image Generator")

col1, col2 = st.columns([4, 4], gap="large")

col1.markdown("## Generate Art")
# Text prompt input
prompt = col1.text_input("Prompt", placeholder="Describe the image you want generated")
file = col1.file_uploader("Upload Style Image (Optional)")

# Generate Image button
generate_button = col1.button("Generate Image")

# Placeholder for displaying the generated image
with col2:
    st.write("Your image will appear here.")

# Image generation logic
if generate_button and prompt:
    pipe = load_pipeline()
    
    # Load initial image if provided
    if file:
        init_image = Image.open(file)
    else:
        # Use a default image if no style image is uploaded
        url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/img2img-init.png"
        init_image = load_image(url)
        
    with st.spinner("Generating image..."):
        # Generate image with the prompt and optional style image
        generated_image = pipe(prompt, image=init_image).images[0]
        
        # Display both images in a grid
        st.image(make_image_grid([init_image, generated_image], rows=1, cols=2), caption=["Style Image", "Generated Image"], use_column_width=True)
