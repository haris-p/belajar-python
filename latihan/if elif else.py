ipk = 0
counter = 0
n = float(input("masukan batas matkul: "))

while counter <= n-1:
    nilai = float(input("Nilai makul ke - {} :".format(counter)))
    if nilai >= 85:
        ipk += 4
    elif nilai >= 70 and nilai < 85:
        ipk += 3
    elif niali >= 60 and nilai < 70:
        ipk += 2
    elif nilai >= 50 and nilai < 60:
        ipk = ipk+1
    counter = counter+1

print("ipk :", ipk/counter)