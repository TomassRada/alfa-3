import yaml
import os
import mysql.connector
import datetime
from mysql.connector import pooling
import csv
import json
import xml.etree.ElementTree as ET

#načítaní dat o připojení z konfiguračního souboru
root_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(root_path, "..", "config", "conf.yml")

with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

c_host = config['database_conn']['host']
c_user = config['database_conn']['user']
c_password = config['database_conn']['pass']
c_database = config['database_conn']['database']

class Model:
    """ Třída Model slouží k práci s databází"""

    def __init__(self):
        """
        Kontruktor, vytváří pool pro připojení do databáze
        """
        self.conn_pool = mysql.connector.pooling.MySQLConnectionPool(
                                                                    pool_name = "mypool",
                                                                    pool_size = 3,
                                                                    pool_reset_session = True,
                                                                    host= c_host,
                                                                    user= c_user,
                                                                    password= c_password,
                                                                    database= c_database)

    def add_produkt(self,jmeno,cena,vaha,velikost,typ,pocet):
        """
        metoda add_produkt
        provede insert nad tabulkou produkt

        paramerty: jmeno, cena, vaha, velikost, typ, pocet 
        """
        try:   
            sklad_ID = 1     
            #insert produktu
            query = "INSERT INTO Produkt (sklad_ID, jmeno, cena, vaha, velikost, typ) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (sklad_ID, jmeno, cena, vaha, velikost, typ )
            #conn pool a provedení sql
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, values)
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            cursor.close()
            conn.commit()
            conn.close()
    
    def update_produkt(self,produkt_ID, jmeno, cena, vaha, velikost, typ):
        """
        metoda update_produkt
        provede update nad tabulkou produkt 

        paremetry: produkt_id, jmeno, cena, vaha, velikost, typ
        """
        try:
            sklad_ID = 1
            #update produktu
            query = "UPDATE Produkt SET sklad_ID = %s, jmeno = %s, cena = %s, vaha = %s, velikost = %s, typ = %s WHERE ID = %s; "
            values = (sklad_ID, jmeno, cena, vaha, velikost, typ, produkt_ID)
            #conn pool a provedení sql 
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(query,values)
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            cursor.close()
            conn.commit()
            conn.close()

    def delete_produkt(self, produkt_ID):
        """
        metoda delete_produkt
        vymaže záznam z tabulky produkt

        parametry: produkt_id    
        """
        try:
            #sql
            query = "DELETE FROM produkt WHERE ID = %s;"
            values = (produkt_ID,)
            #conn pool
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(query,values)
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            cursor.close
            conn.commit()
            conn.close()




    def select_produkt(self):
        """
        metoda select_produkt
        provede select * z tabulky produkt

        returns: všechny záznamy z tabulky produkty
        """
        try:
            #conn pool
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            #sql 
            query = "SELECT * FROM produkt"
            cursor.execute(query)
            produkty = cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            cursor.close()
            conn.close()
        return produkty

    def select_zakaznik(self):
        """
        metoda select_zakaznik
        provede select * z tabulky zakaznik

        retruns: všechny záznamy z tabulky zakaznik
        """
        try:
            #conn pool
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            #sql
            query = "SELECT * FROM zakaznik"
            cursor.execute(query)
            zakaznici = cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            cursor.close()
            conn.close()
        return zakaznici

    def select_objednavka(self):
        """
        metoda select_objednavka
        provede select * z tabulky objednavka

        returns: všechny záznamy z tabulky objednavka
        """
        try:
            #conn pool
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            #sql
            query = "SELECT * FROM objednavka"
            cursor.execute(query)
            objednavky = cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            cursor.close()
            conn.close()
        return objednavky


    def transakce(self):
        """
        metoda transkace
        provede transakci, update tabulky sklad a insert do tabulky objednavka
        
        """
        try:
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            #transakce
            cursor.execute('START TRANSACTION')
            # Update tabulky Sklad
            cursor.execute("UPDATE Sklad SET pocet = pocet - 1 WHERE ID = 1")
            # Insert do tabulky Objednavka
            cursor.execute("INSERT INTO Objednavka (zakaznik_ID, produkt_ID, datum_objednavky, cena_objednavky) VALUES (1, 1, CURRENT_TIMESTAMP, (SELECT cena FROM Produkt WHERE ID = 1))")
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            conn.commit()
            cursor.close()

    def print_report(self):
        """
        metoda print_report
        provede selecty z tabulek produkt, objednavka a zakaznik

        returns: pocet prodanych kol podle typu, trzbu podle adresy, prumernou vahu podle velikosti
        """
        try:
            #conn
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            #počet prodaných kol podle typu
            cursor.execute("SELECT typ, COUNT(*) as 'pocet prodanych' FROM Produkt JOIN Objednavka ON Produkt.ID = Objednavka.produkt_ID GROUP BY typ")
            produkty_prodane_typ = cursor.fetchall()
            #tržba podle adressy
            cursor.execute("SELECT adresa, SUM(cena_objednavky) as 'celkova trzba' FROM Zakaznik JOIN Objednavka ON Zakaznik.ID = Objednavka.zakaznik_ID GROUP BY adresa")
            trzba = cursor.fetchall()
            #prumerná váha podle velikosti
            cursor.execute("SELECT velikost, AVG(vaha) as 'prumerna vaha' FROM Produkt GROUP BY velikost")
            prumerna_vaha = cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            conn.commit()
            cursor.close()
        return produkty_prodane_typ, trzba, prumerna_vaha

    def import_produkt(self, file_path):
        """
        metoda import_produkt
        provede insert dat ze souboru do tabulky produkt

        parametry: file_path - cesta k souboru ze kterého chceme číst
        """
        try:
            sklad_ID = 1
            #vytvoření conn pool
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            #sql statment
            sql = "INSERT INTO Produkt (sklad_ID, jmeno, cena, vaha, velikost, typ) VALUES (%s, %s, %s, %s, %s, %s)"
            #získání souborové přípony
            _, file_extension = os.path.splitext(file_path)
            file_format = file_extension[1:].lower() 
            #csv
            if file_format == "csv":
                with open(file_path, newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        values = (sklad_ID, row['jmeno'], row['cena'],row['vaha'], row['velikost'], row['typ'])
                        cursor.execute(sql, values)                    
            #xml
            elif file_format == "xml":
                tree = ET.parse(file_path)
                root = tree.getroot()
                for element in root.iter('produkt'):
                    values = (sklad_ID, element.findtext('jmeno'), element.findtext('cena'), element.findtext('vaha'), element.findtext('velikost'), element.findtext('typ'))
                    cursor.execute(sql, values)
            #json
            elif file_format == "json":
                with open(file_path) as file:
                    data = json.load(file)
                    for item in data:
                        values = (sklad_ID, item['jmeno'], item['cena'],item['vaha'], item['velikost'], item['typ'])
                        cursor.execute(sql, values)
            else:
                print("Invalid file format")
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            conn.commit()
            cursor.close()


    
    def import_zakaznik(self,file_path):
        """
        metoda import_zakaznik
        provede insert dat ze souboru do tabulky zakaznik
        
        parametry: file_path - cesta k souboru ze ktereho chceme cist
        """
        try:
            #conn pool
            conn = self.conn_pool.get_connection()
            cursor = conn.cursor()
            #sql statment
            sql = "INSERT INTO Zakaznik (jmeno, adresa, telefon, email) VALUES (%s, %s, %s, %s)"
            #získání souborové přípony
            _, file_extension = os.path.splitext(file_path)
            file_format = file_extension[1:].lower()  
            #csv
            if file_format == "csv":
                with open(file_path, newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        values = (row['jmeno'], row['adresa'], row['telefon'], row['email'])
                        cursor.execute(sql, values)
                        pass
            #xml       
            elif file_format == "xml":
                tree = ET.parse(file_path)
                root = tree.getroot()
                for element in root.iter():
                    values = (element.findtext('jmeno'), element.findtext('adresa'), element.findtext('telefon'), element.findtext('email'))
                    cursor.execute(sql, values)
                    pass
            #json    
            elif file_format == "json":
                with open(file_path) as file:
                    data = json.load(file)
                    for item in data:
                        values = (item['jmeno'], item['adresa'], item['telefon'], item['email'])
                        cursor.execute(sql, values)
                        pass
            else:
                print("Invalid file format")
        except mysql.connector.Error as e:
            print("Erorr: {}".format(e))
        finally:
            #conn close
            conn.commit()
            cursor.close()        