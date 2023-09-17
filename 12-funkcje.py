#Funkcje definiujemy za pomocą słowa def
countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)
#Słownik zawiera nazwy krajów (jako klucze) które mają przypisane krotki z
#nazwą stolicy oraz liczbą mieszkanóców kraju w milionach 

def show_country_info(country):
    country_information = countries_information.get(country)
#konsola wyświetla listę krajów, użytkownik podaje o jakim kraju chce
#wyświetlić informacje
#kraj który wybierze użytkownik jest zapisywany w zmiennej country_information
    print()
    print(country)
    print("---------")
    print("Stolica:" + country_information[0])
    print("Liczba mieszkańców (mln): " + str(country_information[1]))
for country in countries_information.keys():
    print(country)

country = input("Informacje o jakim kraju chcesz wyświetlić? ")
show_country_info(country)
