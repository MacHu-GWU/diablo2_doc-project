# -*- coding: utf-8 -*-

from diablo2_doc.helpers import read_list_table

lt_exp_table = read_list_table(__file__, "升级所需经验表", "exp_table.tsv")
lt_exp_level_penalty = read_list_table(__file__, "经验随着等级衰减惩罚系数表", "exp_level_penalty.tsv")
lt_exp_level_diff_penalty_below_25 = read_list_table(__file__, "在25级以下时玩家与怪物等级差经验系数表", "exp_level_diff_penalty_below_25.tsv")
lt_exp_level_diff_penalty_above_25 = read_list_table(__file__, "在25级以上时玩家与怪物等级差经验系数表", "exp_level_diff_penalty_above_25.tsv")

if __name__ == "__main__":
    print(lt_exp_level_diff_penalty_above_25.render())