# Args (non-keyword arguments)
# Used to pass variable number of arguments to a function
# It is used to pass a non-key worded, variable-length argument list. 
# Used when we dont know how many arguments are present 


def myFunction(* args):
    for arg in args:
        print(arg)

myFunction('Apple', 'Mango', 'Banana', 'Pineapple')



def myFun( *args):
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum 
 
 
ans = myFun(2, 4, 6, 8)
print(ans)