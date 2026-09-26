# 📰 NLP-Based News Category Classification

## 📌 Project Overview

This project classifies news articles into different categories using
Natural Language Processing (NLP) and Deep Learning.

The text data is preprocessed and converted into numerical sequences
using tokenization. A GRU (Gated Recurrent Unit) neural network is then
used to predict the category of a news article.

## 🎯 Objective

The main objective of this project is to automatically classify news
articles into their appropriate categories based on their textual content.

## 🧠 Technologies Used

- Python
- Natural Language Processing (NLP)
- TensorFlow / Keras
- GRU (Gated Recurrent Unit)
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Streamlit

## 🔄 Project Workflow

1. Load the news dataset
2. Clean and preprocess the text
3. Tokenize the news articles
4. Convert text into numerical sequences
5. Apply padding
6. Split the dataset into training and testing data
7. Build the GRU deep learning model
8. Train the model
9. Evaluate the model
10. Predict the news category
11. Deploy the model using Streamlit

## 📊 Model

The project uses a **GRU (Gated Recurrent Unit)** neural network
for text classification.

GRU is suitable for NLP tasks because it can learn patterns and
dependencies in sequential text data.

## 📁 Project Files

| File | Description |
|------|-------------|
| `New_Category_Classification_NLP.ipynb` | Complete project notebook |
| `app.py` | Streamlit application |
| `news_category_gru_final.keras` | Trained GRU model |
| `news_category_tokenizer.pkl` | Saved text tokenizer |
| `test.csv` | Test dataset |
| `README.md` | Project documentation |

> `train.csv` is not included because the file size exceeds GitHub's
> browser upload limit.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/laharibathala/New_Category_Classification_NLP.git

### 2. Install required libraries
pip install pandas numpy scikit-learn tensorflow streamlit joblib
### 3. Run the Streamlit application
streamlit run app.py
💻 Sample Prediction

Example:
- Input:
A major sports event was held today...

- Predicted Category:
Sports

- Confidence:
98.18%
📌 Applications
- Automatic news classification
- News recommendation systems
- News portals
- Content organization
- Text classification systems
👩‍💻 Author

- Lahari Bathala

B.Tech Graduate | Aspiring Data Scientist

- Skills

- Python | SQL | Machine Learning | NLP | Deep Learning | Data Analysis


### Step 3: Save it

- After pasting:

**Scroll down → Commit changes**

- Commit message:

```text
Update project README
