# -*- coding: utf-8 -*-

"""

"""

import gzip
import typing
import pandas as pd
from pathlib_mate import PathCls as Path


def make_gzip(this_file, *parts):
    """
    将文件名为 <filename> 的 ``.tsv`` 文件 (后缀名必须是tsv, 否则出粗) 压缩成 ``.tsv.gz``
    的压缩包文件. 执行该操作的 python 脚本必须和 ``.tsv`` 文件在同一目录下.

    :type this_file: str
    :param this_file: 当前 python 脚本的文件全路径

    :type parts: typing.List[str]
    :param filename: ``.tsv`` 文件名
    """
    if not parts[-1].endswith(".tsv"):
        raise ValueError("You have to specify a '.tsv' file")

    src = Path(this_file).parent.append_parts(*parts)
    dst = src.change(new_basename=src.basename + ".gz")

    if not dst.exists():
        with gzip.open(dst.abspath, "wb") as f:
            f.write(src.read_bytes())


def read_compressed_tsv(this_file, *parts):
    """
    从当前脚本所在的文件夹读取压缩的 ``.tsv.gz`` 文件. 读成 ``pd.DataFrame``.

    :type this_file: str
    :param this_file:

    :type filename: str
    :param filename: ``.tsv.gz`` 文件

    :rtype: pd.DataFrame
    """
    if not parts[-1].endswith(".tsv.gz"):
        raise ValueError("You have to specify a '.tsv.gz' file")
    src = Path(this_file).parent.append_parts(*parts)
    return pd.read_csv(
        src.abspath,
        sep="\t", compression="gzip",
    )


if __name__ == "__main__":
    make_gzip(__file__, "test.tsv")
    df = read_compressed_tsv(__file__,"test.tsv.gz")
    print(df)