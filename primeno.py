n=int(input("enter no "))
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print(n,"is not prime")
                break
        else:
            print(n,"is prime")

if n>0:
    prime(n)
else:
    print("positive no ")
