跑步速度与冲锋速度的计算
==============================================================================

术语:

- Walk_Speed: 走路速度.
- Run_Speed: 跑步速度.
- Charge_Speed: 冲锋速度.
- FRW: Faster run/walk, 装备增加的走路/跑步速度的总和.
- Other_Speed_Bonus: 其它对走路 / 跑步速度的影响, 包括技能提供的增速 和 装甲盾牌造成的减速. 中型甲 / 中型盾 -5%, 重型甲 / 重型盾 -10%

公式:

- Walk_Speed = 4 * (1 + FRW * 1.5 / (FRW + 1.5) + Other_Speed_Bonus)
- Run_Speed = 2 + Walk_Speed
- Charge_Speed = 9 * ( 1 + Other_Speed_Bonus)

注: 冲锋没有最低速度限制

移动速度的单位: 码/s

**不使用加速技能的情况下, FRW 与移动速度的关系见下表**:

.. jinja:: doc_data

    {{ doc_data.lt_move_speed_vs_frw.render() }}


附录: TU 与 Yard
------------------------------------------------------------------------------

TU: tile unit. 菱形的地图单元, 对角线长度分别为: 水平32像素, 竖直16像素.

1 Yard = 1.5 TU

因此, 通过计算可得:

800 x 600 = 25 TUs × 37.5 TUs = 16.6 yards × 25 yards
640 x 480 = 20 TUs × 30 TUs = 13.3 yards × 20 yards
