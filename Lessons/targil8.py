##For loops

'''
list_idan=["banana","apple","mango"]
for x in list_idan:
	print(x)


#same result will be
list_idan=["banana","apple","mango"]
for x in range(len(list_idan)):
	print(list_idan[x])
'''

from time import sleep

print("now we will get all the details about your class: \n")
for i in range(4):
	name=input("Enter a Name: ")
	age=int(input("Enter an age:"))
	phone=input("Enter a phone:")
	print("Printing student number " + str(i+1) + " Details…\n")
	sleep(3)
	print("Full name: " + name  + "\nAge: " + str(age) + "\nPhone: " + phone + "\n")