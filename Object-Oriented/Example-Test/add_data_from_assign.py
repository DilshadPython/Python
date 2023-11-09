from assignments import MaxSizeList
from best_assign import LanguageList

a_obj = MaxSizeList(4)
b_obj = MaxSizeList(2)

a_obj = LanguageList(4)
b_obj = LanguageList(2)

a_obj.push('Python')
a_obj.push('Javas')
a_obj.push('C++')
a_obj.push('JavaScript')

b_obj.push('A')
b_obj.push('B')
b_obj.push('C')
b_obj.push('D')
b_obj.push('E')
b_obj.push('F')



print(a_obj.get_list())
print('\n', b_obj.get_list())