# #otwieranie pliku z katalogu (który już istnieje)
# file = open("conutry_capitols.txt")


#tworzenie pliku w katalogu (podanie argumentu w+ (write))
file = open("countries_and_capitals.txt","w+")
#istnieje możliwość otwieranie plikó do zapisu, odczytu i do zapisu odczyty
#w dokumentacji rozpisane są komendy który ustalają w którym miejscu pliku ustawić kursor
#czy na początku (wtedy to co będziemy dopisywali do pliku pojawi się na początku) czy na
#końcu (wtedy dopisane fragmenty dopisywane będę na koniec pliku)


#zapisywanie do pliku
countries_and_capitals = {'Poland': 'Warsaw',
                          'Czechia': 'Prague', 'Germany': 'Berlin'}

for country, capital in countries_and_capitals.items():
    file.write(country + "-" + capital + "\n")
#"\n" to znak nowej linni
#zapisanie państ i ich stolic do pliku countries_and_capitals


file.close() 
#zamknięcie połączenia z plikiem


#wyświetlanie treści pliku w konsoli 
file = open("countries_and_capitals.txt")

for line in file.readlines():
    print(line.strip())


file.close() 
#zamknięcie połączenia z plikiem