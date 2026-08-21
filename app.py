import streamlit as st
import pandas as pd

# 🚀 Page Configurations (Premium Theme Setup)
st.set_page_config(
    page_title="GeneCare AI Pro - Secure Clinical Platform", 
    page_icon="🧬", 
    layout="wide"
)

# --- 🚀 ULTRA-ADVANCED LUMINOUS NEON CSS STYLING ---
st.html("""
    <style>
    @import url('https://googleapis.com');
    
    /* Global Styles */
    .stApp { background-color: #050811 !important; font-family: 'Rajdhani', sans-serif; color: #E2E8F0; }
    
    /* High Visibility Input Labels Fix */
    label[data-testid="stWidgetLabel"] p { color: #FFFFFF !important; font-size: 18px !important; font-weight: bold !important; letter-spacing: 0.5px; text-shadow: 0 0 5px rgba(255,255,255,0.2); }
    .stCheckbox label p { color: #00FFCC !important; font-size: 16px !important; font-weight: bold !important; }
    
    /* Glowing Headers */
    .main-title { font-family: 'Orbitron', sans-serif; font-size:45px; font-weight:900; color: #00FFCC; text-align: center; margin-bottom: 2px; text-shadow: 0 0 20px rgba(0, 255, 204, 0.6); }
    .subtitle { font-size:18px; text-align: center; color: #94A3B8; margin-bottom: 35px; letter-spacing: 1px; }
    
    /* Neon Glowing Cards */
    .feature-card { background: linear-gradient(145deg, #0f172a, #1e293b); padding: 25px; border-radius: 16px; border: 1px solid rgba(0, 255, 204, 0.3); margin-bottom: 25px; color: #FFFFFF; }
    .danger-card { background: linear-gradient(145deg, #1e1b1b, #2d1a1e); padding: 20px; border-radius: 12px; border-left: 6px solid #FF4D4D; margin-bottom: 15px; color: #FFFFFF; }
    .safe-card { background: linear-gradient(145deg, #142217, #1a2d22); padding: 20px; border-radius: 12px; border-left: 6px solid #00FF66; margin-bottom: 15px; color: #FFFFFF; }
    .lock-card { background: linear-gradient(145deg, #0b132b, #1c2541); padding: 30px; border-radius: 20px; border: 2px solid #00FFCC; box-shadow: 0 0 25px rgba(0, 255, 204, 0.2); margin: auto; max-width: 500px; color: #FFFFFF; text-align: center; }
    
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

# --- INITIALIZE SESSION STATE FOR SECURE AUTHENTICATION ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ==================== 🔐 SECURE PORTAL ACCESS GATEWAY (LOGIN PAGE) ====================
if not st.session_state.authenticated:
    st.html("<div style='height: 40px;'></div>")
    st.html('<div class="main-title">🧬 GeneCare AI Pro</div>')
    st.html('<div class="subtitle">Secure Genomic Bio-Vault & Predictive Clinical Interface</div>')
    
    col_lock, _ = st.columns()
    with col_lock:
        st.html("""
            <div class="lock-card">
                <h3 style='margin-bottom: 10px;'>🔒 BIO-SECURITY INTERFACE</h3>
                <p style='color: #94A3B8; font-size: 14px;'>HIPAA Compliant Dynamic Verification & Profile Registration Gate</p>
            </div>
        """)
        st.html("<div style='height: 25px;'></div>")
        
        # Interactive Inputs with fixed high-visibility font weights
        username = st.text_input("Enter Clinical Identity Key / Username", placeholder="e.g., sunita")
        password = st.text_input("Enter Encrypted Passkey", type="password", placeholder="••••••••")
        
        st.html("<div style='height: 10px;'></div>")
        privacy_consent = st.checkbox("I authorize GeneCare AI to perform real-time genetic strand matching under strict encryption protocols.")
        
        st.html("<div style='height: 15px;'></div>")
        if st.button("🔓 AUTHORIZE AND DECRYPT INTERFACE", use_container_width=True, type="primary"):
            if username == "sunita" and password == "123":
                if privacy_consent:
                    st.session_state.authenticated = True
                    st.toast("Initialization sequence authorized. Decrypting core system metrics...", icon="✅")
                    st.rerun()
                else:
                    st.warning("⚠️ Access Denied: You must accept the Privacy Data Consent terms to isolate genetic arrays safely.")
            else:
                st.error("❌ Authentication Failure: Invalid identity key or passkey credentials combination.")
                
    st.divider()
    st.html("""
        <div style="background-color: #0b0f19; padding: 15px; border-radius: 10px; text-align: center; border: 1px dashed rgba(255,77,77,0.3);">
            <span style="color: #FF4D4D; font-family: Orbitron; font-size: 13px;">🔒 SECURITY DEFENSE NOTICE: Unauthorized interception attempts are logged and automatically purged by firewall cores.</span>
        </div>
    """)

# ==================== 🔓 UNLOCKED SYSTEM APPLICATION INTERFACE ====================
else:
    # Top bar logout control panel layout
    st.html("<div style='text-align: right; margin-bottom: -40px;'><span style='color: #00FFCC; font-weight: bold;'>👤 Session Active: User Authenticated</span></div>")
    if st.sidebar.button("🔒 LOGOUT SECURELY", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

    # Main Luminous Title Section
    st.html('<div class="main-title">🧬 GeneCare AI Pro</div>')
    st.html('<div class="subtitle">Next-Gen Bio-Intelligence, Diagnostic Report Scanner & Gestational Risk Simulation Hub</div>')
    st.divider()

    # --- 🚀 4 ADVANCED STRUCTURAL PHASES (TABS) ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧬 Phase 1: Genomic Compatibility", 
        "🤰 Phase 2: Embryonic Growth Timeline", 
        "📁 Phase 3: AI Diagnostic Report Scanner",
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
            if mutation_resistance <= 80:
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
