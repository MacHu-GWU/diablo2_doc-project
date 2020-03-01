# -*- coding: utf-8 -*-

"""
Data is from Google Sheet ``Diablo2-Data-Set``
"""

import logging

try:
    from . import char
except Exception as e:
    logging.warning(str(e))

doc_data = dict(
    lt_base_stats_each_class=char.lt_base_stats_each_class,
    lt_hit_factor_for_each_class=char.lt_hit_factor_for_each_class,
    lt_move_speed_vs_frw=char.lt_move_speed_vs_frw,
)
