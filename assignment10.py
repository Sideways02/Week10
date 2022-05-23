
finame = input("Please tell me what you would like to call the file: ")
name = input("Please enter your name: ")
address = input("Please enter your address: ")
phone = input("Please enter your phone number: ")


filename = finame
with open(filename, 'w') as file_object:
    file_object.write(name + ', ')
    file_object.write(address + ', ')
    file_object.write(phone)



with open(finame) as file_object:
    contents = file_object.read()
    print(contents)
