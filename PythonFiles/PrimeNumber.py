number=11
Match=True

for num in range (2,number+1):
    number%num
    if number%num==0:
        Match=False
        
if Match:
    print( f'{num} is prime.')

else:
    print(f'{num} is not prime.')