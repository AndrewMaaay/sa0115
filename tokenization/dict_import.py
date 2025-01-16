from typing import List, Set


def dict_import(dict_list: List[str],file_path:str,sub_name:str) -> Set[str]:
    word_dict = set()
    for dict_category in dict_list:
        with open(file_path +sub_name+ dict_category +'.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            word_dict.add(line.strip().split('\t')[0])
    return word_dict