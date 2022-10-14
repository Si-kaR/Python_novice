def main():
    n = eval(input("Input the number of days in the month (28-31): "))
    d = eval(input("Input the starting day (0=sun, 1=mon, ...): "))
    i = 1
    while i <= n:
        print(i)
        i = i + 1

main()
