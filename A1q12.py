s1,s2,s3=input('Enter the sides=').split()
print(s1,s2,s3)

if s1==s2 and s2==s3:
    print('Triangle is equilateral')
elif s1==s2 or s2==s3 or s1==s3:
    print('Triangle is iscoscles')
else:
    print('Triangle is Scalene')