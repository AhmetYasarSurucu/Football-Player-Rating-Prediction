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

# Tensor'lara dönüştür
X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test.values, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

# Yapay sinir ağı modeli
class NeuralNetwork(nn.Module):
    def __init__(self, input_size):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

# Modeli oluştur
input_size = X_train.shape[1]
model = NeuralNetwork(input_size)

# Kayıp fonksiyonu ve optimizasyon
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Eğitim
epochs = 1000
losses = []
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    y_pred = model(X_train_tensor)
    loss = criterion(y_pred, y_train_tensor)
    loss.backward()
    optimizer.step()
    losses.append(loss.item())
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}")

# Test setinde tahmin yapma
model.eval()
y_pred_train_tensor = model(X_train_tensor).detach().numpy()
y_pred_test_tensor = model(X_test_tensor).detach().numpy()

# Performans ölçümleri hesaplama
def calculate_metrics(y_true, y_pred, X):
    residuals = y_true - y_pred.ravel()
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
train_metrics = calculate_metrics(y_train.values, y_pred_train_tensor, X_train)
test_metrics = calculate_metrics(y_test.values, y_pred_test_tensor, X_test)

# En iyi parametreleri ekrana yazdır
print("En iyi parametreler: ", {
    "Learning Rate": 0.01,
    "Epochs": epochs,
    "Optimizer": "Adam",
    "Loss Function": "MSELoss",
    "Layer Sizes": [X_train.shape[1], 64, 32, 1]
})

# Performans sonuçlarını tabloya dönüştürme
performance_results = pd.DataFrame({
    "Kriter": list(train_metrics.keys()),
    "Eğitim": list(train_metrics.values()),
    "Test": list(test_metrics.values())
})

# Performans sonuçlarını Excel'e yazdırma
performance_results.to_excel("NeuralNetwork_Performans_Sonuclari_Optimized1.xlsx", index=False)
print("Performans sonuçları 'NeuralNetwork_Performans_Sonuclari_Optimized.xlsx' dosyasına kaydedildi.")

# Tahminlerin ve gerçek değerlerin grafiği
plt.plot(y_test.values, label='Gerçek Değerler', color='blue')
plt.plot(y_pred_test_tensor, label='Tahminler', color='red')
plt.legend()
plt.title("Yapay Sinir Ağı Gerçek Değerler ve Tahminler")
plt.show()

# Gerçek ve tahmin değerlerinin karşılaştırılması
plt.scatter(y_test, y_pred_test_tensor, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.xlabel("Gerçek Değerler")
plt.ylabel("Tahmin Değerleri")
plt.title("Yapay Sinir Ağı Gerçek ve Tahmin Karşılaştırması")
plt.show()
