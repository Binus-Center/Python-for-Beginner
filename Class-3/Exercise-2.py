print("""
+-------------------+
| Azhar Rizki Zulma |
|      Bintaro      |
+-------------------+
|      Program      |
|   Kategori Umur   |
+-------------------+
""")

g_int_umur = int(input("Masukkan Umur: "))

if ( g_int_umur > 0 ):
    if ( ( g_int_umur >= 0 )
     and ( g_int_umur <  2 ) ):
        print("Ini merupakan Bayi")
    elif ( ( g_int_umur >= 2 )
       and ( g_int_umur <  4 ) ):
        print("Ini merupakan Batita")
    elif ( ( g_int_umur >= 4 )
       and ( g_int_umur <  6 ) ):
        print("Ini merupakan Balita")
    elif ( ( g_int_umur >= 6 )
       and ( g_int_umur <  13 ) ):
        print("Ini merupakan Anak-anak")
    elif ( ( g_int_umur >= 13 )
       and ( g_int_umur <  18 ) ):
        print("Ini merupakan Remaja")
    elif ( ( g_int_umur >= 18 )
       and ( g_int_umur <  22 ) ):
        print("Ini merupakan ABG")
    elif ( ( g_int_umur >= 22 )
       and ( g_int_umur <  31 ) ):
        print("Ini merupakan Pra Dewasa")
    elif ( ( g_int_umur >= 31 )
       and ( g_int_umur <  51 ) ):
        print("Ini merupakan Dewasa")
    elif ( ( g_int_umur >= 51 )
       and ( g_int_umur <  71 ) ):
        print("Ini merupakan Pra Lansia")
    elif ( ( g_int_umur >= 71 )
       and ( g_int_umur <  121 ) ):
        print("Ini merupakan Lansia")
    else:
        print("Anda Sepuh, karena mustahil manusia punya umur diatas 121 tahun")
else:
    print("Tidak ada umur yang negatif")
