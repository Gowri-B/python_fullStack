n=str(input("How many values do you want to add : "))

strings = []

for i in range(n):
    string_List= str(input(f" Enter numbers {i+1} : "))
    strings.append(string_List)
print(strings)

while True:
    print("option: add, insert, modify, delete, display, exit")

    choice = input("Enter your option : ")

    if choice == "add":
        print(f"Before String Values list : {strings}")
        string_List=str(input("Enter the string to add :"))
        strings.append(string_List)
        print(f"After string values list : {strings} ")

    elif choice == "insert":
        print(f"Before string values list : {strings}")
        position = str(input("Enter index position :"))
        string_List = str(input("Enter numbers to insert into list : "))
        strings.insert(position)
        print(f"After string values list : {strings}")
    
    elif choice == "modify":
        print(f"Before string values list : {strings}")
        position=str(input("Enter index position :"))
        string_List=str()
        print(f"After string values list : {strings}")


