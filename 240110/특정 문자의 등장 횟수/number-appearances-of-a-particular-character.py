string = input()

temp = string
cnt1 = cnt2 = 0
idx = temp.find('ee')
while idx != -1:
    if idx == len(temp):
        break
    cnt1 += 1
    temp = temp[idx+1 : -1]
    idx = temp.find('ee')

temp = string
idx = temp.find('eb')
while idx != -1:
    if idx == len(temp):
        break
    cnt2 += 1
    temp = temp[idx+1 : -1]
    idx = temp.find('eb')

print(cnt1, cnt2)