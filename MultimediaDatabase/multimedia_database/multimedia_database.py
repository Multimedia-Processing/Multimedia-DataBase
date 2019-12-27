"""
「多媒體資料庫模組」(Multimedia DataBase Module).

多媒體資料庫的控制模組，以提供執行架設、運作與佈署等功能，並提供指令的操作與控制。
"""
import csv
import yaml
from .multimedia_info import MultimediaInfo
from .multimedia_summary import HashMultimedia


class MultimediaDatabase():
    """Multimedia Database."""

    def save_info_yaml(self, media_path='../.temp/None.mp4',
                       save_path='../.mmdb/info/'):
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
