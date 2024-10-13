import csv

# Открываем CSV-файл
with open('divanpars\divanpars\spiders\svet.csv', 'r') as csvfile:
    # Создаем объект чтения CSV-файла
    csvreader = csv.reader(csvfile)
    
    # Пропускаем заголовок
    next(csvreader)
    
    # Создаем новый список для записи преобразованных данных
    new_data = []
    
    # Проходим по каждой строке в CSV-файле
    for row in csvreader:
        # Преобразуем цену в числовой формат
        price = float(row[1].replace(' ', ''))
        
        # Создаем новую строку с преобразованной ценой
        new_row = [row[0], price, row[2]]
        
        # Добавляем новую строку в список
        new_data.append(new_row)
    
    # Записываем новые данные в CSV-файл
    with open('svet_prices_updated.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['name', 'price', 'url'])
        csvwriter.writerows(new_data)