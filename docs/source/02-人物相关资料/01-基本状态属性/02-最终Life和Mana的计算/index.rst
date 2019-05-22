最终Life和Mana的计算
===============================================================================

以 life 为例，life 和 mana 道理相同。

``life =（base_life + equip_life）*（1 + amplifier %）+ equip_stamina * stamina_multiplier + gear_life``

解释各个参数意义如下：

- ``base_life``：char的基本life: 包括1级时获得的life，升级时获得的life 奖励，act3 quest1的20life任务奖励，靠stat升在活力上获得的life。
- ``equip_life``：装备和charm上的+life之和。
- ``amplifier``：各种+max life%的技能（如bo，dru的变身，招灵等）和装备（如tp+的%max life）之和。
- ``equip_stamina``：装备和charm上 + 耐力（包括+所有属性）之和。
- ``gear_life``：装备上的+life之和，gear_life 和 equip_life 的区别是 gear_life 是 + life based on char‘s lvl (根据级别+life的属性)。
- ``stamina_multiplier`` : 一点活力对应x点life，因char而异。
