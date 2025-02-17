import subprocess
import sys

# Gerekli kütüphaneleri kontrol et ve yükle
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} yüklenemedi. Şimdi yükleniyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Gerekli kütüphaneler
required_packages = ['pandas', 'torch', 'openpyxl', 'numpy', 'matplotlib', 'sklearn']

for package in required_packages:
    if package == 'torch':  # PyTorch için özel kontrol
        try:
            import torch
        except ImportError:
            print("PyTorch yüklenemedi. Lütfen manuel olarak yükleyin: https://pytorch.org/get-started/locally/")
    else:
        install_and_import(package)


import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Veriyi yükle
file_path = 'Standartlastirilmis.xlsx'
data = pd.read_excel(file_path)

# 'name' değişkenini ve hedef değişkeni ayır
if 'name' in data.columns:
    data = data.drop(columns=['name'])

# Eksik verileri kontrol et ve temizle
data = data.dropna()

# Hedef ve bağımsız değişkenlerin tanımlanması
X = data.drop(columns=['overall_rating'])
y = data['overall_rating']

# Veri setini eğitim ve test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lineer Regresyon Modeli
lr_model = LinearRegression()

# Modeli eğit
lr_model.fit(X_train, y_train)

# Tahmin yap
y_pred_train = lr_model.predict(X_train)
y_pred_test = lr_model.predict(X_test)

# Performans ölçümleri hesaplama
def calculate_metrics(y_true, y_pred, X):
    residuals = y_true - y_pred
    n = len(y_true)
    p = X.shape[1]
    mean_y = np.mean(y_true)

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    rrmse = rmse / mean_y
    mad = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs(residuals / y_true)) * 100
    rsq = r2_score(y_true, y_pred)
    adj_rsq = 1 - (1 - rsq) * ((n - 1) / (n - p - 1))
    sdr = np.std(residuals) / mean_y
    cv = np.std(y_pred) / np.mean(y_pred)
    aic = n * np.log(mean_squared_error(y_true, y_pred)) + 2 * (p + 1)
    caic = aic + (p + 1) * (np.log(n) - 1)

    return {
        "RMSE": rmse,
        "RRMSE": rrmse,
        "SDR": sdr,
        "CV": cv,
        "MAD": mad,
        "MAPE": mape,
        "Rsq": rsq,
        "ARsq": adj_rsq,
        "AIC": aic,
        "CAIC": caic
    }

# Eğitim ve test metriklerini hesaplama
train_metrics = calculate_metrics(y_train, y_pred_train, X_train)
test_metrics = calculate_metrics(y_test, y_pred_test, X_test)

# Performans sonuçlarını tabloya dönüştürme
performance_results = pd.DataFrame({
    "Kriter": list(train_metrics.keys()),
    "Eğitim": list(train_metrics.values()),
    "Test": list(test_metrics.values())
})

# Performans sonuçlarını Excel'e yazdırma
performance_results.to_excel("LinearRegression_Performans_Sonuclari_Optimized.xlsx", index=False)
print("Performans sonuçları 'LinearRegression_Performans_Sonuclari_Optimized.xlsx' dosyasına kaydedildi.")

# Tahminlerin ve gerçek değerlerin grafiği
plt.plot(y_test.values, label='Gerçek Değerler', color='blue')
plt.plot(y_pred_test, label='Tahminler', color='red')
plt.legend()
plt.title("Lineer Regresyon Gerçek Değerler ve Tahminler")
plt.show()

# Gerçek ve tahmin değerlerinin karşılaştırılması
plt.scatter(y_test, y_pred_test, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.xlabel("Gerçek Değerler")
plt.ylabel("Tahmin Değerleri")
plt.title("Lineer Regresyon Gerçek ve Tahmin Karşılaştırması")
plt.show()
