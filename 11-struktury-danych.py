# #LISTA
# # lista jest strukturą danych na której elementy mogą się powtarzać (tzn. moze np na liście imion wystąpić dwa razy Kamil) 
# names_list = [] #liste tworzymy za pomocą nawiasów kwadratowych []
# names_list.append("Kamil")
# names_list.append("Mariusz") #metoda .append pozwala dołączać kolejne wpisy na liście
#służy zazwyczaj do pogrupowania elementów tego samego typu


# #listę można wypełnić od razu podczas definicji
# names_list = ["Kamil","Mariusz"]
# print(names_list)


# #aby wyświetlić poszczególne elementy listy za pomocą pętli for
# for name in names_list:
#     print(name)
# #definiujemy jak ma się nazywać zmienna którą chcemy wyświetlać (w tym przypadku name)
# #i za pomocą "in" wskazujemy z której listy ma się wyświetlać (w tym przpadku names_list)


# #odwracanie listy
# names_list.reverse()


# #sortowanie listy (alfabetycznie)
# names_list.sort()
# #sortowanie alfabetyczne ale od końca
# names_list.sort(reverse=True)

# #odwoływanie się do konkretnego elementu w liście
# print(names_list[0]) #w tym przypadku do pierwszego elementu o indeksie 0


# #zliczanie elementów listy
# print(names_list.count("Rafał"))
# #zwraca liczbę która informuje ile razy dane słowo pojawiło się na liscie
# #jeśli szukane słowo nie występuje ani razu to zwracane jest 0


# #sprawdzanie długości listy 
# print(len(names_list))
# #zwraca liczbę informującą ile elementów zawiera lista


# #wyświetlanie elementów listy i usuwanie ich z lity (metoda .pop)
# print(names_list)
# print() #wstawia pustą linijkę
# print(names_list.pop(0)) #usuwa element o indeksie 0 (pierwszy element) z listy names_list
# print()
# print(names_list)
# #po wykonaniu powyższego bloku zostanie wyświetlona lista, następnie wyświetlony 1 element
# #i na końcu lista bez 1 elementu


# #usuwanie elementu z lity (metoda .remove)
# names_list.remove("Kamil") #jako argument .remove podajemy element który chcemy usnąć z listy
# print(names_list) #lista zostanie wyświetlona bez elementu Kamil
# #metoda .remove usuwa pierwsze wystąpienie danego elementu tzn jesli lista zawierała więcej niż jedno 
# #wystąpienie zmiennej Kamil to zostatnie usnięta tylko pierwsza z nich


# #usuwanie wszystkich elementów z listy (metoda .clear()
# names_list.clear()
# print(names_list) #zwraca pustą liste []


# #łączenie list
# names_list2 = ["Dominik"]
# names_list3 = names_list + names_list2
# print(names_list3)





#KROTKA (ang. tuple)
#krotke tworzy się tak jak listę z tą różnica, że zamist nawiasów kwadratowych
##stosuje się nawiasy okrągłe ()
#krotka jak juz powstanie to jest strukturą niezmienną
#nie da się stworzyć pustej krotki 
#krotki w przeciwieńśtwie do listy nie można modyfikować
#krotka nazywana jest struktuą niemutowalną
#krotki uzywamy do zgrupowania danych dotyczących pewnego konceptu

person = ("Kamil","Brzeziński",32) #krotka (mogą występować rózne typy danych)

#sprawdzanie rozmiauru
print(len(person))  

#sprawdzzanie wystąpienia danego elementu
print(person.count("Kamil"))

#SET (zbiór)
#Podobny do listy
#Nie można mieć zdubplikowanyhc danych 
#definiuje sie go za pomocą nawiasów klamrowych {}
names_set = {"Kamil", "Mariusz"}
#Set to struktura danych w której elementy nie są w żaden sposob uporządkowane (nie wiemy w jakiej kolejności
# się wyświetlą) 
#elementy dodawane do setu muszą być niemutowalne (tak jak wcześniej opisana krotka)

#tworzenie pustego setu
names_set = set()
#dodawanie elementów do setu (metoda .add)
names_set.add("Kamil")
names_set.add("Dominik")
names_tuple = ()
names_set.add(names_tuple)
#nie można dodawać listy do setu ponieważ jest ona elementem mutowalnym

#Usuwanie leementu z setu (metoda discard)
names_set.discard("Kamil")
#Usuwanie elementu z setu (metoda remove)
names_set.remove("Kamil")
#W metodzie discard po podaniu elementu który nie istnieje w secie nic się nie stanie
#natomiast w metodzie removed gdy podamy element który nie istnieje w secie wyświetlony zostanie błąd


#Wyświetlanie elementów całego setu
for name in names_set:
    print(name)


#dodawanie setów do siebie
names_set2 = {"Mariusz", "Tytus"}

names_set3 = names_set.union(names_set2)
#za pomocą metody .union dodajemy set names)set2 (podany w argumencie metody) do names_set
#metoda union zwraca nam nowy set, nie modyfikuje oryginalnego setu
for name in names_set3:
    print(name)

#jeśli chcemy zmodyfikować set już istniejący to stosujemy metode .update
names_set.update(names_set2) 
#w argumencie metody podajemy nazwę setu który ma zostać dodany do pierwszego setu


#Porównywanie setów (metoda .difference)
names_set3 = names_set.difference(names_set2)
#Bierzemy elementy z pierwszego setu i usuwamy z niego elementy które znaleśliśmy
#w drugim secie.


#Porównywanie setów (metoda .intersecction)
names_set3 = names_set.intersection(names_set2)
#zwraca część wspólną obydwuch setów     


#Porównywanie setów (metoda .symmetric_difference)
names_set3 = names_set.symmetric_difference(names_set2)
#Zwraca elementy spoza części wspólnej (te które występują tylko w jednym zbiorze)

#czyszczenie setu (metoda .clear)
names_set.clear()


#Dodawanie setu do listy (metoda .extend)
names_list = ["Artur", "Rafał"]
names_set2 = {"Mariusz", "Tytus"}
names_list.extend(names_set2)


#DICTIONARY (Słownik)
#w słowniku nie możemy mieć dwóch takich samych kluczy 
#struktura, wartość
#słownik tworzy się za pomocą nawiasów klamrowych {}
countries_and_capitals = {"Poland":"Warsaw","Germany":"Berlin"}  

#wyświetlanie słownika
print(countries_and_capitals)

#dodawanie elementów do słownika
countries_and_capitals['Czechia'] = "Prague"
#w nawiasie kwadratowym [] podajemy klucz pod którym chcemy przechować wartość 
#wartość podajemy po równa się =


#wyświetlanie wszystkich klluczy słownika (metoda .keys)
for country in countries_and_capitals.keys():
    print(country) 
    #nazwe country została wybrana bo pasuje do przykładu ale ogólnie jest dowolna

#wyświetlanie wszystkich wartości słownika (metoda .values)
for capital in countries_and_capitals.values():
    print(capital) 

#wyświetlanie kluczy i wartości słownika (metoda .items)
for country, capital in countries_and_capitals.items():
    print(country + "-" + capital) 

#wyświetlanie wartości pobranej z danego klucza (klucz w nawiasie kwadratowym [])
print(countries_and_capitals["Poland"])
#wyświetlanie wartości pobranej z danego klucza (metoda .get)
print(countries_and_capitals.get("Poland"))
#Różnica bolega na tym, że w metodzie. get jeśli klucz nie zostanie znaleziony to 
#zwracana jest wartość typu None (w przypadku nawiasów kwadaratowych wyświetalny jest bład)


#ustawanie domyślny wartości klucza 
print(countries_and_capitals.setdefault("USA", "Washington DC"))
#setdefault zwraca wartość z danego klucza, lecz jeżeli dany klucz nie istnieje 
#to wstawia nowy lkucz z przypisująć mu drugi argument metody.setdefault

#jeśli drugi raz podamy wartość dla jakiegoś klucza to spowodujemy podmienienie wartości w kluczu np.
countries_and_capitals["Poland"] = "Cracow"

#Usuwanie wartości znajdującej się pod danym kluczem (metoda .pop)
print(countries_and_capitals.pop("Poland"))
print(countries_and_capitals)
#metoda .pop zwraca takżę wartość usuniętą 
#jesli w argumencie metody podamy klucz który nie istnieje to zostanie wyświetlony bład
print(countries_and_capitals.pop("USA","Washington DC"))  
#W przypadku kiedy podamy 2 argumenty, czyli klucz i wartość które nie istnieją w słowniku,
# to metoda .pop nie usunie nic z listy, mimo to zwróci wratość 2 argumentu 

#usuwanie ostnio dodanego klucza (metoda .popitem)    
print(countries_and_capitals.popitem()) 
#metoda .popitem także zwraca to co usuwa 

#sprawdzanie czy w słownku istnieje wybrany klucz (metoda .keys)
if "Poland" in countries_and_capitals.keys():
    print("Znaleziono!")
else:
    print("Nie znaleziono!")

#sprawdzanie czy w słownku istnieje wybrany klucz (wersja bez .keys)
if "Poland" in countries_and_capitals:
    print("Znaleziono!")
else:
    print("Nie znaleziono!")

print("Poland" in countries_and_capitals)
#print(nazwa_klucza in dictionary) zwraca wartości:
#True - jeśli podany klucz znajduje się w słowniku
#False - jeśli podany klucz nie znajduje się w słowniku


#czyszczenie słownika (metoda .clear)
countries_and_capitals.clear()

print(countries_and_capitals)
#Zwraca puste nawiasy klamrowe {}

