import subprocess
import sys
import numpy as np  # NumPy'yi ekledim

# Gerekli kütüphanelerin yüklenmesini kontrol eden fonksiyon
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Gerekli kütüphaneler
required_packages = ['pandas', 'matplotlib', 'seaborn', 'openpyxl', 'numpy']  # NumPy de eklendi
for package in required_packages:
    install_and_import(package)

# Kütüphanelerin import edilmesi
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükleme
file_path = 'fifa5_ana_veri.xlsx'  # Excel dosyanızın yolu
data = pd.read_excel(file_path)

# Sadece mevcut sütunlar
columns = ['overall_rating', 'potential', 'crossing', 'finishing', 'heading_accuracy',
           'short_passing', 'volleys', 'dribbling', 'curve', 'freekick_accuracy',
           'long_passing', 'ball_control', 'acceleration', 'sprint_speed', 'agility',
           'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength',
           'long_shots', 'aggression', 'interceptions', 'positioning', 'vision',
           'penalties', 'composure', 'marking', 'standing_tackle', 'sliding_tackle']

# 1. Tek Değişkenli Analiz: 'overall_rating' dağılımı
plt.figure(figsize=(10, 6))  # Grafik boyutunu belirleme
sns.histplot(data['overall_rating'], kde=True, bins=30, color='blue')  # Histogram ve KDE
plt.title('Overall Rating (Genel Derecelendirme) Dağılımı', fontsize=16)  # Başlık
plt.xlabel('Overall Rating', fontsize=12)  # X ekseni etiketi
plt.ylabel('Frekans', fontsize=12)  # Y ekseni etiketi
plt.grid(True, linestyle='--', alpha=0.7)  # Arka plan ızgarası
plt.show()

# 2. Korelasyon Matrisinin Sadece Üst Üçgeni
plt.figure(figsize=(15, 10))  # Grafik boyutunu belirleme
corr_matrix = data[columns].corr()  # Korelasyon matrisini hesaplama
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Üst üçgen için maske oluşturma
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)  # Heatmap oluşturma
plt.title('Oyuncu Özellikleri Korelasyon Heatmapi', fontsize=16)  # Başlık
plt.show()

# 3. Scatter Plot: Overall Rating ve Potential
plt.figure(figsize=(10, 6))  # Grafik boyutunu belirleme
sns.scatterplot(x=data['potential'], y=data['overall_rating'], alpha=0.7, color='green')  # Scatter plot
plt.title('Overall Rating (Genel Derecelendirme) ve Potential (Potansiyel) Dağılımı', fontsize=16)  # Başlık
plt.xlabel('Potential', fontsize=12)  # X ekseni etiketi
plt.ylabel('Overall Rating', fontsize=12)  # Y ekseni etiketi
plt.grid(True, linestyle='--', alpha=0.7)  # Arka plan ızgarası
plt.show()

# 4. Scatter Plot: Sprint Hızı ve Dayanıklılık İlişkisi
if 'agility' in columns and 'stamina' in columns:
    plt.figure(figsize=(10, 6))  # Grafik boyutunu belirleme
    sns.scatterplot(x=data['stamina'], y=data['agility'], alpha=0.7, color='purple')  # Scatter plot
    plt.title('Agility (Çeviklik) ve Stamina (Dayanıklılık) İlişkisi', fontsize=16)  # Başlık
    plt.xlabel('Çeviklik', fontsize=12)  # X ekseni etiketi
    plt.ylabel('Dayanıklılık', fontsize=12)  # Y ekseni etiketi
    plt.grid(True, linestyle='--', alpha=0.7)  # Arka plan ızgarası
    plt.show()

# 5. Box Plot: Strength ve Aggression
if 'strength' in columns and 'aggression' in columns:
    plt.figure(figsize=(12, 8))  # Grafik boyutunu belirleme
    sns.boxplot(x='aggression', y='strength', data=data, palette="viridis")  # Box plot
    plt.title('Strength (Güç) ve Aggression (Agresiflik) İlişkisi', fontsize=16)  # Başlık
    plt.xlabel('Aggression', fontsize=12)  # X ekseni etiketi
    plt.ylabel('Strength', fontsize=12)  # Y ekseni etiketi
    plt.grid(True, linestyle='--', alpha=0.7)  # Arka plan ızgarası
    plt.show()

# 6. Box Plot: Şut Gücü ve Agresiflik İlişkisi
if 'shot_power' in columns and 'penalties' in columns:
    plt.figure(figsize=(12, 8))  # Grafik boyutunu belirleme
    sns.boxplot(x='penalties', y='shot_power', data=data, palette="mako")  # Box plot
    plt.title('Shot Power (Şut Gücü) ve Penalties (Penaltı) İlişkisi', fontsize=16)  # Başlık
    plt.xlabel('Penaltı', fontsize=12)  # X ekseni etiketi
    plt.ylabel('Şut Gücü', fontsize=12)  # Y ekseni etiketi
    plt.grid(True, linestyle='--', alpha=0.7)  # Arka plan ızgarası
    plt.show()
