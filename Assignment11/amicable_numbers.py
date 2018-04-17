import time
def sum_factor(n):
    total = 0
    for i in range(1, n/2 + 1):
        if n % i == 0:
            total += i
    return total

def compare(size = 100000):
    amicables = []
    for i in range(1, size):
        s_fact = sum_factor(i)
        if (s_fact > i):
            if (sum_factor(s_fact) == i):
                amicables.append((i, s_fact))
    return amicables

if __name__ == '__main__':
    start = time.time()
    answer = compare()
    total = 0;
    for i in range(len(answer)):
        print(answer[i])
        total += answer[i][0] + answer[i][1]
    end = time.time()
    print 'Sum:', total
    print 'Time:', round((end - start) * 1000, 2), 'ms'