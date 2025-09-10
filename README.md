# Анализ данных о поездках Uber

### Импорт библиотеки pandas
```import pandas as pd```

## Шаг 1: Загрузка и первичный осмотр данных

1. Загружаем датасет ```ncr_ride_bookings.csv``` в DataFrame ```df```

```df = pd.read_csv('ncr_ride_bookings.csv')```

2. Выводим первые 5 строк датасета

```print (df.head())```

#### Вывод:
<img width="666" height="231" alt="image" src="https://github.com/user-attachments/assets/42724f64-4d4f-4f02-8552-d1373d190a87" />

3. Далее выводим общую информацию о датасете (количество записей, количесвто столбцов, типы данных, количесвто недопустимых значений)
```print(df.info())```

#### Вывод: 

<img width="770" height="799" alt="image" src="https://github.com/user-attachments/assets/50e0d528-c412-495f-bf94-923813b2f0d8" />

4. Выводим статистическое описание числовых столбцов датасета

```print(df.describe())```

#### Вывод: 

<img width="806" height="315" alt="image" src="https://github.com/user-attachments/assets/d7552fab-2112-4384-8f11-ad71ba90acaa" />

5. Определяем количество строк и столбцов в датасете

```print(f"Количество строк и столбцов: {df.shape}")```

#### Вывод:

<img width="421" height="43" alt="image" src="https://github.com/user-attachments/assets/ff21f56c-150d-411e-ae42-61e485629f51" />

## Шаг 3: Выборка и фильтрация данных

1. Выбрал только столбцы ```Booking ID```, ```booking_datetime```, ```Booking Status```, ```Vehicle Type```, ```Payment Method``` и вывел первые 5 строк

```
df['booking_datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
selected_columns = df[['Booking ID', 'booking_datetime', 'Booking Status', 'Vehicle Type', 'Payment Method']]
print(selected_columns.head())
```

#### Вывод:

<img width="763" height="223" alt="image" src="https://github.com/user-attachments/assets/e54501ef-1271-4b18-9969-fb365575fcc0" />

2. Отфильтровать и вывести все бронирования, которые имеют статус "Cancelled by Driver"

```
cancelled_by_driver = df[df['Booking Status'] == 'Cancelled by Driver']
print(cancelled_by_driver)
```

#### Вывод: 

<img width="696" height="391" alt="image" src="https://github.com/user-attachments/assets/9e37055c-2556-4998-8150-bc6eb58ad9b8" />

3. Отфильтровать и вывести все бронирования, выполненные с использованием ```Vehicle Type``` "Auto", иимеющие ```Booking Value``` более 500

```
auto_high_value = df[(df['Vehicle Type'] == 'Auto') & (df['Booking Value'] > 500)]
print(auto_high_value)
```

#### Вывод: 

<img width="714" height="406" alt="image" src="https://github.com/user-attachments/assets/c2c27b8d-a8a0-4de2-817e-b12c50760b5a" />

4. Отфильтровать и вывести все бронирования, которые были сделаны с ```2024-03-01``` по ```2024-03-31``` включительно

```
start_date = '2024-03-01'
end_date = '2024-03-31'
march_2024_bookings = df[(df['booking_datetime'] >= start_date) & (df['booking_datetime'] <= end_date)]
print(march_2024_bookings)
```

#### Вывод: 

<img width="728" height="399" alt="image" src="https://github.com/user-attachments/assets/c598bd45-c436-4f42-a475-a8462e084f20" />
