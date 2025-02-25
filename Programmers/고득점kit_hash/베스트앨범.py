"""
목표: 장르 별로 가장 많이 재생된 노래를 "두 개"씩 모아 베스트 앨범을 출시
속한 노래가 많이 재생된 장르를 먼저 수록
장르 내에서 많이 재생된 노래를 먼저 수록
장르 내에서 재생 횟수가 같은 노래중에서는 고유 번호가 낮은 순으로 먼저 수록

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
return = [4, 1, 3, 0]
클래식 장르 => [0]500 + [2]150 + [3]800 = 1450회
pop 장르 => [1] 600 + [4] 2500 = 3100회
"""

"""genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

album = {}
cnt_album = {}

for i in range(len(genres)):
    album.setdefault(genres[i], []).append((i, plays[i]))

for i in album:
    album[i].sort(key=lambda x : (-x[1], x[0]))
    if len(album[i]) > 2:
        album[i] = album[i][:2]
res = []
for i in album:
    for j in album[i]:
        res.append(j[0])"""

#풀고 보니 장르별 전체 재생횟수 비교하여 장르를 정렬을 안했다.. key값은 set형인데 어떻게 정렬을 할까...

"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

album = {}
cnt_album = {}

for i in range(len(genres)):
    album.setdefault(genres[i], []).append((i, plays[i]))
    cnt_album[genres[i]] = cnt_album.get(genres[i], 0) + plays[i]

print(cnt_album)
# print(sorted(album.items(), key=lambda x: sum(x[1])))
sorted_albums = sorted(album.items(), key=lambda x: -cnt_album[x[0]])# 이거를 어떻게 했냐..?
print(sorted_albums)"""

"""for i in sorted_albums:
    sorted_albums[i].sort(key=lambda x : (-x[1], x[0]))
    if len(sorted_albums[i]) > 2:
        sorted_albums[i] = sorted_albums[i][:2]
res = []
for i in sorted_albums:
    for j in sorted_albums[i]:
        res.append(j[0])
print(res)"""


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
def solution(genres, plays):
    album = {}
    album_sum = {}  # 장르별 총 재생 횟수를 저장할 딕셔너리

    for i in range(len(genres)):
        album.setdefault(genres[i], []).append((i, plays[i]))
        album_sum[genres[i]] = album_sum.get(genres[i], 0) + plays[i]


    sorted_albums = sorted(album.items(), key=lambda x: -album_sum[x[0]])# 이거를 어케했냐는건데
    

    for _, songs in sorted_albums:
        songs.sort(key=lambda x: (-x[1], x[0]))
    res = []

    for genre, songs in sorted_albums:
        if len(songs) > 2:
            songs = songs[:2]
        for song in songs:
            res.append(song[0])
    return(res)

def solution1(genres, plays):
    album = {}
    album_sum = {}  # 장르별 총 재생 횟수를 저장할 딕셔너리

    for i in range(len(genres)):
        album.setdefault(genres[i], []).append((i, plays[i]))
        album_sum[genres[i]] = album_sum.get(genres[i], 0) + plays[i]

    album_sum = dict(sorted(album_sum.items(), key= lambda x: x[1], reverse=True))
    print(album_sum)

    for _, songs in album.items():
        songs.sort(key=lambda x: (-x[1], x[0]))
    res = []

    for genre in album_sum.keys():
        songs = album[genre]
        if len(songs) > 2:
            songs = songs[:2]
        
        for song in songs:
            res.append(song[0])
    return(res)

prijnt(solution1(genres, plays))