# 📚 Bayesian Text Classification – Naive Bayes Book Categorization

## 📌 Project Overview
This project implements **Bayes' Theorem** in a practical **text classification** setting.  
The goal is to classify Persian-language books into specific categories using **Naive Bayes classification**, after rigorous **text preprocessing**.

---

## 🔧 Key Components

### 1️⃣ Bayes’ Theorem
- Formula:  
  \[
  P(c|x) = \frac{P(x|c)P(c)}{P(x)}
  \]
  - `P(c|x)` – Posterior probability  
  - `P(x|c)` – Likelihood  
  - `P(c)` – Prior  
  - `P(x)` – Evidence  
- Foundation for the **Naive Bayes Classifier** used in this project

---

### 2️⃣ Text Preprocessing (Persian NLP)
- Dataset contains Persian **book descriptions**
- Tools:
  - `hazm` library for Persian text normalization
- Steps:
  - Remove punctuation, numbers, and irrelevant characters
  - Tokenization
  - Stemming & Lemmatization
  - Stop-word removal
  - Constructing **Bag-of-Words (BoW)** vectors

---

### 3️⃣ Book Classification Task

- **Target Labels** (6 categories):
  - 📘 Novels
  - 📗 Short Stories
  - 📕 Sociology
  - 📙 Islamic Studies
  - 📒 Management
  - 📓 Children’s Literature

- Workflow:
  - Train on `books_train.csv`
  - Predict on `books_test.csv`
  - Use **additive smoothing** to handle unseen words in test data

---

## 📈 Project Phases

### ✅ Phase 1: Data Preprocessing
- Clean and normalize text
- Tokenize and build feature vectors (BoW)

### ✅ Phase 2: Naive Bayes Classification
- Train Naive Bayes on training set
- Predict classes on test set
- Handle sparse word issues with **Laplace smoothing**

### ✅ Phase 3: Improving Accuracy
- Apply stemming & lemmatization
- Remove common Persian stop words
- Evaluate accuracy before and after enhancements

---
## 📊 Deliverables

- ✅ **Cleaned and Preprocessed Dataset**
- ✅ **Python Code** for training and testing Naive Bayes classifier
- ✅ **Accuracy Evaluation** with confusion matrix
- ✅ **Final Report** documenting methods, decisions, and accuracy improvements

---

## 🛠️ Libraries Used
`Python` • `hazm` • `NumPy` • `Pandas` • `Matplotlib` • `scikit-learn`

---

## 🎓 Course Information
**Course**: Probability & Statistics  
📍 University of Tehran 
