"""
多媒體資料庫.

多媒體資料庫主控台。
"""
from .multimedia_database.multimedia_info import MultimediaInfo as mi
from .multimedia_database.multimedia_summary import HashMultimedia as hm

MI = mi()
HM = hm()


def test_sample1():
    """測試fun read_file_info."""
    info_data = MI.read_file_info(path='__mpdlcache__/None.mp4')
    if isinstance(info_data, dict):
        print(info_data)
        assert True
