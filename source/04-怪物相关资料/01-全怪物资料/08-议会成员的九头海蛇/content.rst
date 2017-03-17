.. _议会成员的九头海蛇:

议会成员的九头海蛇
===============================================================================
译者前言：崔凡克瘸子、巴尔大殿的巴特克的Hydra为何会对佣兵有那么大的杀伤力？这个悬而未决的难题一度困扰着国内外的许多玩家。PK的Myhrginoc、Nefarius给了我一些相关的信息，但未深入阐述，最终在RTB那里得到了想要的答案，感谢他们的帮助。

Bartuc和Council Member的Hydra，有额外的火焰加成：

引用::

	Councilmember1 (Vilehand and Icefist):
	Slvl 2 Hydra in normal, +40% extra-fire in NM, +100% in Hell

	Councilmember2 (Flamefinger and Voidfinger):
	Slvl 3 Hydra in normal, +40% extra-fire in NM, +100% in Hell

	Councilmember3 (Sparkfist and Dragonhand):
	Slvl 4 Hydra in normal, +40% extra-fire in NM, +100% in Hell

	Baalhighpriest (Bartuc):
	Slvl 4 Hydra in normal, +60% extra-fire in NM, +120% in Hell

译注：CF MonStats.txt & MonProp.txt

下面是理论计算得到的数据，技能伤害加上附加的火焰加成：

引用::

	技能等级  技能伤害     加成     总伤害

	Normal
	2       16.5 - 22.5    +0%    16.5 - 22.5
	3       21.0 - 28.0    +0%    21.0 - 28.0
	4       25.5 - 33.5    +0%    25.5 - 33.5

	NM
	5       30.0 - 39.0   +40%    42.0 - 54.6
	6       34.5 - 44.5   +40%    48.3 - 62.3
	7       39.0 - 50.0   +40%    54.6 - 70.0
	7       39.0 - 50.0   +60%    62.4 - 80.0

	Hell
	9       50.0 - 63.0  +100%  100.0 - 126.0
	10      56.5 - 70.5  +100%  113.0 - 141.0
	11      63.0 - 78.0  +100%  126.0 - 156.0
	11      63.0 - 78.0  +120%  138.6 - 171.6

译注：怪物技能在普通难度技能等级基础上，恶梦难度+3，地狱难度+7。

地狱难度，Travincal的3个瘸子各放一个Hydra，共9头，攻击一个75%FR的佣兵，在10秒内佣兵将受到平均2000左右的伤害。

地狱难度，Bartuc的hydra，平均每个bolt对一个穿Tal套装，FR 75%的Sor的伤害为： ``{[(138.6 + 171.6) / 2]× 17% - 15} × 25% = 2.84``

Nefarius注：Monster's Minion Vs Player: 17%、Monster's Minion Vs Hireing: 100%。这个和玩家的Minion是一样的，没有任何硬代码程序另外注释。

当目标是玩家时，我认为Bartuc和Council Member的Hydra将没有额外的火焰加成，原因不明。

当然在恶梦/地域难度，当瘸子有Fire Enchanted/Extra Strong，作为怪物的Minion，Hydra将得到额外的火焰伤害加成。

Spectral Hit为随机提升Minion的某种元素伤害，我认为未必会提升Hydra的伤害。

译注：我认为Extra Strong应该只是增加怪物Minion的物理伤害。

Fire Enchanted会对怪物本身有火焰伤害加成，这个加成应该也适用于Hrdra（虽然Hrdra属于Minion，但是有特殊的检测机制，如Sor的Hrdra，Fire Mastery，包括火珠就对其有加成 —— -% To Enemy Fire Resistances和+% To Fire Skill Damage都有效） 。