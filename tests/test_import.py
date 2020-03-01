# -*- coding: utf-8 -*-

import pytest
from diablo2_doc.docs import doc_data

def test():
    _ = doc_data

if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
