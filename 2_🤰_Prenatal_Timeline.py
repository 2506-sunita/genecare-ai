import streamlit as st
import plotly.graph_objects as go

# 🚀 Page Configurations
st.set_page_config(page_title="Fetal Growth & Safety Matrix", page_icon="🤰", layout="wide")

# Custom Styles for Visual Consistency
st.markdown("""
    <style>
    .page-title { font-size:40px; font-weight:800; color: #00FFCC; text-align: left; margin-bottom: 5px; }
    .metric-card { background-color: #1A202C; padding: 20px; border-radius: 12px; border-top: 4px solid #00FFCC; text-align: center; }
    .danger-card { background-color: #2D1A1E; padding: 15px; border-radius: 8px; border-left: 5px solid #FF4D4D; margin-bottom: 10px; }
    .safe-card { background-color: #1A2D22; padding: 15px; border-radius: 8px; border-left: 5px solid #00FF66; margin-bottom: 10px; }
    </style>
""", unsafe_allowed_html=True)

st.markdown('<div class="page-title">🤰 Interactive Fetal Organic Development Matrix</div>', unsafe_allowed_html=True)
st.markdown("### *Post-Conception Multi-Variant Timeline & Teratogenic Ingredient Shield*")
st.divider()

# --- 🌟 KILLER FEATURE 3: DYNAMIC PREGNANCY MONTH SLIDER ---
st.subheader("📆 Track Gestational Progression")
selected_month = st.slider("Drag the slider to change pregnancy month and observe real-time physiological updates:", min_value=1, max_value=9, value=3, step=1, format="Month %d")

st.divider()

# --- BACKEND SIMULATION DATA ENGINE ---
# This dictionary maps exactly what happens inside the womb month-by-month
fetal_data_engine = {
    1: {"size": "Poppy Seed (0.1 cm) 🪹", "organs": ["Neural Tube Formation", "Blastocyst Implantation", "Early Cell Differentiation"], "neuro": 10, "skeletal": 5, "cardio": 5},
    2: {"size": "Raspberry (1.6 cm) 🍇", "organs": ["Heart Begins Beating", "Early Limb Buds Appearing", "Brain Hemispheres Developing"], "neuro": 25, "skeletal": 15, "cardio": 30},
    3: {"size": "Lime (5.4 cm) 🍋", "organs": ["Fingerprints Forming", "Vocal Chords Initial Setup", "Kidneys Start Producing Urine"], "neuro": 45, "skeletal": 30, "cardio": 50},
    4: {"size": "Avocado (11.6 cm) 🥑", "organs": ["Sucking Reflex Development", "Eyes Move to Front of Face", "Heart Pumping 25 Quarts/Day"], "neuro": 60, "skeletal": 45, "cardio": 70},
    5: {"size": "Banana (25.6 cm) 🍌", "organs": ["Hearing Functions Active", "Vernix Caseosa Coats Skin", "Maternal Movements Felt"], "neuro": 75, "skeletal": 60, "cardio": 80},
    6: {"size": "Eggplant (35.6 cm) 🍆", "organs": ["Lungs Produce Surfactant", "Taste Buds Fully Formed", "Footprints & Handprints Set"], "neuro": 85, "skeletal": 70, "cardio": 85},
    7: {"size": "Coconut (39.9 cm) 🥥", "organs": ["Eyelids Open & Close", "Brain Surface Folds Developing", "Regulating Body Temperature"], "neuro": 90, "skeletal": 80, "cardio": 90},
    8: {"size": "Cantaloupe (46.2 cm) 🍈", "organs": ["Rapid Brain Growth", "Bones Harden (Except Skull)", "Fat Deposition Under Skin"], "neuro": 95, "skeletal": 90, "cardio": 95},
    9: {"size": "Watermelon (50.7 cm) 🍉", "organs": ["Full Term Lung Maturity", "Coordinating Sucking/Swallowing", "Immune System Boost From Mom"], "neuro": 100, "skeletal": 100, "cardio": 100}
}

current_data = fetal_data_engine[selected_month]

# --- DISPLAY DYNAMIC COLUMNS BASED ON SLIDER ---
col1, col2, col3 = st.columns([1, 1.2, 1.2])

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <h4>📏 Relative Fetal Size</h4>
            <h2 style='color: #00FFCC; margin: 15px 0;'>{current_data['size']}</h2>
            <p style='color: #A0AEC0;'>Month-to-month volumetric macro scaling index.</p>
        </div>
    """, unsafe_allowed_html=True)

with col2:
    st.markdown("#### 🩺 Active Organ Development Logs")
    for organ in current_data['organs']:
        st.markdown(f"🧬 **{organ}**")

with col3:
    st.markdown("#### ⚡ Systemic Biological Maturity Bars")
    
    # Render interactive progress visualizations
    st.caption("Neural Complexity")
    st.progress(current_data['neuro'])
    
    st.caption("Skeletal Calcification")
    st.progress(current_data['skeletal'])
    
    st.caption("Cardiovascular Pump Efficiency")
    st.progress(current_data['cardio'])

st.divider()

# --- THE PRENATAL SAFETY GUARD (TERATOGEN COMPOUND SCREENING CHECK) ---
st.subheader("🛡️ Teratogenic Chemical Active Diagnostic Guard")
st.write("Select ingredients or everyday consumption habits to evaluate dynamic safe boundaries during current prenatal phases:")

options = st.multiselect(
    "Choose compounds or substances to filter through the clinical placenta barrier:",
    ["Retinol / Retinoids (Skincare)", "Salicylic Acid (High Dose)", "Raw Seafood / Sushi", "Unpasteurized Dairy", "Folic Acid Supplements"]
)

if options:
    st.markdown("##### 🔬 Compound Analysis Breakdown Matrix:")
    for item in options:
        if item == "Retinol / Retinoids (Skincare)":
            st.markdown(f"""
                <div class="danger-card">
                    <strong>🚨 CRITICAL DANGER: {item}</strong><br>
                    <strong>Molecular Impact:</strong> Highly Teratogenic. Crosses the placental barrier effortlessly. High correlation with Congenital Retinoid Syndrome, leading to cranial-facial and central nervous system defects. Avoid immediately.
                </div>
            """, unsafe_allowed_html=True)
        elif item == "Salicylic Acid (High Dose)":
            st.markdown(f"""
                <div class="danger-card">
                    <strong>⚠️ WARNING FLAG: {item}</strong><br>
                    <strong>Molecular Impact:</strong> Oral ingestion increases terminal bleeding risks during late-stage trimesters. Switch to safe alternatives like glycolic or lactic acids.
                </div>
            """, unsafe_allowed_html=True)
        elif item == "Raw Seafood / Sushi":
            st.markdown(f"""
                <div class="danger-card">
                    <strong>🚨 CONTAMINATION RISK: {item}</strong><br>
                    <strong>Molecular Impact:</strong> Major risk of Listeria monocytogenes bacterial infections. Causes acute maternal septicemia leading to fetal distress or spontaneous termination. Consume fully cooked food matrices only.
                </div>
            """, unsafe_allowed_html=True)
        elif item == "Unpasteurized Dairy":
            st.markdown(f"""
                <div class="danger-card">
                    <strong>🚨 MICROBIAL THREAT: {item}</strong><br>
                    <strong>Molecular Impact:</strong> Contains dangerous active pathogen strands of Salmonella and E. coli. Threatens fetal liver integrity and causes localized amniotic fluid infection risks.
                </div>
            """, unsafe_allowed_html=True)
        elif item == "Folic Acid Supplements":
            st.markdown(f"""
                <div class="safe-card">
                    <strong>✅ ESSENTIAL NUTRIENT CLEARANCE: {item}</strong><br>
                    <strong>Molecular Impact:</strong> Crucial bio-catalyst needed for DNA methylation. Eliminates up to 70% of potential Spina Bifida and Neural Tube Defects (NTDs). Safely cleared for immediate uptake.
                </div>
            """, unsafe_allowed_html=True)
else:
    st.info("💡 Select one or more compounds from the dropdown list above to simulate structural placenta barrier filtration calculations.")
