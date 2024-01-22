import streamlit as st
import os
import time
from deep_translator import GoogleTranslator
from audio_recorder_streamlit import audio_recorder
from textblob import TextBlob
import uuid
import io
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def speech_to_text():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = r.listen(source)
#         st.write("Generating...")
#     try:
#         user_input = r.recognize_google(audio)
#         # st.code(f'YOU: {user_input}')
#         return user_input
#     except sr.UnknownValueError:
#         st.write("Oops, I didn't get your audio, Please try again.")
#         return None

# def text_to_speech(key, value):
#     engine = pyttsx3.init()
#     engine.save_to_file(key, f'{str(value)}.mp3')
#     engine.runAndWait()
#     st.audio(f'{str(value)}.mp3')

# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# chat = ChatOpenAI(
#     temperature=0.5,
#     model_name="gpt-3.5-turbo",
#     openai_api_key=openai_api_key,
#     max_tokens=10
# )

# def get_response(user_input):
#     intro_message = """You are a Mental Health Care Expert for OSTF Organization, here to guide and assist people with their health questions and concerns. Please provide accurate and helpful information, and always maintain a polite and professional tone.
#                        Your answer should be complete and precise."""

#     messages = [
#         SystemMessage(content=intro_message),
#         HumanMessage(content=user_input),
#     ]

#     response = chat(messages).content

#     return response

# questions = [
#     ("What is your name?", 1),
#     ("What brings you to counseling at this time? Is there something specific, such as particular event? Please be as detailed as feels comfortable?", 2),
#     ("What are your goals for therapy? How are you hoping to feel? How are you hoping to experience life?", 3),
#     ("Describe your current living situation. Do you live alone, with family, roommate(s), pets(s)?", 4),
#     ("What is your level of education (highest grade, type of degree)?", 5),
#     ("What is your current occupation? Describe what you do for work and how long have you been doing it.", 6),
#     ("If you are in a relationship, please describe the nature of that relationship (including months years together).", 7),
#     ("Who is your primary care physician? Please include type of MD, name, and contact information (phone number, office location, etc).", 8),
#     ("About when was the last time you had a physical with your PCP, including blood work?", 9),
#     ("If taking prescription medication, who is your prescribing MD? Please include type of MD, name, and contact information (phone number, office location, etc).", 10),
#     ("Please specify all medications and supplements you are taking currently, and for what reason.", 11),
#     ("Have you worked with a mental health professional before (Say Yes or No)?", 12),
#     ("Have you ever been hospitalized for a psychiatric concern (Say Yes or No)?", 13),
#     ("Do you have suicidal thoughts (Say Yes or No)?", 14),
#     ("Have you ever attempted suicide (Say Yes or No)?", 15),
#     ("Do you have thoughts or urges to harm others (Say Yes or No)?", 16),
#     ("Do you drink alcohol (Say Yes or No)?", 17),
#     ("Do you use recreational drugs? (Say Yes or No)?", 18),
#     ("In the past 6 months, have you experienced any of the following? Please select: Increased appetite, Decreased appetite, Trouble concentrating, Difficulty sleeping, Excessive sleep, Low motivation, Isolation from others, Fatigue or low energy, Low self-esteem, Depressed mood, Tearful or crying spells, Anxiety, Fear, Hopelessness, Panic attack, Flashbacks, Intrusive thoughts, Nightmares, Auditory like sound hallucinations, Visual hallucinations, Compulsions like strong urges to do things, Obsessive thoughts like cannot shift thought even with effort, Significant loss like person, job, relationship, quality of life, etc.", 19),
#     ("Please briefly describe what life was like for you as a child?", 20),
#     ("Please briefly describe what you were like as a child. What do others tell you about your childhood?", 21),
#     ("Were you adopted or raised by someone other than your biological parents? If so, please describe that relationship.", 22),
#     ("Did you grow up with siblings? If so, how many? Were you the oldest, youngest, middle child? Generally, how was your relationship with your siblings?", 23),
#     ("Do you have a history of abuse or trauma (psychological, verbal, emotional, physical, racial, religious, cultural, sexual, reproductive trauma or a traumatic birthing experience, etc.)? Note: Trauma can be anything from growing up with an emotionally distant parent, to a car accident, or a personal assault.", 24),
#     ("Is there a history of mental illness in your family?", 25),
#     ("Do you (or any members of your immediate family) have a history of disordered eating? Please describe.", 26),
#     ("How many pregnancies have you had, or have you been a part of?", 27),
#     ("How many births have you had, or have you been a part of?", 28),
#     ("How many fetal losses have you had, or have you been a part of?", 29),
#     ("Do you have any children that are not currently living?", 30),
#     ("Have you recently lost someone or something? If so, do you believe this loss is impacting your daily functioning? Is this loss preventing you from living in ways you would like to?", 31),
#     ("If you have experienced a recent loss, have you experienced any of the following in the past 6 months? Please select all that apply: Intrusive images related to the loss, Intrusive memories related to the loss, Intrusive reminders related to the loss, Avoiding reminders of the thing you lost (such as people, places, or things that remind you of the loss), Spend more time than you'd like thinking about disturbing aspects of the loss, Nightmares related to the loss, Other.", 32),
#     ("What are your greatest strengths as a person? (If this feels hard to answer, think about how your best friend might describe you & allow that to support your answer!)", 33),
#     ("Do you have a religious preference that you would like incorporated into therapy?", 34),
#     ("Please describe how your life experiences were and or are affected by the COVID-19 pandemic.", 35),
#     ("I am looking forward to working with you! What else would you like me to know about you and your history that will help us get started?", 36),
#     ("How did you learn about Three Oaks Behavioural Health & Wellness?", 37),
#     ("How are you feeling right now?", 38),

# ]

# # Initialize the responses using Streamlit's session state
# if 'responses' not in st.session_state:
#     st.session_state.responses = {}

# st.cache()
# # Streamlit app
# def ask_question():

#         for i, (question, answer) in enumerate(questions):
#             response_key = f"response_{i}"
#             if response_key not in st.session_state.responses:
#                 st.session_state.responses[response_key] = ""
#             with st.expander(f"Question: {answer}"):
#                 if st.button(f"Question: {i + 1}", key = str(f"Q{i}+1")):
#                     speak(question)
#                     st.subheader(f"Q{i+1}-  {question}")
                
#                 # if st.button(f"Answer: {i + 1}", key = str(f"A{i}+1")):
#                     user_input = speech_to_text()
#                     if user_input:
#                         st.session_state.responses[response_key] = user_input
#                         output = get_response(user_input)
#                         v = str(f"{i+1}")
#                         text_to_speech(output, v)
#                         st.success("Please move to another question.")
#             st.divider()
        
# def intro():
#     return speak("Welcome to OSTF Organization. To better assist you, please complete the required information below. Your cooperation ensures swift and precise support tailored to your needs.")


# st.set_page_config(layout="wide")
# st.image('Shine.png')
# # , caption='Copyright 2024 by OSTF. All Rights Reserved.'
# st.header('Health Intake Questionnaire', divider='rainbow')
# st.markdown('''Welcome To! :blue[O] :blue[S] :blue[T] :blue[F] - :blue[Organization]''')
# # code = '''print("Made by: Hassan Mustafa")'''
# # st.code(code, language='python')


# tab1, tab2 = st.tabs(["Q & A", "Stored Data"])

# with tab1:
#     st.warning("Refrain from speaking until the *(listening...)* text appears.")
#     if st.button("Start"):
#         intro()

#     ask_question()

# with tab2:
#         st.write("### User Stored Data")
#         # st.success("Stored Data")
#         for i, (question, _) in enumerate(questions):
#             response_key = f"response_{i}"
#             if response_key in st.session_state.responses:
#                 st.write(f"Q{i+1} - {question} <br> A{i+1} - {st.session_state.responses[response_key]}", unsafe_allow_html=True)
#                 st.divider()



















def speak(question, key, lang):
    speech = gTTS(text=question, lang=lang, slow=False, tld="co.in")
    filename = f'Questions/Q{key}.mp3'
    speech.save(filename)
    st.audio(filename)

os.makedirs('Questions', exist_ok=True)

def speech_to_text_english(lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
        st.write("Generating...")
    try:
        user_input = r.recognize_google(audio, language=lang)
        st.warning(f'You: {user_input}')
        return user_input
    except sr.UnknownValueError:
        st.write("Oops, I didn't get your audio, Please try again.")
        return None

def speech_to_text_urdu(lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("بولنا شروع کریں ...")
        audio = r.listen(source)
        st.write("براہ مہربانی جواب کا انتظار کریں")
    try:
        user_input = r.recognize_google(audio, language=lang)
        st.warning(f'آپ: {user_input}')
        return user_input
    except sr.UnknownValueError:
        st.write("اوہو، مجھے آپ کا آڈیو نہیں ملا، براہ کرم دوبارہ کوشش کریں...")
        return None

def text_to_speech(answer, key, lang):
    speech = gTTS(text=answer, lang=lang, slow=False, tld="co.in")
    filename = f'Answers/A{key}.mp3'
    speech.save(filename)
    st.audio(filename)

os.makedirs('Answers', exist_ok=True)


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(
    temperature=0.5,
    model_name="gpt-3.5-turbo",
    openai_api_key=openai_api_key,
    max_tokens=100,
)

def get_response(user_input):
    intro_message = """You are a Mental Health Care Expert for OSTF Organization, here to guide and assist people with their health questions and concerns. Please provide accurate and helpful information, and always maintain a polite and professional tone.
                       Your answer should be complete and precise.
                       You have to answer only health related questions.
                       You understand only urdu and english.
                       If a user tell his/her name, age, address, phone number, YES or No then you have to thank him for giving the response."""
    messages = [
        SystemMessage(content=intro_message),
        HumanMessage(content=user_input),
    ]
    response = chat(messages).content
    return response

questions = [
    ("What is your name?", 1, "آپ کا نام کيا ہے?"),
    ("What is your age?", 2, "آپ کی عمر کیا ہے؟"),
    # ("What is your address?", 3, "آپ کا پتہ کیا ہے؟"),
    # ("Are you taking any Medicine? If yes, then please tell name of the medicines", 4, "کیا آپ کوئی دوا لے رہے ہیں؟اگر ہاں. پھر دوا کا نام بتائیں "),
    # ("What other medicine you have taken in the Past?", 5, "آپ نے ماضی میں اور کون سی دوا لی ہے؟ "),
    # ("What is your major complaint?", 6, "آپ کی سب سے بڑی شکایت کیا ہے؟ "),
    # ("Have you previously suffered from this complaint?: If Yes, enter previous therapists seen for complaint and describe treatment, Aggravating Factors, Relieving Factors.", 7, "کیا آپ کو پہلے اس شکایت کا سامنا کرنا پڑا ہے؟: اگر ہاں، تو شکایت کے لئے دیکھے گئے پچھلے تھراپسٹوں کو درج کریں، علاج، بڑھنے والے عوامل، راحت دینے والے عوامل کی وضاحت کریں."),
    # ("Were you adopted? If yes, at what age?", 8, "کیا آپ کو گود لیا گیا تھا؟ اگر ہاں، تو کس عمر میں؟ "),
    # ("How is your relationship with your mother?", 9, "ماں کے ساتھ آپ کا رشتہ کیسا ہے؟ "),
    # ("How is your relationship with your father?", 10, "اپنے والد کے ساتھ آپ کے تعلقات کیسے ہیں؟"),
    # ("How is your relationship with your siblings? Also mention their ages.", 11, "اپنے بہن بھائیوں کے ساتھ آپ کے تعلقات کیسے ہیں؟ ان کی عمروں کا بھی ذکر کریں")
]

# Initialize the responses using Streamlit's session state
if 'responses' not in st.session_state:
    st.session_state.responses = {}

st.cache()
# Streamlit app
def ask_question():

        for i, (question, key, urdu_question) in enumerate(questions):
            response_key = f"response_{i}"
            if response_key not in st.session_state.responses:
                st.session_state.responses[response_key] = ""
            if selected_language == 'en':
                with st.expander(f"Question: {key}"):
                    # if st.button(f"Question: {i + 1}", key = str(f"Q{i}+1")):
                    speak(question, key, selected_language)
                    
                    # st.subheader(f"Q{i+1}-  {question}")
                    if st.button(f"Answer", key = str(f"A{i+1}")):
                        # st.write("Don't speak until the *(listening...)* text appears.")
                        user_input = speech_to_text_english('en-EN')
                        if user_input:
                            st.session_state.responses[response_key] = user_input
                            output = get_response(user_input)
                            v = str(f"{i+1}")
                            text_to_speech(output, v, 'en')
                            st.success(f"{output}")
                            

            elif selected_language == 'ur':
                with st.expander(f"Question: {key}"):
                    # if st.button(f"Question: {i + 1}", key = str(f"Q{i}+1")):
                    speak(urdu_question, key, selected_language)

                    if st.button(f"جواب", key = str(f"A{i+1}")):
                        st.write("اس وقت تک بات نہ کریں جب تک *(میں آپ کو سن رہا ہوں ...)* تحریری متن ظاہر نہ ہو۔")
                        user_input = speech_to_text_urdu('ur-UR')
                        if user_input:
                            st.session_state.responses[response_key] = user_input
                            output = get_response(user_input)
                            v = str(f"{i+1}")
                            text_to_speech(output, v, 'ur')
                            st.success(f"{output}")

            else:
                if selected_language == 'en':
                    st.warning("Please select the language first.")
                elif selected_language == 'ur':
                    st.warning("براہ مہربانی دوسرے سوال کی طرف جائیں۔")
            st.divider()


def intro():
    if selected_language == 'en':
        speak("Welcome to ICNA-Relief","0", 'en')
    elif selected_language == 'ur':
        speak("آئی سی این اے ریلیف میں خوش آمدید. شکریہ", '0', 'ur')

st.set_page_config(
    page_title="OSTF App",
    page_icon="🧊",
    layout="wide",
)
# st.image('Shine.png')
# , caption='Copyright 2024 by OSTF. All Rights Reserved.'
st.header('Health Intake Questionnaire', divider='rainbow')
st.markdown('''Welcome To! :blue[O] :blue[S] :blue[T] :blue[F] - :blue[Organization]''')
# code = '''print("Made by: Hassan Mustafa")'''
# st.code(code, language='python')

selected_language = st.selectbox("Select Language", ["en", "ur"])

tab1, tab2, tab3 = st.tabs(["Q & A", "Translator", "Stored Data"])

with tab1:
    # if st.button("Start"):
    intro()
    ask_question()

with tab2:
    st.balloons()
    

with tab3:
    st.write("### User Stored Data")
    # st.success("Stored Data")
    for i, (question, key, urdu_question) in enumerate(questions):
        response_key = f"response_{i}"
        if response_key in st.session_state.responses:
            if selected_language == 'en':
                st.write(f"Q{i+1} - {question} <br> A{i+1} - {st.session_state.responses[response_key]}", unsafe_allow_html=True)
                st.divider()
            if selected_language == 'ur':
                st.write(f"Q{i+1} - {urdu_question} <br> A{i+1} - {st.session_state.responses[response_key]}", unsafe_allow_html=True)
                st.divider()






























# def recognize_audio(audio_bytes):
#     query = ""  # Initialize query outside the try block
#     if audio_bytes:
#         # st.audio(audio_bytes, format="audio/wav")
#         r = sr.Recognizer()
#         try:
#             with io.BytesIO(audio_bytes) as wav_io:
#                 with sr.AudioFile(wav_io) as source:
#                     audio_data = r.record(source)
#                     query = r.recognize_google(audio_data)  # Change the language code if needed
#                     st.warning(f"You: {query}\n")
#         except sr.UnknownValueError:
#             st.error("Google Speech Recognition could not understand audio.")
#         except sr.RequestError as e:
#             st.error(f"Could not request results from Google Speech Recognition service; {e}")
    
#     return query

# def recognize_audio(audio_bytes, lang):
#     query = ""  
#     if audio_bytes:
#         # st.audio(audio_bytes, format="audio/wav")
#         r = sr.Recognizer()
#         try:
#             with io.BytesIO(audio_bytes) as wav_io:
#                 with sr.AudioFile(wav_io) as source:
#                     audio_data = r.record(source)
#                     query = r.recognize_google(audio_data, language= lang)  # Change the language code if needed
#                     st.warning(f"You: {query}\n")
#         except sr.UnknownValueError:
#             st.error("Google Speech Recognition could not understand audio.")
#         except sr.RequestError as e:
#             st.error(f"Could not request results from Google Speech Recognition service; {e}")
    
#     return query

# def recognize_audio_2(audio_bytes):
#     query = ""  
#     if audio_bytes:
#         # st.audio(audio_bytes, format="audio/wav")
#         r = sr.Recognizer()
#         try:
#             with io.BytesIO(audio_bytes) as wav_io:
#                 with sr.AudioFile(wav_io) as source:
#                     audio_data = r.record(source)
#                     query = r.recognize_google(audio_data)  # Change the language code if needed
#                     st.warning(f"You: {query}\n")
#         except sr.UnknownValueError:
#             st.error("Google Speech Recognition could not understand audio.")
#         except sr.RequestError as e:
#             st.error(f"Could not request results from Google Speech Recognition service; {e}")
    
#     return query

# def speak(question, key, lang):
#     speech = gTTS(text=question, lang=lang, slow=False, tld="co.in")
#     filename = f'Questions/Q{key}.mp3'
#     speech.save(filename)
#     st.audio(filename)

# os.makedirs('Questions', exist_ok=True)

# def speech_to_text_english(lang):
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = r.listen(source)
#         st.write("Generating...")
#     try:
#         user_input = r.recognize_google(audio, language=lang)
#         st.warning(f'You: {user_input}')
#         return user_input
#     except sr.UnknownValueError:
#         st.write("Oops, I didn't get your audio, Please try again.")
#         return None

# def speech_to_text_urdu(lang):
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("بولنا شروع کریں ...")
#         audio = r.listen(source)
#         st.write("براہ مہربانی جواب کا انتظار کریں")
#     try:
#         user_input = r.recognize_google(audio, language=lang)
#         st.warning(f'آپ: {user_input}')
#         return user_input
#     except sr.UnknownValueError:
#         st.write("اوہو، مجھے آپ کا آڈیو نہیں ملا، براہ کرم دوبارہ کوشش کریں...")
#         return None

# def text_to_speech(answer, key, lang):
#     speech = gTTS(text=answer, lang=lang, slow=False, tld="co.in")
#     filename = f'Answers/A{key}.mp3'
#     speech.save(filename)
#     st.audio(filename)

# os.makedirs('Answers', exist_ok=True)


# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# chat = ChatOpenAI(
#     temperature=0.5,
#     model_name="gpt-3.5-turbo",
#     openai_api_key=openai_api_key,
#     max_tokens=100,
# )

# def get_response(user_input):
#     intro_message = """You are a Mental Health Care Expert for OSTF Organization, here to guide and assist people with their health questions and concerns. Please provide accurate and helpful information, and always maintain a polite and professional tone.
#                        Your answer should be complete and precise.
#                        You have to answer only health related questions.
#                        You understand only urdu and english.
#                        If a user tell his/her name, age, address, phone number, YES or No then you have to thank him for giving the response."""
#     messages = [
#         SystemMessage(content=intro_message),
#         HumanMessage(content=user_input),
#     ]
#     response = chat(messages).content
#     return response

# def display_languages(languages):
#     # st.header("Translator", divider='green')
#     st.subheader("Language Names")

#     # Extract language names from the tuple
#     language_names = languages[::2]

#     st.write(language_names)

# def lang_speak(text, lang):
#     if not text:
#         st.warning("No text to speak.")
#         return
#     speech = gTTS(text=text, lang=lang, slow=False, tld="co.in")
#     key = str(uuid.uuid4())
#     filename = f'Languages/{lang+"_"+key}.mp3'
#     speech.save(filename)
#     with st.spinner('Wait for it...'):
#         time.sleep(2)
#     return st.audio(f'Languages/{lang+"_"+key}.mp3')

# # Make a folder
# os.makedirs('Languages', exist_ok=True)

# questions = [
#     ("What is your name?", 1, "آپ کا نام کيا ہے?"),
#     ("What is your age?", 2, "آپ کی عمر کیا ہے؟"),
#     ("What is your address?", 3, "آپ کا پتہ کیا ہے؟"),
#     ("Are you taking any Medicine? If yes, then please tell name of the medicines", 4, "کیا آپ کوئی دوا لے رہے ہیں؟اگر ہاں. پھر دوا کا نام بتائیں "),
#     ("What other medicine you have taken in the Past?", 5, "آپ نے ماضی میں اور کون سی دوا لی ہے؟ "),
#     # ("What is your major complaint?", 6, "آپ کی سب سے بڑی شکایت کیا ہے؟ "),
#     # ("Have you previously suffered from this complaint?: If Yes, enter previous therapists seen for complaint and describe treatment, Aggravating Factors, Relieving Factors.", 7, "کیا آپ کو پہلے اس شکایت کا سامنا کرنا پڑا ہے؟: اگر ہاں، تو شکایت کے لئے دیکھے گئے پچھلے تھراپسٹوں کو درج کریں، علاج، بڑھنے والے عوامل، راحت دینے والے عوامل کی وضاحت کریں."),
#     # ("Were you adopted? If yes, at what age?", 8, "کیا آپ کو گود لیا گیا تھا؟ اگر ہاں، تو کس عمر میں؟ "),
#     # ("How is your relationship with your mother?", 9, "ماں کے ساتھ آپ کا رشتہ کیسا ہے؟ "),
#     # ("How is your relationship with your father?", 10, "اپنے والد کے ساتھ آپ کے تعلقات کیسے ہیں؟"),
#     # ("How is your relationship with your siblings? Also mention their ages.", 11, "اپنے بہن بھائیوں کے ساتھ آپ کے تعلقات کیسے ہیں؟ ان کی عمروں کا بھی ذکر کریں")
# ]

# # Initialize the responses using Streamlit's session state
# if 'responses' not in st.session_state:
#     st.session_state.responses = {}

# st.cache()
# # Streamlit app
# def ask_question():
#         for i, (question, key, urdu_question) in enumerate(questions):
#             response_key = f"response_{i}"
#             if response_key not in st.session_state.responses:
#                 st.session_state.responses[response_key] = ""
#             if selected_language == 'en':
#                 with st.expander(f"Question: {key}"):
#                     # if st.button(f"Question: {i + 1}", key = str(f"Q{i}+1")):
#                     speak(question, key, selected_language)
                    
#                     # st.subheader(f"Q{i+1}-  {question}")
#                     # if st.button(f"Answer", key = str(f"A{i+1}")):
#                         # st.write("Don't speak until the *(listening...)* text appears.")
#                     audio_bytes = audio_recorder(key = str(f"A{i+1}"))
#                     query = recognize_audio(audio_bytes, "en-EN")
#                         # user_input = speech_to_text_english('en-EN')
#                     if query:
#                         st.session_state.responses[response_key] = query
#                         output = get_response(query)
#                         v = str(f"{i+1}")
#                         text_to_speech(output, v, 'en')
#                         st.success(f"{output}")
                            

#             elif selected_language == 'ur':
#                 with st.expander(f"Question: {key}"):
#                     # if st.button(f"Question: {i + 1}", key = str(f"Q{i}+1")):
#                     speak(urdu_question, key, selected_language)
                    
#                     audio_bytes = audio_recorder(key = str(f"A{i+1}"))
#                     query = recognize_audio(audio_bytes, "ur-UR")
#                     # if st.button(f"جواب", key = str(f"A{i+1}")):
#                     #     st.write("اس وقت تک بات نہ کریں جب تک *(میں آپ کو سن رہا ہوں ...)* تحریری متن ظاہر نہ ہو۔")
#                     #     user_input = speech_to_text_urdu('ur-UR')
#                     if query:
#                         st.session_state.responses[response_key] = query
#                         output = get_response(query)
#                         v = str(f"{i+1}")
#                         text_to_speech(output, v, 'ur')
#                         st.success(f"{output}")

#             else:
#                 if selected_language == 'en':
#                     st.warning("Please select the language first.")
#                 elif selected_language == 'ur':
#                     st.warning("براہ مہربانی دوسرے سوال کی طرف جائیں۔")
#             st.divider()


# def intro():
#     if selected_language == 'en':
#         speak("Welcome to ICNA-Relief","0", 'en')
#     elif selected_language == 'ur':
#         speak("آئی سی این اے ریلیف میں خوش آمدید. شکریہ", '0', 'ur')

# st.set_page_config(
#     page_title="OSTF App",
#     page_icon="🧊",
#     layout="wide",
# )
# # st.image('Shine.png')
# # , caption='Copyright 2024 by OSTF. All Rights Reserved.'
# st.header('Health Intake Questionnaire', divider='blue')
# st.markdown('''Welcome To! :blue[ICNA] - :blue[Relief]''')
# # code = '''print("Made by: Hassan Mustafa")'''
# # st.code(code, language='python')

# selected_language = st.selectbox("Select Language", ["en", "ur"])

# tab1, tab2, tab3 = st.tabs(["Q & A", "Translator", "Stored Data"])

# with tab1:
#     # if st.button("Start"):
#     intro()
#     ask_question()

# with tab2:
#     dic = (
#         'arabic', 'ar', 
#         'bengali', 'bn', 
#         'chinese (simplified)', 'zh-cn', 
#         'chinese (traditional)', 'zh-tw',
#         'english', 'en',
#         'french', 'fr', 
#         'german', 'de',
#         'gujarati', 'gu',  
#         'hawaiian', 'haw', 
#         'hebrew', 'he', 
#         'hindi', 'hi',
#         'italian', 'it', 
#         'japanese', 'ja',
#         'korean', 'ko',
#         'malayalam', 'ml',
#         'marathi', 'mr',
#         'nepali', 'ne', 
#         'russian', 'ru', 
#         'spanish', 'es',
#         'tamil', 'ta',
#         'urdu', 'ur',) 

#     # Your dictionary of language codes
#     languages_dict = {
#         'arabic': 'ar', 
#         'bengali': 'bn',  
#         'chinese (simplified)': 'zh-CN', 
#         'chinese (traditional)': 'zh-TW',  
#         'english': 'en',  
#         'french': 'fr', 
#         'german': 'de', 
#         'gujarati': 'gu', 
#         'hebrew': 'iw', 
#         'hindi': 'hi',  
#         'italian': 'it', 
#         'japanese': 'ja',  
#         'korean': 'ko', 
#         'malayalam': 'ml',  
#         'marathi': 'mr',  
#         'nepali': 'ne', 
#         'russian': 'ru', 
#         'spanish': 'es', 
#         'tamil': 'ta',  
#         'urdu': 'ur', 
#         }

#     # languages_dict = {
#     #     'english': 'en',
#     #     'urdu': 'ur',
#     # }

#     display_languages(dic)
#     # Get user's selection (single select)
#     selected_language = st.selectbox("Select Language", list(languages_dict.keys()))

#     # Map selected language to its corresponding code
#     selected_language_code = languages_dict[selected_language]

#     # Display selected language code
#     # st.write("Selected Language Code:", selected_language_code)

#     audio_bytes = audio_recorder()
#     query = recognize_audio_2(audio_bytes)
#     translated = GoogleTranslator(source='auto', target=f'{selected_language_code}').translate(query)
    
#     if translated is not None:
#         st.warning(f"Translate: {translated}")
        
#         # Generate the audio
#         audio = lang_speak(str(translated), selected_language_code)
        

# with tab3:
#     st.write("### User Stored Data")
#     # st.success("Stored Data")
#     for i, (question, key, urdu_question) in enumerate(questions):
#         response_key = f"response_{i}"
#         if response_key in st.session_state.responses:
#             if selected_language == 'en':
#                 st.write(f"Q{i+1} - {question} <br> A{i+1} - {st.session_state.responses[response_key]}", unsafe_allow_html=True)
#                 st.divider()
#             if selected_language == 'ur':
#                 st.write(f"Q{i+1} - {urdu_question} <br> A{i+1} - {st.session_state.responses[response_key]}", unsafe_allow_html=True)
#                 st.divider()