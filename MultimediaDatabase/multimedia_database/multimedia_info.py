"""
多媒體資訊擷取.

將不同類型的媒體讀取資訊後儲存在物件區並搭配上資料表
"""


import csv
import yaml
from MediaInfo import MediaInfo
from .multimedia_summary import HashMultimedia


HM = HashMultimedia()


class MultimediaInfo():
    """
    讀取多媒體資料.

    讀取多媒體資料後使用YAML語言儲存資訊的函式庫。
    """

    def __init__(self):
        """
        初始化.

        初始化
        """
        self.info_data = None

    def read_file_info(self, path='../.temp/None.mp4'):
        """
        多媒體資訊.

        顯示多媒體資訊，目前只有影片、聲音。
        """
        info = MediaInfo(filename=path)
        self.info_data = info.getInfo()
        return self.info_data

    def read_folder_info(self, path='../.temp/'):
        """
        目錄下多媒體資訊.

        讀取指定的目錄下所有的媒體的資訊。
        """
        multimedias = HM.scan_folder(path=path)
        for multimedia in multimedias:
            self.read_file_info(path + multimedia)

    def save_info_yaml(self, media_path='../.temp/None.mp4',
                       save_path='../.mmdb/info/'):
        """
        儲存媒體資訊.

        將指定媒體在讀取資訊後將YAML儲存到指定的目錄底下。
        """
        data = self.read_file_info(path=media_path)
        stream = open('document.yaml', 'a')
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


if __name__ == '__main__':
    MI = MultimediaInfo()
    MI.read_file_info()
    MI.read_folder_info()
    MI.multimedia_folder_hash_csv()
