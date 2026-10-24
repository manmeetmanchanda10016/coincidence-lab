# 🔬 Coincidence Lab — The Mathematics of Coincidence

An interactive Streamlit application exploring how probability, randomness, and repeated statistical tests produce surprising outcomes.

## 🧠 About the Project

Coincidence Lab investigates events that appear unlikely or suspicious but can emerge naturally from mathematical probability. Through interactive visualizations and simulations, the project demonstrates how intuition can misjudge randomness.

## 🔍 Experiments

### 1. 🎂 Birthday Paradox
Explore how the probability of at least two people sharing a birthday changes as group size increases.

- Interactive group-size selection
- Theoretical probability calculations
- Probability curve visualization

### 2. 🪙 Randomness Looks Suspicious
Investigate how streaks and clusters naturally occur in sequences of fair coin tosses.

- Generate random coin-toss sequences
- Calculate the longest Heads streak
- Simulate multiple sequences to estimate streak probabilities

### 3. 🧪 The False Positive Problem
Understand how testing many hypotheses can produce apparently significant results purely by chance.

- Simulate p-values under true null hypotheses
- Compare observed and expected false positives
- Visualize the probability of at least one false positive

### 4. 🔢 The Coincidence Multiplier
Explore how repeated independent opportunities increase the probability of observing at least one match.

- Interactive attempt counter
- Theoretical probability calculations
- Probability curve visualization

## 🛠️ Tech Stack

- **Python** — simulation and probability calculations
- **Streamlit** — interactive web application
- **NumPy** — random number generation and numerical computation
- **Plotly** — interactive data visualizations

## 📐 Mathematical Concepts

- Birthday paradox
- Independent random events
- Monte Carlo simulation
- Statistical significance and false positives
- Multiple hypothesis testing
- Complementary probability

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/manmeetmanchanda10016/coincidence-lab.git
cd coincidence-lab
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

## 📊 Key Insights

- A group of 23 people has approximately a **50.7%** chance of containing at least one shared birthday, assuming equally likely birthdays across 365 days.
- Random sequences can contain long streaks even when each coin toss is fair.
- Testing many hypotheses increases the expected number of false positives.
- Repeated independent opportunities can make an unlikely match substantially more probable.

## ⚠️ Assumptions and Limitations

- Birthday calculations assume 365 equally likely birthdays and ignore leap years.
- Coin-toss simulations assume independent, fair tosses.
- The false-positive experiment simulates independent p-values uniformly distributed between 0 and 1 under true null hypotheses.
- The four-digit matching model assumes independent, uniformly random guesses from 10,000 possible codes.
- Simulation results are estimates; theoretical probabilities depend on the stated assumptions.

## 🎯 Project Goal

To demonstrate how mathematical probability and statistical simulation help explain surprising coincidences and challenge common intuitions about randomness.

---

**Built with Python, Streamlit, NumPy, and Plotly.**
