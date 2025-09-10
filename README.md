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

