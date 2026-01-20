import streamlit as st
import pandas as pd
import joblib

# Başlık ve Arayüz Ayarları
st.set_page_config(page_title="Kredi Risk Tahmini", layout="centered")
st.title("Kredi Risk Analiz Sistemi")

# Modeli Yükleme Fonksiyonu
@st.cache_resource
def load_model():
    return joblib.load('model.pkl')

try:
    model = load_model()
    
    # Giriş Alanları
    st.subheader("Müşteri Bilgileri")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Yaş", 18, 100, 30)
        amount = st.number_input("Kredi Miktarı (Euro)", 100, 20000, 5000)
        duration = st.slider("Vade (Ay)", 4, 72, 24)

    with col2:
        sex = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
        housing = st.selectbox("Konut", ["Kira", "Mülk", "Ücretsiz"])

    # Tahmin Butonu
    if st.button("Risk Analizi Yap"):
        # Verileri sayısallaştırma (Encoding)
        sex_val = 1 if sex == "Erkek" else 0
        housing_val = 0 if housing == "Kira" else (1 if housing == "Mülk" else 2)
        
        # Giriş verisi (9 sütun: Age, Sex, Job, Housing, Saving, Checking, Purpose, Amount, Duration)
        # Diğer değerleri (Job, Saving vb.) varsayılan orta değerlerde tutuyoruz
        data = [[age, sex_val, 2, housing_val, 0, 0, 1, amount, duration]]
        
        prediction = model.predict(data)
        prob = model.predict_proba(data)

        if prediction[0] == 1:
            st.success(f"✅ GÜVENLİ: Kredi Onaylanabilir! (Olasılık: %{prob[0][1]*100:.1f})")
            st.balloons()
        else:
            st.error(f"❌ RİSKLİ: Başvuru Reddedilebilir! (Risk: %{prob[0][0]*100:.1f})")

except Exception as e:
    st.error(f"Model yüklenemedi: {e}")