import os
import re


def removing_extra_characters(user_list):
    if len(user_list) != 0:
        for index in range(len(user_list)):
            user_list[index] = re.sub(r'\D', r'', user_list[index])
        return list(filter(None, user_list))
    else:
        pass


def returned_contract(user_list):
    for index in range(len(user_list)):
        user_list[index] = user_list[index] + ';;;;;'
    change_text = '\n'.join(user_list)
    return change_text


def returned_ls(user_list):
    for index in range(len(user_list)):
        user_list[index] = ';' + user_list[index] + ';;;;'
    change_text = '\n'.join(user_list)
    return change_text


def returned_po(user_list):
    for index in range(len(user_list)):
        if len(user_list[index]) > 10:
            user_list[index] = ';;' + user_list[index] + ';;;'
        else:
            user_list[index] = ';;7' + user_list[index] + ';;;'
    change_text = '\n'.join(user_list)
    return change_text


def remove_symbol(user_list, removing_symbol):
    for index in range(len(user_list)):
        for symbol in removing_symbol:
            user_list[index] = user_list[index].replace(symbol, '')
    change_text = '\n'.join(user_list)
    return change_text


def replace_symbol(user_list, replace_symbol, symbol_after_replacement):
    for index in range(len(user_list)):
        user_list[index] = user_list[index].replace(replace_symbol, symbol_after_replacement)
    change_text = '\n'.join(user_list)
    return change_text


def delete_7_numbers_zgp(user_list):
    if len(user_list) != 0:
        for index in range(len(user_list)):
            user_list[index] = user_list[index][1:]
        change_text = '\n'.join(user_list)
        return change_text
    else:
        pass


def copy_clipboard(user_list, number):
    if len(user_list) != 0:
        onehundred = user_list[0:number]
        onehundred_text = '\n'.join(onehundred)
        return onehundred_text
    else:
        pass


def remains(user_list, number):
    if len(user_list) > 100:
        remains = user_list[number:]
        remains_list = '\n'.join(remains)
        return remains_list
    else:
        return ''


def cropping_first_func(user_list, number_characters):
    for index in range(len(user_list)):
        user_list[index] = user_list[index][number_characters - 1:]
    change_text = '\n'.join(user_list)
    return change_text


def cropping_last_func(user_list, number_characters):
    for index in range(len(user_list)):
        user_list[index] = user_list[index][0:number_characters]
    change_text = '\n'.join(user_list)
    return change_text


def removing_spaser(user_list):
    if len(user_list) != 0:
        for index in range(len(user_list)):
            user_list[index] = re.sub(r'\s', r'', user_list[index])
        return list(filter(None, user_list))
    else:
        pass


