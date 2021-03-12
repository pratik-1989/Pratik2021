i=int(input("Enter the number of your choice\t"))
rev=0
while i>0:
    rev=(rev*10)+(i%10)
    i=i//10
print("Reverse is=",rev)
      
