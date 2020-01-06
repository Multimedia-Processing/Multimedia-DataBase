"""
多媒體資料庫.

多媒體資料庫主控台。
"""
from multimedia_database.multimedia_database import Insert

INSERT = Insert(mmdb_path='__mmdb__/', mpdlcache_path='__mpdlcache__/')
INSERT.multimedia_folder_hash(table='Table.yaml')
