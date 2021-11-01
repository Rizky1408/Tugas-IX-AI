def hitungJarakSebenar(skala, jarakPeta):
    jarakSebenar = jarakPeta * (skala / 100000)
    jarakSebenar = jarakSebenar / 100000
    
    return jarakSebenar

def hitungSkala(jarakSebenar, jarakPeta):
    skala = float(jarakSebenar * 100000) / jarakPeta
    
    return skala

# Main
print("1.Hitung Skala")
print("2. Hitung Jarak Sebenarnya")
print("3. Jarak Sesungguhnya")
pilihan = int(input("Masukan Pilihan :"))

if pilihan == 1:
    print("Masukan Jarak peta :")
    jarakPeta = int(input())
    print("Masukan Jarak Sebenarnya(km) :")
    jarakSebenarnya = int(input())
    print("Skala adalah 1 : " + str(hitungSkala(jarakSebenarnya, jarakPeta)))

elif pilihan == 2:
        jarakPeta = int(input("Masukan Jarak Peta:"))
        skala = int(input("Masukan skala(dalam cm) :"))
        print("Jarak Sebenarnya : " + str(hitungJarakSebenar(skala, jarakPeta)) + " km")
    
elif pilihan == 3:
            jarakSebenarnya = int(input("Input ruas(ilustrasi JarakPeta) :"))
            jarakSebenarnya = 1 * jarakSebenarnya
            print("Jarak Sebenarnya : " + str(jarakSebenarnya) + " km")
