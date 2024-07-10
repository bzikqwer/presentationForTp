# Переменные

username = "Boriss"
username2 = input("Введите имя переменной: ")
print(username, username2)

# создание списка

support_tickets = ["tick1","tick2", "tick3"]
    print(support_tickets)

# операторы if -else

if username == "Boris":
    print("Welcom, Boris!")
else:
    print("Access denied.")

# циклы

for ticket in support_tickets:
    print(f"Processing {ticket}")

with open("error_log_with_timestamps.txt") as fl:
    for line in fl:
        if line.startswith("WARN"):
            print(line)