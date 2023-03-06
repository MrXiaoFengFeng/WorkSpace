#
# 作用：
# # 元组与列表类似，也是可以存多个任意类型的元素，不同之处在于元组的元素不能修改，即元组相当于不可变的列表，用于记录多个固定不允许修改的值，单纯用于取
# 定义方式：
# # 在()内用逗号分隔开多个任意类型的值
# # >>> countries = ("中国"，"美国"，"英国")  # 本质:countries = tuple("中国"，"美国"，"英国")
# # # 强调：如果元组内只有一个值，则必须加一个逗号，否则()就只是包含的意思而非定义元组
# # >>> countries = ("中国"，)  # 本质:countries = tuple("中国")
# 类型转换：
# # 但凡能被for循环的遍历的数据类型都可以传给tuple()转换成元组类型
# >>> tuple('wdad') # 结果：('w', 'd', 'a', 'd')
# >>> tuple([1,2,3]) # 结果：(1, 2, 3)
# >>> tuple({"name":"jason","age":18}) # 结果：('name', 'age')
# >>> tuple((1,2,3)) # 结果：(1, 2, 3)
# >>> tuple({1,2,3,4}) # 结果：(1, 2, 3, 4)
# # tuple()会跟for循环一样遍历出数据类型中包含的每一个元素然后放到元组中