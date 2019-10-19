
# 선언
mylist = []

# n개의 아이템 입력
## 넣기 
for x in range(100):
    mylist.append(x)

## 확인을 위해 출력
print(mylist)
## 또는 아이템 개별 출력
for x in mylist:
    print(x)

# 리스트 초기화, 전부 비우기
mylist = []

# n개의 랜덤 정수를 입력하고 출력하기
import random
for x in range(200):
    randnum  = random.randint(1, 100)
    mylist.append(randnum)

print(mylist)


