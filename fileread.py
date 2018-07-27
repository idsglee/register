with open('mypage') as file:
    content1 = file.read()

with open('mypage') as file:
    content2 = file.readlines()

print(content1)
print(content2) 

num=1
for line in content2:
    print(str(num) + " : " + line)
    num += 1
