ad_year = int(input())
bd_year = ad_year + 543

str_ad, str_bd = str(ad_year), str(bd_year)
each_ad_num, each_bd_num = [], []
ad_ans, bd_ans = 0, 0

for i, j in zip(str_ad, str_bd):
    each_ad_num.append(int(i))
    each_bd_num.append(int(j))

for i in str_ad:
    for j in str(i):
        ad_ans += int(j)
    each_ad_num.append(ad_ans)

for i in str_bd:
    for j in str(i):
        bd_ans += int(j)
    each_bd_num.append(bd_ans)
    
print(bd_year)
print(ad_ans)
print(bd_ans)