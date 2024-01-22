# import speech_recognition as sr 
# from gtts import gTTS 
# from textblob import TextBlob
# import os 
# from IPython.display import Audio, display
# import uuid
  
# # A tuple containing all the language and 
# # codes of the language will be detcted 
# dic = ('afrikaans', 'af', 'albanian', 'sq',  
#        'amharic', 'am', 'arabic', 'ar', 
#        'armenian', 'hy', 'azerbaijani', 'az',  
#        'basque', 'eu', 'belarusian', 'be', 
#        'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
#        'bg', 'catalan', 'ca', 'cebuano', 
#        'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
#        'zh-cn', 'chinese (traditional)', 
#        'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
#        'czech', 'cs', 'danish', 'da', 'dutch', 
#        'nl', 'english', 'en', 'esperanto', 'eo',  
#        'estonian', 'et', 'filipino', 'tl', 'finnish', 
#        'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
#        'gl', 'georgian', 'ka', 'german', 
#        'de', 'greek', 'el', 'gujarati', 'gu', 
#        'haitian creole', 'ht', 'hausa', 'ha', 
#        'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
#        'hi', 'hmong', 'hmn', 'hungarian', 
#        'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',  
#        'id', 'irish', 'ga', 'italian', 
#        'it', 'japanese', 'ja', 'javanese', 'jw', 
#        'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
#        'km', 'korean', 'ko', 'kurdish (kurmanji)',  
#        'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
#        'latin', 'la', 'latvian', 'lv', 'lithuanian', 
#        'lt', 'luxembourgish', 'lb', 
#        'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
#        'ms', 'malayalam', 'ml', 'maltese', 
#        'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
#        'mn', 'myanmar (burmese)', 'my', 
#        'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
#        'pashto', 'ps', 'persian', 'fa', 
#        'polish', 'pl', 'portuguese', 'pt', 'punjabi',  
#        'pa', 'romanian', 'ro', 'russian', 
#        'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
#        'serbian', 'sr', 'sesotho', 'st', 
#        'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 
#        'slovak', 'sk', 'slovenian', 'sl', 
#        'somali', 'so', 'spanish', 'es', 'sundanese', 
#        'su', 'swahili', 'sw', 'swedish', 
#        'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
#        'te', 'thai', 'th', 'turkish', 
#        'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
#        'ug', 'uzbek',  'uz', 
#        'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
#        'yiddish', 'yi', 'yoruba', 
#        'yo', 'zulu', 'zu') 
  
# def takecommand():
#     r = sr.Recognizer() 
#     with sr.Microphone() as source: 
#         print("listening...") 
#         r.pause_threshold = 1
#         audio = r.listen(source) 
  
#     try: 
#         print("Recognizing...") 
#         query = r.recognize_google(audio, language='en-in') 
#         print(f"You: {query}\n") 
#     except Exception as e: 
#         print("Say that again please...") 
#         return "None"
#     return query
  

# # For Multiple languages
# def destination_language(): 
#     print("Tell the language in which you want to convert: Ex. Urdu, English, Spanish etc.") 
#     # Input destination language in which the user wants to translate 
#     to_lang = takecommand() 
#     while (to_lang == "None"): 
#         to_lang = takecommand() 
#     to_lang = to_lang.lower()
#     return to_lang 
  
# to_lang = destination_language()

# # Mapping it with the code 
# while (to_lang not in dic): 
#     print("Language in which you are trying to convert is currently not available, please input some other language") 
#     to_lang = destination_language() 
  
# to_lang = dic[dic.index(to_lang)+1] 

# prompt = takecommand()
# en_blob = TextBlob(f'{prompt}') 
# translate = en_blob.translate(from_lang='en', to=f'{to_lang}')
# # print(translate)

# def speak(question, lang):
#     speech = gTTS(text=question, lang=lang, slow=False, tld="co.in")
#     key = str(uuid.uuid4())
#     filename = f'Languages/{lang+"_"+key}.mp3'
#     speech.save(filename)
#     return filename

# # Make a folder
# os.makedirs('Languages', exist_ok=True)

# # Generate the audio
# audio = speak(str(translate), to_lang)













# import streamlit as st
# import speech_recognition as sr 
# from gtts import gTTS 
# from textblob import TextBlob
# import os 
# import uuid
# import time


# def display_languages(languages):
#     st.header("Translator", divider='green')
#     st.subheader("Language Names")

#     # Extract language names from the tuple
#     language_names = languages[::2]

#     st.write(language_names)

# # A tuple containing all the language and 
# # codes of the language will be detcted 
# dic = ('afrikaans', 'af', 'albanian', 'sq',  
#        'amharic', 'am', 'arabic', 'ar', 
#        'armenian', 'hy', 'azerbaijani', 'az',  
#        'basque', 'eu', 'belarusian', 'be', 
#        'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
#        'bg', 'catalan', 'ca', 'cebuano', 
#        'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
#        'zh-cn', 'chinese (traditional)', 
#        'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
#        'czech', 'cs', 'danish', 'da', 'dutch', 
#        'nl', 'english', 'en', 'esperanto', 'eo',  
#        'estonian', 'et', 'filipino', 'tl', 'finnish', 
#        'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
#        'gl', 'georgian', 'ka', 'german', 
#        'de', 'greek', 'el', 'gujarati', 'gu', 
#        'haitian creole', 'ht', 'hausa', 'ha', 
#        'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
#        'hi', 'hmong', 'hmn', 'hungarian', 
#        'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',  
#        'id', 'irish', 'ga', 'italian', 
#        'it', 'japanese', 'ja', 'javanese', 'jw', 
#        'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
#        'km', 'korean', 'ko', 'kurdish (kurmanji)',  
#        'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
#        'latin', 'la', 'latvian', 'lv', 'lithuanian', 
#        'lt', 'luxembourgish', 'lb', 
#        'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
#        'ms', 'malayalam', 'ml', 'maltese', 
#        'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
#        'mn', 'myanmar (burmese)', 'my', 
#        'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
#        'persian', 'fa', 
#        'polish', 'pl', 'portuguese', 'pt', 'romanian', 'ro', 'russian', 
#        'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
#        'serbian', 'sr', 'sesotho', 'st', 
#        'shona', 'sn', 'sinhala', 'si', 
#        'slovak', 'sk', 'slovenian', 'sl', 
#        'somali', 'so', 'spanish', 'es', 'sundanese', 
#        'su', 'swahili', 'sw', 'swedish', 
#        'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
#        'te', 'thai', 'th', 'turkish', 
#        'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
#        'ug', 'uzbek',  'uz', 
#        'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
#        'yiddish', 'yi', 'yoruba', 
#        'yo', 'zulu', 'zu') 


# def takecommand():
#     r = sr.Recognizer() 
#     with sr.Microphone() as source: 
#         st.write("listening...") 
#         r.pause_threshold = 1
#         audio = r.listen(source) 
  
#     try: 
#         st.write("Recognizing...") 
#         query = r.recognize_google(audio, language='en-in')
#         st.success(f"You: {query}\n")
#     except Exception as e: 
#         st.write("Say that again please...")
#         return "None"
#     return query
  

# # For Multiple languages
# def destination_language():
#     # Input destination language in which the user wants to translate 
#     to_lang = takecommand() 
#     while (to_lang == "None"): 
#         to_lang = takecommand() 
#     to_lang = to_lang.lower()
#     return to_lang 
  


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
# st.warning("First, tell the language name in which you want to convert your voice then second time you can speak whatever you want to convert.")

# if st.button("Start"):
#     to_lang = destination_language()
    
#     # Mapping it with the code 
#     while (to_lang not in dic): 
#         st.warning("Language in which you are trying to convert is currently not available, please input some other language") 
#         to_lang = destination_language()


#     to_lang = dic[dic.index(to_lang)+1] 

#     prompt = takecommand()
#     en_blob = TextBlob(f'{prompt}')
#     translate = en_blob.translate(from_lang='en', to=f'{to_lang}')
    
#     # Generate the audio
#     audio = speak(str(translate), to_lang)































from deep_translator import GoogleTranslator
import streamlit as st
import speech_recognition as sr 
from gtts import gTTS 
from textblob import TextBlob
import os 
import uuid
import time

def display_languages(languages):
    st.header("Translator", divider='green')
    st.subheader("Language Names")

    # Extract language names from the tuple
    language_names = languages[::2]

    st.write(language_names)

# A tuple containing all the language and 
# codes of the language will be detcted 
dic = ('afrikaans', 'af', 'albanian', 'sq',  
       'amharic', 'am', 'arabic', 'ar', 
       'armenian', 'hy', 'azerbaijani', 'az',  
       'basque', 'eu', 'belarusian', 'be', 
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
       'bg', 'catalan', 'ca', 'cebuano', 
       'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
       'zh-cn', 'chinese (traditional)', 
       'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
       'czech', 'cs', 'danish', 'da', 'dutch', 
       'nl', 'english', 'en', 'esperanto', 'eo',  
       'estonian', 'et', 'filipino', 'tl', 'finnish', 
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
       'gl', 'georgian', 'ka', 'german', 
       'de', 'greek', 'el', 'gujarati', 'gu', 
       'haitian creole', 'ht', 'hausa', 'ha', 
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
       'hi', 'hmong', 'hmn', 'hungarian', 
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',  
       'id', 'irish', 'ga', 'italian', 
       'it', 'japanese', 'ja', 'javanese', 'jw', 
       'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
       'km', 'korean', 'ko', 'kurdish (kurmanji)',  
       'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
       'latin', 'la', 'latvian', 'lv', 'lithuanian', 
       'lt', 'luxembourgish', 'lb', 
       'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
       'ms', 'malayalam', 'ml', 'maltese', 
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
       'mn', 'myanmar (burmese)', 'my', 
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
       'persian', 'fa', 
       'polish', 'pl', 'portuguese', 'pt', 'romanian', 'ro', 'russian', 
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
       'serbian', 'sr', 'sesotho', 'st', 
       'shona', 'sn', 'sinhala', 'si', 
       'slovak', 'sk', 'slovenian', 'sl', 
       'somali', 'so', 'spanish', 'es', 'sundanese', 
       'su', 'swahili', 'sw', 'swedish', 
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
       'te', 'thai', 'th', 'turkish', 
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
       'ug', 'uzbek',  'uz', 
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
       'yiddish', 'yi', 'yoruba', 
       'yo', 'zulu', 'zu') 


def takecommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        st.write("listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
  
    try: 
        st.write("Recognizing...") 
        query = r.recognize_google(audio)
        st.success(f"You: {query}\n")
    except Exception as e: 
        st.write("Say that again please...")
        return "None"
    return query

# For Multiple languages
def destination_language():
    # Input destination language in which the user wants to translate 
    to_lang = takecommand()
    while to_lang == "None":
        to_lang = takecommand()
    to_lang = to_lang.lower()
    return to_lang


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
st.warning("First, tell the language name in which you want to convert your voice then second time you can speak whatever you want to convert.")

if st.button("Start"):
    to_lang = destination_language()
    
    # Mapping it with the code 
    while (to_lang not in dic): 
        st.warning("Language in which you are trying to convert is currently not available, please input some other language") 
        to_lang = destination_language()


    to_lang = dic[dic.index(to_lang)+1] 

    prompt = takecommand()
    translated = GoogleTranslator(source='auto', target=f'{to_lang}').translate(prompt)
    # st.write(translated)
    
    # Generate the audio
    audio = speak(str(translated), to_lang)