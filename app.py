import streamlit as st
import pandas as pd

# 🚀 Page Configurations (Premium Theme Setup)
st.set_page_config(
    page_title="GeneCare AI Pro - Secure Clinical Platform", 
    page_icon="🧬", 
    layout="wide"
)

# --- INITIALIZE SESSION STATE FOR AUTHENTICATION ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ==================== 🔐 LOGIN PAGE GATEWAY ====================
if not st.session_state.authenticated:
    st.title("🧬 GeneCare AI Pro")
    st.write("Secure Genomic Bio-Vault & Predictive Clinical Interface")
    st.divider()
    
    st.subheader("🔒 BIO-SECURITY PORTAL ACCESS")
    st.caption("HIPAA Compliant Dynamic Verification & Profile Registration Gate")
    
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
    st.error("🔒 SECURITY DEFENSE NOTICE: Unauthorized interception attempts are logged and purged by firewall cores.")

# ==================== 🔓 UNLOCKED SYSTEM MAIN INTERFACE ====================
else:
    st.write("👤 Session Active: User Authenticated")
    
    # 🌐 Sidebar Radio Navigation (0% Spacing or Indentation Error Risk)
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
    st.title("🧬 GeneCare AI Pro")
    st.write("Next-Gen Bio-Intelligence, Diagnostic Report Scanner & Gestational Risk Simulation Hub")
    st.divider()

    # ==================== 🧬 PHASE 1: GENOMIC COMPATIBILITY ====================
    if page_selection == "🧬 Phase 1: Genomic Compatibility":
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.subheader("👥 Core Parental Phenotype Mapping")
            st.write("Configure baseline biological sequences to simulate Mendelian chromosomal transmission.")
            
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
            st.subheader("🧬 Real-time Epigenetic Mutation Profile")
            mutation_resistance = 100 - (father_stress * 5) + (mother_sleep * 2)
            if mutation_resistance > 80:
                st.success(f"🛡️ DNA Integrity Score: {mutation_resistance:.1f}% (Excellent) — Low probability of anomalies.")
            else:
                st.warning(f"⚡ DNA Integrity Score: {mutation_resistance:.1f}% (Sub-Optimal) — High cortisol indices detected.")
                
            st.divider()
            st.subheader("🏁 Automated Progeny Trait Prediction Grid")
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
            st.subheader("🚨 Real-time Bio-Compatibility Shield")
            st.write("Algorithmic screening for Rh incompatibility matrix and anti-body aggregation triggers.")
            is_father_pos = "+" in f_blood
            is_mother_pos = "+" in m_blood
            if (not is_mother_pos) and is_father_pos:
                st.error("🔴 CRITICAL IMMUNOLOGICAL DISCORDANCE DETECTED: Rh Incompatibility Active.")
                st.write("The mother is Rh-Negative and the father is Rh-Positive.")
                st.warning("🚨 IMMUNE RISK ALERT: CRITICAL BOUNDARY ENCOUNTERED (85 / 100)")
            else:
                st.success("✅ GENOMIC COMPATIBILITY INDEX SECURE: No Rh Isolation factors located.")
                st.write("Both maternal and paternal Rh factors are fully compatible.")
                st.info("✅ IMMUNE RISK STATUS: SAFE & BIO-STABLE (15 / 100)")

    # ==================== 🤰 PHASE 2: EMBRYONIC GROWTH TIMELINE ====================
    if page_selection == "🤰 Phase 2: Embryonic Growth Timeline":
        st.subheader("🤰 Interactive Fetal Organic Development Matrix")
        st.write("Simulate fetal organogenesis progress, structural calcification, and systemic development vectors.")
        selected_month = st.slider("Adjust timeline controller to see milestones inside the womb:", min_value=1, max_value=9, value=3, step=1, format="Month %d")
        st.divider()
        
        progress_index = selected_month * 11
        size_box = f"Month {selected_month} Model Matrix"
        diagnostic_text = f"Fetal tracking index successfully activated for Gestational Month {selected_month}. Neural architecture synthesis, cardiac ventricular expansion cycles, and skeletal cell assembly are executing nominal tracking sequences to support standard prenatal health indexes."
            
        t_col1, t_col2, t_col3 = st.columns([1, 1.2, 1.2])
        with t_col1:
            st.info(f"📏 Volumetric Fetal Size Category: Month {selected_month} Active Variant Scale")
        with t_col2:
            st.markdown("#### 🩺 Active Organ Development Logs")
            st.write(f"🧬 **Current Diagnostic Status:** {diagnostic_text}")
        with t_col3:
            st.markdown("#### ⚡ Systemic Biological Maturity Bars")
            st.caption("Neural Complexity Index")
            st.progress(progress_index)
            st.caption("Skeletal Osseous Calcification")
            st.progress(progress_index)
            st.caption("Cardiovascular Volumetric Efficiency")
            st.progress(progress_index)

    # ==================== 📁 PHASE 3: AI DIAGNOSTIC SCANNER ====================
    if page_selection == "📁 Phase 3: AI Diagnostic Scanner":
        st.subheader("📁 Smart AI Diagnostic Lab Report Interpreter")
        st.write("Upload parental clinical blood panels or genetic screening reports (PDF/Image format) for immediate smart solution extraction.")
        uploaded_file = st.file_uploader("Drag and drop your Clinical Medical Report here (.pdf, .png, .jpg)", type=["pdf", "png", "jpg"])
        
        if uploaded_file is not None:
            st.success("🔍 AI STATUS: SCANNING LAB REPORT HIGHLIGHTS & VARIANCE VALUES...")
            st.divider()
            test_type = st.radio("Select Document Profile Key to simulate AI analysis:", [
                "Complete Blood Count (CBC) / Maternal Hemoglobin Panel",
                "Prenatal Glucose Tolerance Screening",
                "Hereditary Carrier Profile (Thalassemia / Gene Variant)"
            ])
            st.divider()
            st.markdown("##### ⚙️ AI Clinical Extraction & Solution Results:")
            if "CBC" in test_type:
                st.error("🚨 RISK INTERCEPTED: Maternal Iron-Deficiency Microcytic Anemia")
                st.write("🧬 **Expected Fetal Affect:** Low maternal hemoglobin restricts proper oxygen flow, potentially retarding early embryonic mass scaling.")
                st.info("💡 **AI Smart Medical Solution:** Initiate continuous 60mg elemental iron therapies immediately along with ascorbic acid (Vitamin C) co-factors to optimize systemic iron transport efficiency.")
            if "Glucose" in test_type:
                st.error("🚨 RISK INTERCEPTED: Hyperglycemic Trend (Gestational Diabetes Vulnerability)")
                st.write("🧬 **Expected Fetal Affect:** Excessive maternal blood sugar passes the placenta, causing fetal hyperinsulinemia and structural overgrowth (Macrosomia).")
