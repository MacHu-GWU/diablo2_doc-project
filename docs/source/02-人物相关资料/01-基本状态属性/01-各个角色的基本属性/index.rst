.. _各个角色的基本属性:

各个角色的基本属性
===============================================================================

缩略语:

- Str: Strength, 力量.
- Dex: Dexterity, 敏捷.
- Vit: Vitality, 体力.
- Eng: Energy, 能量.
- Sta: Stamina, 精力.
- Life: 生命
- Mana: 法力
- L/L: Life Per Level, 每升一级增加的生命.
- M/L: Mana Per Level, 每升一级增加的法力.
- S/L: Stamina Per Level, 每升一级增加的精力
- L/V: Life Per Vitality, 每加一点Vit增加的生命.
- M/E: Mana Per Energy, 每加一点Eng增加的法力.

下表中的 Str, Dex, Vit, Eng, Sta, Life, Mana 都是各个角色起始的状态.

.. jinja:: doc_data

    {{ doc_data.lt_base_stats_each_class.render() }}


.. _各个角色的基础命中率和基础防御力:

各角色的 基础命中率 (Attack Rating) 和 基础防御力 (Defence)
-------------------------------------------------------------------------------

``Base_Attack_Rating`` = ``Dex`` * 5 - 35 + ``To_Hit_Factor``

``To_Hit_Factor`` 就是一个根据职业的固定修正值, 具体数值为:

.. jinja:: doc_data

    {{ doc_data.lt_hit_factor_for_each_class.render() }}

``Base_Defence`` = [ ``Dex`` / 4 ], 方括号表示向下取整数.
