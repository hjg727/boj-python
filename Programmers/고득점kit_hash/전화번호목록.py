phone_book = ["12","123","1235","567","88"]
phone_book.sort()
print(phone_book)
"""
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if  phone_book[j].startswith(phone_book[i]):
                return False
    
    return True
"""

def solution(phone_book):

    hash_map = set(phone_book)

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            if arr in hash_map and arr != nums:
                return False

    return True