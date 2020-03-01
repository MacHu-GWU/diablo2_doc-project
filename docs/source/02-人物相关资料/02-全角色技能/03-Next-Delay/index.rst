.. _NextDelay机制

Next Delay 机制
===============================================================================

一句话解释, 炮轰的 Next Delay 是 0.16 秒, 那么即使有 8 个亚马逊角色对同一目标使用炮轰时, 该目标每 0.16 秒只会受到一次炮轰攻击.

Next Delay 属性是用以激活一个隐藏的攻击次数限制, 来限制一组人能伤害到同一目标的某种攻击的频率. 他的作用类似与用来限制的能作出的某种攻击次数的frame per attack. 但与frame per attack不同的是, Next Delay 并不阻止你的攻击动作, **他通过在 Next Delay 时间之内, 将该组人马击中目标的几率设为零而生效. 换而言之, Next Delay 是一端时间内攻击无效**, frame per attack是一端时间内不能攻击.

各技能的 Next Delay 时间:

25-Frame Delay (1秒)

- Shock Web 雷电网
- Blade Sentinel 刃之守护
- Twister 小旋风
- Tornado 龙卷风 (由于某种未知的原因, Tornado 的 Next Delay没有生效)

10-Frame Delay (0.4秒)

- Volcano (initial eruption) 火山

6-Frame Delay (0.24秒)

- War Cry 战斗狂嗥
- Grim Ward 残酷吓阻

5-Frame Delay (0.2秒)

- Fissure 火山爆
- Volcano (small fireball) 火山的小火球

4-Frame Delay (0.16秒)

- Multi Shot 多重箭
- Strafe 炮轰
- Lightning Strike 闪电攻击
- Chain Lightning 连锁闪电
- Nova 新星
- Frost Nova 霜之新星
- Poison Nova 剧毒新星
- Shock Wave 震波
- Fist of Heavens (Holy Bolts) 天堂之拳的圣光弹
- Wake of Fire 火焰复生
- Claws of Thunder (only 2nd and 3rd charge charges have Next Delay. 1st charge does not trigger Next Delay) 雷电爪 (聚气二和聚气三有 Next Delay, 聚气一没有)
- Phoenix Strike (only 2nd Chain Lightning and 3rd Chaos Orb charge have Next Delay. 1st charge does not trigger Next Delay) 凤凰攻击 (第二次和第三次聚气有 Next Delay, 第一次没有)
- Dragon Flight 飞龙在天
- Battle Cry 战嗥
- Battle Command 战斗指挥
- Battle Orders 战斗体制

以上技能中任何一种伤害目标后, 在相应的frame之内, 以上任何skil都不能再次
伤害目标, 而不管最初的伤害是不是你造成的.

一些 boss skill 的 Next Delay:

- diablight: 3frames
- diabfire: 4frames
- baal inferno: 4frames
- baal nova: 4frames
- baal cold maker: 4frames
- baal cold trail: 4frames
- meph frost nova: 4frames
- baal taunt lightning: 10frames
- baal taunt lightning trail: 10frames
