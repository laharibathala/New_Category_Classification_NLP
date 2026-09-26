# 📰 NLP-Based News Category Classification

## 📌 Project Overview

This project classifies news articles into different categories using Natural Language Processing (NLP) and Deep Learning.

The text data is preprocessed and converted into numerical sequences using tokenization. A GRU (Gated Recurrent Unit) neural network is used to predict the category of a news article.

## 🎯 Objective

The main objective of this project is to automatically classify news articles into their appropriate categories based on their textual content.

## 🧠 Technologies Used

- Python
- Natural Language Processing (NLP)
- Machine Learning
- Deep Learning
- TensorFlow / Keras
- GRU (Gated Recurrent Unit)
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

## 📰 News Categories

The model predicts news articles into four categories:

- 🌍 World
- 🏏 Sports
- 💼 Business
- 💻 Sci/Tech

## 🔄 Project Workflow

1. Load the news dataset
2. Clean and preprocess the text
3. Tokenize the news articles
4. Convert text into numerical sequences
5. Apply padding
6. Split the data into training and testing sets
7. Build the GRU deep learning model
8. Train the model
9. Evaluate the model
10. Predict the news category
11. Deploy the model using Streamlit

## 🤖 Model

The project uses a GRU (Gated Recurrent Unit) neural network for news text classification.

GRU is a type of recurrent neural network that is suitable for sequential data such as text. It learns patterns and dependencies in news articles and uses them to predict the appropriate category.

## 📁 Project Files

| File | Description |
|---|---|
| `New_Category_Classification_NLP.ipynb` | Complete NLP and model development notebook |
| `app.py` | Streamlit application |
| `news_category_gru_final.keras` | Trained GRU model |
| `news_category_tokenizer.pkl` | Saved text tokenizer |
| `test.csv` | Test dataset |
| `requirements.txt` | Required Python libraries |
| `README.md` | Project documentation |

> `train.csv` is not included because the file size exceeds GitHub's browser upload limit.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/laharibathala/New_Category_Classification_NLP.git
```

### 2. Install required libraries

```bash
pip install pandas numpy scikit-learn tensorflow streamlit joblib
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

## 💻 Sample Prediction

### Input

```text
A major sports event was held today and the team won the match by five wickets.
```

### Output

```text
Predicted Category: Sports
Confidence: 98.18%
```

## 📌 Applications

- Automatic news classification
- News recommendation systems
- News portals
- Content organization
- Text classification systems
- Automated content categorization

## 🚀 Live Demo

[Click here to try the News Category Classification App](https://newcategoryclassificationnlp-aeh4uku4exzgr3dfwq4uit.streamlit.app/)

## 📈 Model Performance

The model performance can be evaluated using the test dataset. The testing accuracy can be added here based on the final evaluation result from the notebook.

## 👩‍💻 Author

**Lahari Bathala**

B.Tech Graduate | Aspiring Data Scientist

### Skills

Python | SQL | Machine Learning | NLP | Deep Learning | Data Analysis
