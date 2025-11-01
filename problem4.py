def next_collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3 * n + 1
    
def collatz_length(n):
    steps = 0
    while True:
       a = next_collatz(n)
       steps += 1
       n = a
       if n == 1:
           break
    return steps

def max_in_collatz(n):
    max_value = n
    while True:
        a = next_collatz(n)
        if a > max_value:
            max_value = a

        n = a
        if n == 1:
            break
    
    return max_value

def print_collatz_sequence(n, max_steps):
    print(f"  Step 0: {n}")
    for i in range(1, max_steps + 1):
       a = next_collatz(n)
       print(f"  Step {i:.0f}: {a:.0f}")
    
       n = a
       if n == 1:
           break

print("\n\nCollatz Sequence Analyzer")
print("----------------------------------------")
n = 6
print(f"Steps to reach 1 from {n}: {collatz_length(n):.0f}")
n = 7

print(f"Steps to reach 1 from {n}: {collatz_length(n):.0f}")
n = 27
print(f"Steps to reach 1 from {n}: {collatz_length(n):.0f}")

print(f"\nMaximum value in sequence from {n}: {max_in_collatz(n):.0f}\n")

n = 19
print(f"Collatz sequence starting from {n}:")

print_collatz_sequence(n, max_steps = 10)

print(f"\nSequence length comparison:")

n = 15
print(f"  Starting from {n}: {collatz_length(n):.0f} steps")
n = 16
print(f"  Starting from {n}: {collatz_length(n):.0f} steps")
n = 17
print(f"  Starting from {n}: {collatz_length(n):.0f} steps\n\n")





