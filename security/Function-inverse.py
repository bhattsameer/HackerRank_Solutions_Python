# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
x = map(int, raw_input().rstrip().split())

for i in range(1,len(x)+1):
    for j in range(0,len(x)):
        if x[j] == i:
            print j+1
 