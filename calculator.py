#i am updating this calc on 13/08/2025 23:21 to record history of all the calculations:
# a calculator shall do addition, subtraction, multiplication, division and loop around if the user wants to extend the calculation

def history(num1, num2, b, result):
    with open('calchistory.txt','a') as file:
        num1=str(num1)
        num2=str(num2)
        result=str(result)
        #we will write the history in the file so
        data=num1 + b + num2 + '=' + result + '\n'
        file.write(data)

def show():
    with open('calchistory.txt','r') as file:
        #we will read from it
        data3=file.readlines()
        finedata=[line.strip() for line in data3]
        print(finedata)

def clear():
    with open('calchistory.txt','w') as file:
        #we will clear 
        data5=""
        file.write(data5)

#call them functions
print('1.check history  2. clear history    3. proceed to calculation')
while True:
    inp=int(input('enter choice: '))
    if inp==1:
        show()
        print('here is the history')
    elif inp==2:
        clear()
        print('done, all clear')
    else:
        print('invalid')
        break
#it is a simple calculator so i am gonna use two variables

num1=float(input('enter num1: '))
num2=float(input('enter num 2:'))
#now we have used input function to enter the data
#next we would perform the operations
#for that we can use operators
#Addition
b=input('enter operation: ')
#we shall not except any other entries except '+','-','*','/'(and num 1 will always remain before num2)

if b=='+':
    result=num1+num2
    print(result)
    history(num1, num2, b, result)
elif b=='-':
    result=num1-num2
    print(result)
    history(num1, num2, b, result)
elif b=='*':
    result=num1*num2
    print(result)
    history(num1, num2, b, result)
elif b=='/':
    try:
        result=num1/num2
        print(result)
        history(num1, num2, b, result)
    except ZeroDivisionError:
        print('its not defined')
else:
    a='not a valid operation'
    print(a)
result='this is the required result'
print(result)

#in this I have used built in functions and have not introduced any built in modules or libraries
'''used functions are:
input()
float()
print() and inbuilt operators
'''