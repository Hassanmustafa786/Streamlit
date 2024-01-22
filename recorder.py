from deep_translator import GoogleTranslator
from audio_recorder_streamlit import audio_recorder
import streamlit as st
import speech_recognition as sr 
from gtts import gTTS 
from textblob import TextBlob
import os 
import uuid
import time
import io

# def display_languages(languages):
#     st.header("Translator", divider='green')
#     st.subheader("Language Names")

#     # Extract language names from the tuple
#     language_names = languages[::2]

#     st.write(language_names)

# dic = (
#        'arabic', 'ar', 
#        'bengali', 'bn', 
#        'chinese (simplified)', 'zh-cn', 
#        'chinese (traditional)', 'zh-tw',
#        'english', 'en',
#        'french', 'fr', 
#        'german', 'de',
#        'gujarati', 'gu',  
#        'hawaiian', 'haw', 
#        'hebrew', 'he', 
#        'hindi', 'hi',
#        'italian', 'it', 
#        'japanese', 'ja',
#        'korean', 'ko',
#        'malayalam', 'ml',
#        'marathi', 'mr',
#        'nepali', 'ne', 
#        'russian', 'ru', 
#        'spanish', 'es',
#        'tamil', 'ta',
#        'urdu', 'ur',) 

# # Your dictionary of language codes
# languages_dict = {
#     'arabic': 'ar', 
#     'bengali': 'bn',  
#     'chinese (simplified)': 'zh-CN', 
#     'chinese (traditional)': 'zh-TW',  
#     'english': 'en',  
#     'french': 'fr', 
#     'german': 'de', 
#     'gujarati': 'gu', 
#     'hebrew': 'iw', 
#     'hindi': 'hi',  
#     'italian': 'it', 
#     'japanese': 'ja',  
#     'korean': 'ko', 
#     'malayalam': 'ml',  
#     'marathi': 'mr',  
#     'nepali': 'ne', 
#     'russian': 'ru', 
#     'spanish': 'es', 
#     'tamil': 'ta',  
#     'urdu': 'ur', 
#     }

# # languages_dict = {
# #     'english': 'en',
# #     'urdu': 'ur',
# # }


# def speak(question, lang):
#     speech = gTTS(text=question, lang=lang, slow=False, tld="co.in")
#     key = str(uuid.uuid4())
#     filename = f'Languages/{lang+"_"+key}.mp3'
#     speech.save(filename)
#     with st.spinner('Wait for it...'):
#         time.sleep(2)
#     return st.audio(f'Languages/{lang+"_"+key}.mp3')

# # Make a folder
# os.makedirs('Languages', exist_ok=True)

# #Streamlit App
# st.set_page_config(layout='wide')

# display_languages(dic)
# # Get user's selection (single select)
# selected_language = st.selectbox("Select Language in which you want to convert your voice", list(languages_dict.keys()))

# # Map selected language to its corresponding code
# selected_language_code = languages_dict[selected_language]

# # Display selected language code
# # st.write("Selected Language Code:", selected_language_code)

# audio_bytes = audio_recorder()
# if audio_bytes:
#     # st.audio(audio_bytes, format="audio/wav")
#     r = sr.Recognizer()
#     try:
#         with io.BytesIO(audio_bytes) as wav_io:
#             with sr.AudioFile(wav_io) as source:
#                 audio_data = r.record(source)
#                 query = r.recognize_google(audio_data)  # Change the language code if needed
#                 st.success(f"You: {query}\n")
#     except sr.UnknownValueError:
#         st.error("Google Speech Recognition could not understand audio.")
#     except sr.RequestError as e:
#         st.error(f"Could not request results from Google Speech Recognition service; {e}")

   
#     translated = GoogleTranslator(source='auto', target=f'{selected_language_code}').translate(query)
#     st.warning(f"Translate: {translated}")
    
#     # Generate the audio
#     audio = speak(str(translated), selected_language_code)
    
















def display_languages(languages):
    st.header("Translator", divider='green')
    st.subheader("Language Names")

    # Extract language names from the tuple
    language_names = languages[::2]

    st.write(language_names)

dic = (
       'english', 'en',
       'urdu', 'ur',) 

languages_dict = {
    'english': 'en',
    'urdu': 'ur',
}

def speak(question, lang):
    speech = gTTS(text=question, lang=lang, slow=False, tld="co.in")
    key = str(uuid.uuid4())
    filename = f'Languages/{lang+"_"+key}.mp3'
    speech.save(filename)
    with st.spinner('Wait for it...'):
        time.sleep(2)
    return st.audio(f'Languages/{lang+"_"+key}.mp3')

# Make a folder
os.makedirs('Languages', exist_ok=True)

#Streamlit App
st.set_page_config(layout='wide')

display_languages(dic)

# Display selected language code
col1, col2 = st.columns(2)

with col1:
    selected_language = st.selectbox("Select source language", list(languages_dict.keys()), key="original", index=0)
    selected_language_code = languages_dict[selected_language]
    audio_bytes = audio_recorder()
    st.caption("Complete voice message in 10 secs")
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        st.caption("Source voice")
        r = sr.Recognizer()
        try:
            with io.BytesIO(audio_bytes) as wav_io:
                with sr.AudioFile(wav_io) as source:
                    audio_data = r.record(source)
                    query = r.recognize_google(audio_data)  # Change the language code if needed
                    st.success(f"You: {query}\n")
        except sr.UnknownValueError:
            st.error("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")

with col2:
    selected_language = st.selectbox("Select target language", list(languages_dict.keys()), key="translate", index=1)
    selected_language_code = languages_dict[selected_language]
    
    if 'query' in locals():
        translated = GoogleTranslator(source='auto', target=f'{selected_language}').translate(query)
        st.warning("Translating...")

        # Generate the audio
        audio = speak(translated, selected_language_code)
        st.caption("Target Voice")
        st.success(f"Translate: {translated}")