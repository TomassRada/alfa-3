Instalace:
naistalujte si alpha3.zip, poté ho rozbalte do dávmi určené složky. Ujistěte si že máte naistalovaný python3.

Konfigurace:
aplikace se konfiguruje ve složce config v souboru conf.yaml. konfigurovat se dá připojení do databáze(hostname,username,password,databasename).  

Spuštění:
ve složce src, klinkněte na soubor main pravým tlačítkem, poté otevřít v programu a vybrete python3, otevře se vám console s menu.
 
Aplikace se ovládá klávesnicí pomocí textového menu.
Menu:
1. Vytvoření nového produktu (vytvoří nový produkt s hodnotami z klavesnice)
2. Update produktu (upraví produkt podle hodnot zadaných z klávesnice)
3. Smazaní produktu (smaže produkt s id zaného z klávesnice)
4. Transkace (provede transkaci: vytvoří novou objednávku a odebere ze skladu)
5. Souhrný report (vypíše report: počet prodaných kol podle typu,tržbu podle adressy a prumernou váhu podle velikosti)
6. Import dat do tabulky zakaznik (importuje data do tabulky ze souboru) 
7. Import dat do tabulky produkt (importuje data do tabulky ze souboru) 
8. Terminate Program (ukončí program) 

Po zadání daného číšla a entru aplikace provede daný ukon.
Pokud zadaná hodnota není platná program vás požádá o znovu zadaní.
Program ukončíte klávesou 8
