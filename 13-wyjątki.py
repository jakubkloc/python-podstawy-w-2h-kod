# countries_and_capitals = {'Poland': 'Waraw', 
#                           'Czechia': 'Prague', 'Germany': 'Berlin'}

# try:
#     print(countries_and_capitals['USA'])
# except:
#     print("Klucz nie został znaleziony")

# print("Jestem tutaj")
#w bloku try została zapisna komenda któa może powodować błąd
#w bloku except zapisana została komenda która wykona się zamiast 
#komendy powodującej bład, a następnie program dalej się wykona
#komenta w bloku try specjalnie została napisana w taki sposób aby
#spowodować bład (USA nie znajduje się w słowniku countries_and_capitals)

#jeśli w bloku try zjadą się komendy powodujące bład nazywamy to przechwyceniem wyjątku
#kidy wykonają się alternatywne instrukcje w bloku except nazywamy to obsłużeniem wyjątku 
#ważne jest aby przechwytywać włąściwy wyjątek, tak ,żeby działania której podejmiemy były
#właściwe w odniesieniu do konkretnego typu wyjątku
 

#  countries_and_capitals = {'Poland': 'Waraw', 
#                           'Czechia': 'Prague', 'Germany': 'Berlin'}

# try:
#     print(countries_and_capitals['USA'])
# except KeyError:
#     print("Klucz nie został znaleziony")

# print("Jestem tutaj")
# #kod został uzupełniony o rodzaj wyjątku który może zostać spowodowany instrukcją w 
# #bloku try



#  countries_and_capitals = {'Poland': 'Waraw', 
#                           'Czechia': 'Prague', 'Germany': 'Berlin'}

# try:
#     print(2 / 0)
#     print(countries_and_capitals['USA'])
# except KeyError:
#     print("Klucz nie został znaleziony")

# print("Jestem tutaj")
# #w bloku try została dodana komenda powoduja bład dzielenia przez zero
# #program nie wykona się ponieważ wyjątek obługuje tylko KeyError

#  countries_and_capitals = {'Poland': 'Waraw', 
#                           'Czechia': 'Prague', 'Germany': 'Berlin'}


# try:
#     print(2 / 0)
#     print(countries_and_capitals['USA'])
# except KeyError:
#     print("Klucz nie został znaleziony")
# except ZeroDivisionError:
#     print("Występuje dzielenie przez zero")
# print("Jestem tutaj")
# #kod został zmodyfikowany w taki sposób, że został dodany 2 blok except obsługujący bład 
# #dzielenia przez zero.
# #Warto zwrócić uwagę, że kiedy w bloku try wystąpi błąd to od razu jest wykonywany blok except 
# #(dlatego podczas wykonywania tej wersji programu nie wyświetli się komunikat o nieznalezieniu klucza
# # a jedynie komunikat o występowaniu dzielenia przez zero).


# try:
#     print(2 / 0)
#     print(countries_and_capitals['USA'])
# except:
#     print("Wystąpił wyjątek")

# print("Jestem tutaj")

# #kiedy szukamy jakiegokolwiek wyjątku to możemy po prostu zostawić komendę except
# #bez podawania rodzaju błedu i wyświetlić komunikat o wystąpieniu wyjątku.
# #jest to podejście mniej czytelne i lepiej jest wiedzieć jakiego rodzaju to może być wyjątek
# #dzięki czemu szukanie ewentualnego błedu w kodzie jest znacznie prostrze.


# try:
#     print(2 / 0)
# except:
#     print("Wystąpił wyjątek")
# finally:
#     print("To wykona się zawsze")

# print("Jestem tutaj")
# #instrukcje w bloku finnaly wykonają się zawsze niezależnie czy wystąpi wyjątek czy nie
# #blok finnaly jest wykorzystywany do zamknięcia zasobów tzn. jeśli otworzymy jakieś pliki lub
# #połączenie do bazy danych to w bloku finnaly możemy te pliki i to połączenie zamknąć 
# #niezależnie od tego czy nasza operacja się powiadła czy nie, nie powinniśmy zostawiać otwartych połączeń.