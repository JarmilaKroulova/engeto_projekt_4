"""
main.py: čtvrtý projekt do Engeto Online Python Akademie

author: Jarmila Kroulová
email: jarmilxxx@seznam.cz
""" 


import json
import os


def pridat_ukol(seznam, ukol, popis): 
    """
    Zapíše úkol do seznamu slovníků
    """ 
    try:
        if not ukol:
            print("Úkol nebyl zadán, opakujte prosím zadání úkolu.")
            return seznam
        if not popis:
            print("Popis nebyl zadán, opakujte prosím zadání úkolu.")
            return seznam
        if len(ukol) > 100:
            print("Úkol je moc dlouhý (max. 100 znaků).")
            return seznam
        seznam.append({"název": ukol, "popis": popis})
        print(f"Úkol {ukol} byl přidán.")
    except Exception as e:
        print(f"Chyba při zadání úkolu: {e}")
    return seznam


def zobrazit_ukol(seznam) -> list[dict]:
    """ 
    Zobrazí seznam slovníků ve formě
    číslo - název úkolu - popis úkolu
    """
    print("Seznam úkolů:")
    if not seznam:
        print("Žádné úkoly")
    try:
        for cislo, ukol in enumerate(seznam, start= 1):
            nazev = ukol["název"]
            popis = ukol["popis"]
            print(f"{cislo}. {nazev} - {popis}")  
    except TypeError:
        print("Zkuste to znovu.")  


def odstranit_ukol(seznam)-> list[dict]:
    """
    Ze seznamu slovníků odstraní slovník
    dle zadané hodnoty
    """
    zobrazit_ukol(seznam)
    print("_"*40)
    if seznam:
        odstraneni = input("Zadejte číslo úkolu, který chcete odstranit:  ")
        if not odstraneni.isnumeric():
            print("Neplatné číslo.")
            return seznam
        index = int(odstraneni)
        if not (1 <= index <= len(seznam)):
            print("Zadané číslo není v seznamu.")
            return seznam
        ukol = seznam[index-1]["název"]
        seznam.pop(index - 1)
        print(f"Úkol '{ukol}' byl odstraněn")
        return seznam


def nacist_predchozi_ukoly(seznam_json):
    if os.path.exists(seznam_json):
        try:
            with open(seznam_json, mode="r", encoding="utf-8") as json_seznam:
                data = json.load(json_seznam)
                if isinstance(data, list):
                    return data
                else:
                    print("Neplatná struktura dat.")
        except Exception as e:
            print(f"Chyba - {e} při načítání úkolů.")
    return []


def zapsat_do_souboru(seznam, seznam_json):
    try:
        with open(seznam_json, mode="w", encoding="utf-8") as json_seznam:
            json.dump(seznam, json_seznam, ensure_ascii=False)
    except Exception as e:
        print(f"Chyba - {e} při zápisu do souboru.")


def hlavni_menu():
    oddelovac = "_"*40
    ukoly_json = "seznam_ukolu.json"
    ukoly = nacist_predchozi_ukoly(ukoly_json)
    while True:
        print(oddelovac)
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
        print(oddelovac)    
            
        if not vyber.isnumeric(): 
            print("Neplatná volba")
            continue
        vyber = int(vyber)
        if vyber not in range(1,5):
            print("Neplatná volba")
            continue 
           
        if vyber == 1:
            ukol = input("Zadejte název úkolu - max. 100 znaků:  ")
            popis = input("Zadejte popis úkolu:  ")
            pridat_ukol(ukoly, ukol, popis)
            print(oddelovac)
            zapsat_do_souboru(ukoly,ukoly_json)
        elif vyber == 2:
            zobrazit_ukol(ukoly)
            print(oddelovac)
        elif vyber == 3:
            ukoly = odstranit_ukol(ukoly)
            print(oddelovac)
            zapsat_do_souboru(ukoly, ukoly_json)
        else:
            print("Konec programu.")
            print(oddelovac)
            break
  

if __name__ == "__main__":
    hlavni_menu()
