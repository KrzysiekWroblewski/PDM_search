def znajdz_indeks(lista, szukany_element):
    for indeks, element in enumerate(lista):
        if element in szukany_element:
            return indeks
    return -1  # zwracamy -1, jeśli element nie został znaleziony


# Przykładowa lista stringów
lista_stringow = ["abc", "def", "aaa", "ghi", "aaa", "jkl"]

# Wywołanie funkcji
indeks = znajdz_indeks(lista_stringow, "aaa")

if indeks != -1:
    print(f"Indeks, na ktorym znajduje sie 'aaa': {indeks}")
else:
    print("'aaa' nie zostało znalezione w liscie.")
