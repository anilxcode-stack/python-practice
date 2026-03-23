# Types of Recursion

# Tail Recursion

# def tail_fact(n, acc=1):
#     #Base Case
#     if n == 0:
#         return acc
#     #Tail recursive call with an accumulator
#     else:
#         return tail_fact(n-1, acc*n)
    
# print(tail_fact(5))


# def nontail_fact(n):
#     if n == 1:
#         return 1
#     # Non - tail recursive call because the
#     # Multiplication happen after the call
#     else:
#         return n * nontail_fact(n-1)

# print(nontail_fact(5))


# def sumOfN(n):
#     if n == 0:
#         return 1
#     return n + sumOfN(n-1)

# print(sumOfN(5))


