"""
多媒體資訊擷取.

將不同類型的媒體讀取資訊後儲存在物件區並搭配上資料表
"""


from MediaInfo import MediaInfo
from .multimedia_summary import HashMultimedia
import yaml


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


if __name__ == '__main__':
    MI = MultimediaInfo()
    MI.read_file_info()
    MI.read_folder_info()
