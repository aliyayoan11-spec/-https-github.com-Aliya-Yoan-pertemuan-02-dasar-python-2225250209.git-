import math

# Program Kalkulator Jarak Dua Titik Koordinat
print("=== KALKULATOR JARAK KOORDINAT ===")
x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

# Menghitung jarak rumus Euclidean: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("\nJarak antara titik (", x1, ",", y1, ") dan (", x2, ",", y2, ") adalah:", jarak)