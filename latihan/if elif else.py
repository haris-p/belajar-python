uas = float(input("masukan nilai uas: "))
uts = float(input("masukan nilai uts: "))
tgs = float(input("masukan nilai tugas: "))
hdr = float(input("masukan nilai hadir: "))

na = (uas * 40)+(uts * 30)+(tgs * 20)+(hdr * 10)

if na >= 80:
    index = "A"
elif na >= 70:
    index = "B"
elif na >= 60:
    index = "C"
else:
    index = "tidak lulus"

print("nilai akhir anda: ",na)
print("nilai index anda: ",index)