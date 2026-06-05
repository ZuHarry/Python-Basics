def arrayMenu():
    num1 = int(input("Enter first number = "))
    num2 = int(input("Enter second number = "))
    total = num1 + num2
    print("\nTotal = ",total)

def calculatorMenu():
    print("This is calculator")
    arraySize = int(input("Enter size of array =  "))
    
    arr = []
    
    for i in range(arraySize):
        arr.append(int(input("Enter number " +str(i)+" = ")))
    

    arr = []

    for i in range(arraySize):
        arr.append(int(input("Enter number " + str(i+1) + " = ")))

    print("\nYou entered = ", end="")
    for i in range(len(arr)):
        print(arr[i], end = " ")
        
def stringMenu():
    print("Welcome to String Menu")
    print("1. Reverse a String")
    print("2. Divide a String")
    print("3. Merge two String")
    print("4. Count vowels in String")
    

print("\n==================================")
print("Welcome to Program")
print("==================================")
print("\n1. Calculator")
print("2. Array")
choice = input("Choose = ")

if choice=="1":
    arrayMenu()
elif choice=="2":
    calculatorMenu()
elif choice=="3":
    calculatorMenu()