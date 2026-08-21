import streamlit as st
import pandas as pd

# 🚀 Page Configurations (Premium Theme Setup)
st.set_page_config(
    page_title="GeneCare AI - NextGen Genetic Platform", 
    page_icon="🧬", 
    layout="wide"
)

# --- 🚀 ULTRA-ADVANCED LUMINOUS NEON CSS STYLING ---
st.html("""
    <style>
    @import url('https://googleapis.com');
    
    /* Global Styles */
    .stApp { background-color: #050811 !important; font-family: 'Rajdhani', sans-serif; color: #E2E8F0; }
    
    /* Glowing Headers */
    .main-title { font-family: 'Orbitron', sans-serif; font-size:48px; font-weight:900; color: #00FFCC; text-align: center; margin-bottom: 2px; text-shadow: 0 0 20px rgba(0, 255, 204, 0.6), 0 0 40px rgba(0, 255, 204, 0.2); }
    .subtitle { font-size:19px; text-align: center; color: #94A3B8; margin-bottom: 35px; letter-spacing: 1px; }
    
    /* Neon Glowing Cards */
    .feature-card { background: linear-gradient(145deg, #0f172a, #1e293b); padding: 25px; border-radius: 16px; border: 1px solid rgba(0, 255, 204, 0.3); margin-bottom: 25px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.1); color: #FFFFFF; }
    .danger-card { background: linear-gradient(145deg, #1e1b1b, #2d1a1e); padding: 20px; border-radius: 12px; border-left: 6px solid #FF4D4D; border-top: 1px solid rgba(255, 77, 77, 0.2); margin-bottom: 15px; color: #FFFFFF; box-shadow: 0 0 15px rgba(255, 77, 77, 0.1); }
    .safe-card { background: linear-gradient(145deg, #142217, #1a2d22); padding: 20px; border-radius: 12px; border-left: 6px solid #00FF66; border-top: 1px solid rgba(0, 255, 102, 0.2); margin-bottom: 15px; color: #FFFFFF; box-shadow: 0 0 15px rgba(0, 255, 102, 0.1); }
    
    /* Status Analytics Boxes */
    .status-box { padding: 22px; border-radius: 12px; margin-top: 25px; font-family: 'Orbitron', sans-serif; font-weight: bold; font-size: 22px; text-align: center; letter-spacing: 1px; box-shadow: 0 5px 15px rgba(0,0,0,0.5); }
    .metric-card { background-color: #0b0f19; padding: 25px; border-radius: 14px; border: 1px solid rgba(0, 255, 204, 0.2); border-top: 6px solid #00FFCC; text-align: center; color: #FFFFFF; }
    
    /* Typography Overrides */
    h3, h4 { color: #00FFCC !important; font-family: 'Orbitron', sans-serif; letter-spacing: 0.5px; }
    strong { color: #F59E0B !important; } /* Golden Highlights */
    
    /* Custom Navigation Tabs styling */
    .stTabs [data-baseweb="tab-list"] { gap: 12px; }
    .stTabs [data-baseweb="tab"] { background-color: #0f172a; border: 1px solid rgba(255,255,255,0.1); padding: 10px 24px; border-radius: 8px; color: #94A3B8; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #00FFCC !important; color: #050811 !important; font-weight: bold; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4); }
    </style>
""")

# Main Luminous Title Section
st.html('<div class="main-title">🧬 GeneCare AI Pro</div>')
st.html('<div class="subtitle">Enterprise Bio-Intelligence & Advanced Fetal Risk Simulation Architecture</div>')
st.divider()

# --- 🚀 4 ADVANCED STRUCTURAL PHASES (TABS) ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🧬 Phase 1: Genomic Compatibility", 
    "🤰 Phase 2: Embryonic Growth Timeline", 
    "🛡️ Phase 3: Teratogenic Vision Shield",
    "🥗 Phase 4: Prenatal Nutrition Matrix"
])

# ==================== 🛠️ TAB 1: GENOMIC COMPATIBILITY ====================
with tab1:
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.html('<div class="feature-card"><h3>👥 Core Parental Phenotype Mapping</h3>Configure baseline biological sequences to simulate Mendelian chromosomal transmission.</div>')
        
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            st.markdown("👨 **Father's Bio-Markers (Allele Set)**")
            f_blood = st.selectbox("Father's Blood Group Type", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="f_b")
            f_eye = st.selectbox("Father's Iris Allele Expression", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="f_e")
            father_stress = st.slider("Father's Cortisol Strain (Daily Stress Index)", 1, 10, 4)
        
        with sub_col2:
            st.markdown("👩 **Mother's Bio-Markers (Allele Set)**")
            m_blood = st.selectbox("Mother's Blood Group Type", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="m_b")
            m_eye = st.selectbox("Mother's Iris Allele Expression", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="m_e")
            mother_sleep = st.slider("Mother's Sleep Optimization Scale (Hours/Night)", 4, 10, 8)

        st.divider()
        
        # --- 💥 NEW LOGICAL ATTRACTION: EPIGENETIC MUTATION RESISTANCE RESISTANCE ---
        st.subheader("🧬 Real-time Epigenetic Mutation Profile")
        mutation_resistance = 100 - (father_stress * 5) + (mother_sleep * 2)
        if mutation_resistance > 80:
            st.success(f"🛡️ **DNA Integrity Score: {mutation_resistance:.1f}% (Excellent)** — Low probability of stress-induced methylation anomalies.")
        else:
            st.warning(f"⚡ **DNA Integrity Score: {mutation_resistance:.1f}% (Sub-Optimal)** — High parental cortisol indices detected. Fetal cellular adaptive systems may experience stress acceleration.")
            
        st.divider()
        st.subheader("🏁 Automated Progeny Trait Prediction Grid")
        st.caption("Calculates the structural Mendelian cross-matrix variables for phenotypic expression probabilities.")
        
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
        st.html('<div class="feature-card"><h3>🚨 Real-time Bio-Compatibility Shield</h3>Algorithmic screening for Rh incompatibility matrix and anti-body aggregation triggers.</div>')
        
        is_father_pos = "+" in f_blood
        is_mother_pos = "+" in m_blood
        
        if (not is_mother_pos) and is_father_pos:
            st.error("🔴 CRITICAL IMMUNOLOGICAL DISCORDANCE DETECTED: Rh Incompatibility Condition Active.")
            st.write("**Clinical Manifestation:** The mother is **Rh-Negative** and the father is **Rh-Positive**. Fetal erythroblastosis risks are heightened due to potential maternal anti-Rh antibody generation.")
            st.info("📌 **Mandatory Preventive Action:** Administer **Anti-D (RhoGAM)** immunoglobulin prophylaxis at gestational week 28 and post-delivery within 72 hours.")
            
            st.html("""
                <div class="status-box" style="background: linear-gradient(135deg, #4A1A1D, #7F1D1D); color: #FF4D4D; border: 2px solid #FF4D4D; text-shadow: 0 0 10px #FF4D4D;">
                    🚨 FETAL IMMUNE RISK: CRITICAL (85 / 100)
                </div>
            """)
        else:
            st.success("✅ GENOMIC COMPATIBILITY INDEX SECURE: No Rh Isolation factors located.")
            st.write("Maternal and paternal Rh antigen arrangements match standard biological boundaries for a risk-free gestation cycle.")
            
            st.html("""
                <div class="status-box" style="background: linear-gradient(135deg, #143E25, #065F46); color: #00FFCC; border: 2px solid #00FFCC; text-shadow: 0 0 10px #00FFCC;">
                    ✅ FETAL IMMUNE RISK: BIO-STABLE (15 / 100)
                </div>
            """)

# ==================== 🤰 TAB 2: EMBRYONIC TIMELINE ====================
with tab2:
    st.html('<div class="feature-card"><h3>🤰 Interactive Fetal Organic Development Matrix</h3>Simulate fetal organogenesis progress, structural calcification, and systemic development vectors.</div>')
    
    st.subheader("📆 Track Gestational Progression Metrics")
    selected_month = st.slider("Adjust tracking timeline controller to calculate systemic organ milestones inside the womb:", min_value=1, max_value=9, value=3, step=1, format="Month %d")
    
    st.divider()
    
    fetal_data_engine = {
        1: {"size": "Poppy Seed (0.1 cm) 🪹", "organs": ["Neural Tube Formation", "Blastocyst Implantation", "Early Cell Differentiation"], "neuro": 10, "skeletal": 5, "cardio": 5},
        2: {"size": "Raspberry (1.6 cm) 🍇", "organs": ["Heart Begins Beating", "Early Limb Buds Appearing", "Brain Hemispheres Developing"], "neuro": 25, "skeletal": 15, "cardio": 30},
        3: {"size": "Lime (5.4 cm) 🍋", "organs": ["Fingerprints Forming", "Vocal Chords Initial Setup", "Kidneys Start Producing Urine"], "neuro": 45, "skeletal": 30, "cardio": 50},
        4: {"size": "Avocado (11.6 cm) 🥑", "organs": ["Sucking Reflex Development", "Eyes Move to Front of Face", "Heart Pumping 25 Quarts/Day"], "neuro": 60, "skeletal": 45, "cardio": 70},
        5: {"size": "Banana (25.6 cm) 🍌", "organs": ["Hearing Functions Active", "Vernix Caseosa Coats Skin", "Maternal Movements Felt"], "neuro": 75, "skeletal": 60, "cardio": 80},
        6: {"size": "Eggplant (35.6 cm) 🍆", "organs": ["Lungs Produce Surfactant", "Taste Buds Fully Formed", "Footprints & Handprints Set"], "neuro": 85, "skeletal": 70, "cardio": 85},
        7: {"size": "Coconut (39.9 cm) 🥥", "organs": ["Eyelids Open & Close", "Brain Surface Folds Developing", "Regulating Body Temperature"], "neuro": 90, "skeletal": 80, "cardio": 90},
