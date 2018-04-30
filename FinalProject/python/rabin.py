
def rabin_karp_search(pattern, s, d=5294212309, q=9743212277):
    """Rolling Hash
    The idea is to not recompute and store the hash every time,
    as we can compute quickly the hash given the previous string
    """
    m, n = len(pattern), len(s)
    # h = pow(d,m-1)%q
    # mod as we go
    h = 1
    for _ in range(m-1):
        h = (d * h)%q
    p, t = 0, 0
    result = []
    for i in range(m): 
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(s[i]))%q
    for k in range(n-m+1):
        if p == t: # check character by character
            match = True
            for i in range(m):
                if pattern[i] != s[k+i]:
                    match = False
                    break
            if match:
                result = result + [k]
        if k < n-m:
            t = (t-h*ord(s[k]))%q 
            t = (t*d+ord(s[k+m]))%q 
            t = (t+q)%q 
    return result

def build_string(A, B, S):
    """Finds the lowest cost of making a string given
    append cost A, substring copy cost B, and target string S
    """
    RABIN_VERSION = True  

    cost = [0] + ([300000000] * len(S))
    copy_length = min(1, B/A)
    for i in range(1, len(cost)):
        cost[i] = min(cost[i], cost[i-1] + A)

        # while you are in range AND it makes sense to copy
        # AND you are able to copy, do it.
        j = copy_length
        if RABIN_VERSION:
            while j <= i and i + j < len(cost) and rabin_karp_search(S[i:i+j], S[:i]):
                cost[i+j] = min(cost[i+j], cost[i] + B)
                j += 1
        else: 
            while j <= i and i < len(cost) - j and S[i:i+j] in S[:i]:
                cost[i+j] = min(cost[i+j], cost[i] + B)
                j += 1

    return cost[-1]