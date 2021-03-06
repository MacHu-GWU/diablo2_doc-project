.. _多人游戏对怪物各个属性的影响:

多人游戏对怪物各个属性的影响
===============================================================================
设游戏内的人数为N

**游戏人数会影响怪物的生命值**::

    怪物实际生命值 = 怪物初始生命 * (N + 1) / 2

**游戏人数会影响怪物的经验值**::

    怪物实际经验值 = 怪物初始经验 * (N + 1) / 2

详细计算请看 :ref:`Experience计算的详细流程 <经验获取的详细流程>`。

**游戏人数会影响怪物的伤害值DAM和攻击准确率AR**:

- 普通难度下，怪物的DAM/AR恒定
- 噩梦和地狱难度下，怪物的DAM/AR随人数增加，具体计算公式为::

    怪物实际DAM = 怪物基础DAM * [1 + (N - 1) / 16]
    怪物实际AR = 怪物基础AR * [1 + (N - 1) / 16]


- 需要注意的是，这个奖励跟Champion、Extra Strong属性的伤害/奖励是独立的。如果二者同时存在，则分别计算怪物 ``实际DAM/AR = 基础数值 x Champion / Unique属性奖励 × 游戏人数奖励``

**游戏人数会影响人物的冰冻持续时间**:

- 普通难度下，怪物普通攻击附加的冰冻持续时间恒定
- 噩梦和地狱难度下，附加的冰冻持续时间随人数增加，具体计算公式为::

    怪物普通攻击附加的实际冰冻持续时间 = 怪物原始冰冻持续时间 * [1 + (N - 1) / 16]
    怪物原始冰冻持续时间详见全怪物资料.

**游戏人数会影响人物的中毒持续时间**:

- 普通难度下，怪物普通攻击附加的中毒持续时间为原始中毒持续时间*2.
- 噩梦和地狱难度下，附加的中毒持续时间随人数增加，具体计算公式为::

    怪物普通攻击附加的实际中毒持续时间 = 怪物原始中毒持续时间 * 2 * [1 + (N - 1) / 16]
    怪物原始中毒持续时间详见全怪物资料.

**游戏人数会影响物品掉落的几率**:

对普通怪物、仆从和Boss来说，都有一定比例的Nodrop率，即不掉物品的概率。游戏人数增加会降低这个比率。具体请看多人游戏对物品掉落的影响。

对头目级和暗金级怪物来说，Nodrop率为0，所以它们的掉率不受游戏人数影响。

游戏人数不会影响掉落物品的成色判断。

**游戏人数对怪物属性的额外奖励表格**::

    =============================
    人数   生命/经验值    DAM/AR
    -----------------------------
    1           0           0
    2         50%       6.25%
    3        100%      12.50%
    4        150%      18.75%
    5        200%      25.00%
    6        250%      31.25%
    7        300%      37.50%
    8        350%      43.75%
    =============================
