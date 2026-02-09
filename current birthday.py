#calcular edad del usuario con año, mes y dia de nacimiento y dias transcurridos en el año actual 
year = input("Please enter your year of birth: ")
year = int(year)

month = input("Please enter your month of birth (1-12): ")
month = int(month) 

day = input("Please enter your day of birth (1-31): ")
day = int(day)

current_day = 9
current_month = 2
current_year = 2026 

age = current_year - year 

# # dias vividos en el año actual 
# days_this_year = (current_month - 1) * 30 + current_day

# #dias desde cumpleaños hasta del año pasado (aprox) 
# days_since_birthday = (current_month - month) * 30 + (current_day - day)

# days_extra = days_this_year + days_since_birthday
# days_extra = days_extra / 365 

# print(f"Tienes {age} años y {days_extra} días vividos en el año actual.") 

