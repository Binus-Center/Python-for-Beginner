g_flt_length = float(input("Masukkan Panjang: "))
g_flt_wide = float(input("Masukkan Lebar: "))
g_flt_height = float(input("Masukkan Tinggi: "))

g_flt_luas = g_flt_length * g_flt_wide

g_flt_vol = (1 * g_flt_luas * g_flt_height)/3

print("Luas Volume dari Limas Segiempat adalah " + str(g_flt_vol) + " m³")
