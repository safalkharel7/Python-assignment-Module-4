import random
N = int(input("\nEnter the number of random points to generate: "))
i = 0
n = 0
while i <N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2+y**2<1:
        n +=1
    i +=1
pi_est = 4*n/N
print(f"\nThe approx value of pi based on number of random points you entered is: {pi_est}")
