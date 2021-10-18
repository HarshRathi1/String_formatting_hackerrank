def print_formatted(n):
    result=[]
    for i in range(1, n + 1):
        a=str(i)
        b = str(oct(i)[2:])
        c = str(hex(i)[2:]).upper()
        d = str(bin(i)[2:])
        result.append([a,b,c,d])
    width=len(result[-1][3])
    for i in result:
        print(*(rep.rjust(width) for rep in i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)