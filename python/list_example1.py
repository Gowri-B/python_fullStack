#list example
#ordered,mutuable(add,delete,modify),allow duplicates values

frontendLanguage = ["html","css","javascript"]  # list craetion
print(f"frontend Languages : {frontendLanguage}")

#append is used to direct value at end of list
frontendLanguage.append("bootstrap")
print(f"values after appending : {frontendLanguage}")

#insert is used to insert value by using (index value,value)
frontendLanguage.insert(2,"TypeScript")
print(f"list after inserting the value : {frontendLanguage}")

#delete ---> to delete the value by using the remove 
frontendLanguage.remove("css")
print(f"value after removing the element : {frontendLanguage}")

#delete ---> to delete the value by using the remove 
del frontendLanguage[2]
print(f"value after deleting the element : {frontendLanguage}")

#modify ---> to modify the given content
frontendLanguage[0]="Dart"
print(f"value after modifing the list : {frontendLanguage}")

#inserting the duplicate values
frontendLanguage.append("Dart")
print(f"after entring the duplicate value: {frontendLanguage}")

