# The Project: Build a CLI (Command Line Interface) app where users can input daily expenses,
#  categorize them (Food, Rent, Fun), and set a monthly budget. The script should warn the user if they exceed
#  their budget and save the data to a local file (.csv or .txt). Why it helps with ML:
#  You’ll get comfortable with data persistence, reading/writing files, and structuring
#  data using nested dictionaries and lists—the exact way data flows into an AI model. moreover, 
# dont use ai and try to use OOPS , object oriented progar...., so tahat you can have a grasp on that
budget=10000
class Expense:
    def __init__(self):
        self.amount_spent=0
       
    def display_info(self,food,rent,fun,price1, price2 , price3):
        return(f"Food_name:{food} | Rent_Asset:{rent} | Fun:{fun}| Food_price:{price1}|Rent_cost:{price2}|Fun_cost:{price3}")
    def total_expenditure(self,price1, price2 , price3):
         self.amount_spent += (price1+price2+price3)
         return(self.amount_spent)
p1= Expense()
while True:
    food=input("Enter the food ordered-")
    rent=input("Enter the name of Rented asset -")
    fun=input("Enter the name of fun activity -")
    price1=int(input("enter the cost for food"))
    price2=int(input("enter the cost of rented asset"))
    price3=int(input("enter the total cost for fun"))
     
    print(p1.display_info(food,rent,fun,price1, price2 , price3))
    a=(p1.total_expenditure(price1, price2 , price3))
    print (a)
    with open("expenses.txt","a")as file:
        file.write(p1.display_info(food,rent,fun,price1, price2 , price3))
        file.write(f"the total expenditure till now is {a}")
    # checkng monthly budget
    if(a>budget):
            print("Warning!! \n you exceed the monthly budget")
            break
    else:
        print("Safe! Money Left")


     
   







