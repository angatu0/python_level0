# The function is for check if number is prime or return prime number closest, below.
def maior_primo(k):
    count = k  # Start with the value "k" for to be decreasing during the count.
    x = 0  # This return the value count the numbers below the "k" until arrive in the next prime number.
    while count >= 1:
        for x in range(2, k + 1):  # This important "+ 1" for counter return the same number of the "count"
            # Before the " range " start in "0".
            if count % x == 0:
                break
        if x == count:
            return x  # Find the prime number
        count -= 1  # Decreasing count
        return maior_primo(count)


