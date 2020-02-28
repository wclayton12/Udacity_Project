def is_even(number):
    return number %  2 ==   0
def check_number(number):
    if  is_even(number):
        number = number //   2
        collatz(number)
    else:
        number= 3  *  number +  1
        collatz(number)
def collatz(number):
    if number != 1:
        print(number)
        check_number(number)
    if number == 1:
        print("Final number is: "  +  str(number))
       

if   __name__==   "__main__":
    number = int(input("Enter a  number:"))
    collatz(number)
