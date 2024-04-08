dic={1:30,2:10,3:20}
a=10
# d2=sorted(dic.items(),key = lambda t:t[1],reverse=True)



# for i in range(len(d2)):
#     if d2[i][1]==a:
#         print('present')
#     else:
#         print('not present')
    

l1=list(dic.keys())

for i in range(len(dic)):
    if dic[l1[i]]==a:
        print('present')


