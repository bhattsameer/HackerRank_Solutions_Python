# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
x = map(int, raw_input().rstrip().split())

if len(set(x)) == len(x):
    print("YES")
else:
    print("NO")