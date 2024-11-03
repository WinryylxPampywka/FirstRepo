try:
   print("Start of Try Block")
   print(10 / 5)
   print(12 / 2)
   # print(10 / 0)
   # print(value_1)
   print("End of Try Block")
except ZeroDivisionError:
   print("division by zero")
except NameError:
    print("Такої змінной не існує")
except ValueError:
   print("ERROR \\ помилка з перетворення до iteger")


print("Next code")