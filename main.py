import pandas as pd
#pd.set_option('display.width', None)

df = pd.read_csv('ncr_ride_bookings.csv')

print (df.head())

print(df.info())

print(df.describe())

print(f"Количество строк и столбцов: {df.shape}")

df['booking_datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
selected_columns = df[['Booking ID', 'booking_datetime', 'Booking Status', 'Vehicle Type', 'Payment Method']]
print(selected_columns.head())

cancelled_by_driver = df[df['Booking Status'] == 'Cancelled by Dr№iver']
print(cancelled_by_driver)

auto_high_value = df[(df['Vehicle Type'] == 'Auto') & (df['Booking Value'] > 500)]
print(auto_high_value)

#Задаем даты начала и конца периода
start_date = '2024-03-01'
end_date = '2024-03-31'
# Фильтруем
march_2024_bookings = df[(df['booking_datetime'] >= start_date) & (df['booking_datetime'] <= end_date)]
print(march_2024_bookings)

