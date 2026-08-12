print ("Hello, World!")

# Comment wow shocking 
#only use f stringn if need to add text to an output

#variables = reusbale for a value



#strings = any value (i think)
city = "canberra"
print (f"location {city}") #F string and then everything needs to be in the same quotations for it to work

#integers = whole numbers
population = 500000
print (f"population {population}") 

#float = numbers with decimal points
temperature = 25.5
print (f"temperature {temperature}")

#boolean = either true or false
is_in_Australia = True #needs to be capitalised 
print (f"is in Australia {is_in_Australia}") #typically dont output diretcly 




#if statment will come back to this later

if is_in_Australia:
    print ("This city is in Australia") #needs to be indented to be part of the if statement
else: #needs to be non indepnted 
    print ("This city is not in Australia") #needs to be indented to be part of the else statement



#math and how to do it in python
dog = 1
dog += 1 #this is the same as dog = dog + 1 ==== called an arguemneted assignemenrt operator
print (dog)

#same follows for subtraction, multiplication and division
# / = float divison
#//  = returns an imterger 
#% = returns the remainder of a division put number divided by after the remiander



#type castung = changing the type of a variable to another type
state = "ACT"
formed = 1911
life = 82.5
is_capital = True



life = str(life) 
print(life) #this will now print as a string and not a float

state = bool(state) #now a bool and not a string

#inputs will always be a string if user made this is important to keep in mind 






# inputs 
name = input("What is your name? ")
print (f"Hello {name}!") #this will print the name of the user that was inputted = also fotr the record an f string lets yoyu put any varibale in and it can parse it or somehtingh like that
#AGAIN USER INPUT IS ALWAYS A STRING  


# if statemennts 
### its kinda obvoiuous but it ontly runs if the condition is met and if its not met it wont 
# ORDER DOES MATTER THIS IS IMPORTANT TO REMEMBER 


rando = int(input("pick a number: ")) #int always GOES BEFORE the input function 

if rando >= 5: #i think if next line is idnetednted yiyu needd the semicolon at the end of the if statement
    print ("you picked a number greater than or equal to 5")
elif rando >10: #used if not one of two     
    print ("you picked a number greater than 10") #this will only run if the if statement is not met and the elif statement is met    thios is useful by going down fhe ;istf until condition is met
elif rando == 0: #to show how elif workws
    print ("you picked zero")
else: 
    print ("you picked a number less than 5") #this will only run if the if statement is not met     this is userful at nthe end to catch all other conditions that are not met by the if and elif statements


has_pet = True
if has_pet: 
    print ("you have a pet") #i need to stop using vscode autocmomplete
else:
    print ("you dont have a pet") 
