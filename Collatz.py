####The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term.
## if the previous term is odd, the next term is 3 times the previous term plus 1### The conjecture is that no matter what value of n, the sequence will always reach 1. 
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
        print("You have selected: ", number)
        check_number(number)
    if number == 1:
        print("Final number is: "  +  str(number))
       

if   __name__==   "__main__":
    number = int(input("Enter a  number:"))
    collatz(number)
