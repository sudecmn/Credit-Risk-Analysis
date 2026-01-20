# 🏦 Fintech: Credit Risk Analysis & Prediction

Bu proje, bankacılık sektöründe hayati önem taşıyan kredi risk analizini otomatize etmek amacıyla geliştirilmiş bir makine öğrenmesi çalışmasıdır. **German Credit Dataset** kullanılarak hazırlanan model, bir müşterinin demografik ve finansal verilerine dayanarak kredi geri ödeme riskini (Good/Bad) tahmin eder.

---

## 📊 Proje Genel Bakışı
Kredi risk yönetimi, finans kuruluşlarının karlılığını doğrudan etkileyen bir süreçtir. Bu çalışmada:
* **Veri Analizi:** Müşteri profilleri (yaş, cinsiyet, konut durumu) ile kredi riski arasındaki korelasyonlar incelendi.
* **Makine Öğrenmesi:** Sınıflandırma problemi olarak ele alınan risk tahmini için Random Forest algoritması kullanıldı.
* **Optimizasyon:** Model performansı, GridSearchCV ile hiperparametre optimizasyonu yapılarak maksimize edildi.

---

## 🛠️ Teknik Araçlar ve Kütüphaneler
* **Programlama Dili:** Python
* **Veri Manipülasyonu:** Pandas, NumPy
* **Veri Görselleştirme:** Seaborn, Matplotlib
* **Yapay Zeka & ML:** Scikit-Learn (Random Forest, GridSearchCV, LabelEncoder)

---

## ⚙️ Uygulanan Adımlar

### 1. Veri Ön İşleme (Preprocessing)
* `Saving accounts` ve `Checking account` sütunlarındaki eksik veriler, veri kaybını önlemek için "unknown" olarak etiketlendi.
* Kategorik veriler (Label Encoding ve One-Hot Encoding) makine öğrenmesi modellerine uygun sayısal formatlara dönüştürüldü.

### 2. Model Eğitimi ve Hiperparametre Optimizasyonu
* Veri seti %80 eğitim, %20 test olarak ayrıldı.
* Random Forest modelinde en iyi sonuçları veren `n_estimators`, `max_depth` ve `min_samples_split` değerleri otomatik olarak belirlendi.

### 3. Performans Değerlendirmesi
* Model, test verisi üzerinde yüksek bir doğruluk (accuracy) oranı sergiledi.
* **Feature Importance:** Analiz sonucunda kredi miktarı (`Credit amount`) ve kredi süresinin (`Duration`) risk üzerindeki en etkili faktörler olduğu saptandı.

---

## 📂 Dosya Yapısı
* `/data`: Ham veri seti (german_credit_data.csv).
* `/notebooks`: Analiz ve model eğitim süreçlerini içeren Jupyter Notebook dosyası.
* `requirements.txt`: Projenin çalışması için gerekli Python kütüphaneleri.
* `app.py`: Kullanıcıların canlı kredi risk analizi yapabildiği interaktif web uygulaması (Streamlit).
* `model.pkl`: Eğitilmiş ve kullanıma hazır olan Random Forest makine öğrenmesi modeli dosyası.   


---
## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için şu adımları izleyin:

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/sudecmn/Credit-Risk-Analysis.git](https://github.com/sudecmn/Credit-Risk-Analysis.git)
   cd Credit-Risk-Analysis
    ```
    ---
2. **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
   python -m pip install -r requirements.txt
    ```
   ---
    
4. **Web Uygulamasını Başlatın:**
    ```bash
   python -m streamlit run app.py
    ```
   ---
   Not: Uygulama tarayıcınızda otomatik olarak açılacaktır.

   
