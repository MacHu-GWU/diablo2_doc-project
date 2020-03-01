# -*- coding: utf-8 -*-

from diablo2_doc.helpers.df_int import df_to_list_table
from diablo2_doc.helpers.tsv_gz import make_gzip, read_compressed_tsv

tsv_filename = "base_stats_each_class.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")

for c in df.columns:
    if c != "基础属性":
        df[c] = df[c].apply(lambda x: str(x).replace(".0", ""))
lt_base_stats_each_class = df_to_list_table(df=df, title="各职业的基础属性")

if __name__ == "__main__":
    print(lt_base_stats_each_class.render())
