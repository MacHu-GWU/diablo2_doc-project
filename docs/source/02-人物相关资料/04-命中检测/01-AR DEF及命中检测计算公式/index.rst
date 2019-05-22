AR DEF及命中检测计算公式
===============================================================================


Defence: 防御值
-------------------------------------------------------------------------------


玩家
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DR1 = [(armor class + base defense) + (armor class + base defense) × item_armor_percent%] × Armor_override_percent

* armor class: 装备提供的总防御值
* base defense: int(Dexterity/4)
* item_armor_percent%: 提升防御值的%，包括各种技能、非防具上的(如武器Ribcracker Quarterstaff上的，技能holyshield、各种冰甲等)
* Armor_override_percent: = 0，特指Bar的Berserk技能

DR2 = DR1 + Def Vs Missile / Def Vs Melee

* 可以看到，如果在使用Berserk技能时，如果装备提供 ``Def Vs Missile`` 或 ``Def Vs Melee``，此时的防御值并不是我们所想象的那样为0。


怪物
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DR2 = AC_MonStats.txt × AC%_MonLvl.txt × (1 + Other%)

* other%: 如Stone Skin属性


佣兵
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DR2 = [Defense + int[△Hlvl × (Def / Lvl)] + int(Dexterity / 4) + Item_Defense] × (1 + Other%)

* Defense: 基础等级的防御值(CF Hireling.txt)
* △Hlvl: 与基础等级的等级差
* Def/Lvl: 防御/等级因子(CF Hireling.txt)
* Dexterity: 敏捷，包括自身和装备提供的
* Item_Defense: 装备提供的防御
* Other%: 非装备提供的防御%


玩家的各种Minion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
可以从Skills.txt，MonStats.txt中得到各种Minion的具体防御值，当然如女武神、影子等可以通过装备/技能(如Shadow使用魔影斗篷)得到提升，不一一赘述。


Attack Rating: 攻击准确率
-------------------------------------------------------------------------------


玩家
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
①AR1 = Dexterity × 5 + Tohit - (35) + ToHitFactor(CF Charstats.txt)

* Tohit: 直接加的AR，即 ``+x to attack rating`` 属性

②调用ITD和Fractional Target AC程序段

ITD

仅对怪物有效

如果目标品质 = 0A，则无效

如果目标是eBoss(CF Monstat.txt)，则无效

如果目标是佣兵，则无效

*0A的范围不能确定，应该是超级金怪(CF superuniques.txt)和随机金怪以及对冠军级Champion怪物。

*关于ITD的被作用对象，会另文讨论，v1.10时Myrdinn对此做过hardcoded的程序解析，我有空会试着做下v1.11b的解析。

Fractional AC

- Target Defense X%(即如ETH Rune):
-
如果目标为玩家(可能包括玩家的minions和summoner)、佣兵或者eBoss怪物，则效果减半

上限为100%

DR = DR2 - DR2 × (X/100)

* 这里Myrdinn可能漏看了些程序段，如的-def(如Inner Sight，-X to target defense per hit)和-%def(Skill)(如Cloak of Shadows/Battle Cry/Conviction等)；

实际计算时-def为: armorclass = armorclass - def - %def(Skill): armorclass + basedefense = (armorclass + basedefense) - (armorclass + basedefense) × %def(Skill)

Monster Specifics AR%: 对特定怪物的AR%奖励

如果怪物为Demon，则AR%(Skill) = AR%(Skill) + item_demon_tohit
如果怪物为Undead，则AR%(Skill) = AR%(Skill) + item_Undead_tohit

* item_demon_tohit: +X To Attack Rating Against Vs Demon
* item_Undead_tohit: +X To Attack Rating Against Vs Demon
* 是的，以上都算AR%，而不是+AR —— 这个测试验证起来比较简单

是否为Attack ranged范围攻击

如果是，则忽略AR%(Mastery)

* AR%(Mastery): Bar的各种武器掌握，Asn的爪掌握

所以如Bar的Double Throw，Asn的Blade Fury/Blade Sentinel不能从其Weapon Mastery上的AR%属性处得到AR%加成 —— 这个我之前在Ranged Attack Skills上的Attack Rating% bonuses中已经做过测试验证

③AR% = AR% (Mastery + Skill + item_tohit_percent + attack_vs_montype + item_demon_tohit + item_Undead_tohit)

* AR%(Mastery): Bar的各种武器掌握，Asn的爪掌握
* AR%(Skill): 技能提供的AR%，如Blessed Aim/Enchant
* AR%(item_tohit_percent): 装备提供的AR%
* AR%(attack_vs_montype): 对不同怪物类型提升的AR%奖励
* AR%(item_demon_tohit): 前面已经解释过
* AR%(item_Undead_tohit): 前面已经解释过


怪物
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AR = ToHit + Tohit(Skill) + 5 × Dexterity

* ToHit:
    * Monster: TH_MonStats.txt×TH%_MonLvl.txt;
    * Mercenary: [AR + int[△Hlvl×(AR/Lvl)]，CF Hireling.txt;
    * Play's Minion: CF Skills.txt & MonStats.txt，不一一赘述
* Tohit(Skill): 技能上直接加的AR
* 5×Dexterity: 此处应该是指Mercenary(佣兵也属于怪物的一种)，Myrdinn认为此处的敏捷是指装备提供的，佣兵自身的敏捷不算在内，但我认为如防御计算一样，自身和装备提供的敏捷都参与计算; Play's Minion(如Asn的Shadow自身提供的，Shadow/Valkyrie装备提供的)是否能从敏捷上得到加成未能确定 —— 也许需要测试验证，但是忒有难度了

AR% = item_tohit_percent (No Skill Bonus)
* item_tohit_percent: 装备上的AR%，此处应该是指Mercenary、Asn的Shadow、Ama的Valkyrie等
* No skill Bonus: 技能上的AR%，这个有点晕，雇主或结盟成员的技能上(如Blessed Aim/Fanaticism/Heart of Wolverine)提供的AR%对佣兵，Nec的骷髅等都是没有用的？

即便如Duriel的Jab，ACT2 Pet本身的Jab/Blessed Aim都不能得到AR%加成？

怪物自身的Blessed Aim/Fanaticism等特殊属性的AR%也是没作用的？

或者说上面AR中的Tohit(Skill)，这个已经是经过AR%(Skill)提升后的AR

——需要做些测试验证


最终攻击准确率
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Final AR = AR + AR × (AR% / 100)


ToHit Formula: 命中率公式
-------------------------------------------------------------------------------
检测参数

如果DR<0，则AR = AR - DR且DR = 0，*即Tohit% = 2 × [ALVL / (ALVL + DLVL)] × 100

如果AR<0，则DR = DR - AR且AR = 0，*即命中率为下限5%

如果DR<0，则AR = AR - DR(如果AR和DR都<0，将进行二次检测)，*即Tohit% = 2 × [ALVL / (ALVL + DLVL)] × 100

* 如检测到防守者为Running状态，则跳过ToHit%程序，即100%命中。

命中率公式

Tohit% = 2 × [ALVL / (ALVL + DLVL)] × 100 × [AR / (AR + DR)]

* ALVL: 攻击者等级
* DLVL: 防守者等级
* AR: 攻击者的最终攻击准确率
* DR: 防守者的最终防御值
* 命中率下限为5%，上限为95%

击中后

攻击者调用PMH子程序段

防守者调用Block/Evade等子程序段