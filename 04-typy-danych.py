#stringi
#nafme = "Kamil"  #w tym przypadku aby odać nową linie zamiast entera trzeba wprowadzić \n (newline)
#name = 'Kamil ' #w tym przypadku nie można zastsować apostrofu ' w tekście ponieważ spowoduje on zakończenie sringa (chyba, że użyjemy / przed ' (chracter escape))
#name = """Kamil""" #w tym przypadku w przeciwieństwie do przypadku 1, można ustawić położenie wyrazów w innych linijkach za pomocą entera 
#print(name)


#zmienne liczbowe
#a = 10
#b = 2.5 
#print(a + b)
#niema problemu z dodaniem liczb zmiennoprzeciwej i całkowitej do siebie, python zgodzi ich typy do siebie.
#w kodzie przy dużych liczbach w celu poprawienia czytelności można stosować podkreślenia np a = 1_000_000 (podkreślenia nie są potem wyświetlane w terminalu)


#zmienne bolean
#is_sky_blue = True
#is_sun_blue = False
#konwencja w pythonie: jeśli w nazwie zmiennej występuje więcej słów to odziellamy je od siebie podkreślnikiem _ (snake_case)
#print(is_sky_blue)
#print(is_sun_blue)


#Sprawdzanie typu zmienych 
#print(type(name))
#print(type(a))
#print(type(is_sky_blue))


#konwersja typów zmiennych
#first = 2
#second = "3"
#string to integer (5)
#print(first + int(second))
#intiger to string (23)
#print(str(first) + second)
