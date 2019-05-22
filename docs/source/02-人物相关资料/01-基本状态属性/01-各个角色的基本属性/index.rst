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

下表中的 Str,Dex,Vit,Eng,Sta,Life,Mana 都是各个角色起始的状态.

.. list-table:: 各角色起始状态的基础属性
   :widths: 15 15 15 15 15 15 15 15 15 15 15 15 15 
   :header-rows: 1
   
   * - 角色
     - Str
     - Dex
     - Vit
     - Eng
     - Sta
     - Life
     - Mana
     - L/L
     - M/L
     - S/L
     - L/V
     - M/E
   * - Ama
     - 20
     - 25
     - 20
     - 15
     - 84
     - 50
     - 15
     - 2
     - 1.5
     - 1
     - 3
     - 1.5
   * - Sor
     - 10
     - 25
     - 10
     - 35
     - 74
     - 40
     - 35
     - 1
     - 2
     - 1
     - 2
     - 2
   * - Nec
     - 15
     - 25
     - 15
     - 25
     - 79
     - 45
     - 25
     - 1.5
     - 2
     - 1
     - 2
     - 2
   * - Pal
     - 25
     - 20
     - 25
     - 15
     - 89
     - 55
     - 15
     - 2
     - 1.5
     - 1
     - 3
     - 1.5
   * - Bar
     - 30
     - 20
     - 25
     - 10
     - 92
     - 55
     - 10
     - 2
     - 1
     - 1
     - 4
     - 1
   * - Dru
     - 15
     - 20
     - 25
     - 20
     - 84
     - 55
     - 20
     - 1.5
     - 2
     - 1
     - 2
     - 2
   * - Asn
     - 20
     - 20
     - 20
     - 25
     - 95
     - 50
     - 25
     - 2
     - 1.5
     - 1.25
     - 3
     - 1.75

各角色的基础命中率(Attack Rating)和防御力(Defence)
-------------------------------------------------------------------------------

``Base_Attack_Rating`` = ``Dex`` * 5 - 35 + ``To_Hit_Factor``

``To_Hit_Factor`` 为:

.. list-table:: 各角色的To_Hit_Factor
   :widths: 15 15 15 15 15 15 15 15
   :header-rows: 0

   * - class  
     - Ama
     - Sor
     - Nec
     - Pal
     - Bar
     - Dru
     - Asn
   * - Factor 
     - 5 
     - -15
     - -10
     - 20
     - 20
     - 5
     - 15

``Base_Defence`` = [``Dex`` / 4], 方括号表示向下取整数.