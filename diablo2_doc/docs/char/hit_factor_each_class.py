# -*- coding: utf-8 -*-

from diablo2_doc.helpers.df_int import df_to_list_table
from diablo2_doc.helpers.tsv_gz import make_gzip, read_compressed_tsv

tsv_filename = "hit_factor_each_class.tsv"
make_gzip(__file__, tsv_filename)
df = read_compressed_tsv(__file__, tsv_filename + ".gz")

lt_hit_factor_for_each_class = df_to_list_table(df=df, title="各职业的 Hit Factor")

if __name__ == "__main__":
    print(lt_hit_factor_for_each_class.render())
