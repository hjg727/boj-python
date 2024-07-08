"""
arr = [1,2,3,4,4,4,4,5,5,6,7,7]

counter = {}

for i in arr:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

yes_duplicate = False

res = []
for num, cnt in counter.items():
    if cnt > 1:
        res.append(cnt)
        yes_duplicate = True

if not yes_duplicate:
    print(-1)
else:
    print(res)"""

def solution(arr):
    ans = []
    byte = ""

    type_dict = {
        "BOOL": 1,
        "SHORT": 2,
        "FLOAT": 4,
        "INT": 8,
        "LONG": 16
    }

    for item in arr:
        if len(byte) + type_dict[item] > 8:
            byte += "." * (8 - len(byte))
            ans.append(byte)
            byte = ""
        
        if type_dict[item] == 1:
            byte += "#"
        elif type_dict[item] == 2:
            if len(byte) % 2 == 0:
                byte += "##"
            else:
                byte += "." + "##"
        
        elif type_dict[item] == 4:
            if len(byte) % 4 == 0:
                byte += "####"
            else:
                byte += "." * (4-len(byte) % 4) + "####"
        elif type_dict[item] == 8:
            ans.append("########")
        elif type_dict[item] == 16:
            ans.append("########")
            ans.append("########")
        

        if len(byte) == 8:
            ans.append(byte)
            byte = ""
        
        if len(ans) > 16:
            return "HALT"
    
    if len(byte) > 0:# 나머지 처리 
        byte += "."*(8 - len(byte))
        ans.append(byte)
    
    if len(ans) > 16:
        return "HALT"
    
    return ",".join(ans)

print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"]))