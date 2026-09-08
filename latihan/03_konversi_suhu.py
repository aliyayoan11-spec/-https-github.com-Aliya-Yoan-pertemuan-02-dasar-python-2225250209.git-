# Program Konversi Suhu Celcius
celcius = float(input("Masukkan suhu dalam Celcius (°C): "))

fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15
reamur = celcius * 4/5

print("\n=== HASIL KONVERSI SUHU ===")
print("Fahrenheit :", fahrenheit, "°F")
print("Kelvin     :", kelvin, "K")
print("Reamur     :", reamur, "°R")