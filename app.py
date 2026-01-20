import streamlit as st
import pandas as pd
import joblib
import os

# 1. Sayfa Ayarları
st.set_page_config(page_title="Fintech: Kredi Risk Analiz", layout="centered")


# 2. Model Yükleme
@st.cache_resource
def load_model():
    if os.path.exists('model.pkl'):
        return joblib.load('model.pkl')
    return None

model = load_model()

# 3. Ana Başlık
st.title(" Fintech: Kredi Risk Analiz Sistemi")

# 4. Giriş Alanları (Analiz dosyasındaki sırayla eşleşecek şekilde)
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Yaş", 18, 100, 35)
    sex = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
    housing = st.selectbox("Konut Durumu", ["Mülk", "Kira", "Ücretsiz"])
    amount = st.number_input("Kredi Miktarı (Euro)", 100, 20000, 1000)

with col2:
    duration = st.slider("Vade (Ay)", 4, 72, 12)
    # Sabit tutulan teknik değerler (Analizdeki 'yeni_musteri' örneğinden)
    st.caption("Not: Diğer finansal parametreler varsayılan değerlerde tutulmuştur.")

# 5. Hesaplama
if st.button("Risk Analizi Yap"):
    if model is not None:
        # --- ANALİZ DOSYASIYLA %100 UYUMLU MAPPING ---
        sex_val = 1 if sex == "Erkek" else 0
        # Housing: own:1, rent:2, free:0
        housing_val = 1 if housing == "Mülk" else (2 if housing == "Kira" else 0)
        
        # Sütun Sırası: [Age, Sex, Job, Housing, Saving, Checking, Credit amount, Duration, Purpose]
        # Sabitler: Job=2, Saving=0, Checking=0, Purpose=1
        features = [[age, sex_val, 2, housing_val, 0, 0, amount, duration, 1]]
        
        prediction = model.predict(features)
        proba = model.predict_proba(features)
        
        st.markdown("---")
        # Analiz: 1=GÜVENLİ, 0=RİSKLİ
        if prediction[0] == 1:
            score = proba[0][1] * 100
            st.success(f" GÜVENLİ: Kredi Onaylanabilir! (Güven: %{score:.1f})")
            st.balloons()
        else:
            score = proba[0][0] * 100
            st.error(f" RİSKLİ: Başvuru Reddedilebilir! (Risk: %{score:.1f})")
    else:
        st.error("Model dosyası bulunamadı!")