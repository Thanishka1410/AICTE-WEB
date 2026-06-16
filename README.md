# UGC Institutional Risk Predictor

An AI-powered web application that predicts the risk level of educational institutions based on performance and compliance metrics. Built for **AICTE (All India Council for Technical Education)** to assist in institutional risk assessment.

---

## Overview

This application uses a trained machine learning model to classify institutions into risk categories based on key performance indicators and regulatory compliance data. It provides a user-friendly web interface for administrators and evaluators to quickly assess institutional risk.

---

## Features

- Predicts institutional risk using 7 key metrics
- Clean, interactive web interface powered by Gradio
- Pre-trained ML model for instant predictions
- Lightweight and easy to deploy

---

## Input Parameters

| Parameter | Description |
|---|---|
| Faculty-Student Ratio | Ratio of faculty members to students |
| NAAC CGPA | National Assessment and Accreditation Council grade |
| NIRF Score | National Institutional Ranking Framework score |
| Placement Percentage | Percentage of students placed |
| Infrastructure Score | Quality rating of campus infrastructure |
| Document Sufficiency (%) | Completeness of institutional documentation |
| Past Compliance Issues | History of compliance violations (0 = No, 1 = Yes) |

---

## Tech Stack

- **Frontend:** Gradio
- **Backend:** Python
- **ML Framework:** Scikit-learn
- **Model Serialization:** Joblib
- **Numerical Computing:** NumPy

---

## Project Structure

```
AICTE-WEB/
├── app.py                      # Main application file
├── institution_risk_model.pkl  # Pre-trained ML model
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Thanishka1410/AICTE-WEB.git
   cd AICTE-WEB
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the app**
   Open the local URL displayed in the terminal (usually `http://127.0.0.1:7860`)

---

## How It Works

1. The user enters institutional metrics through the web interface
2. Input values are converted to a NumPy array
3. The pre-trained model processes the data and generates a prediction
4. The risk classification is displayed as output

---

## Use Cases

- AICTE institutional evaluations
- NAAC accreditation risk screening
- Internal audits by educational institutions
- Regulatory compliance monitoring

---

## License

This project is open source and available for educational purposes.

---

## Author

**Thanishka R**
GitHub: [Thanishka1410](https://github.com/Thanishka1410)
