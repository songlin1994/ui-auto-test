#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tools.make_addr import make_addr
from tools.make_id_card_number import make_id
from tools.make_name import make_name
from tools.make_phone import random_phone


def make_info():
    id_num = make_id()
    info_dic ={"身份证号":id_num}
    sex = ''
    if int(id_num[14:-1]) % 2 == 0:
        sex = '女'
    else:
        sex='男'
    info_dic['性别'] = sex
    info_dic['手机号'] = random_phone()
    info_dic['地址'] = make_addr(id_num)
    info_dic['姓名'] = make_name()
    return info_dic


if __name__ == '__main__':
    print(make_info())
