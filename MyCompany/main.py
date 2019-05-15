from MyCompany.PurchaseList import PurchaseList
from MyCompany.Event import Event
import os
from MyCompany.Product import Product

if __name__ == "__main__":
    pl = PurchaseList(Event.Kolacja, 10, 15, 20)
    pl.generateList()
    pl.printAllProducts()
    script_dir = "../produkty.txt"  # <-- absolute dir the script is in

    pl.readProductsFromFile(script_dir)
    pl.printAllAviableProducts()