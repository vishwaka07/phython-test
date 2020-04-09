age = input("Enter your age: ")
age = int(age)

if age==0 or age <0:
    print("You cannot watch movie")
elif 0<age<=3:
    print("Ticket price : Free")
elif 3<age<=10:
    print("Ticket price: 100")
elif 10<age<=60:
    print("Ticket price: 300")
else:
    print("Ticket price: 200")