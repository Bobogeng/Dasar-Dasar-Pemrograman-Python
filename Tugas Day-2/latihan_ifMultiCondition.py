nama = "Budi Santoso"
matpel = "Matematika"
nilai = 59.99  # uji grade dengan IF Multi Kondisi
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai < 85):
    grade = "B"
elif(nilai >= 60 and nilai < 75):
    grade = "C"
elif(nilai >= 30 and nilai < 60):
    grade = "D"
else:
    grade = "E"
