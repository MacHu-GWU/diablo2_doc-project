# -*- coding: utf-8 -*-

from rstobj import ListTable
from .df_int import df_to_list_table
from .tsv_gz import make_gzip, read_compressed_tsv


def read_list_table(this_file, title, *parts) -> ListTable:
    """

    :param this_file:
    :param parts:
    :return:
    """
    make_gzip(this_file, *parts)
    parts_list = list(parts)
    parts_list[-1] = parts_list[-1] + ".gz"
    df = read_compressed_tsv(this_file, *parts_list)
    return df_to_list_table(df=df, title=title)
