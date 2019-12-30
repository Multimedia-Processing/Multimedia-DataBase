"""
「多媒體資料庫模組」(Multimedia DataBase Module).

多媒體資料庫的控制模組，以提供執行架設、運作與佈署等功能，並提供簡單新增、刪除、修改與查
詢的操作與控制。
"""
import csv
import yaml
from .multimedia_info import MultimediaInfo
from .multimedia_summary import HashMultimedia


MI = MultimediaInfo()
HM = HashMultimedia()


class Insert():
    """
    Insert.

    新增多媒體資料到資料庫。
    """

    def __init__(self, mmdb_path='../__mmdb__/',
                 mpdlcache_path='../__mpdlcache__/'):
        """類別初始化."""
        self.mmdb_path = mmdb_path
        self.mpdlcache_path = mpdlcache_path
        self.mmdb_path_object = "object/"
        self.mmdb_path_table = "table/"

    def save_info_yaml(self, media_path='../__mpdlcache__/None.mp4'):
        """
        儲存媒體資訊.

        將指定媒體在讀取資訊後將YAML儲存到指定的目錄底下。
        """
        data = self.read_file_info(path=media_path)
        stream = open('document.yaml', 'w')
        yaml.dump(data, stream)

    def multimedia_folder_hash_csv(self, input_path='../.temp/',
                                   output_path='../.mmdb/object/',
                                   save_path='../.mmdb/info/info.csv'):
        """
        檔案與雜湊值對應CSV.

        將檔案雜湊後得出的雜湊值與檔名搭配後存入CSV檔
        """
        multimedias = HM.scan_folder(path=input_path)
        for multimedia in multimedias:
            HM.multimedia_hash(input_path=input_path + multimedia,
                               output_path=output_path)

            with open(save_path,
                      mode='a', newline='', encoding='utf8') as csvfile:
                # 建立 CSV 檔寫入器g
                writer = csv.writer(csvfile)

                # 寫入一列資料
                writer.writerow([HM.hashfilename, HM.filename])

    def multimedia_folder_hash_yaml(self, input_path='../.temp/',
                                    output_path='../.mmdb/object/',
                                    save_path='../.mmdb/info/info.csv'):
        """
        檔案、雜湊值與檔案資訊資料表.

        將檔案雜湊後得出的雜湊值與檔名搭配後存入YAML。
        """
        multimedias = HM.scan_folder(path=input_path)
        for multimedia in multimedias:
            HM.multimedia_hash(input_path=input_path + multimedia,
                               output_path=output_path)

            with open(save_path,
                      mode='a', newline='', encoding='utf8') as csvfile:
                # 建立 CSV 檔寫入器g
                writer = csv.writer(csvfile)

                # 寫入一列資料
                writer.writerow([HM.hashfilename, HM.filename])
