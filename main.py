# 1 задание
s = '8'*68
while '888' in s or '888' in s:
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)
print('Ответ на 1 задание:', s, sep=" ")

# 2 задание
s = '1'*10 + '2'*3
while '11' in s:
    if '112' in s:
        s = s.replace('112', '6', 1)
    else:
        s = s.replace('11', '3', 1)
summ = 0
for i in range(0, len(s)):
    summ = summ + int(s[i])
print('Ответ на 2 задание:', summ, sep=" ")

# 3 задание
s = '1' + '8'*80
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2', 1)
    else:
        if '288' in s:
            s = s.replace('288', '3', 1)
        else:
            s = s.replace('3888', '1', 1)
print('Ответ на 3 задание:', s, sep=" ")

# 4 задание
s = '8'*99 + '1'
while '113' in s or '881' in s:
    if '133' in s:
        s = s.replace('133', '81', 1)
    else:
        s = s.replace('881', '13', 1)
print('Ответ на 4 задание:', s, sep=" ")

# 5 задание
s = '1' + '9'*98
while '19' in s or '299' in s or '3999' in s:
    s = s.replace('19', '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print('Ответ на 5 задание:', s, sep=" ")
