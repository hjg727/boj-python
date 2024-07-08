import sys

input = sys.stdin.readline

S = input().rstrip()

res = []
tmp_tag = ""
tmp_origin = ""
is_tag = False

def reverse_word(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

for char in S:
    
    if char == "<":
        is_tag = True

        if tmp_origin:
            res.append(reverse_word(tmp_origin))
            tmp_origin = ""
        
        tmp_tag += char
    
    elif char == ">":
        is_tag = False
        tmp_tag += char
        res.append(tmp_tag)
        tmp_tag = ""
    
    elif not is_tag:
        tmp_origin += char
    elif is_tag:
        tmp_tag += char

if tmp_origin: # 남은 문자열 처리하깅
    res.append(reverse_word(tmp_origin))
    tmp_origin = ""

print(''.join(res))