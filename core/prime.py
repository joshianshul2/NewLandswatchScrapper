f=0
def prime(n):
    i=2
    while i<n :
        if n%i==0 :
            f=0
            break
        else :
            f=1
        i=i+1
    return f

f=prime(89)
if f==1:
    print("Prime No")
       
else :
    print("Not a Prime No")



# print("Hello, World!")

