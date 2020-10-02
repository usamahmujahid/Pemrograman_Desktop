def ui(nilai):
    nilai.sort()
    print("Nilai: ", nilai)
#___RATA-RATA (MEAN)___#
    mean = sum(nilai) / len(nilai)
    print("\nRata-Rata (mean): ", mean)
#___NILAI TENGAH (MEDIAN)___#
    total=0
    x = len(nilai) // 2
    if len(nilai) % 2 == 1:
        print("Nilai Tengah (median): ", nilai[x])
    else: 
        total = (nilai[x] + nilai[x-1]) / 2
        print("Nilai Tengah (median): ", total)
#___FREKUENSI TERBANYAK (MODUS)___#
    cost=[]
    i=0
    while i < len(nilai) : 
        cost.append(nilai.count(nilai[i])) 
        i += 1
    d1 = dict(zip(nilai, cost)) 
    d2 = {k for (k,v) in d1.items() if v == max(cost) }
    print("frekuensi terbanyak (modus): " + str(d2))
nilai = [11, 10, 101, 57, 32, 32, 32]
ui(nilai)
