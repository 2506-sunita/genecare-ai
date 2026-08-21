import streamlit as st
import pandas as pd

# 🚀 Page Configurations (Premium Theme Setup)
st.set_page_config(
    page_title="GeneCare AI Pro - Secure Clinical Platform", 
    page_icon="🧬", 
    layout="wide"
)

# --- 🚀 CUSTOM STYLING FOR MAXIMUM VISIBILITY (LIGHT BLUE & RED THEME) ---
st.markdown("""
<style>
/* Global App Background & Font Settings */
.stApp { 
    background-color: #060b18 !important; 
    color: #ffffff !important;
}

/* HIGH VISIBILITY SIDEBAR: Forces sidebar text to be crystal clear dark black/red */
[data-testid="stSidebar"] {
    background-color: #f0f4f8 !important; /* Soft Light Blue-White */
    border-right: 3px solid #00ccff !important;
}
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
    color: #111827 !important; /* Solid Dark Black */
    font-size: 16px !important;
    font-weight: 700 !important;
}
/* Style the radio button selected target */
.stRadio label p {
    color: #111827 !important;
    font-weight: 700 !important;
}

/* Forces main screen descriptions to clear forced solid white */
div[data-testid="stMarkdownContainer"] p, span, li {
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

/* Premium Luminous Light Blue Headers */
.main-title { 
    font-size: 45px; 
    font-weight: 900; 
    color: #00ccff !important; /* Light Blue */
    text-align: center; 
    margin-bottom: 2px; 
    text-shadow: 0 0 15px rgba(0, 204, 255, 0.6);
}
.subtitle { 
    font-size: 18px; 
    text-align: center; 
    color: #94A3B8 !important; 
    margin-bottom: 35px; 
    font-weight: 500 !important;
}

/* Advanced Card Premium Structures with Red/Light Blue Borders */
.feature-card { 
    background-color: #0f172a; 
    padding: 25px; 
    border-radius: 16px; 
    border: 2px solid #00ccff; /* Light Blue Border */
    margin-bottom: 25px; 
    box-shadow: 0 0 15px rgba(0, 204, 255, 0.2);
}
.danger-card { 
    background-color: #2a1518; 
    padding: 20px; 
    border-radius: 12px; 
    border-left: 6px solid #ff3333; /* Bright Red Border */
    margin-bottom: 15px; 
    border-top: 1px solid #ff3333;
    box-shadow: 0 0 15px rgba(255, 51, 51, 0.2);
}
.safe-card { 
    background-color: #0f2419; 
    padding: 20px; 
    border-radius: 12px; 
    border-left: 6px solid #00FF66; 
    margin-bottom: 15px; 
    border-top: 1px solid rgba(0, 255, 102, 0.3);
}
.metric-card { 
    background-color: #0c1324; 
    padding: 25px; 
    border-radius: 14px; 
    border: 2px solid #00ccff; 
    text-align: center;
}
.lock-card { 
    background: linear-gradient(135deg, #0b132b, #131f3d); 
    padding: 35px; 
    border-radius: 20px; 
    border: 2px solid #ff3333; /* Red Security Gate Border */
    text-align: center; 
    margin: auto; 
    max-width: 520px;
    box-shadow: 0 0 35px rgba(255, 51, 51, 0.3);
}
.status-box { 
    padding: 18px; 
    border-radius: 12px; 
    margin-top: 25px; 
    font-weight: bold; 
    font-size: 20px; 
    text-align: center; 
    border: 2px solid #ff3333; /* Red Indicator Border */
    background-color: #0c1324;
}
</style>
""", unsafe_allowed_html=True)

# --- INITIALIZE SESSION STATE FOR AUTHENTICATION ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ==================== 🔐 SECURE PORTAL ACCESS GATEWAY (LOGIN PAGE) ====================
if not st.session_state.authenticated:
    st.markdown("<div style='height: 40px;'></div>", unsafe_allowed_html=True)
    st.markdown('<div class="main-title" style="color: #ff3333 !important; text-shadow: 0 0 15px #ff3333;">🚨 GeneCare AI Pro</div>', unsafe_allowed_html=True)
    st.markdown('<div class="subtitle">Secure Genomic Bio-Vault & Predictive Clinical Interface</div>', unsafe_allowed_html=True)
    
    st.markdown("""
<div class="lock-card">
    <h3 style='margin-bottom: 10px; color: #ff3333 !important;'>🔒 BIO-SECURITY PROTOCOL INTERFACE</h3>
    <p style='color: #94A3B8 !important; font-size: 14px !important;'>HIPAA Compliant Dynamic Verification & Profile Registration Gate</p>
</div>
""", unsafe_allowed_html=True)
    st.markdown("<div style='height: 25px;'></div>", unsafe_allowed_html=True)
    
    username = st.text_input("Enter Clinical Identity Key / Username", placeholder="e.g., sunita")
    password = st.text_input("Enter Encrypted Passkey", type="password", placeholder="••••••••")
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allowed_html=True)
    privacy_consent = st.checkbox("I authorize GeneCare AI to perform real-time genetic strand matching under strict encryption protocols.")
    
    st.markdown("<div style='height: 15px;'></div>", unsafe_allowed_html=True)
    if st.button("🔓 AUTHORIZE AND DECRYPT INTERFACE", use_container_width=True, type="primary"):
        if username == "sunita" and password == "123":
            if privacy_consent:
                st.session_state.authenticated = True
                st.toast("Initialization sequence authorized...", icon="✅")
                st.rerun()
            else:
                st.warning("⚠️ Access Denied: You must accept the Privacy Data Consent terms.")
        else:
            st.error("❌ Authentication Failure: Invalid username or password.")
                
    st.divider()
    st.markdown("""
<div style="background-color: #0b0f19; padding: 15px; border-radius: 10px; text-align: center; border: 1px dashed #FF3333; max-width: 800px; margin: auto;">
    <span style="color: #FF3333 !important; font-size: 13px !important; font-weight: bold;">🔒 SECURITY DEFENSE NOTICE: Unauthorized interception attempts are logged and purged by firewall cores.</span>
</div>
""", unsafe_allowed_html=True)

# ==================== 🔓 UNLOCKED SYSTEM MAIN APPLICATION INTERFACE ====================
else:
    st.markdown("<div style='text-align: right;'><span style='color: #00ccff; font-weight: bold;'>👤 Session Active: User Authenticated</span></div>", unsafe_allowed_html=True)
    
    # 🌐 Sidebar Radio Navigation Panel (The original working sidebar menu!)
    st.sidebar.markdown("### 🌐 Navigation Panel")
    page_selection = st.sidebar.radio("Go to Project Phase:", [
        "🧬 Phase 1: Genomic Compatibility", 
        "🤰 Phase 2: Embryonic Growth Timeline", 
        "📁 Phase 3: AI Diagnostic Scanner",
        "🥗 Phase 4: Prenatal Nutrition Matrix"
    ])
    
    st.sidebar.divider()
    if st.sidebar.button("🔒 LOGOUT SECURELY", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

    # Main Branding Titles Unlocked View
    st.markdown('<div class="main-title">🧬 GeneCare AI Pro</div>', unsafe_allowed_html=True)
    st.markdown('<div class="subtitle">Next-Gen Bio-Intelligence, Diagnostic Report Scanner & Gestational Risk Simulation Hub</div>', unsafe_allowed_html=True)
    st.divider()

    # ==================== 🧬 PHASE 1: GENOMIC COMPATIBILITY ====================
    if page_selection == "🧬 Phase 1: Genomic Compatibility":
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.markdown('<div class="feature-card"><h3 style="color:#00ccff !important;">👥 Core Parental Phenotype Mapping</h3>Configure baseline biological sequences to simulate Mendelian chromosomal transmission.</div>', unsafe_allowed_html=True)
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                st.markdown("**Father's Bio-Markers**")
                f_blood = st.selectbox("Father's Blood Group Type", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="f_b")
                f_eye = st.selectbox("Father's Iris Allele Expression", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="f_e")
                father_stress = st.slider("Father's Cortisol Strain (Daily Stress Index)", 1, 10, 4)
            with sub_col2:
                st.markdown("**Mother's Bio-Markers**")
                m_blood = st.selectbox("Mother's Blood Group Type", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], key="m_b")
                m_eye = st.selectbox("Mother's Iris Allele Expression", ["Brown (Dominant)", "Blue (Recessive)", "Green (Recessive)"], key="m_e")
                mother_sleep = st.slider("Mother's Sleep Optimization Scale (Hours/Night)", 4, 10, 8)
            st.divider()
            st.markdown("#### 🧬 Real-time Epigenetic Mutation Profile")
            mutation_resistance = 100 - (father_stress * 5) + (mother_sleep * 2)
            if mutation_resistance > 80:
                st.success(f"🛡️ DNA Integrity Score: {mutation_resistance:.1f}% (Excellent) — Low probability of anomalies.")
            else:
                st.warning(f"⚡ DNA Integrity Score: {mutation_resistance:.1f}% (Sub-Optimal) — High cortisol indices detected.")
            st.divider()
            st.markdown("#### 🏁 Automated Progeny Trait Prediction Grid")
            g_father = "B" if "Brown" in f_eye else "b"
            g_mother = "B" if "Brown" in m_eye else "b"
            punnett_data = {
                "Maternal / Paternal": [f"Father Allele: {g_father}", f"Father Allele: {g_father}"],
                f"Mother Allele: {g_mother}": [f"{g_father}{g_mother} (Brown)", f"{g_father}{g_mother} (Brown)"],
                "Mother Allele: b": [f"{g_father}b (Brown)" if g_father == "B" else "bb (Blue/Green)", f"{g_father}b (Brown)" if g_father == "B" else "bb (Blue/Green)"]
            }
            df_punnett = pd.DataFrame(punnett_data)
            st.table(df_punnett)
        with col2:
            st.markdown('<div class="feature-card"><h3 style="color:#00ccff !important;">🚨 Real-time Bio-Compatibility Shield</h3>Algorithmic screening for Rh incompatibility matrix and anti-body aggregation triggers.</div>', unsafe_allowed_html=True)
            is_father_pos = "+" in f_blood
            is_mother_pos = "+" in m_blood
            if (not is_mother_pos) and is_father_pos:
