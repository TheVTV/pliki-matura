file_name = "pliki/liczby_przyklad.txt"

with open(file_name, "r", encoding="utf-8") as file:
    lines = [line.strip().split() for line in file]




for line in lines:
    number1 = line[0]
    number2 = line[1]