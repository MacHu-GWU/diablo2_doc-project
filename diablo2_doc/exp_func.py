# -*- coding: utf-8 -*-

"""
人物和怪物等级之间的计算公式

- CLVL = Char Level
- MLVL = Monster Level

若CLVL < 25::

    CLVL-MLVL    exp％ 
    0-5            100
    6            81
    7            62
    8            43
    9            24
    10或10以上    5

    MLVL-CLVL    exp％
    0-5            100
    6            88
    7            68
    8            36
    9            15
    10或10以上    2

若CLVL >= 25::

    CLVL-MLVL    exp％ 
    0-5            100
    6            81
    7            62
    8            43
    9            24
    10或10以上    5

    MLVL-CLVL    exp％
    0-99        (CLVL/MLVL)
"""
from collections import OrderedDict

monster_base_exp_table = OrderedDict()
 
for i in range(1, 100+1):
    monster_base_exp_chart[i] = i * 100

def find_party_exp_ratio(mlvl, plvl_list):
    """计算组队状态下, 怪物的基础经验值加成。
    """
    counter = 0
    for plvl in plvl_list:
        if abs(plvl - mlvl):
            counter += 1
    if counter >= 2:
        ratio = 1.0 + (counter - 1) * 0.15
    else:
        ratio = 1.0
    return ratio

gained_party_exp = monster_base_exp

gained_exp = gained_monster_exp
    
mlvl = 50
plvl_list = [45, 47, 50, 52, 55]
mylvl = 50

monster_base_exp = monster_base_exp_table[mlvl] 
ratio = find_party_exp_ratio(mlvl, plvl_list)
shared_exp = monster_base_exp * ratio / len(plvl_list)

gained_exp = shared_exp 

# def find_gained_exp(shared_exp, ):
{
    7: 1.2,
    6: 1.2,
    5: 1.2,
    4: 1.1,
    3: 1.1,
    2: 1.0,
    1: 1.0,
    0: 1.0,
    -1: 1.0,
    -2: 1.0,
    -3: 0.8,
    -4: 0.8,
    -5: 0.8, 
}

def find_gained_exp(plvl, mlvl, partylvl_list=None):
    monster_base_exp = monster_base_exp_table[mlvl]
    
    # 非组队状态
    if partylvl_list is None:
        shared_exp = monster_base_exp
    
    # 组队状态
    else:
        counter = 0
        for playerlvl in partylvl_list:
            if abs(playerlvl - mlvl) <= 5:
                counter += 1
        ratio = 1.0 + counter * 0.15
        shared_exp = monster_base_exp * ratio / (len(partylvl_list) + 1) 

    

