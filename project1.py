import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini okuma
df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')

# Sayısal sütunları seçin (Ülke isimlerini ve sıralama sütununu çıkarıyoruz)
numeric_df = df.drop(columns=['Rank', 'Country'])

# İlk birkaç satırı görüntüleyin
print(df.head())

# Özet istatistikler
print(df.describe())

# En yüksek ve en düşük değerler
for column in df.columns[2:]:
    max_value = df[column].max()
    min_value = df[column].min()
    max_country = df[df[column] == max_value]['Country'].values[0]
    min_country = df[df[column] == min_value]['Country'].values[0]
    print(f"{column} - Max: {max_value} ({max_country}), Min: {min_value} ({min_country})")

# Korelasyon matrisi
corr_matrix = numeric_df.corr()
print(corr_matrix)

# Heatmap oluşturma
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Scatter plot örneği
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Cost of Living Index', y='Rent Index', data=df)
plt.title('Cost of Living Index vs Rent Index')
plt.show()

# Bar grafiği örneği
plt.figure(figsize=(12, 8))
df_sorted = df.sort_values('Cost of Living Index', ascending=False)
sns.barplot(x='Cost of Living Index', y='Country', data=df_sorted)
plt.title('Cost of Living Index by Country')
plt.show()

# Trend analizi örneği
df_sorted = df.sort_values('Cost of Living Index', ascending=False)
plt.figure(figsize=(12, 8))
sns.lineplot(x='Country', y='Cost of Living Index', data=df_sorted)
plt.title('Cost of Living Index Trend by Country')
plt.xticks(rotation=90)
plt.show()
