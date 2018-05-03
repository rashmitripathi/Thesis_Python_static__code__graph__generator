
def countSum(numbers):

 sum=0
 length=len(numbers)
 for i in range(0,length):
    value=numbers[i]
    print("value",value)
    sum=sum+1
    for j in range(3,value):
            print(value , j)
            if not j%2 == 0:
             if value % j == 0:
                print("true")
                sum=sum+j


 return sum

print("sum",countSum([1,6,10]))