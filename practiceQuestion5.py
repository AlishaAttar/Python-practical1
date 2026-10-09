#print the following pattern 
#   *
#   ##
#   ***
#   ####
n=int(input("Enter the number"))
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print("*",end=" ")
        else:    
            print("#",end=" ")
    print()