def kelipatan4(bilangan):
    if bilangan % 4 == 0:
        return "bilangan kelipatan"
    
    return "bukan bilangan kelipatan"

nomor = int(input("Bilangan: "))

print(kelipatan4(nomor))