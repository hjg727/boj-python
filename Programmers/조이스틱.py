def up_down(words):
    cnt = []
    for word in words:
        cnt.append(min(ord(word) - ord('A'), ord('Z') - ord(word) + 1))
    return cnt

    