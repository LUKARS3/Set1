s11, s22 = map(str, input().split())
# zero_pop = len(s2)
if len(s11) < len(s22):
    s = len(s11)
    zero_pop = len(s22)
else:
    s = len(s22)
    zero_pop = len(s11)
lst1 = list('0') * zero_pop
for i1 in range(s):
    if s22 in s11 or s11 in s22:
        lst1[i1] = '1'
    if s11[i1] == s22[i1]:
        lst1[i1] = '1'

print(lst1.count('0'))
# print(lst)
