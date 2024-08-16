import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Natural Earth verilerini doğrudan internetten indir
url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
world = gpd.read_file(url)

# Yaşam maliyeti verilerini oku (CSV dosyasını uygun şekilde güncelleyin)
cost_of_living_data = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')

# Harita ve veri setini, ülkeleri birleştirerek bir araya getir
world = world.rename(columns={'ADMIN': 'Country'})
merged = world.set_index('Country').join(cost_of_living_data.set_index('Country'))

# Haritayı renklendir (Yaşam Maliyeti İndeksine göre)
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.plot(column='Cost of Living Index', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Başlık ekle
ax.set_title('World Map - Cost of Living Index', fontdict={'fontsize': 20}, loc='center')

# Göster
plt.show()
