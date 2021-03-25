#Memasukkan usia saat ini
usia = int(input("Berapa usia kamu? "))

#Pengujian
minimal_usia = 21
if minimal_usia <= usia:
    ujian_kualifikasi = input("Apakah anda sudah lulus ujian kualifikasi? (Y/T) ")
    if ujian_kualifikasi=="Y":
        print("Anda dapat mendaftar di kursus.")
    elif ujian_kualifikasi!="Y":
        print("Anda tidak dapat mendaftar di kursus.")
else:
    print("Anda tidak dapat mendaftar di kursus.")