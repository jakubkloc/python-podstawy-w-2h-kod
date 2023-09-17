number = 1

# while number < 6:
#     print(number)
#     number += 1


# for number in range(1, 6, 2): 
#zakres od lewej strony jest zakresem dokmkniętym a od prawej zakresem otwartym 
#trzeci argument to krok 
        # print(number)


# #instrukcja przerywająca - break
# for number in range(1, 6): 
#     if number == 5:
#         break
#     print(number)    

# #break przerywa pętle, spowoduje to, że iterenacje dla 5 i 6 się nie wykonają


# #instrukcja - continue
for number in range(1, 6): 
    if number == 5:
        continue
    print(number) 
#continue przerywa aktualne wywołanie pętli i przechodzi do kolejnego wykonania (5 nie została wyświetlona)