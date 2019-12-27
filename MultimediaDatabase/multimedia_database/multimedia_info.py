"""
多媒體資訊擷取.

將不同類型的媒體讀取資訊後儲存在物件區並搭配上資料表
"""
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


if __name__ == '__main__':
    MI = MultimediaInfo()
    MI.multimedia_folder_hash_csv()
