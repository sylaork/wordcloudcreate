# Gerekli kütüphaneleri içe aktar
import nltk
from nltk import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import stylecloud
from PIL import Image
import matplotlib.pyplot as plt

# NLTK kütüphanesinden gerekli bileşenleri indir
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_and_create_stylecloud(file_path, output_name='stylecloud.png', 
                                     icon_name='fas fa-laptop', lang='english'):
    # Metni dosyadan oku
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Türkçe stopwords listesini yükle
    stop_words = set(stopwords.words(lang))

    # Noktalama işaretlerini kaldır
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Metni tokenlere ayır ve küçük harfe çevir
    tokens = word_tokenize(text.lower(), language=lang)

    # Stopwords'ü filtrele
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Filtrelenmiş tokenleri birleştir
    processed_text = ' '.join(filtered_tokens)

    # StyleCloud oluştur
    stylecloud.gen_stylecloud(text=processed_text,
                              icon_name=icon_name,
                              output_name=output_name)
    # Oluşturulan StyleCloud'u göster
    im = Image.open(output_name)
    plt.figure(figsize=(10, 10))
    plt.imshow(im)
    plt.axis('off')  # Eksenleri gizle
    plt.show()

#pip install pillow==9.4


preprocess_and_create_stylecloud(file_path='AI.txt', 
                             output_name='computer_ai.png', icon_name='fas fa-laptop', lang='english')

import streamlit as st
import stylecloud

def create_stylecloud(text, language, icon):
    output_file = "stylecloud.png"
    
    stylecloud.gen_stylecloud(text=text,
                              icon_name=icon,
                              output_name=output_file)
    
    return output_file

st.title("WordCloud Creator")

file = st.file_uploader("Import txt file", type=["txt"])

if file is not None:
    text = file.getvalue().decode("utf-8")
    
    language = st.radio("Language", ["tr", "en"])
    
    icon_options = ["fas fa-car", "fas fa-star", "fas fa-trophy", "fas fa-heart", 'fas fa-wifi', 'fas fa-laptop', 'fas fa-coffee', 'fas fa-radio', 'fas fa-snowflake']
    icon = st.selectbox("İkon Seçimi", icon_options, index=1)
    
    if st.button("Create"):
        output_file = create_stylecloud(text, language, icon)
        st.markdown(f"### [Download WordCloud](./{output_file})")

        image = Image.open(output_file)
        st.image(image, caption='WordCloud', use_column_width=True)
