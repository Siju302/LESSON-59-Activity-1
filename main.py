def print_pyramid(n, current=1):
    if current > n:
        return
    print(' ' * (n - current) + '* ' * current)
    print_pyramid(n, current + 1)

# Try it!
print("🎇 Recursive Star Pyramid 🎇")
print_pyramid(5)
print("\n🎇 Iterative Star Pyramid 🎇")
def print_pyramid_iterative(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)
print_pyramid_iterative(5)
print("\n🎇 Recursive Star Pyramid with Spaces 🎇")
def print_pyramid_spaces(n, current=1):
    if current > n:
        return
    print(' ' * (n - current) + '* ' * current)
    print_pyramid_spaces(n, current + 1)
print_pyramid_spaces(5)
print("\n🎇 Iterative Star Pyramid with Spaces 🎇")
def print_pyramid_iterative_spaces(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)