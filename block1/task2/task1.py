def calc_fib(n):
    if n < 1:
        return n
    a = 0
    b = 1
    for i in range(1, n):
        temp = a
        a = b
        b = temp + b
    return b
n = open("input.txt").readline()
o = open("output.txt", "w")
o.write(str(calc_fib(int(n))))
o.close()