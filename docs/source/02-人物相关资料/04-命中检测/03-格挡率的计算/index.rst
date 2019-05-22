格挡率的计算
===============================================================================
术语:

- Block_Chance: 最终的格挡率
- Blocking: 盾牌格挡率
- Clvl: 人物等级

其中, 盾牌格挡率 ＝ 盾牌基础格挡率 ＋ 盾牌上的属性加的格挡率 ＋ 身上的装备加的格挡率 ＋ 圣盾技能加的格挡率

公式：

代码:

Block_Chance = Blocking * ( Dexterity - 15 ) / ( Clvl * 2 )

Block_Chance 不能大于 75%。

注意：

* 人物最终格挡率的查看方法: 打开状态窗口(默认是"A"键), 将鼠标悬停于防御值上, 出现一个浮动条,显示的就是最终格挡率;

* 除了刺客外,其他人物使用盾牌时才有格挡率;

* 不同的角色使用同一个盾牌, 其 Blocking 是不一样的. Dru/Nec/Sor最低, Ama/Asn/Bar 在 Dru/Nec/Sor Blocking 基础上加5%, Pal加10%;

* 如果盾牌有"xx% increased chance of blocking", 其显示的格挡率可能出现问题. 比如一个基础格挡60%的盾, 又带20% increased chance of blocking, 其 Blocking 是80%, 但盾牌上只显示 75% . 计算时仍以 80% 计算.

移动中的情况：

跑动中的Block_Chance=(Blocking * (Dexterity - 15)) / (Character Level * 2)/3，即原有格挡率的1/3。 

这个也有一个上限，即25%，超过25%按照25%计算，不会出现 > 25%的情况出现，即使拥有再多的dex也没用,同时跑动时不会检测防御值。

走动时Block_Chance不变.

格挡率实例计算：

一个90级的Pal使用"暴风之盾-统治者大盾"，穿"守护天使-圣堂武士外袍"，开25级"神圣之盾"技能
需多少敏捷才能达到格挡75？

解：

统治者大盾的基础格挡为42，pal看时会加10点，为52；

“暴风之盾”有"+25% 格挡机率"属性；

“守护天使”有"+20% 格挡机率"属性；

25级“神圣之盾”增加36%格挡机率；

则盾牌格挡 ＝ 盾牌基础格挡＋盾牌上的属性加的格挡＋身上的装备加的格挡＋圣盾技能加的格挡 ＝ 52＋25＋20＋36 ＝ 133

注意此时在游戏里看到的盾牌格挡仍为75。

代入以下公式：

Block_Chance = Blocking * ( Dexterity - 15 ) / ( Clvl * 2 )

0.75 = 1.33 * (Dexterity - 15) / 90 / 2

得Dexterity＝116.50

向上取整，需要敏捷117。

weapon block：

asn 的weapon block 是一個特殊的技能，在裝備兩個爪類武器之後，如果有加此技能，則會有格檔率，

且可以格檔一些 magic 類型的攻擊。

此时的格挡率即技能所加的格挡率。

在Stand、Attack、Cast状态及"Whirlwind"状态中均保持不变；

Walk状态，为0；

Run状态理论上为0，但是有bug，出现格挡的几率在3%左右。


能被格挡的人物远程技能
-------------------------------------------------------------------------------
以下的远程技能，如果其中包含有物理伤害，是可以造成对方的格挡的，这其中包括：

- Amazon Bow Skills
- Amazon Javelin Skills (除去Lightning Bolt）*
- War Cry
- Whirlwind
- Blade Sentinel
- Molten Boulder
- Twister
- Tornado
- Volcano
- Molten Boulder
- Armageddon
- Shockwave
- Blade Fury
- Blade Shield
- Psychic Hammer


* 注：Amazon的Javelin Skills中，闪电标枪系只有标枪物理伤害和附加到标枪上的元素伤害可以被格挡，而技能本身的闪电伤害是不能被格挡的。

ASN的Weapon Block技能可以格挡一些盾牌无法格挡的技能。列表如下

**Asn**

::

    Blade Fury          - Blockable
    Blade Sentinel      - Blockable
    Blade Shield        - Blockable
    Phoenix Strike      - Blockable
    Lightning Sentry    - Blockable
    Wake of Inferno     - UnBlockable

**Nec**

::

    Poison Nova         - Blockable
    Teeth               - Blockable
    Bone Spear          - Blockable
    Bone Spirit         - Blockable

**Pal**

::

    Blessed Hammer      - Blockable
    Fist of the Heavens - Blockable
    Smite               - Blockable

**Sor**

::

    Fireball            - Blockable
    Firebolt/Hydra      - Blockable
    Meteor              - Blockable
    Firewall            - Unblockable
    Blaze               - Unblockable
    Blizzard            - Blockable
    Ice Bolt            - Blockable
    Frozen Orb          - Blockable
    Chain lightning     - Blockable
    lightning           - Blockable

**Druid**

::

    Fissure             - Unblockable
    Hurricane           - Blockable
    Molten Boulder      - Unblockable
    Artic Blast         - Unblockable