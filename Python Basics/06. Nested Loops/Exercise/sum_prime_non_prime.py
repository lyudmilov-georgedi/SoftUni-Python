prime_sum = 0
nonprime_sum = 0

while True:
    num = input()
    if num == "stop":
        break
    num = int(num)
    if num < 0:
        print("Number is negative.")
        continue
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        prime_sum += num
    else:
        nonprime_sum += num

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {nonprime_sum}")
