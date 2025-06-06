# 🎲 Advanced Probability Applications – Probability & Statistics Project

## 📌 Project Overview
This project explores and applies advanced topics in **probability theory**, including **Conditional Distributions**, **Moment Generating Functions (MGF)**, and **Bayesian Estimation**.  
Real datasets and Python-based simulation methods are used to connect theoretical probability with practical applications.

---

## 🔧 Key Components

### 1️⃣ Conditional Distribution – Public Transport Usage
- Dataset: `tarbiat.csv` – contains metro and bus station pass records
- Defined random variables:
  - Number of **bus** passes
  - Number of **metro** passes
- Tasks:
  - Histogram analysis of both variables
  - Fit to possible distributions (e.g. Poisson, Binomial, Geometric)
  - Estimate parameters and compare with empirical data

---

### 2️⃣ Moment Generating Function (MGF) – Coupon Collector's Problem
- Problem: Estimate expected trials (X) to collect all unique items
- Techniques:
  - 🔁 **Monte Carlo Simulation** to empirically estimate `E[X]`
  - 🧠 **MGF derivation** using symbolic math (`SymPy`)
  - Comparison of theoretical vs. simulated expectations

---

### 3️⃣ Bayesian Estimation – Handwritten Digits
- Dataset: `digits.csv` – binary pixel data of handwritten digits
- Objective:
  - For each pixel: model as **Bernoulli distribution**
  - Use **Beta distribution** as prior
  - Perform **Bayesian Updating** to compute posterior
- Tools:
  - Visualize prior and posterior distributions
  - Track changes in belief as more data is observed

---

## 📊 Deliverables

- 🐍 **Python Code**:
  - For each theoretical component, with simulation and visualization
- 📉 **Graphs & Plots**:
  - Histograms, MGF estimation curves, Bayesian posterior updates
- 📑 **Statistical Analysis**:
  - Evaluation of fitting models, derivations, and performance of estimation techniques

---

## 🛠️ Libraries Used
`NumPy` • `Matplotlib` • `SymPy` • `Pandas` • `SciPy`

---

## 🎓 Course Information
**Course**: Probability & Statistics  
📍 University of Tehran  
