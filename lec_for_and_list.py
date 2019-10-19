# 간단한 사용
mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(mylist)

mylist = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
print(mylist)


# 위와 같은 리스트를 만들어 보자
## 리스트 비우기
mylist = []
for x in range(100):
    num = 2 * x
    mylist.append(num)

print(mylist)

mylist = []
for x in range(100):
    mum = 2^x
    mylist.append(num)

print(mylist)



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


