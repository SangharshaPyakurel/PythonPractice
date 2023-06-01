i = []
x = []
a = int(input("Enter value of a"))
c = int(input("Enter value of c"))
n = int(input("Enter value of n"))
m = int(input("Enter value of m"))
seed = int(input("Enter number of seed"))
def mixedlcg():
    x[0] = seed
    for i in range():
	    x[i] = (a*x[i-1]+c) % m
print("x[n] = x[i]")
mixedlcg()