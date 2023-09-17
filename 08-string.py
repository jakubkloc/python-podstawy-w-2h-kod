name = "kamil" #atring (zmienna tesktowa)
#print(len(name)) #len od lenght (długośc) zwaraca liczbe znakow (np dla kamil zwórci 5)
#obiekt string ma przypisane pewne metody
#motedy stosujemy podająć nazwę zmiennej . nazwę metody
#metody podobnie jak funkcje mogą przyjmować argumenty

#metoda capitalize (pierwsza litera słowa zostaje zmieniona na wileką litere) 
#print(name.capitalize()) #capitalize nie przyjmuje arguemntów dlatego pusty nawias ()   

##metoda upper (wszystkie litery w danym słowie zamieni na wielkie litery)
#print(name.upper()) 

#analogicznie lower (wszystkie litery zostaną zamienione na litery małe)
#print(name.lower()) 

#możena wyświetlać konkretne litery stringa
#w nawiasach kwadratowych [] odowłujemy się do konkretnej litery, pierwsza litera ma indeks 0
#print(name[0])
#Jeśli chcemy wyświetlić więcej liter to po dwukrupku podajemy liczbe liter
#print(name[0:2])
#Aby wyświetlić część wyrazu od konkretnej litery aż do końcam, wpisujemy numer litery i dwukropek : 
#print(name[3:])
#numer litery można także podać licząc od końca wyrazu wstawiając minus - przed numere litery
#print(name[-3:]) #pierwsza litera od końca ma indeks -1 a nie -0

#Dzielenie i łączenie wyrazów
#chanel = "Jak nauczyć się programowania"
#print(chanel.split(" ")) #podajemy metodę split, jako jej argument podając znak który będzie powodował rozdzielenie stringa

# join_string = "-" #definiujemy zmienną która zostanie wstawiona pomiędzy stringi
# print(join_string.join(['Jak', 'nauczyć','się','programowania'])) #jako argumenty podajemy stringi które mają zostać złączone za pomocą join_string

#sprawdzanie na jaką literę sie zaczyna
# print(name.endswith("K"))
# print(name.endswith("k"))
#wielkkość liter ma znaczenie
#zwraca zmienną bolean (True lub False)

#Analogicznie działa metoda endswith
# print(name.endswith("L"))
# print(name.endswith("l"))

#Usuwanie liter z końca i poczatku oraz usuwanie nadmiernych spacji
# print(name.strip()) 
#strip() usuwa spacje z początku i końca stringa 
#lstrip() usuwa spacje z lewej strony stringa
#rstrip() usuwa spacje z prawej strony stringa
#jeśli w argumencie podamy literę to zostanie usunięta ta litera (odpowiednio z lewej strony, prawej strony lub z obydwóch stron)

#łączenie stringów
# first_name = "Kamil"
# last_name = "Brzeziński"

#pierwszy sposób (przy uzyciu sumowania stringów)
# print(first_name + " " + last_name)
#drugi sposób (przy uzyciu metody .join)
# join_string = " "
# print(join_string.join([first_name, last_name]))

#wypełanianie zerami .zfill
# james_bond = 7
# print(str(james_bond).zfill(3)) 
#najpierw konwetujemy zmienną int na zmienną string
#następnie jako arguemnt .zfill podajemy liczbę znaków z których ma skłądać się wyjściowy string