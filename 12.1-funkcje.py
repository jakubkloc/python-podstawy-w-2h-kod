#aby funkcja mogła coś zwracać trzeba użyć komendy return i podać co ma zwracać
def display_sum(a, b):
    print(a+b)
#wynkcja podczas wykonywania wyśweitla sumę a+b ale nie zwraca żadnego wyniku
def calculate_sum(a, b):
    return a + b
#ta funkcja zwraca wynik dodawania a+b
sum = calculate_sum(2,3)
print(sum)
#to co zwraca funkcja calculate_sum przypisaliśmy do zmiennej sum i wyświetliliśmy

def print_message():
    print("To jest super wiadomość")
#powyższa funkcja nizczego nie przyjmuje ani niczego nie zwraca, po 
#prostu podczas wykonania wyświetla komunikat
print_message()
