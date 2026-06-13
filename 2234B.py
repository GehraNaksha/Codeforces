t = int(input(""))
for _ in range(t):
    n = int(input(""))
    result = [-1]
    
    #10 is the only edge case where a valid pair cannot exist
    #use a dictionary to resolve tle
    if n != 10:
        remainder_to_palindrome = {
            0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5,
            6: 6, 7: 7, 8: 8, 9: 9, 10: 22, 11: 11
        }
        
        remainder = n % 12
        a = remainder_to_palindrome[remainder]
        b = n - a
        result = [a, b]
        
    print(*result)