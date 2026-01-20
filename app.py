import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# 1. Sayfa Ayarları
st.set_page_config(page_title="Fintech Risk Analyzer", layout="centered")

# 2. Model Yükleme
@st.cache_resource
def load_model():
    if os.path.exists('model.pkl'):
        return joblib.load('model.pkl')
    return None

model = load_model()

# 3. Ana Başlık
st.title(" Fintech: Kredi Risk Analiz Sistemi")


# 4. Giriş Alanları
st.subheader(" Müşteri Bilgileri")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Yaş", 18, 100, 35)
    sex = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
    housing = st.selectbox("Konut Durumu", ["Mülk", "Kira", "Ücretsiz"])

with col2:
    amount = st.number_input("Kredi Miktarı (Euro)", 100, 20000, 1000)
    duration = st.slider("Vade (Ay)", 4, 72, 12)
    st.caption("Not: Diğer parametreler varsayılan değerlerdedir.")

# 5. Hesaplama ve Görselleştirme
if st.button("Risk Analizi Yap"):
    if model is not None:
        # Teknik Mapping
        sex_val = 1 if sex == "Erkek" else 0
        housing_val = 1 if housing == "Mülk" else (2 if housing == "Kira" else 0)
        
        # Sütun Sırası ve Sabitler
        features = [[age, sex_val, 2, housing_val, 0, 0, amount, duration, 1]]
        
        prediction = model.predict(features)
        proba = model.predict_proba(features)
        
        st.markdown("---")
        
        # Sonuç Paneli
        if prediction[0] == 1:
            st.success(f" GÜVENLİ: Kredi Onaylanabilir! (Güven: %{proba[0][1]*100:.1f})")
            st.balloons()
        else:
            st.error(f" RİSKLİ: Başvuru Reddedilebilir! (Risk: %{proba[0][0]*100:.1f})")

        #   Model Karar Analizi
        st.subheader(" Model Karar Analizi")
        st.write("Modelin bu kararı verirken en çok dikkat ettiği özellikler:")
        
        # Özellik isimleri ve modelden gelen önem değerleri
        feature_names = ['Yaş', 'Cinsiyet', 'İş', 'Konut', 'Birikim', 'Hesap Durumu', 'Kredi Miktarı', 'Vade', 'Kullanım Amacı']
        importances = model.feature_importances_
        
        # Grafiği oluşturma
        fi_df = pd.DataFrame({'Özellik': feature_names, 'Önem': importances}).sort_values(by='Önem', ascending=True)
        
        fig, ax = plt.subplots()
        ax.barh(fi_df['Özellik'], fi_df['Önem'], color='#4CAF50' if prediction[0] == 1 else '#FF5252')
        st.pyplot(fig)
    else:
        st.error("Model yüklenemedi!")

st.markdown("---")
st.caption("© 2026 Fintech Risk Analyzer")