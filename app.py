import streamlit as st
import pandas as pd

# 🚀 Page Configurations (Premium Theme Setup)
st.set_page_config(
    page_title="GeneCare AI - NextGen Genetic Platform", 
    page_icon="🧬", 
    layout="wide"
)

# --- Premium Cyberpunk Neon CSS Styling ---
st.html("""
    <style>
    .main-title { font-size:45px; font-weight:800; color: #00FFCC; text-align: center; margin-bottom: 5px; text-shadow: 0 0 10px #00FFCC; }
    .subtitle { font-size:18px; text-align: center; color: #A0AEC0; margin-bottom: 30px; }
    .feature-card { background-color: #161B22; padding: 25px; border-radius: 15px; border-left: 6px solid #00FFCC; margin-bottom: 25px; color: #FFFFFF; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .status-box { padding: 20px; border-radius: 10px; margin-top: 25px; font-weight: bold; font-size: 20px; text-align: center; font-family: Arial; }
    .metric-card { background-color: #1A202C; padding: 25px; border-radius: 12px; border-top: 5px solid #00FFCC; text-align: center; color: #FFFFFF; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
    .danger-card { background-color: #2D1A1E; padding: 18px; border-radius: 10px; border-left: 6px solid #FF4D4D; margin-bottom: 15px; color: #FFFFFF; }
    .safe-card { background-color: #1A2D22; padding: 18px; border-radius: 10px; border-left: 6px solid #00FF66; margin-bottom: 15px; color: #FFFFFF; }
    h3, h4 { color: #00FFCC !important; }
    </style>
""")

# Main Title Section
st.html('<div class="main-title">🧬 GeneCare AI: Clinical Allele Predictor</div>')
st.html('<div class="subtitle">Advanced Pre-Conception & Prenatal Bio-Intelligence Simulation Platform</div>')
st.divider()

# --- Tabs for clean layout ---
tab1, tab2 = st.tabs(["🧬 Phase 1: Pre-Conception Screening", "🤰 Phase 2: Prenatal Development Timeline"])

with tab1:
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.html('<div class="feature-card"><h3>👥 Core Parental Phenotype Mapping</h3>Provide initial biological baseline configurations below to simulate genetic outcomes.</div>')
        
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            st.markdown("👨 **Father's Bio-Markers**")
            f_blood = st.selectbox("Father's Blood Group", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="f_b")
            f_eye = st.selectbox("Father's Eye Color Allele", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="f_e")
        
        with sub_col2:
            st.markdown("👩 **Mother's Bio-Markers**")
            m_blood = st.selectbox("Mother's Blood Group", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="m_b")
            m_eye = st.selectbox("Mother's Eye Color Allele", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="m_e")

        st.divider()
        
        st.subheader("🏁 Live Progeny Trait Prediction Grid")
        st.caption("This grid calculates the Mendelian probability matrix of the child's physical traits instantly based on parental chromosomes.")
        
        g_father = "B" if "Brown" in f_eye else "b"
        g_mother = "B" if "Brown" in m_eye else "b"
        
        punnett_data = {
            "Maternal / Paternal": [f"Father Allele: {g_father}", f"Father Allele: {g_father}"],
            f"Mother Allele: {g_mother}": [f"{g_father}{g_mother} (Brown)", f"{g_father}{g_mother} (Brown)"],
            "Mother Allele: b": [f"{g_father}b (Brown)" if g_father == "B" else "bb (Blue/Green)", 
                                 f"{g_father}b (Brown)" if g_father == "B" else "bb (Blue/Green)"]
        }
        df_punnett = pd.DataFrame(punnett_data)
        st.table(df_punnett)

    with col2:
        st.html('<div class="feature-card"><h3>🚨 Real-time Bio-Compatibility Risk Shield</h3>Automated screening for Rh incompatibility and structural genetic variance.</div>')
        
        is_father_pos = "+" in f_blood
        is_mother_pos = "+" in m_blood
        
        if (not is_mother_pos) and is_father_pos:
            st.error("🔴 CRITICAL WARNING DETECTED: Rh Incompatibility Condition Imminent.")
            st.write("**Medical Reason:** The mother is Rh-Negative and the father is Rh-Positive. The maternal immune system might generate antibodies against fetal red blood cells, risking complications.")
            st.info("📌 **Action Plan:** Anti-D (RhoGAM) immunoglobulin injections must be scheduled during week 28 of pregnancy and within 72 hours of delivery to ensure absolute safety.")
            
            st.html("""
                <div class="status-box" style="background-color: #4A1A1D; color: #FF4D4D; border: 2px solid #FF4D4D;">
                    🚨 CLINICAL RISK ENGINE VALUE: CRITICAL ALERT LEVEL (85 / 100)
                </div>
            """)
        else:
            st.success("✅ BIO-COMPATIBILITY INDEX SECURE: No Rh Incompatibility detected.")
            st.write("Both maternal and paternal Rh factor combinations are fully compatible for a safe pregnancy cycle.")
            
            st.html("""
                <div class="status-box" style="background-color: #1A4A2B; color: #00FFCC; border: 2px solid #00FFCC;">
                    ✅ CLINICAL RISK ENGINE VALUE: BIO-STABLE & SECURE (15 / 100)
                </div>
            """)

with tab2:
    st.html('<div class="feature-card"><h3>🤰 Interactive Fetal Organic Development Matrix</h3>Track embryonic progress and filter out harmful toxic compounds month-by-month.</div>')
    
    st.subheader("📆 Track Gestational Progression")
    selected_month = st.slider("Drag the slider to change pregnancy month and observe real-time physiological updates in the womb:", min_value=1, max_value=9, value=3, step=1, format="Month %d")
    
    st.divider()
    
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
    
    t_col1, t_col2, t_col3 = st.columns([1, 1.2, 1.2])
    
    with t_col1:
        st.html(f"""
            <div class="metric-card">
                <h4>📏 Relative Fetal Size</h4>
                <h2 style='color: #00FFCC; margin: 15px 0;'>{current_data['size']}</h2>
                <p style='color: #A0AEC0;'>Month-to-month volumetric macro scaling indicator.</p>
            </div>
        """)
        
    with t_col2:
        st.markdown("#### 🩺 Active Organ Development Logs")
        for organ in current_data['organs']:
            st.markdown(f"🧬 **{organ}**")
            
    with t_col3:
        st.markdown("#### ⚡ Systemic Biological Maturity Bars")
        st.caption("Neural Complexity")
        st.progress(current_data['neuro'])
        st.caption("Skeletal Calcification")
        st.progress(current_data['skeletal'])
        st.caption("Cardiovascular Pump Efficiency")
        st.progress(current_data['cardio'])
        
    st.divider()
    
    # --- TERATOGEN ACTIVE CHECK PANEL ---
    st.subheader("🛡️ Teratogenic Chemical Active Diagnostic Guard")
    st.write("Select common lifestyle or skincare ingredients to simulate placenta barrier filtration safety checks:")
    
    options = st.multiselect(
        "Choose compounds or substances to analyze safety clearance boundaries:",
        ["Retinol / Retinoids (Skincare)", "Salicylic Acid (High Dose)", "Raw Seafood / Sushi", "Unpasteurized Dairy", "Folic Acid Supplements"]
    )
    
    if options:
        st.markdown("##### 🔬 Compound Molecular Analysis Output:")
        for item in options:
            if "Retinol" in item:
                st.html('<div class="danger-card"><strong>🚨 CRITICAL DANGER: Retinol</strong><br>Highly Teratogenic. Crosses the placental barrier effortlessly. High correlation with Congenital Retinoid Syndrome. Avoid completely.</div>')
            elif "Salicylic" in item:
                st.html('<div class="danger-card"><strong>⚠️ WARNING FLAG: Salicylic Acid</strong><br>Oral high-dose ingestion increases terminal bleeding risks during late trimesters. Avoid high systemic intake.</div>')
            elif "Seafood" in item:
                st.html('<div class="danger-card"><strong>🚨 CONTAMINATION RISK: Raw Seafood</strong><br>Major risk of Listeria monocytogenes bacterial infections. Threatens fetal development. Consume fully cooked items only.</div>')
            elif "Dairy" in item:
