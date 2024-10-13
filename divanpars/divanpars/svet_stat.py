# import csv
import pandas as pd
import matplotlib.pyplot as plt

# Открываем обновленный CSV-файл
data = pd.read_csv('svet_prices_updated.csv')

# Расчет средней цены
mean_price = data['price'].mean()
print(f"Средняя цена: {mean_price:.2f}")

# Создание гистограммы
plt.figure(figsize=(10, 6))
data['price'].hist(bins=10, color='skyblue')

# Добавление вертикальной линии для средней цены
plt.axvline(mean_price, color='r', linestyle='--', label=f'Средняя цена светильника {int(mean_price)} руб. ')

plt.xlabel('Цена (рубли)')
plt.ylabel('Количество светильников')
plt.title('Гистограмма цен на светильники', fontsize=16, fontweight='bold', loc='center', color='black', pad=20)
plt.legend()
plt.show()