赌博
===============================================================================
赌博时, 每次与 NPC 说话, 供赌博的物品都会被刷新. 供赌博的物品的生成过程如下:

1. 生成基础级(Base)物品

生成的基础级物品的 Qlvl 不高于 Clvl+4 .生成的基础级物品的 Ilvl 在 Clvl-5 到 Clvl+4 之间随机.

Clvl:赌博者的等级

关于 Qlvl 请看这里
关于 Ilvl 请看这里

赌博不会生成除刺客爪子之外的角色专用物品。

2. 基础级物品升级成扩展级(Exceptional)物品

升级成扩展级的概率为:

Excep% = (1 + (Ilvl - Excep_Qlvl) * 0.9)%

其中 Excep_Qlvl 为基础级物品对应的扩展级物品的Qlvl. 若 Ilvl < Excep_Qlvl, 则不会发生升级.

3. 扩展级物品升级成精华级(Elite)物品

升级成精华级的概率为:

Elite% = (1 + (Ilvl - Elite_Qlvl) * 0.33)%

其中 Elite_Qlvl 为扩展级物品对应的精华级物品的Qlvl. 若 Ilvl < Elite_Qlvl, 则不会发生升级.

4. 物品成色的决定

v1.10和beta相比，作了少许调整：

- magic: 89.85%
- rare: 10%
- set: 0.1%
- unique: 0.05%

5. 对亮金和蓝色物品选择词缀

**相关FAQ**：

1. mf对gamble的成色判断有影响吗？游戏人数对gamble有影响吗？

没有，没有

2. 不同的难度和npc对gamble有区别吗？

他们唯一的区别就是赌博出的物品再sell回去的价钱

3. 如果物品的ilvl足够支持它的qlvl，但不足以支持该物品的unique形态，将会如何．

物品被降格为rare，并且耐久度变为3倍

4. circlets, coronets, tiaras，diadems 是如何划分扩展和精华的？

- circlet -> tiara -> diadem
- coronet -> tiara -> diadem

如果系统生成一个coronet，并且成功的升级为tiara（或者diadem），在图象上仍会保留coronet的形象。

注：circlet不会升级为tiara或diadem。

5. gamble会得到白色物品吗？

不会

6. gamble会得到ethreal形态物品吗？

不会, 除非是那几个天生eth的unique物品
