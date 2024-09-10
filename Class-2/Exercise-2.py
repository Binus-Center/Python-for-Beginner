PI = 3.14159265358979323846

g_int_radius = float(input("Masukkan Jari-jari: "))
g_flt_height = float(input("Masukkan Tinggi: "))

g_flt_vol = PI * (g_int_radius * g_int_radius) * g_flt_height

print("Luas Volume dari Tabung adalah " + str(g_flt_vol) + " m³")
