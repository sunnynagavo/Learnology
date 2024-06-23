import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define Streamlit app
def main():
    st.title("Teaching Image Generator")

    # Render form for entering prompt
    prompt = st.text_area("Enter the description of the image you want to create (up to 200 words):", max_chars=1000)
    if st.button("Generate Image"):
        # Process prompt and generate image
        image_url = process_prompt(prompt)
        # Display image
        if image_url:
            st.image(image_url, caption="Generated Image", use_column_width=True)
        else:
            st.error("Failed to generate image. Please try again.")

# Function to process prompt and generate image
def process_prompt(prompt):
    try:
        # Get Azure OpenAI Service settings
        api_base = os.getenv("AZURE_OAI_ENDPOINT")
        api_key = os.getenv("AZURE_OAI_KEY")
        api_version = '2024-02-15-preview'

        # Call the DALL-E model
        url = f"{api_base}openai/deployments/dalle3/images/generations?api-version={api_version}"
        headers = { "api-key": api_key, "Content-Type": "application/json" }
        body = {
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        }
        response = requests.post(url, headers=headers, json=body)

        # Get the image URL from the response
        if response.status_code == 200:
            image_url = response.json()['data'][0]['url']
            return image_url
        else:
            st.error("Failed to generate image. Please try again.")
            return None

    except Exception as ex:
        st.error(f"Error: {ex}")
        return None

# Run the Streamlit app
if __name__ == "__main__":
    main()
