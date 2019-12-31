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
        self.data_list = None

    def read_file_info(self, path='../__mpdlcache__/None.mp4', **kwargs):
        """
        多媒體資訊.

        顯示多媒體資訊，目前只有影片、聲音。
        """
        info = MediaInfo(filename=path)
        self.info_data = info.getInfo()
        kwargs.setdefault('hash_value', None)
        kwargs.setdefault('name', None)
        kwargs.setdefault('info', self.info_data)
        kwargs.setdefault('feature', None)
        if kwargs['name'] is None:
            no_path = -1
            while path[no_path] != "/":
                no_path -= 1
            no_filename_extension = -1
            while path[no_filename_extension] != ".":
                no_filename_extension -= 1
            name = path[no_path + 1:no_filename_extension]
            kwargs.update({'name': name})
        return kwargs

    def read_folder_info(self, path='../.temp/'):
        """
        目錄下多媒體資訊.

        讀取指定的目錄下所有的媒體的資訊。
        """
        multimedias = HM.scan_folder(path=path)
        self.data_list = list()
        for multimedia in multimedias:
            data = self.read_file_info(path + multimedia)
            self.data_list.append(data)
        return self.data_list


if __name__ == '__main__':
    MI = MultimediaInfo()
