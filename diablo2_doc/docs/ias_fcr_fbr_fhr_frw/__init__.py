# -*- coding: utf-8 -*-

from diablo2_doc.helpers import read_list_table

lt_fcr = read_list_table(__file__, "FCR 施法速度表", "fcr.tsv")
lt_ias_ama_bow = read_list_table(__file__, "IAS 弓 攻速表", "ama-bow.tsv")
lt_ias_ama_crossbow = read_list_table(__file__, "IAS 十字弓 攻速表", "ama-crossbow.tsv")
lt_ias_ama_jav = read_list_table(__file__, "IAS 标枪 攻速表", "ama-jav.tsv")
lt_ias_pal_normal_attack_with_20_fana = read_list_table(__file__, "圣骑士普通攻击速度表", "pal-normal-attack-with-20-fana.tsv")
lt_ias_pal_smith_with_20_fana = read_list_table(__file__, "圣骑士重击攻击速度表", "pal-smith-with-20-fana.tsv")
lt_ias_pal_zeal_with_20_fana = read_list_table(__file__, "圣骑士热诚攻击速度表", "pal-zeal-with-20-fana.tsv")

if __name__ == "__main__":
    print(lt_ias_pal_smith_with_20_fana.render().replace(".0", ""))
