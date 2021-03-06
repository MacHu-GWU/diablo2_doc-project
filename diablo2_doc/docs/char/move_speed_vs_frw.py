# -*- coding: utf-8 -*-

from diablo2_doc.helpers.df_int import df_to_list_table
from diablo2_doc.helpers.tsv_gz import make_gzip, read_compressed_tsv

tsv_filename = "move_speed_vs_frw.tsv"
make_gzip(__file__, tsv_filename)
df = read_compressed_tsv(__file__, tsv_filename + ".gz")

lt_move_speed_vs_frw = df_to_list_table(df=df, title="不使用加速技能的情况下, FRW与移动速度的关系")

if __name__ == "__main__":
    print(lt_move_speed_vs_frw.render())
