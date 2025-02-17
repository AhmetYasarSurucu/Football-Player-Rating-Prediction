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
required_packages = ['pandas', 'openpyxl', 'numpy', 'matplotlib', 'xgboost', 'sklearn']
for package in required_packages:
    install_and_import(package)

# Gerekli kütüphaneleri yükleme
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, ParameterGrid
import numpy as np
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

# Hiperparametre arama için grid tanımlama
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 6, 10],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

best_rmse = float('inf')
best_params = None
best_model = None

# Tüm parametre kombinasyonlarını deneme
for params in ParameterGrid(param_grid):
    print(f"Testing parameters: {params}")
    model = XGBRegressor(
        n_estimators=params['n_estimators'],
        max_depth=params['max_depth'],
        learning_rate=params['learning_rate'],
        subsample=params['subsample'],
        colsample_bytree=params['colsample_bytree'],
        random_state=42
    )
    # Modeli eğitme
    model.fit(X_train, y_train)

    # Test setinde tahmin yapma
    y_pred_test = model.predict(X_test)

    # Performans ölçümü
    rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))

    # En iyi modeli saklama
    if rmse < best_rmse:
        best_rmse = rmse
        best_params = params
        best_model = model

print(f"En iyi parametreler: {best_params}, En iyi RMSE: {best_rmse}")

# En iyi model ile tahmin yap
y_pred_train = best_model.predict(X_train)
y_pred_test = best_model.predict(X_test)

# Performans metriklerini hesaplama
def calculate_metrics(y_true, y_pred, X):
    residuals = y_true - y_pred
    n = len(y_true)
    p = X.shape[1]
    mean_y = np.mean(y_true)

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    rrmse = rmse / mean_y
    mad = np.mean(np.abs(residuals))
    mape = np.mean(np.abs(residuals / y_true)) * 100
    rsq = r2_score(y_true, y_pred)
    adj_rsq = 1 - (1 - rsq) * ((n - 1) / (n - p - 1))

    # AIC ve CAIC hesaplama
    rss = np.sum(residuals ** 2)
    aic = n * np.log(rss / n) + 2 * p
    caic = aic + (p * (np.log(n) - 1))

    # Diğer metrikler
    sdr = np.std(residuals) / mean_y
    cv = np.std(y_pred) / np.mean(y_pred)

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
performance_results.to_excel("XGBoost_Performans_Sonuclari_Optimized.xlsx", index=False)
print("Performans sonuçları 'XGBoost_Performans_Sonuclari_Optimized.xlsx' dosyasına kaydedildi.")

# Tahminlerin ve gerçek değerlerin grafiği
plt.plot(y_test.values, label='Gerçek Değerler', color='blue')
plt.plot(y_pred_test, label='Tahminler', color='red')
plt.legend()
plt.title("XGBoost Gerçek Değerler ve Tahminler")
plt.show()

# Gerçek ve tahmin değerlerinin karşılaştırılması
plt.scatter(y_test, y_pred_test, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.xlabel("Gerçek Değerler")
plt.ylabel("Tahmin Değerleri")
plt.title("XGBoost Gerçek ve Tahmin Karşılaştırması")
plt.show()
