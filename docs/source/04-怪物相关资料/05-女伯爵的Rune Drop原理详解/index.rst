.. _女伯爵的RuneDrop原理详解:

女伯爵的Rune Drop原理详解
===============================================================================
女伯爵除了普通的掉物品(Item Drop)外, 还有额外的掉神符特性(Rune Drop)。

Rune Drop 最多掉出3个神符。

不同难度下, 她的 Rune Drop 所能掉的最高神符分别为:

- 普通----8 (Ral)
- 噩梦----16 (Io)
- 地狱----24 (Ist)

这并不是说她不能掉更高的神符, 只是更高的神符只能从 Item Drop 中掉出, 而不能从 Rune Drop 中掉出, 因此出现几率是非常非常小的。

当她死时, 先发生 Item Drop, 这部分与其它金怪没什么差别。随后将是她的 Rune Drop过程.

地狱难度里, 她的 Rune Drop 对应的 TC 为 "Countess Rune (H)", 结构如下:

选择次数为3, 选择不掉神符的相对几率为 5, 选择 TC "Runes 12" 的相对几率为15. 也就是说, 在这一步骤里, 选择不掉神符的几率为 5/(5+15) = 25%, 选择 TC"Runes 12" 的几率为 75%. 总共进行三次选择.


TC "Runes 12" 结构如下:
-------------------------------------------------------------------------------
选择次数为1, 选择 Mal(23) 的相对几率为 3, 选择 Ist(24) 的相对几率为 2,

选择 TC "Runes 11" 的相对几率为 5040. 即在这一步骤里, 选择掉 Mal 的几率为 3/(3+2+5040), 选择掉 Ist 的几率为 2/(3+2+5040), 选择次级TC "Runes 11"的几率为 5040/(3+2+5040) . 只进行一次选择.


TC "Runes 11" 结构如下:
-------------------------------------------------------------------------------
选择次数为1, 选择掉 Pul(21) 的相对几率为 3, 选择掉 Um(22) 的相对几率为 2,

选择次级TC "Runes 10" 的相对几率为 2880.


TC "Runes 10" 结构如下:
-------------------------------------------------------------------------------
选择次数为1, 选择 Fal(19) 的相对几率为 3, 选择掉 Lem(20) 的相对几率为 2,

选择次级TC "Runes 9" 的相对几率为 1440.


TC "Runes 9" 及其以下的 Runes TC 结构都与前面类似, TC中两个神符的相对比
-------------------------------------------------------------------------------
率为 3:2, 而次级TC的相对几率极迅速地衰减.

整个rune drop就是这样的一个结构化的递归系统. 现在, 来算算 Rune Drop 选中Ist(24) 的几率:
1 - (1 - 75% * 2/(3+2+5040))^3 = 0.08917%

游戏设定每个怪物最多掉六件物品, 如果掉宝系统选择的掉出物品多于六件, 那么只有前六件能掉出来. 因此, Item Drop 掉出的物品越少, 留给随后的 RuneDrop 的空间越大.游戏中的人数越少, Item Drop 不掉物品的几率就越大. 当然, 人数少时 Rune Drop 不掉物品的几率也大了, 但两相权衡, 还是人数越少对掉神符越有利. 这就是要在人数少的情况下 Run Countess 的原因.所以以上的0.08917%还不是 Ist 的掉出几率. 不要忘了在 Rune Drop 前面还有个Item Drop. 仅当Item Drop 掉出物品的数目不大于3时, 这个数据才是 Ist 的掉出率. 可见, 女伯爵掉 Ist 的几率是非常小的.

补充一下，女伯爵所在的Tower Cellar Level 5在地狱是79级场景，**因此女伯爵的随从可以掉任何级别的rune。但是女伯爵本身tc不受area lvl影响。即使是她的item drop也只能到28#**