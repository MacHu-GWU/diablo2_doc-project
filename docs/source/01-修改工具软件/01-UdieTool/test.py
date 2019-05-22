from pathlib_mate import PathCls as Path
from docfly.doctree import ArticleFolder
from docfly.directives import autotoctree

p = Path(__file__).parent
af = ArticleFolder(p.abspath)
print(af.title)