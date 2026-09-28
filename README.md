# 📐 OptiSpace AI
> Computer Vision-Based Spatial Layout & Ergonomic Optimization System

**CBSE Class XII Artificial Intelligence Capstone Project (Code 843)**  
**Developer:** Kim Dsouza  

---

## 📌 Project Overview
OptiSpace AI is an intelligent spatial optimization tool designed to analyze room layouts using Computer Vision (YOLOv8) and Python rule-based heuristics. It evaluates spatial mass balance, workstation ergonomics, and natural lighting alignment to output actionable room arrangement instructions and non-wasteful product recommendations.

## 🚀 Key Features
* **Automated Object Detection:** Detects furniture items (`bed`, `chair`, `desk`, `tv`, `potted plant`) from a single 2D photo using YOLOv8.
* **Spatial Mass Balance Engine:** Calculates visual weight distribution across the vertical midpoint to detect room lopsidedness.
* **Ergonomic & Lighting Advice:** Highlights screen glare risks and pathway blockages.
* **SDG Alignment:** Supports **SDG 3 (Good Health and Well-Being)** and **SDG 12 (Responsible Consumption and Production)**.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** Streamlit
* **Computer Vision:** YOLOv8 (Ultralytics) & OpenCV
* **Data Libraries:** NumPy, Pandas, PIL

## 🏃 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/kimrdsouza-beep/OptiSpace-AI.git](https://github.com/kimrdsouza-beep/OptiSpace-AI.git)
   cd OptiSpace-AI
