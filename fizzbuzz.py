#print numbers from 1 to 100
#if the number is divisible by 3 print Fizz
#if the number is divisible by 5 print Buzz
#if the number is divisible by 3 and 5 print FizzBuzz

x = 1
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print ("FizzBuzz")
    elif x % 3 == 0:
        print ("Fizz")
    elif x % 5 == 0:
        print ("Buzz")
    else:
        print (x)
    x = x + 1
else:
    print("\nAll Done")
    


