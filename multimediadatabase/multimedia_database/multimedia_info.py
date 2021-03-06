"""
多媒體資訊擷取.

將不同類型的媒體讀取資訊後儲存在物件區並搭配上資料表
"""
from pyprobe import VideoFileParser
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

    def read_file_info(self, path='../__mpdlcache__/None.mp4',
                       ffprobe="ffprobe", **kwargs):
        """
        多媒體資訊.

        顯示多媒體資訊，目前只有影片、聲音。
        """
        parser = VideoFileParser(
            ffprobe=ffprobe, includeMissing=True, rawMode=True)
        self.info_data = parser.parseFfprobe(path)
        self.info_data.pop('path')
        self.info_data.update({'extension': None})
        kwargs.setdefault('hash', None)
        kwargs.setdefault('name', None)
        kwargs.setdefault('info', self.info_data)
        kwargs.setdefault('feature', None)
        if kwargs['name'] is None:
            name = HM.path_string_extraction(
                text=path, folder=False, file=True, file_extension=False)
            extension = HM.path_string_extraction(
                text=path, folder=False, file=False, file_extension=True)
            kwargs.update({'name': name})
            kwargs['info'].update({'extension': extension})
        return kwargs

    def read_folder_info(self, path='../__mpdlcache__/'):
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
