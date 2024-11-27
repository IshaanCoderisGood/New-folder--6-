def computepower(userinputx, userinputy):
    result = 1
    while userinputy > 0:
     if  userinputy % 2 ==0:
       userinputx = userinputx * userinputx
       userinputy >>=1
     else:
       result = result * userinputx
       userinputy = userinputy - 1
    return result
userinputx = int(input("Enter number: "))
userinputy = int(input("Enter number: "))
print("Total:",computepower(userinputx, userinputy))

        
