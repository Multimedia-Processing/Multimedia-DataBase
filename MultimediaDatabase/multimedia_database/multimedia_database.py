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


class Create():
    """
    Create.

    新增資料表到資料庫。
    """

    def __init__(self, mmdb_path='../__mmdb__/',
                 mpdlcache_path='../__mpdlcache__/'):
        """類別初始化."""
        self.mmdb_path = mmdb_path
        self.mpdlcache_path = mpdlcache_path
        self.mmdb_path_object = "object/"
        self.mmdb_path_table = "table/"

    @classmethod
    def create_table_csv(cls,
                         save_path='__mmdb__/table/table.csv',
                         mode='a', newline='', encoding='utf8', **kwargs,):
        """
        建立CSV.

        將用於建立CSV檔，並提供在尾端新增資料的功能。
        """
        kwargs.setdefault('hash', None)
        kwargs.setdefault('info', None)
        kwargs.setdefault('feature', None)
        with open(save_path,
                  mode=mode, newline=newline, encoding=encoding) as csvfile:
            # 建立 CSV 檔寫入器g
            writer = csv.writer(csvfile)

            # 寫入一列資料
            writer.writerow(
                [kwargs['hash'], kwargs['info'], kwargs['feature']])

    @classmethod
    def create_table_yaml(cls,
                          save_path='../__mmdb__/table/Table.yaml',
                          mode='a', newline='', encoding='utf8', **kwargs,):
        """
        建立YAML.

        將用於建立YAML檔，並提供在尾端新增資料的功能。
        """
        kwargs.setdefault('hash', None)
        kwargs.setdefault('info', None)
        kwargs.setdefault('feature', None)
        table = [{
            'hash': kwargs['hash'],
            'info': kwargs['info'],
            'feature': kwargs['feature']
        }]
        with open(save_path,
                  mode=mode, newline=newline, encoding=encoding) as yamlfile:
            # 建立 CSV 檔寫入器
            yaml.dump(table, yamlfile)


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

    def save_info_yaml(self, hash_value=None,
                       media_path='../__mpdlcache__/None.mp4'):
        """
        儲存媒體資訊.

        將指定媒體在讀取資訊後將YAML儲存到指定的目錄底下。
        """
        data = MI.read_file_info(path=media_path)
        data.update({'hash': hash_value})
        yaml_data = yaml.dump(data).encode('utf8')
        HM.save_file(text=yaml_data,
                     path=self.mmdb_path + self.mmdb_path_object,
                     encoding='utf8', mode='w')
        return HM.hashfilename

    def multimedia_folder_hash(self, table='Table.yaml'):
        """
        檔案、雜湊值與檔案資訊資料表.

        將檔案雜湊後得出的雜湊值與檔名搭配後存入YAML。
        """
        file_extension = HM.path_string_extraction(
            text=table, folder=False, file=False, file_extension=True)
        save_table_path = self.mmdb_path + self.mmdb_path_table + table
        multimedias = self.check_database()
        for multimedia in multimedias:
            HM.multimedia_hash(input_path=input_path + multimedia,
                               output_path=output_path)
    def check_database(self):
        """
        資料庫檢查.

        檢查資料表、物件以及暫存檔之間是否正確連結。
        會先檢查資料表與物件之間的關聯，再來會確定暫存檔是否已經進資料庫。
        階段一檢查:比對object名稱與資料表是否一致。
        階段二檢查:比對暫存與資料表。
        階段三檢查:回傳比對結果。

        快速檢查:不重新計算object雜湊值，比對資料表。
        慢速檢查:重新計算object雜湊值，比對資料表。
        """
        table_and_object_check = list()
        objects = HM.scan_folder(
            path=self.mmdb_path + self.mmdb_path_object)
        tables = HM.scan_folder(
            path=self.mmdb_path + self.mmdb_path_table)
        multimedias = HM.scan_folder(
            path=self.mpdlcache_path)
        for table in tables:
            table_file = self.mmdb_path + self.mmdb_path_table + table
            file_extension = HM.path_string_extraction(
                text=table_file, folder=False, file=False, file_extension=True)
            if file_extension == ".yaml":
                yamlfile = HM.read_file(
                    path=table_file, mode='r', encoding='utf8')
                data = yaml.load(yamlfile)
                for row in data:
                    for column in row:
                        if row[column] in objects and row[column] is not None:
                            table_and_object_check.append(row[column])
                    info_object = self.mmdb_path + \
                        self.mmdb_path_table + row['info']
                    yamlfile = HM.read_file(
                        path=info_object, mode='r', encoding='utf8')
                    info_data = yaml.load(yamlfile)
                    name = info_data['name']
                    if name in multimedias:
                        multimedias.pop(name)
        return multimedias


if __name__ == '__main__':
    MMDB = Insert()
    MMDB.multimedia_folder_hash()
