# PoliceSentencingSimulator-
# ⚖️ Sentencing Decision Simulator
### Multi-Agent AI System for Simulated Judicial Decision-Making

> Inspired by the COMPAS risk assessment framework, this project explores how multi-agent systems can model competing perspectives in criminal sentencing while emphasizing fairness, transparency, and ethical AI design.

---

## 📌 Overview

The **Sentencing Decision Simulator** is a multi-agent AI orchestration project that simulates how sentencing decisions may emerge from competing institutional perspectives.

Rather than relying on a single predictive model, the system uses a **fan-out / fan-in orchestration architecture** where specialized agents independently analyze a criminal case profile before submitting their reasoning to a final **Judge Agent**.

### 🎯 Objectives
- Explore fairness in algorithmic decision-making
- Simulate competing legal perspectives
- Study ethical AI orchestration patterns
- Investigate explainable sentencing logic
- Analyze bias in predictive justice systems

---

# 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │   Case Profile   │
                    └────────┬─────────┘
                             │
               ┌─────────────┼─────────────┐
               │             │             │
               ▼             ▼             ▼
      ┌────────────┐ ┌────────────┐ ┌────────────┐
      │ Prosecutor │ │  Defense   │ │ Risk Agent │
      └────────────┘ └────────────┘ └────────────┘
               │             │             │
               └─────────────┼─────────────┘
                             ▼
                    ┌────────────────┐
                    │ Fairness Agent │
                    └────────┬───────┘
                             ▼
                     ┌─────────────┐
                     │ Judge Agent │
                     └─────────────┘
                             ▼
                    Final Sentencing Decision
```

---

# 🤖 Agents

## 🟥 Prosecutor Agent
Represents punitive reasoning and public safety concerns.

### Responsibilities
- Argue for harsher sentencing
- Emphasize criminal history
- Focus on recidivism risk
- Prioritize community safety

---

## 🟦 Defense Agent
Represents mitigating circumstances and rehabilitation potential.

### Responsibilities
- Advocate for reduced sentencing
- Highlight contextual factors
- Emphasize fairness and proportionality
- Consider rehabilitation opportunities

---

## 🟨 Risk Assessment Agent
Generates a heuristic-based risk score inspired by predictive justice systems such as COMPAS.

### Factors Considered
- Prior offense count
- Charge severity
- Age grouping

### Example Formula

```python
risk_score = (
    0.5 * priors_score +
    0.3 * age_score +
    0.2 * charge_score
)
```

---

## 🟩 Fairness Agent
Acts as an ethical oversight layer.

### Responsibilities
- Detect potentially biased reasoning
- Prevent protected attributes from influencing outcomes
- Monitor disproportionate recommendations
- Encourage transparent decision-making

### Explicitly Excluded Factors
- Race
- Ethnicity
- Gender

---

## ⚖️ Judge Agent
The final decision-making authority.

### Responsibilities
- Aggregate all agent reasoning
- Balance fairness, risk, and legal arguments
- Produce a final sentencing recommendation
- Explain the reasoning behind the verdict

---

# 🔄 Orchestration Pattern

This project uses a **Fan-Out / Fan-In** multi-agent architecture.

## Fan-Out
A criminal case profile is distributed to multiple specialized agents simultaneously.

## Fan-In
The Judge Agent synthesizes all agent outputs into a final sentencing decision.

### Why This Matters
- Encourages competing perspectives
- Enables modular reasoning
- Improves explainability
- Simulates real-world institutional conflict

---

# 📂 Dataset Inspiration

The simulator was inspired by the **COMPAS risk assessment dataset** used in criminal justice systems.

### Example Features
- `priors_count`
- `age`
- `c_charge_degree`
- `c_charge_desc`
- `v_charge_desc`

---

# 🛠️ Tech Stack

- Python
- Multi-Agent Systems
- Prompt Engineering
- JSON-Based Agent Communication
- Claude/OpenAI API Integration
- Heuristic Risk Scoring

---

# 🚨 Ethical Considerations

Predictive justice systems have faced criticism for:
- Algorithmic bias
- Lack of transparency
- Discriminatory outcomes
- Reinforcing historical inequalities

This simulator was created to explore:
- Fairness-aware AI systems
- Ethical orchestration patterns
- Explainable decision-making

> This project is intended for educational and research purposes only.

---

# 📌 Example Output

```json
{
  "final_decision": "detain",
  "risk_score": 0.71,
  "fairness_flag": false,
  "reasoning": "The defendant presents elevated recidivism risk due to multiple prior offenses and felony classification. Mitigating factors were considered before reaching the final decision."
}
```

---

# 🚀 Future Improvements

- Randomized case selection
- Dynamic case generation
- Explainability dashboards
- Bias evaluation metrics
- LLM-based reasoning expansion
- Comparative COMPAS analysis
- Interactive UI

---

# 📖 Research Inspiration

- COMPAS Risk Assessment
- AI Ethics
- Fairness in Machine Learning
- Multi-Agent Systems
- Algorithmic Accountability

---

# 👥 Authors

Developed by Sayde Surratt and collaborators as part of a multi-agent systems and AI ethics project.

---

# ⚠️ Disclaimer

This project is an academic simulation and should **NOT** be used for real judicial or legal decision-making.
