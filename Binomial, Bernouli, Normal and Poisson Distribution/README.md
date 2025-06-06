# 📈 Statistical Distributions & Approximations – Probability & Statistics Project

## 📌 Project Overview
This project explores the properties and interconnections of common **statistical distributions**, including **Bernoulli**, **Binomial**, **Poisson**, and **Normal** distributions.  
The goal is to simulate these distributions, understand their relationships, and analyze their applicability in real-world scenarios through **Python-based statistical modeling**.

---

## 🔧 Key Components

### 1️⃣ Binomial & Bernoulli Distributions
- Demonstrates how repeated **Bernoulli trials** lead to a **Binomial distribution**
- Simulates different success probabilities `p` and calculates:
  - 📊 Mean: `E[Y] = np`
  - 📉 Variance: `Var(Y) = np(1 - p)`
- Compares simulated vs. theoretical values

---

### 2️⃣ Approximating Binomial: Poisson & Normal
- Investigates how the **Binomial distribution** can be approximated under specific conditions:
  - 🟣 **Poisson Approximation**: Works well when `n` is large and `p` is small (sparse events)
  - 🔵 **Normal Approximation**: Accurate when `n` is large and `p ≈ 0.5`
- Visual comparisons:
  - Simulated Binomial vs. approximating Poisson / Normal distribution
  - Accuracy of fit depending on parameters

---

### 3️⃣ Normal Distribution in Practice
- Demonstrates core features of the **Normal distribution**
- Shows how it emerges from the **Central Limit Theorem (CLT)**
- Applies normal approximation to real-world scenarios:
  - Probabilities of events
  - Standardization and Z-scores

---

## 📦 Deliverables

- ✅ **Python Code**:
  - Simulates Binomial, Bernoulli, Poisson, and Normal distributions
  - Performs approximation checks and theoretical validation

- 📈 **Graphs**:
  - Visualize fit between distributions
  - Compare experimental vs. theoretical mean/variance

- 📊 **Statistical Analysis**:
  - When and why approximations hold
  - Impact of parameters on distribution shape and accuracy

---

## 🛠️ Libraries Used
`NumPy` • `SciPy` • `Matplotlib` • `Seaborn` • `Statsmodels`

---

## 🎓 Course Information
**Course**: Probability & Statistics  
📍 University of Tehran  
