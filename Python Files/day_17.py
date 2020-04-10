def abundant(n):
        k = [i if n%i == 0 else 0 for i in range(1,(n//2)+1)]
        k = sum(k)
        if k > n:
                return True
        return False


def sum_abundant(n):
	
        i, k = 1, []
        while len(k) < n:
                if abundant(i):
                        k.append(i)
                i += 1
        return k, sum(k)

print(sum_abundant(7))
