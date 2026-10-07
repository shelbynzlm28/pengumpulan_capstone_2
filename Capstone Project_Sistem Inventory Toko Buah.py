listDictBuah = [
    {"ID_Buah":"F001", "Batch":"B001", "nama":"Apel","tgl_datang":"13/09/2026", "Qty_datang":1, "Harga_Normal":10000},
    {"ID_Buah":"F002", "Batch":"B001", "nama":"Jeruk","tgl_datang":"13/09/2026", "Qty_datang":3, "Harga_Normal":15000},
    {"ID_Buah":"F003", "Batch":"B001", "nama":"Mangga","tgl_datang":"13/09/2026", "Qty_datang":3, "Harga_Normal":25000},
    {"ID_Buah":"F001", "Batch":"B002", "nama":"Apel","tgl_datang":"20/09/2026", "Qty_datang":5, "Harga_Normal":10000},
    {"ID_Buah":"F002", "Batch":"B002", "nama":"Jeruk","tgl_datang":"20/09/2026", "Qty_datang":10, "Harga_Normal":15000},
    {"ID_Buah":"F003", "Batch":"B002", "nama":"Mangga","tgl_datang":"20/09/2026", "Qty_datang":3, "Harga_Normal":25000},
    {"ID_Buah":"F001", "Batch":"B003", "nama":"Apel","tgl_datang":"28/09/2026", "Qty_datang":20, "Harga_Normal":10000},
    {"ID_Buah":"F002", "Batch":"B003", "nama":"Jeruk","tgl_datang":"28/09/2026", "Qty_datang":15, "Harga_Normal":15000},
    {"ID_Buah":"F003", "Batch":"B003", "nama":"Mangga","tgl_datang":"28/09/2026", "Qty_datang":25, "Harga_Normal":25000}]


from datetime import datetime, date
batas_segar = 10
batas_kurang_segar = 20

def Umur_Buah(tgl_datang):
    tgl_datang = datetime.strptime(tgl_datang,"%d/%m/%Y").date()
    umur_buah = (date.today() - tgl_datang).days
    return umur_buah
def Kondisi_Buah(umur_buah):
    if umur_buah <= batas_segar:
        return "Segar"
    elif umur_buah <= batas_kurang_segar:
        return "Kurang Segar"
    else:
        return "Busuk"
def diskon_buah(umur_buah):
    if umur_buah <= 10:
        diskon = 0
    elif 10 < umur_buah <= 15:
        diskon = 10
    elif 15 < umur_buah <= 20:
        diskon = 20
    else:
        diskon = 0
    return diskon
def Harga_Jual(harga_normal, diskon):
    harga_jual = harga_normal - (harga_normal * (diskon / 100))
    return harga_jual


def Tabel_Buah():
    print("\nTabel Master Buah\n")
    print("=" * 73)
    print("|Index\t|ID Buah|Nama Buah\t|Qty Stok (kg)\t|Harga Jual Normal\t|")
    print("=" * 73)

    buah_sudah_ditampilkan = []
    index = 0

    for data in listDictBuah:
        if data["ID_Buah"] not in buah_sudah_ditampilkan:
            total_qty = 0
            for data2 in listDictBuah:
                if data2["ID_Buah"] == data["ID_Buah"]:
                    total_qty += data2["Qty_datang"]

            umur_buah = Umur_Buah(data["tgl_datang"])
            diskon = diskon_buah(umur_buah)
            harga_jual = Harga_Jual(data["Harga_Normal"],diskon)

            print(
                f"|{index}"
                f"\t|{data['ID_Buah']:<5}"
                f"\t|{data['nama']}"
                f"\t\t|{total_qty}"
                f"\t\t|Rp{harga_jual:,.0f}"
                f"\t\t|")

            buah_sudah_ditampilkan.append(data["ID_Buah"])
            index += 1
    print("=" * 73)
def Tabel_Batch_Buah():
    print("\nTabel Batch Buah\n")

    print("Pilihan Tampilan:")
    print("1. Semua Batch")
    print("2. Berdasarkan ID Batch")
    print("3. Berdasarkan ID Buah")

    pilihan = input("Masukkan pilihan tampilan: ")
    if pilihan == "1":
        data_filter = listDictBuah.copy()
    elif pilihan == "2":
        id_batch = input("Masukkan ID Batch: ").capitalize()
        data_filter = []
        for data in listDictBuah:
            if data["Batch"] == id_batch:
                data_filter.append(data)
    elif pilihan == "3":
        id_buah = input("Masukkan ID Buah: ").capitalize()
        data_filter = []
        for data in listDictBuah:
            if data["ID_Buah"] == id_buah:
                data_filter.append(data)
    else:
        print("Pilihan tidak tersedia.")
        return

    if len(data_filter) == 0:
        print("Data tidak ditemukan.")
        return

    data_filter = sorted(data_filter,key=lambda x: x["nama"])

    print("\nTabel Data Buah\n")
    print("=" * 137)
    print(
        "|Batch\t|ID Buah|Nama Buah\t"
        "|Tanggal Datang\t|Qty Datang\t|Umur Buah\t"
        "|Kondisi Buah\t|Harga Normal\t|Diskon\t|Harga Jual\t|"
    )

    print("=" * 137)
    for i in range(len(data_filter)):
        umur_buah = Umur_Buah(data_filter[i]["tgl_datang"])
        kondisi_buah = Kondisi_Buah(umur_buah)
        diskon = diskon_buah(umur_buah)
        harga_jual = Harga_Jual(data_filter[i]["Harga_Normal"],diskon)
        print(
            f"|{data_filter[i]['Batch']:<5}"
            f"\t|{data_filter[i]['ID_Buah']:<5}"
            f"\t|{data_filter[i]['nama']}\t"
            f"\t|{data_filter[i]['tgl_datang']}"
            f"\t|{data_filter[i]['Qty_datang']}"
            f"\t\t|{umur_buah:>4} hari"
            f"\t|{kondisi_buah:<15}"
            f"|Rp{data_filter[i]['Harga_Normal']:,.0f}"
            f"\t|{diskon}%"
            f"\t|Rp{harga_jual:,.0f}"
            f"\t|")
    print("=" * 137)
def Menu_Read():
    while True:
            print("\n=== Tabel Data Buah ===")
            print("1. Master Data Buah")
            print("2. Data Buah Berdasarkan Batch")
            print("3. Kembali ke Menu Utama")
            pilihan = input("Masukkan pilihan: ")
            if pilihan == "1":
                Tabel_Buah()
            elif pilihan == "2":
                Tabel_Batch_Buah()
            elif pilihan == "3":
                return
            else:
                print("Pilihan tidak tersedia.")


def Tambah_Jenis_Buah():
    print("\nTambah Jenis Buah Baru")
    id_buah = input("Masukkan ID Buah: ").capitalize()
    for data in listDictBuah:
        if data["ID_Buah"] == id_buah:
            print("ID Buah sudah digunakan.")
            return
    nama_buah = input("Masukkan Nama Buah: ")

    data_baru = {
        "ID_Buah": id_buah,
        "Batch": "",
        "nama": nama_buah,
        "tgl_datang": "",
        "Qty_datang": 0,
        "Harga_Normal": 0
    }

    listDictBuah.append(data_baru)
    print("Jenis buah berhasil ditambahkan.")
def Tambah_Batch_Buah():
    print("\n=== Tambah Batch Buah Baru ===")
    id_batch = input("Masukkan ID Batch: ").capitalize()
    id_buah = input("Masukkan ID Buah: ").capitalize()
 
    buah_ditemukan = None
    for data in listDictBuah:
        if data["ID_Buah"] == id_buah:
            buah_ditemukan = data
            break

    if buah_ditemukan is None:
        print("ID Buah tidak ditemukan.")
        return

    nama_buah = buah_ditemukan["nama"]

    tgl_datang = input("Masukkan tanggal datang (DD/MM/YYYY): ")
    try:
        tanggal = datetime.strptime(
            tgl_datang,
            "%d/%m/%Y"
        ).date()
    except ValueError:
        print("Format tanggal tidak valid.")
        return

    if tanggal > date.today():
        print("Tanggal datang tidak boleh melebihi tanggal hari ini.")
        return

    qty_datang = float(input("Masukkan Qty datang (kg): "))
    harga_normal = int(input("Masukkan Harga Normal: "))

    data_baru = {
        "ID_Buah": id_buah,
        "Batch": id_batch,
        "nama": nama_buah,
        "tgl_datang": tgl_datang,
        "Qty_datang": qty_datang,
        "Harga_Normal": harga_normal
    }
    listDictBuah.append(data_baru)
    print("Batch buah berhasil ditambahkan.")
def Menu_Create():
    while True:
        print("\n=== Menambahkan Data Buah ===")
        print("1. Menambahkan Jenis Buah Baru")
        print("2. Menambahkan Batch Buah Baru")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            Tambah_Jenis_Buah()
        elif pilihan == "2":
            Tambah_Batch_Buah()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak tersedia.")


def Menu_Update():
    print("\n=== Edit Data Batch Buah ===")
    id_batch = input("Masukkan ID Batch: ").capitalize()
    id_buah = input("Masukkan ID Buah: ").capitalize()
    data_ditemukan = None
    for data in listDictBuah:
        if (data["Batch"] == id_batch and data["ID_Buah"] == id_buah):
            data_ditemukan = data
            break

    if data_ditemukan is None:
        print("Data batch tidak ditemukan.")
        return

    print("\nData ditemukan:")

    print("ID Buah       :", data_ditemukan["ID_Buah"])
    print("ID Batch      :", data_ditemukan["Batch"])
    print("Nama Buah     :", data_ditemukan["nama"])
    print("Tanggal Datang:", data_ditemukan["tgl_datang"])
    print("Qty Datang    :", data_ditemukan["Qty_datang"])
    print("Harga Normal  :", data_ditemukan["Harga_Normal"])

    print("\nKolom yang dapat diubah:")
    print("1. ID Batch")
    print("2. Tanggal Datang")
    print("3. Qty Datang")
    print("4. Harga Normal")

    pilihan = input("Masukkan kolom yang ingin diubah: ")

    if pilihan == "1":
        id_batch_baru = input("Masukkan ID Batch baru: ").capitalize()
        data_ditemukan["Batch"] = id_batch_baru

    elif pilihan == "2":
        tgl_baru = input("Masukkan tanggal baru (DD/MM/YYYY): ")
        try:
            tanggal = datetime.strptime(tgl_baru,"%d/%m/%Y").date()
        except ValueError:
            print("Format tanggal tidak valid.")
            return
        if tanggal > date.today():
            print("Tanggal tidak boleh melebihi hari ini.")
            return
        data_ditemukan["tgl_datang"] = tgl_baru

    elif pilihan == "3":
        qty_baru = float(input("Masukkan Qty baru: "))
        data_ditemukan["Qty_datang"] = qty_baru

    elif pilihan == "4":
        harga_baru = int(  input("Masukkan Harga Normal baru: "))
        data_ditemukan["Harga_Normal"] = harga_baru
    else:
        print("Pilihan tidak tersedia.")
        return
    print("Data berhasil diperbarui.")


def Hapus_Berdasarkan_Nama():
    print("\n=== Hapus Berdasarkan Nama Buah ===")
    nama_buah = input("Masukkan Nama Buah: ")
    data_ditemukan = []
    for data in listDictBuah:
        if data["nama"].lower() == nama_buah.lower():
            data_ditemukan.append(data)
    if len(data_ditemukan) == 0:
        print("Nama buah tidak ditemukan.")
        return
    print("\nData yang akan dihapus:")
    for data in data_ditemukan:
        print(
            data["Batch"],
            "|",
            data["ID_Buah"],
            "|",
            data["nama"],
            "|",
            data["Qty_datang"],
            "kg"
        )
    konfirmasi = input(
        "\nYakin ingin menghapus semua data buah ini? (y/n): "
    )

    if konfirmasi.lower() == "y":

        listDictBuah[:] = [
            data
            for data in listDictBuah
            if data["nama"].lower() != nama_buah.lower()
        ]
        print("Data buah berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
def Hapus_Berdasarkan_Batch():
    print("\n=== Hapus Berdasarkan Batch ===")
    id_batch = input("Masukkan ID Batch: ").capitalize()
    data_ditemukan = []
    for data in listDictBuah:
        if data["Batch"] == id_batch:

            data_ditemukan.append(data)
    if len(data_ditemukan) == 0:

        print("ID Batch tidak ditemukan.")
        return
    print("\nData yang akan dihapus:")
    for data in data_ditemukan:
        print(
            data["Batch"],
            "|",
            data["ID_Buah"],
            "|",
            data["nama"],
            "|",
            data["Qty_datang"],
            "kg"
        )
    konfirmasi = input(
        "\nYakin ingin menghapus batch ini? (y/n): "
    )

    if konfirmasi.lower() == "y":
        listDictBuah[:] = [
            data
            for data in listDictBuah
            if data["Batch"] != id_batch
        ]
        print("Batch berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
def Menu_Delete():
    while True:
        print("\n=== Hapus Data Buah ===")
        print("1. Hapus berdasarkan Nama Buah")
        print("2. Hapus berdasarkan ID Batch")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            Hapus_Berdasarkan_Nama()
        elif pilihan == "2":
            Hapus_Berdasarkan_Batch()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak tersedia.")


def Dashboard_Inventory():
    total_jenis = 0
    total_stok = 0
    stok_segar = 0
    stok_kurang_segar = 0
    stok_busuk = 0
    buah_sudah_dihitung = []
    for data in listDictBuah:
        if data["ID_Buah"] not in buah_sudah_dihitung:
            buah_sudah_dihitung.append(data["ID_Buah"])
            total_jenis += 1

        total_stok += data["Qty_datang"]

        umur_buah = Umur_Buah(data["tgl_datang"])
        kondisi = Kondisi_Buah(umur_buah)

        if kondisi == "Segar":
            stok_segar += data["Qty_datang"]
        elif kondisi == "Kurang Segar":
            stok_kurang_segar += data["Qty_datang"]
        elif kondisi == "Busuk":
            stok_busuk += data["Qty_datang"]

    print("\n=== DASHBOARD INVENTORY ===")
    print("-----------------------------")
    print("Total Jenis Buah :", total_jenis)
    print("Total Stok       :", total_stok, "kg")
    print("Stok Segar       :", stok_segar, "kg")
    print("Stok Kurang Segar:", stok_kurang_segar, "kg")
    print("Stok Busuk       :", stok_busuk, "kg")
    print("-----------------------------")
def Tabel_Stok_Buah():
    print("\n=== TABEL STOK BUAH ===")
    print("=" * 89)
    print(
        "|Index\t|Batch\t|ID Buah|Nama Buah\t"
        "|Qty Stok\t|Umur Buah\t|Kondisi\t|"
    )
    print("=" * 89)
    data_sorted = sorted(listDictBuah,key=lambda x: x["nama"])

    for i in range(len(data_sorted)):
        umur_buah = Umur_Buah(data_sorted[i]["tgl_datang"])
        kondisi = Kondisi_Buah(umur_buah)
        print(
            f"|{i}"
            f"\t|{data_sorted[i]['Batch']}"
            f"\t|{data_sorted[i]['ID_Buah']}"
            f"\t|{data_sorted[i]['nama']}\t"
            f"\t|{data_sorted[i]['Qty_datang']:>4} kg"
            f"\t|{umur_buah:>4} hari"
            f"\t|{kondisi:<15}"
            f"|"
        )
    print("=" * 89)
def Tabel_Kondisi_Buah():
    print("\n=== TABEL KONDISI BUAH ===")
    print("1. Buah Segar")
    print("2. Buah Kurang Segar")
    print("3. Buah Busuk")
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        kondisi_dicari = "Segar"
    elif pilihan == "2":
        kondisi_dicari = "Kurang Segar"
    elif pilihan == "3":
        kondisi_dicari = "Busuk"
    else:
        print("Pilihan tidak tersedia.")
        return

    print("\nData", kondisi_dicari)
    print("=" * 89)
    print(
        "|Index\t|Batch\t|ID Buah|Nama Buah\t"
        "|Qty Stok\t|Umur Buah\t|Kondisi\t|"
    )
    print("=" * 89)
    index = 0
    data_sorted = sorted(listDictBuah,key=lambda x: x["nama"])
    for data in data_sorted:
        umur_buah = Umur_Buah(data["tgl_datang"])
        kondisi = Kondisi_Buah(umur_buah)
        if kondisi == kondisi_dicari:
            print(
                f"|{index}"
                f"\t|{data['Batch']}"
                f"\t|{data['ID_Buah']}"
                f"\t|{data['nama']}\t"
                f"\t|{data['Qty_datang']:>4} kg"
                f"\t|{umur_buah:>4} hari"
                f"\t|{kondisi:<15}"
                f"|"
            )
            index += 1
    print("=" * 89)
def Menu_Laporan_Inventory():
    while True:
        print("\n=== LAPORAN INVENTORY BUAH ===")
        print("1. Dashboard")
        print("2. Tabel Stok Buah")
        print("3. Tabel Kondisi Buah")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            Dashboard_Inventory()
        elif pilihan == "2":
            Tabel_Stok_Buah()
        elif pilihan == "3":
            Tabel_Kondisi_Buah()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak tersedia.")


def Main_Menu():
    while True:
        pilihanMenu = input('''
Selamat datang di Sistem Inventory Toko Buah

List Menu :
1. Data Buah
2. Menambahkan Data Buah
3. Mengedit Data Buah
4. Menghapus Data Buah
5. Laporan Inventory Buah
6. Exit Program
Masukkan angka Menu yang ingin dijalankan :''') #input tampilan menu utama
    
        if pilihanMenu == "1":
            Menu_Read()
        elif pilihanMenu == "2":
            Menu_Create()
        elif pilihanMenu == "3":
            Menu_Update()
        elif pilihanMenu == "4":
            Menu_Delete()
        elif pilihanMenu == "5":
            Menu_Laporan_Inventory()
        elif pilihanMenu == "6":
            print("Terima kasih telah menggunakan sistem inventory.")
            break
        else:
            print("Menu tidak tersedia.")

Main_Menu()