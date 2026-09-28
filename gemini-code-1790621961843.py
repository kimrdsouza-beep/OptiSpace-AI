import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import pandas as pd

# -----------------------------------------------------------------------------
# OPTISPACE AI - CORE APPLICATION CODE
# Developer: Kim Dsouza
# -----------------------------------------------------------------------------

@st.cache_resource
def load_yolo_model():
    # Load pre-trained YOLOv8 model for indoor object detection
    return YOLO('yolov8n.pt')

model = load_yolo_model()

INDOOR_CLASSES = {
    56: 'Chair', 57: 'Couch', 59: 'Bed', 
    60: 'Desk/Table', 62: 'TV/Monitor', 75: 'Potted Plant'
}

def analyze_spatial_layout(detected_objects, image_width):
    """Calculates visual mass balance and ergonomic recommendations."""
    suggestions = []
    left_mass, right_mass = 0, 0
    midpoint_x = image_width / 2

    for obj in detected_objects:
        box = obj['box']
        area = (box[2] - box[0]) * (box[3] - box[1])
        box_center_x = (box[0] + box[2]) / 2

        if box_center_x < midpoint_x:
            left_mass += area
        else:
            right_mass += area

    total_mass = left_mass + right_mass
    if total_mass > 0:
        imbalance_ratio = abs(left_mass - right_mass) / total_mass
        if imbalance_ratio > 0.4:
            heavy_side = "left" if left_mass > right_mass else "right"
            suggestions.append(
                f"⚖️ Visual Imbalance Detected: Heavy furniture concentration on the {heavy_side} side. "
                f"Consider moving major items to the opposite wall."
            )

    return suggestions

# Streamlit Interface Execution
st.title("📐 OptiSpace AI: Room Layout Optimizer")
uploaded_file = st.file_uploader("Upload Room Photo", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)
    results = model.predict(source=img_np, conf=0.35)
    
    # Process detections & run spatial rule engine
    detected_objects = []
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            if cls_id in INDOOR_CLASSES:
                detected_objects.append({
                    'label': INDOOR_CLASSES[cls_id],
                    'box': box.xyxy[0].tolist()
                })
    
    suggestions = analyze_spatial_layout(detected_objects, img_np.shape[1])
    for sug in suggestions:
        st.info(sug)