# Type of the sum like S = 1-2+3-4+5-6 ... -100
## If u enter another type, the result will be False and incorrect


try:
    a = int(input("Enter the first number in your sum : "))
    n = int(input("Enter the last number in your sum : "))
except ValueError:
    print("Enter a numbers")
def sum_calcul(a,n):
    if n%2 == 0:
        return int(a+(n/2))
    else:
        return int(-(n+1)/2)
print(f"S ={sum_calcul(a,n)}")


#Ayoub Lagnaoui XX
