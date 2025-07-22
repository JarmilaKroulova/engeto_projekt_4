import json


def pridat_ukol(seznam): 
    """
    Zapíše úkol do seznamu slovníků
    """ 
    ukol = input("Zadejte název úkolu - max. 100 znaků:  ")
    popis = input("Zadejte popis úkolu:  ")
    try:
        if not ukol or not popis:
            print("Úkol nebo popis nebyl zadán, opakujte prosím zadání úkolu.")
            return seznam
        if not ukol.isalnum() or len(ukol) > 100:
            print("Úkol musí obsahovat pouze písmena a čísla (max. 100 znaků).")
            return seznam
        seznam.append({ukol: popis})
        print(f"Úkol {ukol} byl přidán.")
    except Exception as e:
        print(f"Chyba při zadání úkolu: {e}")
    return seznam


def zobrazit_ukol(seznam) -> list[dict]:
    """ 
    Zobrazí seznam slovníků ve formě
    číslo - klíč - hodnota
    """
    print("Seznam úkolů:")
    for cislo, ukol in enumerate(seznam, start= 1):
            for nazev, popis in ukol.items():
                print(f"{cislo}. {nazev} - {popis}")    


def odstranit_ukol(seznam)-> list[dict]:
    """
    Ze seznamu slovníků odstraní slovník
    dle zadané hodnoty
    """
    zobrazit_ukol(seznam)
    odstraneni = input("Zadejte číslo úkolu, který chcete odstranit:  ")
    if not odstraneni.isnumeric():
        print("Neplatné číslo.")
        return seznam
    index = int(odstraneni)
    if not (1 <= index <= len(seznam)):
        print("Zadané číslo není v seznamu.")
        return seznam
    seznam.pop(index - 1)
    print("Úkol byl odstraněn")
    return seznam

def zapsat_do_souboru(seznam):
    with open("seznam_ukolu.json", mode="w", encoding="utf-8") as json_seznam:
        json.dump(seznam, json_seznam, ensure_ascii=False)


def hlavni_menu():
    ukoly = []
    while True:
        print("""
            Správce úkolů - Hlavní menu
            ___________________________
            1. Přidat nový úkol
            2. Zobrazit všechny úkoly
            3. Odstranit úkol
            4. Konec programu
            ___________________________
            """)
        vyber = input("Vyberte možnost (1 - 4):  ")    
            
        if not vyber.isnumeric(): 
            print("Neplatná volba")
            continue
        vyber = int(vyber)
        if vyber not in range(1,5):
            print("Neplatná volba")
            continue 
           
        if vyber == 1:
            pridat_ukol(ukoly)
            zapsat_do_souboru(ukoly)
        elif vyber == 2:
            zobrazit_ukol(ukoly)
        elif vyber == 3:
            ukoly = odstranit_ukol(ukoly)
            zapsat_do_souboru(ukoly)
        else:
            print("Konec programu.")
            break
  

if __name__ == "__main__":
    hlavni_menu()
