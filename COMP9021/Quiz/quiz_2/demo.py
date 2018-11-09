"""
n = num = int(input('请输入一个数字：'))  #用num保留初始值
f = []  #存放质因数的列表
 
for j in range(int(num/2)+1):  #判断次数仅需该数字的一半多1次
    for i in range(2, n+1):
        t = n % i  #i不能是n本身
        if t == 0:  #若能整除
            f.append(i)  #则表示i是质因数
            n = n//i  #除以质因数后的n重新进入判断，注意应用两个除号，使n保持整数
            break  #找到1个质因数后马上break，防止非质数却可以整除的数字进入质因数列表
 
if len(f) == 0:  #若一个质因数也没有
    print('该数字没有任何质因数。')
else:  #若至少有一个质因数
    f.append(n)  #此时n已被某个质因数整除过，最后一个n也是其中一个质因数
    f.sort()  #排下序
    f.remove(1)
    print(f)
"""
print(1)

def find_prime_factors(num):
    n = num 
    f = []  
    for j in range(int(num / 2) + 1):  
        for i in range(2, n + 1):
            t = n % i  
            if t == 0:  
                f.append(i)  
                n = n // i  
                break  
    f.append(n)  
    f.sort()  
    f.remove(1)

    result = []
    i = 0
    j = 1
    while i < len(f):
        cnt = 1
        while j < len(f): 
            if f[i] == f[j]:
                cnt += 1
                j += 1
            else:
                # print("f[i]", f[i])
                # print("i:",i)
                # print("j:",j)
                result.append((f[i], j - i))
                i = j
                continue
        result.append((f[i], j - i))
        break
    return result

print(find_prime_factors(96))
print(find_prime_factors(7))
print(find_prime_factors(216))
print(find_prime_factors(21))


