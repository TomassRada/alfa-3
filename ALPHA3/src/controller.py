from model import Model 
from view import View

class Controller:
    """Trida Controller spojuje Modul s View"""
    def __init__(self):
        """
        konsturktor
        """
        self.model = Model()
        self.view = View(self)

    def add_produkt(self, jmeno,cena,vaha,velikost,typ,pocet):
        """
        metoda add_produkt 
        volá metodu add_produkt z modulu a show_add_produkt_success z view

        parametry: jmeno, cena, vaha, velikost, typ, pocet - novy zaznam do tabulky produkt
        """
        self.model.add_produkt(jmeno,cena,vaha,velikost,typ,pocet)
        produkty = self.model.select_produkt()
        self.view.show_add_produkt_success(produkty)

    def update_produkt(self, produkt_ID, jmeno, cena, vaha, velikost, typ):   
        """
        metoda update_produkt 
        volá metodu update_produkt z modulu a show_update_produkt_success z view

        parametry: produkt_ID, jmeno, cena, vaha, velikost, typ - nové hodnoty upravovaneho zaznamu
        """
        self.model.update_produkt(produkt_ID, jmeno, cena, vaha, velikost, typ)
        produkty = self.model.select_produkt()
        self.view.show_update_produkt_success(produkty)



    def delete_produkt(self, produkt_ID):
        """
        metoda delete_produkt 
        volá metodu delete_produkt z modulu a show_delete_produkt_success z view

        parametry: produkt_ID - id záznamu který se má vymazat
        """
        self.model.delete_produkt(produkt_ID)
        produkty = self.model.select_produkt()
        self.view.show_delete_produkt_success(produkty)


    def transakce(self):
        """
        metoda transakce
        vola metodu transkace z modulu a show_transakce_success z view 
        """
        self.model.transakce()
        objednavky = self.model.select_objednavka()
        self.view.show_transakce_success(objednavky)


    def print_report(self):
        """
        metoda print_report
        vola metodu print_report z modulu a show_report z view
        """
        produkty_prodane_tyl,trzba,prumerna_vaha  = self.model.print_report()
        self.view.show_report(produkty_prodane_tyl,trzba,prumerna_vaha)

    def import_zakaznik(self,file_path):
        """
        metoda import_zakaznik
        vola metodu import_zakaznik z modelu a show_import_zakaznik_success/error z view
        
        parametry: file_path - cesta k souboru ze kterého chceme číst
        """
        try:
            self.model.import_zakaznik(file_path)
            zakaznici = self.model.select_zakaznik()
            self.view.show_import_zakaznik_success(zakaznici)
        except Exception as e:
            self.view.show_import_error(e)

    def import_produkt(self, file_path):
        """
        metoda import_produkt
        vola metodu import_produkt z modelu a show_import_produkt_success/error z view
        
        parametry: file_path - cesta k souboru ze kterého chceme číst
        """
        try:
            self.model.import_produkt(file_path)
            produkty = self.model.select_produkt()
            self.view.show_import_produkt_success(produkty)
        except Exception as e:
            self.view.show_import_error(e)
            
    
    def terminate(self):
        """
        metoda terminate
        vypíše že se program ukončuje a ukončí hoS
        """
        self.view.show_terminate_message()
        exit()



