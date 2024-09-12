print("""
+-------------------+
| Azhar Rizki Zulma |
|      Bintaro      |
+-------------------+
|      Program      |
|   Konversi Suhu   |
+-------------------+
| 1. C to F         |
| 2. C to K         |
| 3. F to C         |
| 4. F to K         |
| 5. K to C         |
| 6. K to F         |
+-------------------+
""")

g_int_menu = int(input("Masukkan Menu (1-6): "))

if ( g_int_menu == 1 ):
    g_flt_degree = float(input("Masukkan Suhu dalam Celsius: "))
    g_flt_convertDegree = ( ( g_flt_degree * 9 ) / 5 ) + 32
    print( str(g_flt_degree) + "°C sama dengan " + str(g_flt_convertDegree) + "°F")
elif ( g_int_menu == 2 ):
    g_flt_degree = float(input("Masukkan Suhu dalam Celsius: "))
    g_flt_convertDegree = g_flt_degree + 273.15
    print( str(g_flt_degree) + "°C sama dengan " + str(g_flt_convertDegree) + " K")
elif ( g_int_menu == 3 ):
    g_flt_degree = float(input("Masukkan Suhu dalam Fahrenheit: "))
    g_flt_convertDegree = ( ( g_flt_degree - 32 ) * 5 )/ 9
    print( str(g_flt_degree) + "°F sama dengan " + str(g_flt_convertDegree) + "°C")
elif ( g_int_menu == 4 ):
    g_flt_degree = float(input("Masukkan Suhu dalam Fahrenheit: "))
    g_flt_convertDegree = ( ( ( g_flt_degree - 32 ) * 5 )/ 9 ) + 273.15
    print( str(g_flt_degree) + "°F sama dengan " + str(g_flt_convertDegree) + " K")
elif ( g_int_menu == 5 ):
    g_flt_degree = float(input("Masukkan Suhu dalam Kelvin: "))
    g_flt_convertDegree = g_flt_degree - 273.15
    print( str(g_flt_degree) + " K sama dengan " + str(g_flt_convertDegree) + "°C")
elif ( g_int_menu == 6 ):
    g_flt_degree = float(input("Masukkan Suhu dalam Kelvin: "))
    g_flt_convertDegree = ( ( ( g_flt_degree - 273.15 ) * 9 ) / 5 ) + 32
    print( str(g_flt_degree) + " K sama dengan " + str(g_flt_convertDegree) + "°F")
else:
    print("Masukkan Menu yang Valid")
