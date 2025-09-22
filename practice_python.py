#Learning the concept of variables, strings, intergers
# number_1 = 8
# number_2 = "The number is"
# total = str(number_1) + number_2
# print(total)

# calculation = "10 - 7"
# math = 6 + 9
# myaddition = calculation + ' ' + str(math)
# print(myaddition)

# #Example of List Data
# cars = (["mazda", "Toyota", "Benz", "Honda"])
# print(cars)

# username = "ade"
# newusername =username
# username ="shola"
# print("previousname", newusername)
# print ("latestname", username)

# #testing the IF command
# name ="saheed"
# saheed ="boy"
# if name=="saheed" and saheed=="boy":
#     print("yes Saheed is a good boy") 
# else:
#     print("no saheed is not a good boy")

# saheed = 45
# Zahra=  9
# if saheed >= 31 and saheed <= 40:
#     print("Saheed is an Adult")
# elif Zahra >= 3 and Zahra <= 5:
#     print("Zahra is a toddler")
# else:
#     print("Saheed is not an Adult neither Zahra is a toddler")

# Assign a variable named `system` to a specific operating system, represented as a string
# This variable indicates which operating system is running
# Feel free to run this cell multiple times; each time try assigning `system` to different values ("OS 1", "OS 2", "OS 3") and observe the result

# system = "OS 1"

# # If OS 2 is running, then display a "no update needed" message

# if system=="OS 1":
#     print("update needed")
    

# # Assign `system` to a specific operating system
# # This variable represents which operating system is running

# system = "OS 2"

# # If OS 2 is running, then display a "no update needed" message
# # Otherwise, display a "update needed" message

# if system == "OS 2":
#     print("no update needed")
# else:
#     print("update needed")

# # Assign `system` to a specific operating system
# # This variable represents which operating system is running

# system = "OS 1"

# # If OS 2 is running, then display a "no update needed" message
# # Otherwise if OS 1 is running, display a "update needed" message
# # Otherwise if OS 3 is running, display a "update needed" message

# if system == "OS 2":
#     print("no update needed")
# elif system == "OS 1":
#     print("update needed")
# elif system == "OS 3":
#     print ("update needed")

# # Assign `approved_user1` and `approved_user2` to usernames of approved users

# approved_user1 = "elarson"
# approved_user2 = "bmoreno"

# # Assign `username` to the username of a specific user trying to log in

# username = "bmoreno"

# # If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# # Otherwise, display a message that they do not have access to this device

# if username == approved_user1 or approved_user2:
#     print("This user has access to this device.")
# else:
#     print("This user does not have access to this device.")


# # Assign `approved_list` to a list of approved usernames

# approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# # Assign `username` to the username of a specific user trying to log in

# username = "cat"

# # If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# # Otherwise, display a message that they do not have access to this device

# if username in approved_list:
#     print("approved to access")
    
# else:
#     print("do not have access to this device")
    

# for i in range(5):
#     print("i am learning how to use the for loop command")

# for i in [0,1,2,3,5,6,7,8,9,10,11]:
#     print("the number is" + " " + str(i))

my_families = ["`saheed", "idris", "Quadri", "Quam"]
for brothers in my_families:
    print(brothers)