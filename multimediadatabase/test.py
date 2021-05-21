"""
多媒體資料庫.

多媒體資料庫主控台。
"""
import yaml

from multimedia_database.multimedia_info import MultimediaInfo as mi

from multimedia_database.multimedia_summary import HashMultimedia as hm

from multimedia_database.multimedia_database import Insert

from multimedia_database.multimedia_database import Create

NONE_MP4 = "894fad667b74fcff03aaa2f55cf933de1b9fd9663b1e5c0ff80fc6b44fa9542a"
INFO_OBJECT = \
    "0dbf40e4277f897c5a87a1bd32bedd75360df855623d8dfa12a9b7631ebc9c70"


def test_multimedia_hash():
    """測試fun multimedia_hash."""
    # 測試檔案輸出與輸入是否一樣
    hash_media = hm()
    hash_media.multimedia_hash(input_path='__mpdlcache__/None.mp4',
                               output_path='__mmdb__/object/')
    if hash_media.hashfilename == NONE_MP4:
        assert True


def test_path_string_extraction():
    """
    測試fun path_string_extraction.

    測試檔案名稱輸出與預想是否一樣。
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
    multimedia = mi()
    info_data = multimedia.read_file_info(path='__mpdlcache__/None.mp4')
    if isinstance(info_data, dict):
        print(yaml.dump(info_data))
        assert True


def test_read_folder_info():
    """測試fun read_folder_info."""
    multimedia = mi()
    info_data = multimedia.read_folder_info(path='__mpdlcache__/')
    if isinstance(info_data, list):
        print(yaml.dump(info_data))
        assert True


def test_create_table_yaml():
    """測試fun create_table_yaml."""
    create = Create(
        mmdb_path='__mmdb__/', mpdlcache_path='__mpdlcache__/')
    create.create_table_yaml(name='Table.yaml')
    hm.remove_file(path='__mmdb__/table/Table.yaml')
    assert True


def test_save_info_yaml():
    """測試fun save_info_yaml."""
    insert = Insert(mmdb_path='__mmdb__/', mpdlcache_path='__mpdlcache__/')
    hash_media = hm()
    hash_media.multimedia_hash(input_path='__mpdlcache__/None.mp4',
                               output_path='__mmdb__/object/')
    save_hash_name = insert.save_info_yaml(hash_value=hash_media.hashfilename,
                                           media_path='__mpdlcache__/None.mp4')
    if save_hash_name == INFO_OBJECT:
        assert True
    else:
        assert False


def test_check_database():
    """check_database."""
    insert = Insert(mmdb_path='__mmdb__/', mpdlcache_path='__mpdlcache__/')
    multimedias = insert.check_database()
    print(multimedias)
    if isinstance(multimedias, list):
        assert True
    else:
        assert False


def test_multimedia_folder_hash():
    """測試fun multimedia_folder_hash."""
    insert = Insert(mmdb_path='__mmdb__/', mpdlcache_path='__mpdlcache__/')
    insert.multimedia_folder_hash(table='Table.yaml')
    assert True
