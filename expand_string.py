# Input: a1b10
# Output: abbbbbbbbbb

# Input: b3c6d15
# Output: bbbccccccddddddddddddddd

def expand_string(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i].isalpha(): 
            char = s[i]
            i += 1
            num = ""
            while i < len(s) and s[i].isdigit(): 
                num += s[i]
                i += 1
            result += char * int(num) 
    return result

print(expand_string("a1b10"))
print(expand_string("b3c6d15"))