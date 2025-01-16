from dict_import import dict_import

dict_path = '../datasets/THUOCL-master/data/'
dict_categories = ['animal', 'caijing','car','chengyu','diming','food','IT','law','lishimingren','medical', 'poem']
sub_name = 'THUOCL_'
dict_all = dict_import(dict_categories, dict_path,sub_name)

while True:
    token_result = ''
    user_input = input("请输入待分词中文段: ")
    if user_input == 'exit':
        break
    p_start = 0
    while p_start < len(user_input):
        p_end = len(user_input)
        while p_end > p_start:
            if user_input[p_start:p_end] in dict_all:
                token_result += user_input[p_start:p_end] + '/'
                break
            else:
                p_end -= 1
        if p_end == p_start:
            token_result += user_input[p_start:p_end+1] + '/'
            p_start += 1
        else:
            p_start = p_end
    print(f"分词结果：{token_result}")