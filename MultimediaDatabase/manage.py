"""
多媒體資料庫.

多媒體資料庫主控台。
"""

from multimedia_database.multimedia_info import MultimediaInfo as mi


MI = mi()
MI.read_file_info()
MI.read_folder_info(path='.temp/')
