print("""
+-------------------+
| Azhar Rizki Zulma |
|      Bintaro      |
+-------------------+
|      Program      |
|   Ganjil/Genap    |
+-------------------+
""")

g_int_nilai = int(input("Masukkan Nilai Bebas: "))

if ( ( g_int_nilai % 2 ) == 0 ):
    print("Merupakan Bilangan Genap")
else:
    print("Merupakan Bilangan Ganjil")
