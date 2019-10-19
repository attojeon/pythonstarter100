
# 2의 배수를 100개 입력하고, 순서를 출력할 수 있게 하는 방법
## 2, 4, 6, 8, ...
mylist = []
for x in range(1, 101):
    mylist.append(2 * x)

for item in enumerate(mylist):
    print(item)

### 아래에서 왜 index+1을 했나요?
for index, value in enumerate(mylist):
    print("2 X {} = {}".format(index+1, value))


