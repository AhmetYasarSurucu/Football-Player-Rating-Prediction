import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Veriyi yükleme
file_path = 'fifa5_ana_veri.xlsx'
data = pd.read_excel(file_path)

# Sütun türlerini inceleme
print("Sütun türleri:\n", data.dtypes)

# Sayısal sütunları belirleme
numeric_columns = data.select_dtypes(include=['number']).columns

# 1. Eksik Gözlem İşleme
# Eksik değer kontrolü
missing_values = data.isnull().sum()
missing_values_df = pd.DataFrame({
    'Column Name (İngilizce)': missing_values.index,
    'Eksik Gözlem Sayısı (Türkçe)': missing_values.values
})

# 2. Aykırı Gözlem İşleme
# IQR yöntemi ile aykırı değerleri sınırlandırma ve aykırı değer sayısı hesaplama
outlier_counts = []
for column in numeric_columns:
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = ((data[column] < lower_bound) | (data[column] > upper_bound)).sum()
    outlier_counts.append(outliers)

outlier_counts_df = pd.DataFrame({
    'Column Name (İngilizce)': numeric_columns,
    'Aykırı Gözlem Sayısı (Türkçe)': outlier_counts
})

# Eksik ve aykırı gözlem sayıları birleştirilerek Excel'e kaydedilmesi
output_stats = pd.merge(missing_values_df, outlier_counts_df, on='Column Name (İngilizce)', how='left')
output_file_path_stats = 'eksik_aykiri_istatistikler.xlsx'
output_stats.to_excel(output_file_path_stats, index=False)

# Eksik değerlerin doldurulması
data[numeric_columns] = data[numeric_columns].apply(lambda col: col.fillna(col.mean()))
print("\nSayısal sütunlardaki eksik değerler dolduruldu.")

# Aykırı değerlerin sınırlandırılması
for column in numeric_columns:
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data[column] = np.where(data[column] < lower_bound, lower_bound, data[column])
    data[column] = np.where(data[column] > upper_bound, upper_bound, data[column])
print("\nAykırı değerler IQR yöntemiyle sınırlandırıldı.")

# 3. Standartlaştırma
# Sayısal sütunların standartlaştırılması
scaler = StandardScaler()
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
print("\nSayısal sütunlar standartlaştırıldı.")

# İşlenmiş veriyi Excel'e kaydetme
output_file_path = 'veri_onisleme_sonuc.xlsx'
data.to_excel(output_file_path, index=False)

print(f"\nEksik ve aykırı gözlem istatistikleri '{output_file_path_stats}' dosyasına kaydedildi.")
print(f"Veri ön işleme tamamlandı. Sonuçlar '{output_file_path}' dosyasına kaydedildi.")
