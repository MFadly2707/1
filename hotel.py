# TRANSAKSI HOTEL MUHAMMAD FADLY EKA ARDIANSYAH
def garis():
    print("____________________________________________________________")
    print(" ")

all = True
while (all == True) :
    garis()
    print("                 Program Menginap Di Hotel!                 ")
    print(" __________ _______________ _______________ _______________ ")
    print("|   Hari   |    Superior   |     Deluxe    |    Premium    |")
    print("|__________|_______________|_______________|_______________|")
    print("| 1-2 Hari | 100.000/night | 150.000/night | 200.000/night |")
    print("| 3-4 Hari | 90.000/night  | 135.000/night | 180.000/night |")
    print("| > 5 Hari | 80.000/night  | 120.000/night | 160.000/night |")
    print("|__________|_______________|_______________|_______________|")
    print("                                                            ")

    #input
    print ("Tipe kamar  ",  "\n 1.Superior", "\n 2.Deluxe" "\n 3.Premium")
    tipe_kamar = input("Pilih Tipe Kamar : ")
    lama_inap = int(input("Lama Menginap : "))
    
    #logika
    if (tipe_kamar =='1'):
        tipe_kamar = 'Superior'
        if lama_inap <= 2 :
            total_harga = 100000*lama_inap
        elif lama_inap <= 4 :
            total_harga = 90000*lama_inap
        elif lama_inap >= 5:
            total_harga = 80000*lama_inap

    elif (tipe_kamar =='2'):
        tipe_kamar = 'Deluxe'
        if lama_inap <= 2 :
            total_harga = 150000*lama_inap
        elif lama_inap <= 4 :
            total_harga = 135000*lama_inap
        elif lama_inap >= 5:
            total_harga = 120000*lama_inap

    elif (tipe_kamar =='3'):
        tipe_kamar = 'Premium'
        if lama_inap <= 2 :
            total_harga = 200000*lama_inap
        elif lama_inap <= 4 :
            total_harga = 180000*lama_inap
        elif lama_inap >= 5:
            total_harga = 160000*lama_inap

    #output
    print("                      ")
    print("===== Pembayaran =====")
    print("Tipe Kamar :", tipe_kamar)
    print("Lama Menginap :", lama_inap, "hari")
    print("Total Pembayaran : Rp.", total_harga)
    loop = input("Ingin Memesan Lagi? (y/n) : ")
    if (loop == 'n' ) :
        all = False