import subprocess
import sys

# Gerekli kütüphanelerin yüklü olup olmadığını kontrol et ve yükle
required_packages = ['pandas', 'openpyxl']  # Gerekli tüm kütüphaneler

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Tüm gerekli kütüphaneleri yükle
for package in required_packages:
    install_and_import(package)

# Kütüphaneleri yükledikten sonra programın geri kalanı
import pandas as pd
# Excel dosyasını yükleme

data = pd.read_excel('fifa5_ana_veri.xlsx')

# Sayısal sütunları filtreleme
numeric_data = data.select_dtypes(include=['number'])

# Sayısal sütunlar için özet istatistikleri hesaplama
summary_stats_numeric = {
    'Ortalama (Mean)': numeric_data.mean(),
    'Standart Sapma (Std)': numeric_data.std(),
    'Minimum (Min)': numeric_data.min(),
    '1. Çeyrek (25%)': numeric_data.quantile(0.25),
    'Medyan (50%)': numeric_data.median(),
    '3. Çeyrek (75%)': numeric_data.quantile(0.75),
    'Maksimum (Max)': numeric_data.max(),
    'Varyans (Variance)': numeric_data.var(),
    'Aralık (Range)': numeric_data.max() - numeric_data.min(),
    'Basıklık (Kurtosis)': numeric_data.kurtosis(),
    'Çarpıklık (Skewness)': numeric_data.skew(),
    'Mod': numeric_data.mode().iloc[0]  # İlk mod değerini al
}

# Özet istatistikleri DataFrame'e dönüştür
summary_numeric_df = pd.DataFrame(summary_stats_numeric)

# Sütun isimlerini okunabilir hale getiren fonksiyon
def make_readable(column_name):
    return column_name.replace('_', ' ').title()

# Sütun isimlerini okunaklı hale getir ve baş harflerini büyük yap
summary_numeric_df.rename(columns=lambda x: make_readable(x), inplace=True)

# Özet istatistikleri yeni bir Excel dosyasına kaydet
output_file_path = 'ozet_istatistikler.xlsx'
summary_numeric_df.to_excel(output_file_path, sheet_name='Özet İstatistikler', index_label='İstatistikler')

# Kullanıcıya çıktı dosyasının kaydedildiğini bildir
print(f"Özet istatistikler '{output_file_path}' dosyasına kaydedildi.")
