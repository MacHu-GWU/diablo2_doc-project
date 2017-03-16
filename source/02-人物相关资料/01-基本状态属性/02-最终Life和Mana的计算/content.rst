最终Life和Mana的计算
===============================================================================
以life为例，life和mana道理相同。

``life =（a + b）*（1 + c%）+ d * x + e``

解释各个参数意义如下：

- ``a``：char的基本life: 包括1级时获得的life，升级时获得的life 奖励，act3 quest1的20life任务奖励，靠stat升在活力上获得的life。
- ``b``：装备和charm上的+life之和。
- ``c``：各种+max life%的技能（如bo，dru的变身，招灵等）和装备（如tp+的%max life）之和。
- ``d``：装备和charm上+活力（包括+所有属性）之和。
- ``e``：装备上的+life之和，e和b的区别是e是+life based on char‘s lvl(根据级别+life)。
- ``x`` : 一点活力对应x点life，因char而异。