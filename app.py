import streamlit as st
import pandas as pd

# 🚀 Page Configurations (Premium Theme Setup)
st.set_page_config(
    page_title="GeneCare AI Pro - Secure Clinical Platform", 
    page_icon="🧬", 
    layout="wide"
)

# --- 🚀 CUSTOM STYLING FOR MAXIMUM VISIBILITY (100% FIXED SYNTAX WITH st.html) ---
st.html("""
<style>
.stApp { background-color: #050811 !important; color: #E2E8F0 !important; }
label[data-testid="stWidgetLabel"] p, .stMarkdown p, p, span, h1, h2, h3, h4 { color: #FFFFFF !important; }
.stCheckbox label p { color: #00FFCC !important; font-weight: bold !important; }
.main-title { font-size:45px; font-weight:900; color: #00FFCC !important; text-align: center; margin-bottom: 2px; text-shadow: 0 0 20px rgba(0, 255, 204, 0.6); }
.subtitle { font-size:18px; text-align: center; color: #94A3B8 !important; margin-bottom: 35px; }
.feature-card { background-color: #0f172a; padding: 25px; border-radius: 16px; border: 1px solid #00FFCC; margin-bottom: 25px; }
.danger-card { background-color: #2D1A1E; padding: 20px; border-radius: 12px; border-left: 6px solid #FF4D4D; margin-bottom: 15px; border: 1px solid #FF4D4D; }
.safe-card { background-color: #142217; padding: 20px; border-radius: 12px; border-left: 6px solid #00FF66; margin-bottom: 15px; border: 1px solid #00FF66; }
.metric-card { background-color: #0b0f19; padding: 25px; border-radius: 14px; border: 1px solid #00FFCC; text-align: center; }
.lock-card { background-color: #0b132b; padding: 30px; border-radius: 20px; border: 2px solid #00FFCC; text-align: center; margin: auto; max-width: 500px; }
.status-box { padding: 15px; border-radius: 12px; margin-top: 25px; font-weight: bold; font-size: 20px; text-align: center; border: 2px solid #00FFCC; background-color: #0b0f19; }
</style>
""")

# --- INITIALIZE SESSION STATE FOR AUTHENTICATION ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ==================== 🔐 LOGIN PAGE GATEWAY ====================
if not st.session_state.authenticated:
    st.html("<div style='height: 40px;'></div>")
    st.html('<div class="main-title">🧬 GeneCare AI Pro</div>')
    st.html('<div class="subtitle">Secure Genomic Bio-Vault & Predictive Clinical Interface</div>')
    
    st.html("""
<div class="lock-card">
    <h3 style='margin-bottom: 10px; color: #00FFCC;'>🔒 BIO-SECURITY INTERFACE</h3>
    <p style='color: #94A3B8; font-size: 14px;'>HIPAA Compliant Dynamic Verification & Profile Registration Gate</p>
</div>
""")
    st.html("<div style='height: 25px;'></div>")
    
    username = st.text_input("Enter Clinical Identity Key / Username", placeholder="e.g., sunita")
    password = st.text_input("Enter Encrypted Passkey", type="password", placeholder="••••••••")
    
    st.html("<div style='height: 10px;'></div>")
    privacy_consent = st.checkbox("I authorize GeneCare AI to perform real-time genetic strand matching under strict encryption protocols.")
    
    st.html("<div style='height: 15px;'></div>")
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
    st.html("""
<div style="background-color: #0b0f19; padding: 15px; border-radius: 10px; text-align: center; border: 1px dashed #FF4D4D; max-width: 800px; margin: auto;">
    <span style="color: #FF4D4D; font-size: 13px;">🔒 SECURITY DEFENSE NOTICE: Unauthorized interception attempts are logged and purged by firewall cores.</span>
</div>
""")

# ==================== 🔓 UNLOCKED SYSTEM MAIN INTERFACE ====================
else:
    st.html("<div style='text-align: right;'><span style='color: #00FFCC; font-weight: bold;'>👤 Session Active: User Authenticated</span></div>")
    
    # 🌐 Sidebar Radio Navigation (0% spacing error risk)
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

    # Main Branding Titles
    st.html('<div class="main-title">🧬 GeneCare AI Pro</div>')
    st.html('<div class="subtitle">Next-Gen Bio-Intelligence, Diagnostic Report Scanner & Gestational Risk Simulation Hub</div>')
    st.divider()

    # ==================== 🧬 PHASE 1: GENOMIC COMPATIBILITY ====================
    if page_selection == "🧬 Phase 1: Genomic Compatibility":
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.html('<div class="feature-card"><h3 style="color:#00FFCC;">👥 Core Parental Phenotype Mapping</h3>Configure baseline biological sequences to simulate Mendelian chromosomal transmission.</div>')
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
            st.html('<div class="feature-card"><h3 style="color:#00FFCC;">🚨 Real-time Bio-Compatibility Shield</h3>Algorithmic screening for Rh incompatibility matrix and anti-body aggregation triggers.</div>')
            is_father_pos = "+" in f_blood
            is_mother_pos = "+" in m_blood
            if (not is_mother_pos) and is_father_pos:
                st.error("🔴 CRITICAL IMMUNOLOGICAL DISCORDANCE DETECTED: Rh Incompatibility Active.")
                st.write("The mother is Rh-Negative and the father is Rh-Positive.")
                st.html('<div class="status-box" style="color: #FF4D4D; border-color: #FF4D4D;">🚨 IMMUNE RISK: CRITICAL (85 / 100)</div>')
            else:
                st.success("✅ GENOMIC COMPATIBILITY INDEX SECURE: No Rh Isolation factors located.")
                st.write("Both maternal and paternal Rh factors are fully compatible.")
                st.html('<div class="status-box" style="color: #00FFCC; border-color: #00FFCC;">✅ IMMUNE RISK: SAFE (15 / 100)</div>')

    # ==================== 🤰 PHASE 2: EMBRYONIC GROWTH TIMELINE ====================
    if page_selection == "🤰 Phase 2: Embryonic Growth Timeline":
        st.html('<div class="feature-card"><h3 style="color:#00FFCC;">🤰 Interactive Fetal Organic Development Matrix</h3>Simulate fetal organogenesis progress, structural calcification, and systemic development vectors.</div>')
        st.markdown("#### 📆 Track Gestational Progression Metrics")
        selected_month = st.slider("Adjust timeline controller to see milestones inside the womb:", min_value=1, max_value=9, value=3, step=1, format="Month %d")
        st.divider()
        
        size_label = "Fruit Size Indicator"
        progress_val = selected_month * 11
        desc_text = f"Fetal tracking index activated for Gestational Month {selected_month}. All physiological metrics are logging nominal structural developments."
        
        if selected_month == 1:
            size_label, neuro_val, skeletal_val, cardio_val = "Poppy Seed", 10, 5, 5
            desc_text = "Neural Tube Formation and Early Cell Differentiation inside the embryonic sac."
        elif selected_month == 2:
            size_label, neuro_val, skeletal_val, cardio_val = "Raspberry", 25, 15, 30
            desc_text = "Heart Begins Beating and early limb buds appear as brain hemispheres develop."
        elif selected_month == 4:
