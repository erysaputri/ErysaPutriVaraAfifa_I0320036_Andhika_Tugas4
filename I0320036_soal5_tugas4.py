s = "Hey there! What should this string be?"

#Panjangnya harusnya 20
s = s[:20]
print("Panjang dari s = %d" % len(s),'\n')

#Huruf pertama 'a' harusnya di index nomor 8
s = s.replace("there","thera")
print("Kemunculan pertama a = %d" % s.index("a"),'\n')

#Jumlah huruf a harusnya 2
print("a muncul sebanyak %d kali" % s.count("a"),'\n')

#Memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" %s[:5])           #Start to 5
print("Lima karakter berikutnya adalah '%s'" %s[5:10])      #5 to 10
print("Karakter ketiga belas adalah '%s'" %s[12])           #Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" %s[1::2]) #(0-based indexing)
print("Lima karakter terakhir adalah '%s'" %s[-5:],'\n')    #5th-from-last to end

#Konversikan ke upercase
print("String dalam huruf besar: %s" %s.upper(),'\n')

#Konversikan ke lowercase
print("String dalam huruf kecil: %s" %s.lower(),'\n')

#Cek bagaimana string itu dimulai
s = s.replace ("Hey","Str")
if s.startswith("Str"):
    print("String dimulai dengan 'Str'. Good!",'\n')

#Cek bagaimana string itu diakhiri
s = s.replace("shou","ome!")
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!'. Good!",'\n')

#Pisahkan string menjadi tiga string yang terpisah,
#masing-masing hanya berisi satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))