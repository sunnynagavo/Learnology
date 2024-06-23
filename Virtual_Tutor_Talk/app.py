import streamlit as st
import os
import azure.cognitiveservices.speech as speechsdk
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up AzureOpenAI client
os.environ["OPENAI_API_TYPE"] = "azure"
client = AzureOpenAI(
    azure_endpoint=os.environ.get('OPEN_AI_ENDPOINT'),
    api_key=os.environ.get('OPEN_AI_KEY'),
    api_version="2023-05-15"
)
deployment_id = os.environ.get('OPEN_AI_DEPLOYMENT_NAME')

# Set up speech recognition and synthesis
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_config.speech_recognition_language = "en-US"
speech_config.speech_synthesis_voice_name = 'en-US-JennyMultilingualNeural'
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
tts_sentence_end = [".", "!", "?", ";", "。", "！", "？", "；", "\n"]

# Function to ask OpenAI and synthesize response
def ask_openai(prompt):
    response = client.chat.completions.create(model=deployment_id, max_tokens=200, stream=True, messages=[{"role": "user", "content": prompt}])
    collected_messages = []
    last_tts_request = None

    for chunk in response:
        if len(chunk.choices) > 0:
            chunk_message = chunk.choices[0].delta.content
            if chunk_message is not None:
                collected_messages.append(chunk_message)
                if chunk_message in tts_sentence_end:
                    text = ''.join(collected_messages).strip()
                    if text != '':
                        st.write(f"AI Tutor: {text}")
                        last_tts_request = speech_synthesizer.speak_text_async(text)
                        collected_messages.clear()
    if last_tts_request:
        last_tts_request.get()

# Function to continuously listen for speech input
def chat_with_open_ai():
    while True:
        st.write("You say: ")
        try:
            speech_recognition_result = speech_recognizer.recognize_once_async().get()
            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                if speech_recognition_result.text == "Stop.":
                    st.write("Conversation ended.")
                    break
                st.write("Recognized speech: {}".format(speech_recognition_result.text))
                ask_openai(speech_recognition_result.text)
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                st.write("No voice is detected. Conversation ends. {}".format(speech_recognition_result.no_match_details))
                break
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                st.write("Conversation canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    st.write("Error details: {}".format(cancellation_details.error_details))
        except EOFError:
            break

# Main function
def main():
    st.title("Virtual Tutor")

    st.subheader("Please ask questions about studying and the virtual tutor will answer.")

    running = False

    if st.button("Start"):
        running = True

    if st.button("Stop"):
        running = False
        st.write("Conversation ends.")  # Display "Conversation ends" when the "Stop" button is clicked

    if running:
        chat_with_open_ai()

if __name__ == "__main__":
    main()
