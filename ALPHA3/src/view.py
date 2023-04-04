from prettytable import PrettyTable
import os

class View:
    """Třída View slouží k zobrazení user interface"""
    def __init__(self, controller):
        """
        
        """
        self.controller = controller
        self.options = {
            "1": self.controller.add_produkt,
            "2": self.controller.update_produkt,
            "3": self.controller.delete_produkt,
            "4": self.controller.transakce,
            "5": self.controller.print_report,
            "6": self.controller.import_zakaznik,
            "7": self.controller.import_produkt,
            "8": self.controller.terminate
        }

    def display_menu(self):
        """
        metoda display_menu
        vypíše do konzole menu pro praci s databazi
        """
        print("--------------------------------")
        print("Menu:")
        print("1. Vytvoření nového produktu")
        print("2. Update produktu")
        print("3. Smazaní produktu")
        print("4. Transkace")
        print("5. Souhrný report")
        print("6. Import dat do tabulky zakaznik")
        print("7. Import dat do tabulky produkt")
        print("8. Terminate Program")
        print("--------------------------------")

    def run(self):
        """
        metoda run
        spouští inteface
        """
        while True:
            self.display_menu()
            selection = input("Zadejte číslo požadované akce: ")
            try:
                action = self.options[selection]
                #1
                if action == self.controller.add_produkt:
                        while True:
                            jmeno = input("Zadejte jmeno: ")
                            if isinstance(jmeno, str):
                                break
                            print("Jmeno musí být string.")

                        while True:
                            cena = input("Zadejte cenu: ")
                            try:
                                cena = float(cena)
                                break
                            except ValueError:
                                print("Cena musí být float.")

                        while True:
                            vaha = input("Zadejte vahu: ")
                            try:
                                vaha = float(vaha)
                                break
                            except ValueError:
                                print("Vaha musí být float.")

                        while True:
                            velikost = input("Zadejte velikost: ")
                            if isinstance(velikost, str):
                                break
                            print("Velikost musí být string")

                        while True:
                            typ = input("Zadejte typ: ")
                            if isinstance(typ, str):
                                break
                            print("Typ musí být string.")

                        while True:
                            pocet = input("Zadejte pocet: ")
                            try:
                                pocet = int(pocet)
                                break
                            except ValueError:
                                print("Pocet musí být int.")

                        self.controller.add_produkt(jmeno, cena, vaha, velikost, typ, pocet)
                #2
                elif action == self.controller.update_produkt:
                        while True:
                            produkt_ID = input("Zadejte id produktu který checete upravit: ")
                            try:
                                produkt_ID = int(produkt_ID)
                                break
                            except ValueError:
                                print("Id musí být int.")
                        while True:
                            jmeno = input("Zadejte jmeno: ")
                            if isinstance(jmeno, str):
                                break
                            print("Jmeno must be a string, please try again.")

                        while True:
                            cena = input("Zadejte cena: ")
                            try:
                                cena = float(cena)
                                break
                            except ValueError:
                                print("Cena must be a float, please try again.")

                        while True:
                            vaha = input("Zadejte vaha: ")
                            try:
                                vaha = float(vaha)
                                break
                            except ValueError:
                                print("Vaha must be a float, please try again.")

                        while True:
                            velikost = input("Zadejte velikost: ")
                            if isinstance(velikost, str):
                                break
                            print("Velikost must be a string, please try again.")

                        while True:
                            typ = input("Zadejte typ: ")
                            if isinstance(typ, str):
                                break
                            print("Typ must be a string, please try again.")

                        self.controller.update_produkt(produkt_ID,jmeno, cena, vaha, velikost, typ)
                
                #3
                elif action == self.controller.delete_produkt:
                    while True:
                        id = int(input("Zadejte ID produktu který chcete vymazat: "))
                        if isinstance(id, int):
                            self.controller.delete_produkt(id)
                            break
                        else:
                            print("Musíte zadat číslo!")
                #6
                elif action == self.controller.import_zakaznik:                    
                    while True:
                        path = input("Zadejte název souboru s příponou (test.csv): ")
                        file_path = "C:\\Users\\Swagger\\Desktop\\ALPHA3\\import\\{}".format(path) 
                        if os.path.isfile(file_path):
                            self.controller.import_zakaznik(file_path)
                            break
                        else: 
                            print("Tento soubor nexistuje!")
                #7            
                elif action == self.controller.import_produkt:
                    while True:   
                        path = input("Zadejte název souboru s příponou (test.csv): ")
                        file_path = "C:\\Users\\Swagger\\Desktop\\ALPHA3\\import\\{}".format(path) 
                        if os.path.isfile(file_path):
                            self.controller.import_produkt(file_path)
                            break
                        else: 
                            print("Tento soubor nexistuje!")
                else:
                    action()

            except KeyError:
                print(f"Invalid selection: {selection}")
                print("Please try again")


    def show_transakce_success(self, objednavky):
        """
        metoda show_transkace_success
        vypise ze transkace proběhla + tabulku objednavky

        parametry: objednavky - data z tabulky objednavky 
        """
        print("Transkace byla provedna!")
        table = PrettyTable()
        table.field_names = ["ID", "zakaznik_ID", "produkt_ID", "datum_objednavky", "cena_objednavky"]
        for objednavka in objednavky:
            table.add_row(objednavka)
        print(table)


    def show_add_produkt_success(self, produkty):
        """
        metoda show_add_produkt_success
        vypíše že byl produkt přidán + tabulku produkt

        parametry: produkty - data z tabulky produkty
        """
        print("Produkt přidán!")
        table = PrettyTable()
        table.field_names = ["ID","sklad_ID","jmeno", "cena", "vaha", "velikost", "typ"]
        for produkt in produkty:
            table.add_row(produkt)
        print(table)

    def show_update_produkt_success(self, produkty):
        """
        metoda show_update_produkt_success
        vypíše že byl produkt upraven + tabulku produkt

        parametry: produkty - data z tabulky produkty
        """
        print("Produkt byl upraven!")
        table = PrettyTable()
        table.field_names = ["ID","sklad_ID","jmeno", "cena", "vaha", "velikost", "typ"]
        for produkt in produkty:
            table.add_row(produkt)
        print(table)

    def show_delete_produkt_success(self, produkty):
        """
        metoda show_delele_produkt_success
        vypíše že byl produkt odstraněn + tabulku produkt

        parametry: produkty - data z tabulky produkty
        """
        print("Produkt byl vymazán!")
        table = PrettyTable()
        table.field_names = ["ID","sklad_ID","jmeno", "cena", "vaha", "velikost", "typ"]
        for produkt in produkty:
            table.add_row(produkt)
        print(table)

    def show_report(self,produkty_prodane_typ,trzba,prumerna_vaha):
        """
        metoda show_report
        vypíše agregovane data ze 3 tabulek

        parametry: produkty_prodane_typ - pocet prodanych produktu podle typu, trzba - trzba podle adresy, prumerna_vaha - prumerna vaha podle typu kola
        """
        print("+----------REPORT------------+")
        #počet prodaných kol podle typu
        table = PrettyTable()
        table.field_names = ["typ","počet prodaných"]
        for produkt in produkty_prodane_typ:
            table.add_row(produkt)
        print(table)
        #tržba podle adressy
        table = PrettyTable()
        table.field_names = ["adressa","tržba"]
        for t in trzba:
            table.add_row(t)
        print(table)
        #prumerná váha podle velikosti
        table = PrettyTable()
        table.field_names = ["velikost","pruměrná váha"]
        for vaha in prumerna_vaha:
            table.add_row(vaha)
        print(table)

    def show_import_produkt_success(self, produkty):
        """
        metoda show_import_produkt_success
        vypíše že byl produkt importován ze souboru + tabulku produkt

        parametry: produkty - data z tabulky produkty
        """
        print("Data byla importována!")
        table = PrettyTable()
        table.field_names = ["ID","sklad_ID","jmeno", "cena", "vaha", "velikost", "typ"]
        for produkt in produkty:
            table.add_row(produkt)
        print(table)

    def show_import_zakaznik_success(self, zakaznici):
        """
        metoda show_import_zakaznik_success
        vypíše že byl zakaznik importován ze souboru + tabulku zakaznik

        parametry: zakaznici - data z tabulky zakaznik
        """
        print("Data byla importována!")
        table = PrettyTable()
        table.field_names = ["ID","jmeno","adresa","telefon","email"]
        for zakaznik in zakaznici:
            table.add_row(zakaznik)
        print(table)



    def show_import_error(self, error):
        """
        metoda show_import_error
        vypíše error, který nastal v průběhu importu

        parametry: error - error message 
        """
        print("An error occurred while importing the data:")
        print(error)

    def show_terminate_message():
        print("Program se ukončuje.")