#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_common/naming.py
# @DATE: 2023/08/11 周五
# @TIME: 17:55:07
#
# @DESCRIPTION: 命名相关的工具方法


def underscore_to_camelcase(underscore_str: str):
    """
    @description: 下划线命名转小驼峰
    @param {str} underscore_str: 下划线命名字符串
    @return {str}: 小驼峰命名字符串
    """
    # 1. 拆分
    str_list = underscore_str.split("_")
    # 2. 转换
    camelcase_str = ""
    for index, item in enumerate(str_list):
        if index == 0:
            camelcase_str += item
        else:
            camelcase_str += item.capitalize()
    # 3. 返回
    return camelcase_str

def underscore_to_big_camelcase(underscore_str: str):
    """
    @description: 下划线命名转大驼峰
    @param {str} underscore_str: 下划线命名字符串
    @return {str}: 大驼峰命名字符串
    """
    # 1. 拆分
    str_list = underscore_str.split("_")
    # 2. 转换
    camelcase_str = ""
    for item in str_list:
        camelcase_str += item.capitalize()
    # 3. 返回
    return camelcase_str

def camelcase_to_underscore(camelcase_str: str):
    """
    @description: 小驼峰命名转下划线命名
    @param {str} camelcase_str: 小驼峰命名字符串
    @return {str}: 下划线命名字符串
    """
    # 1. 拆分
    str_list = []
    temp_str = ""
    for index, item in enumerate(camelcase_str):
        if item.isupper():
            if index == 0:
                str_list.append(item.lower())
            else:
                str_list.append(temp_str.lower())
                temp_str = item
        else:
            temp_str += item
    str_list.append(temp_str.lower())
    # 2. 拼接
    underscore_str = "_".join(str_list)
    # 3. 返回
    return underscore_str

def camelcase_to_big_underscore(camelcase_str: str):
    """
    @description: 大驼峰命名转下划线命名
    @param {str} camelcase_str: 大驼峰命名字符串
    @return {str}: 下划线命名字符串
    """
    # 1. 拆分
    str_list = []
    temp_str = ""
    for index, item in enumerate(camelcase_str):
        if item.isupper():
            if index == 0:
                temp_str = item
            else:
                str_list.append(temp_str)
                temp_str = item
        else:
            temp_str += item
    str_list.append(temp_str)
    # 2. 拼接
    underscore_str = "_".join(str_list)
    # 3. 转小写
    underscore_str = underscore_str.lower()
    # 4. 返回
    return underscore_str


# 单体测试
if __name__ == "__main__":
    print(underscore_to_camelcase("hello_world"))
    print(underscore_to_big_camelcase("hello_world"))
    print(camelcase_to_underscore("helloWorld"))
    print(camelcase_to_big_underscore("HelloWorld"))
