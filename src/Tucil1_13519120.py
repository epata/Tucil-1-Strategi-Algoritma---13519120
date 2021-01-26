# Nama			: Epata Tuah			   
# NIM			: 13519120			   
# Kelas			: K-03                             
# Mata Kuliah	: Strategi Algoritma               
# Deskripsi		: TUGAS KECIL 1 (merancang algoritma Brute Force pada puzzle Cryptarithmetic)                              

#import library time untuk menghitung waktu yang diperlukan algoritma Brute Force untuk menemukan solusi
import time

#FUNGSI-FUNGSI TAMBAHAN
#Fungsi mengukur panjang dari string
def panjang(string): 
    hitung = 0
    for i in string: 
        hitung+= 1
    return(hitung) 

#fungsi cacahSatuSatu mencacah array string berdasarkan indeksnya, berupa tuple [(indeks,string),...]
def CacahSatuSatu(string,x=0):
	return [(x+i, string[i]) for i in range(panjang(string))]

#Fungsi kombinasi (digunakan sebagai fungsi bantuan pada fungsi permutasi)
def Kombinasi(string, r):
    if not r:
        yield ''
    elif string:
        for i in Kombinasi(string[1:], r-1):
            yield string[0] + i
        yield from Kombinasi(string[1:], r)

#Fungsi permutasi
def Permutasi(string, r):
    if not r:
        yield ''
    else:
        for hasil in Kombinasi(string, r):
            for i, huruf in CacahSatuSatu(hasil):
                total = hasil[:i] + hasil[i+1:] 
                for j in Permutasi(total, r-1):
                    yield huruf + j

#Fungsi UbahKeList mengubah string menjadi list
def UbahKeList(Kata):
	x = []
	for i in Kata:
		x+=i
	return(x)

#Fungsi GantiKarakter mengganti karakter spesifik pada string
def GantiKarakter(Kata,char1,char2):
    kataBaru = ''
    for i in Kata:
        if (i!=char1):
            kataBaru+=i
        else:
            kataBaru+=char2
    return(kataBaru)

#Fungsi ListHurufKata menjadikan list Kata tersebut terdiri dari
#kata-kata yang unik/berbeda
def ListHurufKata(Kata) :
    x = [] 
    for i in Kata:
        if not i in x:
            x+=i
    return(x)

#Prosedur UbahListAngka berfungsi mengisi elemen listAngka dengan
#elemen listArray berdasarkan range listKata dan listKataUnik 
def UbahListAngka(listKata,listKataUnik,listAngka,listArray):
	for i in range(panjang(listKataUnik)):
		for j in range(panjang(listKata)):
			if (listKata[j]==listKataUnik[i]):
				listAngka[j] = listArray[i]

def CekBeradaDiIndeksAwal(array,angka,listKataUnik,listHurufAwal):
	valid = False
	hitungIndeks = 0
	for i in range(panjang(listKataUnik)):
		for j in range(panjang(listHurufAwal)):
			if (listKataUnik[i]==listHurufAwal[j]):
				hitungIndeks +=1
	listSama = [0 for i in range(hitungIndeks)]
	k = 0
	for i in range(panjang(listKataUnik)):
		for j in range(panjang(listHurufAwal)):
			if (listKataUnik[i]==listHurufAwal[j]):
				listSama[k] = i
				k+=1
	for indeks in listSama:
		if (array[indeks]==angka):
			valid = True
	return(valid)

#Fungsi mencari nilai maksimum dari array
def maksimum(array):

    if (panjang(array) == 0):
        return 0

    maks = array[0]

    for i in array:
        if (i>maks):
            maks = i

    return(maks)

#PROGRAM DIMULAI
#Input awal
print("Silahkan cek daftar file teks yang ada di folder directory ../test")
inputAwal = str(input("Ketik nama file yang ingin dites (misal 'test1' tanpa tanda petik): "))
fname = "../test/" + inputAwal + ".txt"
#Membuka file
f = open(fname,'r')
mulai = time.process_time() #Waktu dihitung mulai dari line ini
content = f.readlines()
panjangContentAwal = panjang(content)
for i in range(panjangContentAwal):
    content[i] = GantiKarakter(content[i],'\n','') #menganti karakter newline '\n' dengan ''
    print(content[i]) #output isi file
print('')
blankspace = chr(32) #agar spasi (blankspace) dapat diabaikan
old = ['+',blankspace,'-']
new = ['','','']
for i in range(panjang(content)):
	for j in range(panjang(old)):
		content[i] = GantiKarakter(content[i],old[j],new[j]) #menghapus karakter yang tidak penting
del content[-2] #menghapus content ke-2 terakhir (hanya berisi array '', agar tidak redundant)

#menyatukan semua kata yang ada di array content
#contoh:['SEND','MORE','MONEY'] menjadi 'SENDMOREMONEY'
Kata = content[0]
for i in range(1,panjang(content)):
	Kata = Kata+content[i]

#Mengisi huruf awal setiap kata pada array listHurufAwal
listHurufAwal = ['*' for i in range(panjang(content))]
for i in range(panjang(content)):
	listHurufAwal[i] = UbahKeList(content[i])[0]
listHurufAwal = ListHurufKata(listHurufAwal) #menjadikan isi array unik

#Mencari length kata terpanjang
listPanjang = [0 for i in range(panjang(content))]
for i in range(panjang(content)):
	listPanjang[i] = panjang(content[i])
kataTerpanjang = maksimum(listPanjang)

#INISIALISASI LIST
#list kata lengkap, contoh: ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'E', 'M', 'O', 'N', 'E', 'Y']
listKata = UbahKeList(Kata)

#list kata unik, contoh: ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
listKataUnik = ListHurufKata(listKata)

#list angka kosong, akan diisi dengan list angka permutasi
#contoh: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
listAngka = [0 for i in range(panjang(UbahKeList(Kata)))]

#list indeks, digunakan untuk indeks listAngka yang akan disesuaikan
#dengan operand ke berapa atau hasil
#contoh: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listIndeks = [0 for i in range(panjang(UbahKeList(Kata)))]
for i in range(panjang(listIndeks)):
	listIndeks[i] = i

#ALGORITMA DIMULAI
nilaiPermutasi = Permutasi('0123456789',panjang(listKataUnik))
hitungPercobaan = 0
jumlahSolusi = 0
for angka in nilaiPermutasi:
	hitungPercobaan+=1
	array = [int(x) for x in angka]
	#Cek apakah terdapat huruf awal kata bernilai nol. Jika ada skip ke array permutasi selanjutnya
	if (CekBeradaDiIndeksAwal(array,0,listKataUnik,listHurufAwal)==True):
		continue
	else:
                #mengubah listAngka dengan elemen array sesuai range listKata dan listKataUnik
		UbahListAngka(listKata,listKataUnik,listAngka,array)
		operand = ['' for i in range(panjang(content))] #inisialisasi awal array operand
		count = 0
		#menghasilkan operand-operand sebanyak isi array content
		for i in range(panjang(content)):
			for j in range(panjang(content[i])):
				if (i==0):
					operand[i]+= str(listAngka[j])
				else:
					operand[i]+=str(listAngka[j+count])
			count+=panjang(content[i])
		#menjumlahkan operand-operand
		hasil = int(operand[0]) 
		for i in range(1,panjang(content)-1):
			hasil+= int(operand[i])
		#jika angka terakhir tidak sesuai dengan penjumlahan operand-operandnya, skip ke array permutasi selanjutnya
		if (int(operand[panjang(content)-1])!=hasil):
			continue
		#jika hasil sesuai dengan penjumlahan operand-operandnya, cetak luaran sesuai ketentuan 
		else:
			jumlahSolusi+=1
			for i in range(panjang(content)-1):
				if (i==panjang(content)-2):
					print(str(f"{int(operand[i]):>{kataTerpanjang}}")+'+')
				else:
					print(str(f"{int(operand[i]):>{kataTerpanjang}}"))
			print('------')
			print(str(f"{int(operand[panjang(content)-1]):>{kataTerpanjang}}"),'\n')
			if (jumlahSolusi>1):
				print("Waktu eksekusi saat menemukan solusi ke-",jumlahSolusi," : ",time.process_time() - mulai," detik")
				print("Jumlah total tes yang dilakukan pada solusi ke-",jumlahSolusi," : ",hitungPercobaan,'\n')
			else:	
				print("Waktu eksekusi saat menemukan solusi: ",time.process_time() - mulai," detik")
				print("Jumlah total tes yang dilakukan: ",hitungPercobaan,'\n')
print("Jumlah solusi yang ditemukan:", jumlahSolusi)
print("Waktu eksekusi hingga program berakhir: ",time.process_time()-mulai," detik")



