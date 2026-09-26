import streamlit as st
import tensorflow as tf
import pickle
import re
import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="News Category Classification",
    page_icon="📰",
    layout="centered"
)


# -----------------------------------
# Load Model
# -----------------------------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "news_category_gru_final.keras"
    )


# -----------------------------------
# Load Tokenizer
# -----------------------------------

@st.cache_resource
def load_tokenizer():
    with open(
        "news_category_tokenizer.pkl",
        "rb"
    ) as file:
        return pickle.load(file)


model = load_model()
tokenizer = load_tokenizer()


# -----------------------------------
# Categories
# -----------------------------------

class_names = [
    "World",
    "Sports",
    "Business",
    "Sci/Tech"
]


# -----------------------------------
# Text Preprocessing
# -----------------------------------

def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# -----------------------------------
# Prediction Function
# -----------------------------------

def predict_category(text):

    clean_text = preprocess_text(text)

    sequence = tokenizer.texts_to_sequences(
        [clean_text]
    )

    padded_sequence = pad_sequences(
        sequence,
        maxlen=100,
        padding="post",
        truncating="post"
    )

    prediction = model.predict(
        padded_sequence,
        verbose=0
    )

    predicted_index = np.argmax(
        prediction,
        axis=1
    )[0]

    confidence = prediction[0][predicted_index]

    return (
        class_names[predicted_index],
        confidence
    )


# -----------------------------------
# Streamlit Interface
# -----------------------------------

st.title("📰 News Category Classification")

st.write(
    "Enter a news article and the model "
    "will predict its category."
)

st.info(
    "Categories: World | Sports | Business | Sci/Tech"
)


# -----------------------------------
# News Input
# -----------------------------------

news_text = st.text_area(
    "Enter News Article",
    height=180,
    placeholder="Example: India defeated Australia in the final match."
)


# -----------------------------------
# Prediction Button
# -----------------------------------

if st.button(
    "🔍 Predict Category",
    use_container_width=True
):

    if news_text.strip() == "":
        st.warning(
            "Please enter a news article."
        )

    else:

        category, confidence = predict_category(
            news_text
        )

        st.success(
            f"Predicted Category: {category}"
        )

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )


# -----------------------------------
# Footer
# -----------------------------------

st.divider()

st.caption(
    "Model: Embedding + GRU + Dense | "
    "Dataset: AG News"
)