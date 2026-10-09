#Accept the name and check if its palindrome
name=input("Enter your name:")
if name==name[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")    

   