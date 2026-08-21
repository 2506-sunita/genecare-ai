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
    .main-title { font-family: 'Orbitron', sans-serif; font-size:45px; font-weight:900; color: #00FFCC; text-align: center; margin-bottom: 2px; text-shadow: 0 0 20px rgba(0, 255, 204, 0.6); }
    .subtitle { font-size:18px; text-align: center; color: #94A3B8; margin-bottom: 35px; letter-spacing: 1px; }
    
    /* Neon Glowing Cards */
    .feature-card { background: linear-gradient(145deg, #0f172a, #1e293b); padding: 25px; border-radius: 16px; border: 1px solid rgba(0, 255, 204, 0.3); margin-bottom: 25px; color: #FFFFFF; }
    .danger-card { background: linear-gradient(145deg, #1e1b1b, #2d1a1e); padding: 20px; border-radius: 12px; border-left: 6px solid #FF4D4D; margin-bottom: 15px; color: #FFFFFF; }
    .safe-card { background: linear-gradient(145deg, #142217, #1a2d22); padding: 20px; border-radius: 12px; border-left: 6px solid #00FF66; margin-bottom: 15px; color: #FFFFFF; }
    
    /* Status Analytics Boxes */
    .status-box { padding: 22px; border-radius: 12px; margin-top: 25px; font-family: 'Orbitron', sans-serif; font-weight: bold; font-size: 20px; text-align: center; letter-spacing: 1px; }
    .metric-card { background-color: #0b0f19; padding: 25px; border-radius: 14px; border: 1px solid rgba(0, 255, 204, 0.2); border-top: 6px solid #00FFCC; text-align: center; color: #FFFFFF; }
    
    /* Typography Overrides */
    h3, h4 { color: #00FFCC !important; font-family: 'Orbitron', sans-serif; }
    strong { color: #F59E0B !important; }
    
    /* Custom Navigation Tabs styling */
    .stTabs [data-baseweb="tab-list"] { gap: 12px; }
    .stTabs [data-baseweb="tab"] { background-color: #0f172a; border: 1px solid rgba(255,255,255,0.1); padding: 10px 24px; border-radius: 8px; color: #94A3B8; }
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

# ==================== TAB 1: GENOMIC COMPATIBILITY ====================
with tab1:
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.html('<div class="feature-card"><h3>👥 Core Parental Phenotype Mapping</h3>Configure baseline biological sequences to simulate Mendelian chromosomal transmission.</div>')
        
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            st.markdown("👨 **Father's Bio-Markers**")
            f_blood = st.selectbox("Father's Blood Group Type", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="f_b")
            f_eye = st.selectbox("Father's Iris Allele Expression", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="f_e")
            father_stress = st.slider("Father's Cortisol Strain (Daily Stress Index)", 1, 10, 4)
        
        with sub_col2:
            st.markdown("👩 **Mother's Bio-Markers**")
            m_blood = st.selectbox("Mother's Blood Group Type", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="m_b")
            m_eye = st.selectbox("Mother's Iris Allele Expression", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="m_e")
            mother_sleep = st.slider("Mother's Sleep Optimization Scale (Hours/Night)", 4, 10, 8)

        st.divider()
        
        st.subheader("🧬 Real-time Epigenetic Mutation Profile")
        mutation_resistance = 100 - (father_stress * 5) + (mother_sleep * 2)
        if mutation_resistance > 80:
            st.success(f"🛡️ **DNA Integrity Score: {mutation_resistance:.1f}% (Excellent)** — Low probability of stress-induced methylation anomalies.")
        else:
            st.warning(f"⚡ **DNA Integrity Score: {mutation_resistance:.1f}% (Sub-Optimal)** — High parental cortisol indices detected.")
            
        st.divider()
        st.subheader("🏁 Automated Progeny Trait Prediction Grid")
        
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
            st.write("**Clinical Manifestation:** The mother is **Rh-Negative** and the father is **Rh-Positive**.")
            st.info("📌 **Action Plan:** Administer **Anti-D (RhoGAM)** immunoglobulin prophylaxis at gestational week 28.")
            
            st.html("""
                <div class="status-box" style="background: linear-gradient(135deg, #4A1A1D, #7F1D1D); color: #FF4D4D; border: 2px solid #FF4D4D;">
                    🚨 FETAL IMMUNE RISK: CRITICAL (85 / 100)
                </div>
            """)
        else:
            st.success("✅ GENOMIC COMPATIBILITY INDEX SECURE: No Rh Isolation factors located.")
            st.write("Maternal and paternal Rh antigen arrangements match standard biological boundaries.")
            
            st.html("""
                <div class="status-box" style="background: linear-gradient(135deg, #143E25, #065F46); color: #00FFCC; border: 2px solid #00FFCC;">
                    ✅ FETAL IMMUNE RISK: BIO-STABLE (15 / 100)
                </div>
            """)

# ==================== TAB 2: EMBRYONIC TIMELINE ====================
with tab2:
    st.html('<div class="feature-card"><h3>🤰 Interactive Fetal Organic Development Matrix</h3>Simulate fetal organogenesis progress, structural calcification, and systemic development vectors.</div>')
    
    st.subheader("📆 Track Gestational Progression Metrics")
    selected_month = st.slider("Adjust tracking timeline controller to calculate systemic organ milestones inside the womb:", min_value=1, max_value=9, value=3, step=1, format="Month %d")
    
    st.divider()
    
    # 100% Fixed Engine Structure with Closed Brackets
    fetal_engine = {
        1: {"size": "Poppy Seed", "neuro": 10, "skeletal": 5, "cardio": 5, "desc": "Neural Tube Formation and Early Cell Differentiation inside the embryonic sac."},
        2: {"size": "Raspberry", "neuro": 25, "skeletal": 15, "cardio": 30, "desc": "Heart Begins Beating and early limb buds appear as brain hemispheres develop."},
        3: {"size": "Lime", "neuro": 45, "skeletal": 30, "cardio": 50, "desc": "Fingerprints forming, vocal chords initial setup, and kidneys start urine output."},
        4: {"size": "Avocado", "neuro": 60, "skeletal": 45, "cardio": 70, "desc": "Sucking reflex development and heart pumping 25 quarts of fluid daily."},
        5: {"size": "Banana", "neuro": 75, "skeletal": 60, "cardio": 80, "desc": "Hearing functions active and baby vernix caseosa coats the delicate skin matrix."},
        6: {"size": "Eggplant", "neuro": 85, "skeletal": 70, "cardio": 85, "desc": "Lungs produce crucial surfactant and foot/handprints are established."},
        7: {"size": "Coconut", "neuro": 90, "skeletal": 80, "cardio": 90, "desc": "Eyelids fully open and close, brain surface folds accelerate scaling indices."},
        8: {"size": "Cantaloupe", "neuro": 95, "skeletal": 90, "cardio": 95, "desc": "Rapid brain growth spikes and vital skeletal structures harden safely."},
        9: {"size": "Watermelon", "neuro": 100, "skeletal": 100, "cardio": 100, "desc": "Full term lung maturity achieved. Immune boost transferred directly from maternal system."}
    }
    
    current_data = fetal_engine[selected_month]
    
    t_col1, t_col2, t_col3 = st.columns([1, 1.2, 1.2])
    
    with t_col1:
        st.html(f"""
            <div class="metric-card">
                <h4>📐 Volumetric Scaling Match</h4>
                <h1 style='color: #00FFCC; margin: 15px 0; font-family: Orbitron;'>{current_data['size']}</h1>
                <p style='color: #94A3B8;'>Real-time anatomic model comparison indicator.</p>
            </div>
        """)
        
    with t_col2:
        st.markdown("#### 🩺 Active Organ Development Logs")
        st.write(f"🧬 **Current Diagnostic Status:** {current_data['desc']}")
            
    with t_col3:
        st.markdown("#### ⚡ Systemic Biological Maturity Bars")
        st.caption("Neural Architecture Complexity")
        st.progress(current_data['neuro'])
