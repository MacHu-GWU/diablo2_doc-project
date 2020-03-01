# -*- coding: utf-8 -*-

"""
Data is from Google Sheet ``Diablo2-Data-Set``
"""

from . import char
from . import ias_fcr_fbr_fhr_frw

doc_data = dict(
    lt_base_stats_each_class=char.lt_base_stats_each_class,
    lt_hit_factor_for_each_class=char.lt_hit_factor_for_each_class,
    lt_move_speed_vs_frw=char.lt_move_speed_vs_frw,
    lt_fcr=ias_fcr_fbr_fhr_frw.lt_fcr,
    lt_ias_ama_bow=ias_fcr_fbr_fhr_frw.lt_ias_ama_bow,
    lt_ias_ama_crossbow=ias_fcr_fbr_fhr_frw.lt_ias_ama_crossbow,
    lt_ias_ama_jav=ias_fcr_fbr_fhr_frw.lt_ias_ama_jav,
    lt_ias_pal_normal_attack_with_20_fana=ias_fcr_fbr_fhr_frw.lt_ias_pal_normal_attack_with_20_fana,
    lt_ias_pal_smith_with_20_fana=ias_fcr_fbr_fhr_frw.lt_ias_pal_smith_with_20_fana,
    lt_ias_pal_zeal_with_20_fana=ias_fcr_fbr_fhr_frw.lt_ias_pal_zeal_with_20_fana,
)
