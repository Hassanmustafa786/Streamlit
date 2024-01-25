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
from operator import itemgetter
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnablePassthrough


def recognize_audio(audio_bytes, lang):
    query = ""  
    if audio_bytes:
        # st.audio(audio_bytes, format="audio/wav")
        r = sr.Recognizer()
        try:
            with io.BytesIO(audio_bytes) as wav_io:
                with sr.AudioFile(wav_io) as source:
                    audio_data = r.record(source)
                    query = r.recognize_google(audio_data, language= lang)  # Change the language code if needed
                    st.warning(f"You: {query}\n")
        except sr.UnknownValueError:
            st.error("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
    
    return query

os.makedirs('Questions/English', exist_ok=True)
os.makedirs('Questions/Urdu', exist_ok=True)
os.makedirs('Questions/Spanish', exist_ok=True)
os.makedirs('Questions/Bengali', exist_ok=True)
os.makedirs('Questions/Arabic', exist_ok=True)

os.makedirs('Answers/English', exist_ok=True)
os.makedirs('Answers/Urdu', exist_ok=True)
os.makedirs('Answers/Spanish', exist_ok=True)
os.makedirs('Answers/Bengali', exist_ok=True)
os.makedirs('Answers/Arabic', exist_ok=True)


def speak(question, key, lang):
    if lang == 'en':
        folder_name = 'Questions/English'
    elif lang == 'es':
        folder_name = 'Questions/Spanish'
    elif lang == 'ur': 
        folder_name = 'Questions/Urdu'
    elif lang == 'bn': 
        folder_name = 'Questions/Bengali'
    elif lang == 'ar': 
        folder_name = 'Questions/Arabic'
    
    filename = f'{folder_name}/Q{key}.mp3'
    if not os.path.exists(filename):
        speech = gTTS(text=question, lang=lang, slow=False, tld="co.in")
        speech.save(filename)
    st.audio(filename)

def text_to_speech(answer, key, lang):
    speech = gTTS(text=answer, lang=lang, slow=False, tld="co.in")
    if lang == 'en':
        filename = f'Answers/English/A{key}.mp3'
        speech.save(filename)
    elif lang == 'ur':
        filename = f'Answers/Urdu/A{key}.mp3'
        speech.save(filename)
    elif lang == 'es':
        filename = f'Answers/Spanish/A{key}.mp3'
        speech.save(filename)
    elif lang == 'bn':
        filename = f'Answers/Bengali/A{key}.mp3'
        speech.save(filename)
    elif lang == 'ar':
        filename = f'Answers/Arabic/A{key}.mp3'
        speech.save(filename)
    st.audio(filename)

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(
    temperature=0.5,
    model_name="gpt-3.5-turbo",
    openai_api_key=openai_api_key,
    max_tokens=100,
)

# Create a single memory instance for the entire conversation
memory = ConversationBufferMemory(return_messages=True)

def get_response(input_message, model, memory):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """ You are a Health Care Expert for ICNA Relief, here to guide and assist people with their health questions and concerns. Please provide accurate and helpful information, and always maintain a polite and professional tone.
                       Your answer should be complete and precise.
                       If a user tell his/her name, age, address then just thank him and end the chat.
                       If a user tell his/her about personal life then just thank him and end the chat.
                       You have to answer briefly only health related questions.
                       You understand only these languages urdu, english, spanish, arabic and bengali.
                       If a user talk with different language which is not given then tell him I cannot understand your language."""),
        MessagesPlaceholder(variable_name="history"),
        ("human", f"{input_message}"),
    ])

    chain = (
        RunnablePassthrough.assign(
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
        )
        | prompt
        | model
    )

    inputs = {"input": input_message}
    response = chain.invoke(inputs)

    # Save the context for future interactions
    memory.save_context(inputs, {"output": response.content})
    memory.load_memory_variables({})

    return response.content

questions = [
    ("What is your name?", 1, "آپ کا نام کيا ہے?", "¿Cómo te llamas?", "আপনার নাম কি?", "ما اسمك؟"),
    ("What is your age?", 2, "آپ کی عمر کیا ہے؟", "¿Cuántos años tienes?", "আপনার বয়স কত?", "ما هو عمرك؟"),
    ("What is your address?", 3, "آپ کا پتہ کیا ہے؟", "¿Cuál es su dirección?", "আপনার ঠিকানা কি?", "ما هو عنوانك؟"),
    ("Are you taking any Medications? If yes, then please tell name of the medication.", 4, "کیا آپ کوئی دوا لے رہے ہیں؟اگر ہاں. پھر دوا کا نام بتائیں ", "¿Está tomando algún medicamento? En caso afirmativo, indique el nombre del medicamento.", "আপনি কি কোনো ওষুধ খাচ্ছেন? যদি হ্যাঁ, তাহলে ওষুধের নাম বলুন।", "هل أنت مع أي أدوية؟ إذا كانت الإجابة بنعم، يرجى ذكر اسم الدواء."),
    ("Can you name the medicines?", 5, "کیا آپ ادویات کے نام بتا سکتے ہیں؟ ", "¿Puedes nombrar los medicamentos?", "ওষুধের নাম বলতে পারবেন?", "هل يمكنك تسمية الأدوية؟"),
    ("What other medicine have you taken in the past?", 6, "آپ نے ماضی میں اور کون سی دوا لی ہے؟ ", "¿Qué otro medicamento ha tomado en el pasado?", "অতীতে আপনি অন্য কোন ওষুধ খেয়েছেন?", "ما هي الأدوية الأخرى التي تناولتها في الماضي؟"),
    ("What is your major complaint?", 7, "آپ کی سب سے بڑی شکایت کیا ہے؟ ", "¿Cuál es su principal queja?", "আপনার প্রধান অভিযোগ কি?", "ما هي شكواك الرئيسية؟"),
    ("Have you previously suffered from this complaint?", 8, "کیا آپ کو پہلے بھی اس شکایت کا سامنا کرنا پڑا ہے؟", "¿Ha sufrido anteriormente esta dolencia?", "আপনি কি আগে এই অভিযোগ থেকে ভুগছেন?", "هل عانيت من قبل من هذه الشكوى؟"),
    ("What previous therapists have you seen?", 9, "آپ نے پچھلے کون سے تھراپسٹ کو دیکھا ہے؟", "¿A qué terapeuta has visto anteriormente?", "আপনি কি আগের থেরাপিস্ট দেখেছেন?", "ما المعالجين السابقين الذين رأيتهم؟"),
    ("Can you describe the treatment?", 10, "کیا آپ علاج کی وضاحت کر سکتے ہیں؟", "¿Puede describir el tratamiento?", "আপনি চিকিত্সা বর্ণনা করতে পারেন?", "هل يمكنك وصف العلاج؟"),
    ("What is your family history?", 11, "کیا آپ مجھے اپنے خاندان کی تاریخ کے بارے میں بتا سکتے ہیں؟", "¿Cuál es su historia familiar?", "আপনার পারিবারিক ইতিহাস কি?", "ما هو تاريخ عائلتك؟"),
    ("Are you adopted?", 12, "کیا آپ کو گود لیا گیا تھا؟", "¿Eres adoptado?", "আপনি কি দত্তক?", "هل أنت متبنى؟"),
    ("If yes, at what age were you adopted?", 13, "اگر ہاں، تو آپ کو کس عمر میں گود لیا گیا تھا؟", "En caso afirmativo, ¿a qué edad fue adoptado?", "যদি হ্যাঁ, কোন বয়সে আপনাকে দত্তক নেওয়া হয়েছিল?", "إذا كانت الإجابة بنعم، في أي عمر تم تبنيك؟"),
    ("How is your relationship with your mother?", 14, "ماں کے ساتھ آپ کا رشتہ کیسا ہے؟", "¿Cómo es tu relación con tu madre?", "আপনার মায়ের সাথে আপনার সম্পর্ক কেমন?", "كيف هي علاقتك مع والدتك؟"),
    ("Where did you grow up?", 15, "آپ کہاں بڑے ہوئے؟", "¿Dónde creciste?", "আপনি কোথায় বড় হয়েছেন?", "أين نشأت؟"),
    ("Are you married?", 16, "کيا آپ شادی شدہ ہيں", "¿Estás casado?", "আপনি কি বিবাহিত?", "هل أنت متزوج؟"),
    ("If yes, specify the date of marriage?", 17, "اگر ہاں، تو شادی کی تاریخ بتائیں؟", "En caso afirmativo, especifique la fecha del matrimonio.", "যদি হ্যাঁ, বিয়ের তারিখ উল্লেখ করবেন?", "إذا كانت الإجابة بنعم، حدد تاريخ الزواج؟"),
    ("Do you have children?", 18, "کیا آپ کے بچے ہیں؟", "¿Tienes hijos?", "আপনার কি সন্তান আছে?", "هل لديك أطفال؟"),
    ("If yes, how is your relationship with your children?", 19, "کیا آپ کے بچے ہیں؟", "En caso afirmativo, ¿cómo es su relación con sus hijos?", "যদি হ্যাঁ, আপনার সন্তানদের সাথে আপনার সম্পর্ক কেমন?", "إذا نعم كيف هي علاقتك مع أطفالك؟"),
]

# Initialize the responses using Streamlit's session state
if 'en_responses' not in st.session_state:
    st.session_state.en_responses = {}
if 'ur_responses' not in st.session_state:
    st.session_state.ur_responses = {}
if 'es_responses' not in st.session_state:
    st.session_state.es_responses = {}
if 'bn_responses' not in st.session_state:
    st.session_state.bn_responses = {}
if 'ar_responses' not in st.session_state:
    st.session_state.ar_responses = {}
# ar-SA
# if 'audio_responses' not in st.session_state:
#     st.session_state.audio_responses = {}

st.cache()
# Streamlit app
def ask_question():
    # audio_responses = {}
    for i, (en_question, key, ur_question, es_question, bn_question, ar_question) in enumerate(questions):
        response_key = f"response_{i}"
        st.write(f"Question: {i+1}")
        if selected_language == 'en':
            if response_key not in st.session_state.en_responses:
                st.session_state.en_responses[response_key] = ""
            
            speak(en_question, key, selected_language)
            audio_bytes = audio_recorder(key = str(f"Q{i+1}"))
            user_input = recognize_audio(audio_bytes, "en-EN")
            
            if user_input:
                st.session_state.en_responses[response_key] = user_input
                output = get_response(user_input, chat, memory)
                v = str(f"{i+1}")
                text_to_speech(output, v, 'en')
                st.success(f"{output}")

        elif selected_language == 'ur':
            if response_key not in st.session_state.ur_responses:
                st.session_state.ur_responses[response_key] = ""
            
            speak(ur_question, key, selected_language)
            audio_bytes = audio_recorder(key = str(f"Q{i+1}"))
            user_input = recognize_audio(audio_bytes, "ur-UR")
            if user_input:
                st.session_state.ur_responses[response_key] = user_input
                output = get_response(user_input, chat, memory)
                v = str(f"{i+1}")
                text_to_speech(output, v, 'ur')
                st.success(f"{output}")
        
        elif selected_language == 'es':
            if response_key not in st.session_state.es_responses:
                st.session_state.es_responses[response_key] = ""
            
            speak(es_question, key, selected_language)
            audio_bytes = audio_recorder(key = str(f"Q{i+1}"))
            user_input = recognize_audio(audio_bytes, "es-ES")
            if user_input:
                st.session_state.es_responses[response_key] = user_input
                output = get_response(user_input, chat, memory)
                v = str(f"{i+1}")
                text_to_speech(output, v, 'es')
                st.success(f"{output}")
                
        elif selected_language == 'bn':
            if response_key not in st.session_state.bn_responses:
                st.session_state.bn_responses[response_key] = ""
            
            speak(bn_question, key, selected_language)
            audio_bytes = audio_recorder(key = str(f"Q{i+1}"))
            user_input = recognize_audio(audio_bytes, "bn-BD")
            if user_input:
                st.session_state.bn_responses[response_key] = user_input
                output = get_response(user_input, chat, memory)
                v = str(f"{i+1}")
                text_to_speech(output, v, 'bn')
                st.success(f"{output}")
        elif selected_language == 'ar':
            if response_key not in st.session_state.ar_responses:
                st.session_state.ar_responses[response_key] = ""
            
            speak(ar_question, key, selected_language)
            audio_bytes = audio_recorder(key = str(f"Q{i+1}"))
            user_input = recognize_audio(audio_bytes, "ar-SA")
            if user_input:
                st.session_state.ar_responses[response_key] = user_input
                output = get_response(user_input, chat, memory)
                v = str(f"{i+1}")
                text_to_speech(output, v, 'ar')
                st.success(f"{output}")
        else:
            if selected_language == 'en':
                st.warning("Please select the language first.")
            elif selected_language == 'ur':
                st.warning("براہ مہربانی دوسرے سوال کی طرف جائیں۔")
            elif selected_language == 'es':
                st.warning("Por favor, seleccione el idioma primero.")
            elif selected_language == 'bn':
                st.warning("প্রথমে ভাষা নির্বাচন করুন.")
            elif selected_language == 'ar':
                st.warning("الرجاء تحديد اللغة أولا.")
        
        # audio_responses[response_key] = audio_bytes
        # if response_key not in st.session_state.audio_responses:
        #         st.session_state.audio_responses[response_key] = audio_bytes
        st.divider()
    # return audio_responses

def intro():
    if selected_language == 'en':
        speak("Welcome to ICNA-Relief","0", 'en')
    elif selected_language == 'ur':
        speak("آئی سی این اے ریلیف میں خوش آمدید. شکریہ", '0', 'ur')
    elif selected_language == 'es':
        speak("Bienvenidos a ICNA-Relief", '0', 'es')
    elif selected_language == 'bn':
        speak("ICNA-রিলিফে স্বাগতম", '0', 'bn')
    elif selected_language == 'ar':
        speak("مرحبا بكم في إغاثة ICNA", '0', 'ar')

st.set_page_config(
    page_title="OSTF App",
    page_icon="🧊",
    layout="wide",
)
# st.image('Shine.png')
# st.caption='Copyright 2024 by OSTF. All Rights Reserved.'
st.header('Health Intake Questionnaire', divider='rainbow')
st.markdown('''Welcome To! :blue[I C N A] - :blue[Releif Organization]''')

selected_language = st.selectbox("Select Language", ["en", "ur", "es", "bn", "ar"])
tab1, tab2 = st.tabs(["Q & A", "Stored Data"])
with tab1:
    intro()
    st.divider()
    
    ask_question()

with tab2:
    st.write("### User Stored Data")
    # st.success("Stored Data")
    for i, (question, key, ur_question, es_question, bn_question, ar_question) in enumerate(questions):
        response_key = f"response_{i}"
        if selected_language == 'en':
            if response_key in st.session_state.en_responses:
                st.write(f"Q{i+1} - {question} <br> A{i+1} - {st.session_state.en_responses[response_key]}", unsafe_allow_html=True)
                audio_path = f'Answers/English/A{i+1}.mp3'
                if os.path.exists(audio_path):
                    st.audio(audio_path)
                else:
                    st.warning("Audio file not found.")
        elif selected_language == 'ur':
            if response_key in st.session_state.ur_responses:
                st.write(f"Q{i+1} - {ur_question} <br> A{i+1} - {st.session_state.ur_responses[response_key]}", unsafe_allow_html=True)
                audio_path = f'Answers/Urdu/A{i+1}.mp3'
                if os.path.exists(audio_path):
                    st.audio(audio_path)
                else:
                    st.warning("Audio file not found.")
        elif selected_language == 'es':
            if response_key in st.session_state.es_responses:
                st.write(f"Q{i+1} - {es_question} <br> A{i+1} - {st.session_state.es_responses[response_key]}", unsafe_allow_html=True)
                audio_path = f'Answers/Spanish/A{i+1}.mp3'
                if os.path.exists(audio_path):
                    st.audio(audio_path)
                else:
                    st.warning("Audio file not found.")
        elif selected_language == 'bn':
            if response_key in st.session_state.bn_responses:
                st.write(f"Q{i+1} - {bn_question} <br> A{i+1} - {st.session_state.bn_responses[response_key]}", unsafe_allow_html=True)
                audio_path = f'Answers/Bengali/A{i+1}.mp3'
                if os.path.exists(audio_path):
                    st.audio(audio_path)
                else:
                    st.warning("Audio file not found.")
        elif selected_language == 'ar':
            if response_key in st.session_state.ar_responses:
                st.write(f"Q{i+1} - {ar_question} <br> A{i+1} - {st.session_state.ar_responses[response_key]}", unsafe_allow_html=True)
                audio_path = f'Answers/Arabic/A{i+1}.mp3'
                if os.path.exists(audio_path):
                    st.audio(audio_path)
                else:
                    st.warning("Audio file not found.")
        st.divider()