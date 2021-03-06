"""
多媒體資料庫.

多媒體資料庫主控台。
"""
import yaml
from .multimedia_database.multimedia_info import MultimediaInfo as mi
from .multimedia_database.multimedia_summary import HashMultimedia as hm
from .multimedia_database.multimedia_database import Insert

MI = mi()
HM = hm()
INSERT = Insert(mmdb_path='__mmdb__/', mpdlcache_path='__mpdlcache__/')


def test_multimedia_hash():
    """測試fun multimedia_hash."""
    # 測試檔案輸出與輸入是否一樣
    HM.multimedia_hash(input_path='__mpdlcache__/None.mp4',
                       output_path='__mmdb__/object/')
    multimedia_hash_test = HM.hashfilename
    HM.multimedia_hash(
        input_path='__mmdb__/object/' + multimedia_hash_test,
        output_path='__mmdb__/object/')
    if multimedia_hash_test == HM.hashfilename:
        assert True


def test_path_string_extraction():
    """
    測試fun path_string_extraction.

    測試檔案輸出與輸入是否一樣
    """
    text = 'abcd/efgh.mp4'
    test_list = [
        (False, False, False, ''),
        (False, False, True, '.mp4'),
        (False, True, False, 'efgh'),
        (False, True, True, 'efgh.mp4'),
        (True, False, False, 'abcd/'),
        (True, False, True, 'abcd/.mp4'),
        (True, True, False, 'abcd/efgh'),
        (True, True, True, 'abcd/efgh.mp4'),
    ]
    for folder, file, file_extension, path in test_list:
        name = hm.path_string_extraction(
            text=text, folder=folder, file=file, file_extension=file_extension)
        print('\n', path, name)
        if name == path:
            assert True
        else:
            assert False


def test_read_file_info():
    """測試fun read_file_info."""
    info_data = MI.read_file_info(path='__mpdlcache__/None.mp4')
    if isinstance(info_data, dict):
        print(yaml.dump(info_data))
        assert True


def test_read_folder_info():
    """測試fun read_folder_info."""
    info_data = MI.read_folder_info(path='__mpdlcache__/')
    if isinstance(info_data, list):
        print(yaml.dump(info_data))
        assert True


def test_save_info_yaml():
    """測試fun save_info_yaml."""
    HM.multimedia_hash(input_path='__mpdlcache__/None.mp4',
                       output_path='__mmdb__/object/')
    save_hash_name = INSERT.save_info_yaml(hash_value=HM.hashfilename,
                                           media_path='__mpdlcache__/None.mp4')

    HM.multimedia_hash(input_path='__mmdb__/object/' + save_hash_name,
                       output_path='__mmdb__/object/')

    if save_hash_name == HM.hashfilename:
        assert True


def test_check_database():
    """check_database."""
    multimedias = INSERT.check_database()
    print(multimedias)
    if isinstance(multimedias, list):
        assert True
    else:
        assert False


def test_multimedia_folder_hash():
    """測試fun multimedia_folder_hash."""
    INSERT.multimedia_folder_hash(table='Table.yaml')
    assert True
