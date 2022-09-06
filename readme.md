# Jak generovat kartičky

 - přihlásit se do teamup.com jako admin
 - kliknout na Nastavení
 - kliknout na Export událostí
 - nastavit formát exportu `.csv`
 - zaškrtnout `Exportovat unikátní identifikátor události`
 - nastavit pro `Více kalendářů na jednu událost`: `Jeden řádek`
 - vyexportovat soubor - bude s názvem `events-[digits].csv`
 - vyexportovat **druhý** soubor s nastavením exportu `Registrace k události`
 - oba soubory přesunout do složky `tables`
 - spustit skript `main.py`, nejspíš příkazem `python main.py` nebo něčím podobným
 - skript by neměl zfailit, hotová PDF jsou ve složce pdfOutput (přemazávají se, netřeba promazávat)

na další ročníky je třeba vždfy upravit:
 - v `Activity.py` mapu dní
 - poštelovat zaškrtnutí typu eventu a podle toho upravit kód (2021 měla typ, 2022 ne)