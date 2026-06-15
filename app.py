import gradio as gr
import joblib
import numpy as np

# Load trained model
model = joblib.load("institution_risk_model.pkl")

def predict_risk(faculty_ratio, naac, nirf, placement, infra, doc, compliance):
    input_data = np.array([[faculty_ratio, naac, nirf, placement, infra, doc, compliance]])
    prediction = model.predict(input_data)
    return prediction[0]

interface = gr.Interface(
    fn=predict_risk,
    inputs=[
        gr.Number(label="Faculty-Student Ratio"),
        gr.Number(label="NAAC CGPA"),
        gr.Number(label="NIRF Score"),
        gr.Number(label="Placement Percentage"),
        gr.Number(label="Infrastructure Score"),
        gr.Number(label="Document Sufficiency (%)"),
        gr.Radio([0,1], label="Past Compliance Issues (0 = No, 1 = Yes)")
    ],
    outputs="text",
    title="UGC Institutional Risk Predictor",
    description="AI-based system to classify institutional risk using performance and compliance metrics."
)

interface.launch()
