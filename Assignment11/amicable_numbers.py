def sum_factor(n):
    factors = []
    for i in range(1, n/2 + 1):
        if n % i == 0:
            factors.append(i)
    return sum(factors)

def compare(size = 100000):
    amicables = []
    for i in range(1, size):
        s_fact1 = sum_factor(i)
        if (s_fact1 > i):
            s_fact2 = sum_factor(s_fact1)
            if (s_fact2 == i):
                amicables.append((s_fact1, s_fact2))
    return amicables

if __name__ == '__main__':
    answer = compare()
    total = 0;
    for i in range(len(answer)):
        print(answer[i])
        total += answer[i][0] + answer[i][1]
    print 'Sum:', total