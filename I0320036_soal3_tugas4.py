#Berat bagasi maksimal
beratmaks_lbs = 50
beratmaks_kg = beratmaks_lbs*0.453592

#Berat bagasi lebih dari 110 kg
berat1 = 110
izin = beratmaks_kg > berat1
print(izin)

#Berat bagasi 49 kg
berat2 = 49
izin = beratmaks_kg > berat2
print(izin)