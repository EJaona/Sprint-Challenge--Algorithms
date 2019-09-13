'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    total = 0
    target = 'th'

    
    print(total)

    # TBC
    if len(word) <= 0:
        return 0
    elif word[: 2] == target:
        total += 1
        return total + count_th(word[1:])
    
       
    else:
        return count_th(word[1:])

    return total
    

print(count_th('thafsdfethlkoh'))