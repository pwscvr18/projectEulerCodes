#Problem1.py
#find the sum of all multiples of 5 and 3 between 1 and 1000
 
min_num=1
max_num=1000-1
def arithmetic_series_sum(first_num,max_num):
    print("number:",first_num)
    series_last_num=max_num-(max_num%first_num)
    multiples=series_last_num/first_num
    series_sum=multiples/2*(first_num+series_last_num)
    print(series_sum)
    return series_sum
total_sum=arithmetic_series_sum(3,max_num)+arithmetic_series_sum(5,max_num)
print(total_sum)