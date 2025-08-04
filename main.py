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
        ukol = ukol.strip()
        popis = popis.strip()

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
            if isinstance(ukol, dict) and "název" in ukol and "popis" in ukol:
                nazev = ukol["název"]
                popis = ukol["popis"]
                print(f"{cislo}. {nazev} - {popis}")
            else:
                print(f"{cislo}. [Neplatný formát úkolu]")  
    except Exception as e:
        print(f"Chyba při zobrazování úkolů: {e}")  


def odstranit_ukol(seznam)-> list[dict]:
    """
    Ze seznamu slovníků odstraní slovník
    dle zadané hodnoty
    """
    zobrazit_ukol(seznam)
    print("_"*40)
    if seznam:
        odstraneni = input("Zadejte číslo úkolu, který chcete odstranit:  ").strip()
        if not odstraneni.isdigit():
            print("Neplatné číslo.")
            return seznam
        if len(odstraneni) > 4:
            print("Zadané číslo je příliš dlouhé.")
            return seznam
        index = int(odstraneni)
        if not (1 <= index <= len(seznam)):
            print("Zadané číslo není v seznamu.")
            return seznam
        ukol_data = seznam[index-1]
        if isinstance(ukol_data, dict) and "název" in ukol_data:
            nazev = ukol_data["název"]
        else:
            nazev = "[Neznámý úkol]"

        seznam.pop(index - 1)
        print(f"Úkol '{nazev}' byl odstraněn")
        return seznam
    return seznam


def nacist_predchozi_ukoly(soubor_json):
    if os.path.exists(soubor_json):
        try:
            with open(soubor_json, mode="r", encoding="utf-8") as json_seznam:
                data = json.load(json_seznam)
                if isinstance(data, list):
                    validni_data = []
                    for ukol in data:
                        if(isinstance(ukol, dict)
                           and "název" in ukol and isinstance(ukol["název"], str) and ukol["název"].strip()
                           and "popis" in ukol and isinstance(ukol["popis"], str) and ukol["popis"].strip()
                           ):
                            validni_data.append({"název": ukol["název"].strip(),
                                                 "popis": ukol["popis"].strip()
                                                 })
                        else:
                            print("Varování: Jeden z úkolů má neplatnou strukturu a bude přeskočen.")
                    return validni_data
                else:
                    print("Neplatná struktura dat (není to seznam).")
        except Exception as e:
            print(f"Chyba - {e} při načítání úkolů.")
    return []


def zapsat_do_souboru(seznam, soubor_json):
    try:
        with open(soubor_json, mode="w", encoding="utf-8") as json_seznam:
            json.dump(seznam, json_seznam, ensure_ascii=False)
    except Exception as e:
        print(f"Chyba - {e} při zápisu do souboru.")


def zpracovat_volbu(volba: int, ukoly: list, ukoly_json: str) -> list:
    if volba == 1:
        ukol = input("Zadejte název úkolu - max. 100 znaků:  ")
        popis = input("Zadejte popis úkolu:  ")
        pridat_ukol(ukoly, ukol, popis)
        zapsat_do_souboru(ukoly,ukoly_json)
    elif volba == 2:
        zobrazit_ukol(ukoly)
    elif volba == 3:
        ukoly = odstranit_ukol(ukoly)
        zapsat_do_souboru(ukoly, ukoly_json)
    elif volba == 4:
        print("Konec programu.")
    return ukoly


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
        vyber = input("Vyberte možnost (1 - 4):  ").strip()
        print(oddelovac)    
            
        if not vyber.isdigit() or int(vyber) not in range(1,5): 
            print("Neplatná volba")
            continue

        volba = int(vyber)
        ukoly = zpracovat_volbu(volba, ukoly, ukoly_json)
        if volba == 4:
            print(oddelovac)
            break   
        
  

if __name__ == "__main__":
    hlavni_menu()
