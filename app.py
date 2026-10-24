import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Coincidence Lab",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Coincidence Lab")
st.subheader("The Mathematics of Coincidence")

st.markdown("""
Explore how probability, randomness, and repeated experiments
create events that seem surprisingly unlikely.
""")

st.divider()

st.markdown("### Explore the Experiments")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🎂 01 — Birthday Paradox")
    st.write("How likely is it that two people share a birthday?")

    st.markdown("#### 🪙 02 — Randomness Looks Suspicious")
    st.write("Why do random sequences naturally contain streaks?")

with col2:
    st.markdown("#### 🧪 03 — The False Positive Problem")
    st.write("How can testing many hypotheses create false discoveries?")

    st.markdown("#### 🔢 04 — The Coincidence Multiplier")
    st.write("How does repeating an unlikely event change its probability?")

st.divider()
st.caption("Coincidence Lab | Probability • Statistics • Simulation")

st.divider()
st.header("🎂 Experiment 01 — Birthday Paradox")
st.write(
    "How quickly does the probability of a shared birthday "
    "increase as a group gets larger?"
)

people = st.slider(
    "Number of people in the room",
    min_value=2,
    max_value=100,
    value=23
)

# Theoretical probability of at least one shared birthday
prob_no_match = 1.0

for i in range(people):
    prob_no_match *= (365 - i) / 365

prob_match = 1 - prob_no_match

col1, col2 = st.columns(2)

with col1:
    st.metric("People in the room", people)

with col2:
    st.metric("Probability of a shared birthday", f"{prob_match:.2%}")

# Probability curve
x = list(range(2, 101))
y = []

for n in x:
    p_no_match = 1.0
    for i in range(n):
        p_no_match *= (365 - i) / 365
    y.append(1 - p_no_match)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="lines",
    name="Theoretical probability",
    line=dict(color="#8B5CF6", width=3)
))

fig.add_vline(
    x=23,
    line_dash="dash",
    line_color="#F59E0B",
    annotation_text="23 people"
)

fig.add_trace(go.Scatter(
    x=[people],
    y=[prob_match],
    mode="markers",
    name="Your selection",
    marker=dict(color="#F59E0B", size=12)
))

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Number of people",
    yaxis_title="Probability of a shared birthday",
    yaxis=dict(tickformat=".0%", range=[0, 1]),
    height=450
)

st.plotly_chart(fig, use_container_width=True)

st.info(
    "The surprising result: with just 23 people, "
    "the probability of at least one shared birthday is about 50.7%."
)

st.caption(
    "Assumption: 365 equally likely birthdays; leap years are ignored."
)

st.divider()
st.header("🪙 Experiment 02 — Randomness Looks Suspicious")

st.write(
    "Random sequences can contain surprisingly long streaks. "
    "A streak alone does not prove that a coin is biased."
)

num_tosses = st.slider(
    "Number of coin tosses",
    min_value=10,
    max_value=200,
    value=50,
    key="tosses"
)

num_simulations = st.slider(
    "Number of simulated sequences",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100,
    key="simulations"
)

streak_length = st.slider(
    "Streak length to investigate",
    min_value=2,
    max_value=10,
    value=5,
    key="streak"
)

import numpy as np

rng = np.random.default_rng(42)

# Generate one sequence for display
tosses = rng.integers(0, 2, num_tosses)
labels = ["Heads" if x == 1 else "Tails" for x in tosses]

# Find the longest streak in the displayed sequence
longest = 0
current = 0

for toss in tosses:
    if toss == 1:
        current += 1
        longest = max(longest, current)
    else:
        current = 0

st.metric("Longest Heads streak in this sequence", longest)

# Display tosses as a coloured sequence
fig_tosses = go.Figure()

fig_tosses.add_trace(go.Bar(
    x=list(range(1, num_tosses + 1)),
    y=[1] * num_tosses,
    marker_color=[
        "#8B5CF6" if x == 1 else "#64748B"
        for x in tosses
    ],
    customdata=labels,
    hovertemplate="Toss %{x}: %{customdata}<extra></extra>"
))

fig_tosses.update_layout(
    template="plotly_dark",
    xaxis_title="Toss number",
    yaxis=dict(visible=False, range=[0, 1.5]),
    height=180,
    showlegend=False
)

st.plotly_chart(fig_tosses, use_container_width=True)

st.caption("Purple = Heads | Grey = Tails")

# Simulate many independent sequences
matches = 0

for _ in range(num_simulations):
    sequence = rng.integers(0, 2, num_tosses)
    current = 0
    found = False

    for toss in sequence:
        if toss == 1:
            current += 1
            if current >= streak_length:
                found = True
                break
        else:
            current = 0

    if found:
        matches += 1

estimated_probability = matches / num_simulations

st.metric(
    f"Sequences containing at least {streak_length} consecutive Heads",
    f"{estimated_probability:.1%}"
)

st.write(
    f"Out of {num_simulations:,} simulated sequences, "
    f"{matches:,} contained a Heads streak of at least "
    f"{streak_length}."
)

st.caption(
    "Simulation assumes independent, fair coin tosses. "
    "Results are estimates and may vary with different random samples."
)

st.divider()
st.header("🧪 Experiment 03 — The False Positive Problem")

st.write(
    "If every hypothesis is actually false in the sense that no real effect exists, "
    "some tests can still produce p-values below 0.05 purely by chance."
)

num_tests = st.slider(
    "Number of hypotheses tested",
    min_value=10,
    max_value=1000,
    value=100,
    step=10,
    key="num_tests"
)

significance_level = 0.05

# Simulate p-values under the null hypothesis
rng_fp = np.random.default_rng(42)
p_values = rng_fp.random(num_tests)
significant = p_values < significance_level
false_positives = int(significant.sum())

expected_false_positives = num_tests * significance_level
prob_at_least_one = 1 - (1 - significance_level) ** num_tests

col1, col2, col3 = st.columns(3)

col1.metric("Tests performed", f"{num_tests:,}")
col2.metric("False positives observed", f"{false_positives:,}")
col3.metric("Expected false positives", f"{expected_false_positives:.1f}")

st.metric(
    "Probability of at least one false positive",
    f"{prob_at_least_one:.2%}"
)

# Plot p-values and the significance threshold
fig_fp = go.Figure()

fig_fp.add_trace(go.Bar(
    x=list(range(1, num_tests + 1)),
    y=p_values,
    marker_color=[
        "#F43F5E" if p < significance_level else "#64748B"
        for p in p_values
    ],
    name="Simulated p-values",
    hovertemplate="Test %{x}<br>p-value: %{y:.4f}<extra></extra>"
))

fig_fp.add_hline(
    y=significance_level,
    line_dash="dash",
    line_color="#F59E0B",
    annotation_text="p = 0.05 threshold"
)

fig_fp.update_layout(
    template="plotly_dark",
    xaxis_title="Hypothesis test",
    yaxis_title="Simulated p-value",
    yaxis=dict(range=[0, 1]),
    height=400
)

st.plotly_chart(fig_fp, use_container_width=True)

st.info(
    "Red bars represent p-values below 0.05. In this simulation, "
    "all null hypotheses are true, so these significant results "
    "are false positives by construction."
)

st.caption(
    "The p-values are independently simulated from Uniform(0, 1), "
    "as expected under true null hypotheses with valid continuous tests. "
    "The theoretical probability assumes independent tests."
)

st.divider()
st.header("🔢 Experiment 04 — The Coincidence Multiplier")

st.write(
    "Imagine trying to match one fixed four-digit code, from 0000 to 9999. "
    "A single random guess has only a 1 in 10,000 chance of matching it. "
    "What happens when you get thousands of independent guesses?"
)

attempts = st.slider(
    "Number of independent attempts",
    min_value=1,
    max_value=10000,
    value=1000,
    step=100,
    key="attempts"
)

# Each attempt has a 1/10,000 chance of matching
p_match = 1 / 10000
probability = 1 - (1 - p_match) ** attempts

col1, col2 = st.columns(2)

col1.metric("Number of attempts", f"{attempts:,}")
col2.metric("Chance of at least one match", f"{probability:.2%}")

# Plot theoretical probability across attempts
x_attempts = list(range(1, 10001, 50))
y_probability = [
    1 - (1 - p_match) ** n
    for n in x_attempts
]

fig_cm = go.Figure()

fig_cm.add_trace(go.Scatter(
    x=x_attempts,
    y=y_probability,
    mode="lines",
    name="Probability of a match",
    line=dict(color="#06B6D4", width=3)
))

fig_cm.add_trace(go.Scatter(
    x=[attempts],
    y=[probability],
    mode="markers",
    name="Your selection",
    marker=dict(color="#F59E0B", size=12)
))

fig_cm.add_hline(
    y=0.5,
    line_dash="dash",
    line_color="#F43F5E",
    annotation_text="50% probability"
)

fig_cm.update_layout(
    template="plotly_dark",
    xaxis_title="Independent attempts",
    yaxis_title="Probability of at least one match",
    yaxis=dict(tickformat=".0%", range=[0, 1]),
    height=450
)

st.plotly_chart(fig_cm, use_container_width=True)

st.info(
    "Even after 10,000 independent guesses, the probability is about "
    "63.21%—not 100%. Repeated opportunities increase the chance "
    "of a match, but do not guarantee one."
)

st.caption(
    "This is a theoretical probability model, not a recommendation "
    "to attempt real PINs. It assumes independent, uniformly random guesses."
)
