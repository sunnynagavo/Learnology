import os
import streamlit as st
from openai import AzureOpenAI
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def call_openai_model(system_message, model, client):
    # Format and send the request to the model
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system_message}],
        temperature=0,  # Adjust temperature as needed
        max_tokens=150   # Adjust max tokens as needed
    )
    return response.choices[0].message.content

async def generate_content(subject, length, learning_goal, model, client):
    system_message = f"Please generate teaching content for a class. The subject is {subject}. The length of the class is {length}. The learning goal is {learning_goal}."
    return await call_openai_model(system_message, model, client)

async def main(): 
    try: 
        # Get configuration settings 
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
            azure_endpoint=azure_oai_endpoint,
            api_key=azure_oai_key,
            api_version="2023-05-15"
        )

        st.title("Teaching Plan Generator")

        subject = st.text_input("Enter the subject:")
        length = st.text_input("Enter the length:")
        learning_goal = st.text_input("Enter the learning goal:")

        if st.button("Generate Content"):
            result = await generate_content(subject, length, learning_goal, azure_oai_deployment, client)
            st.write("Generated Content:")
            st.write(result)

    except Exception as ex:
        st.error(f"An error occurred: {ex}")

if __name__ == '__main__':
    asyncio.run(main())
