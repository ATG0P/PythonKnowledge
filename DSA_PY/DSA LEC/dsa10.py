'''given a num array, make a dictionary where numbers(items):no of times numbers are repeated(key)'''
#Method 1 (brutal)
# num = [5,6,7,7,1,9,111,1,1,5,1,1]
# dic={}
# for i in num:
#     n=num.count(i)
#     dic[i] = n
#     n=0
# print(dic)
# print(type(dic))#T.C = O(n^2)

# #Method 2 
# num = [5,6,7,7,1,9,111,1,1,5,1,1]
# freq_map={}
# for i in range(0,len(num)):
#     if num[i] in freq_map:
#         freq_map[num[i]]+=1
#     else:
#         freq_map[num[i]]=1
# print(freq_map) #T.C=O(n)    #S.C=O(n)



#method-3: using hashmap
#before moving to method 3, let's talk abt get() in dictionary
