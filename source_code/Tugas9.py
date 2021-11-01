def hitungJarakSebenar(skala, jarakPeta):
    jarakSebenar = jarakPeta * skala
    
    return jarakSebenar

def hitungSkala(jarakSebenar, jarakPeta):
    skala = float(jarakSebenar) / jarakPeta
    
    return skala

# Main
print("1.Hitung Skala")
print("2. Hitung Jarak Sebenarnya")
print("3. Jarak Sesungguhnya")
pilihan = int(input("Masukan Pilihan :"))

if pilihan == 1:
    jarakPeta = 10
    jarakSebenarnya = 220 * 100000
    print("Skala adalah 1 : " + str(hitungSkala(jarakSebenarnya, jarakPeta)))

elif pilihan == 2:
        jarakPeta = 20
        skala = float(5000000) / 100000
        print("Jarak Sebenarnya : " + str(hitungJarakSebenar(skala, jarakPeta)) + " km")

elif pilihan == 3:
            jarakSebenarnya = 4 * 100000
            jarakSebenarnya = float(jarakSebenarnya) / 100000
            print("Jarak Sebenarnya : " + str(jarakSebenarnya) + " km")
