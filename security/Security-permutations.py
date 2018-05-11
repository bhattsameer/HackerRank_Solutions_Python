# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
y = map(int, raw_input().split())
for i in range (0,n):
    print y[(y[i]-1)]