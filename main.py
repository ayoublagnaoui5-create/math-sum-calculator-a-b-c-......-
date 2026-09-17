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

