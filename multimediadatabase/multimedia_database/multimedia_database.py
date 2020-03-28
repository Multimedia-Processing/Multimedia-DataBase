"""「多媒體資料庫模組」(Multimedia DataBase Module).

- 運作:可利用Python函式與套件去呼叫與執行套件。
- 佈署:可利用Python函式與套件去呼叫與執行套件去建立新的資料庫。
- 資料儲存:儲存匯入進來的多媒體，可以指定檔案、目錄或者暫存。
- 資料管理:管理資料庫裡面的內容，操作基本的新增、刪除、修改與查詢。

並提供簡單資料庫操作方式:

- 新增:新增資料庫。
- 刪除:刪除資料庫。
- 修改:修改資料庫名稱。
- 查詢:提供迴遞的方式掃描所有目錄底下是否有資料庫。

並提供簡單資料表操作方式:

- 新增:新增資料表。
- 刪除:刪除資料表。
- 修改:修改資料表名稱。
- 查詢:查詢資料庫內線有的資料表。

並提供簡單資料操作方式:

- 新增:新增多媒體到資料庫裡面，並將資料紀錄在資料表上。
- 刪除:從資料庫裡面刪除資料，並提供刪除參照或物件的選項。
- 修改:更新資料庫裡面的資料，提供更新資料、多媒體、物件與參照。
- 查詢:查詢資料庫內容，並且依需求將資料匯出。
"""
# Disable all the no-member violations in this function
# pylint: disable=R0205
import os

import shutil

import csv

from os import walk

import yaml

from .multimedia_info import MultimediaInfo

from .multimedia_summary import HashMultimedia


MI = MultimediaInfo()
HM = HashMultimedia()


class DataBase(object):
    """Docstring for database manage class.

    A category for managing databases.Create a new database, enter the path,
    database name, and default table name.
    """

    def __init__(self, path='../../', name='__mmdb__'):
        """Init."""
        super(DataBase, self).__init__()
        self.path = path
        self.database_name = name
        self.table = "table"
        self.object = "object"
        self.mmdb_md = "mmdb.md"
        self.object_md = "object.md"
        self.table_md = "table.md"

    def create_database(self):
        """Create DataBase."""
        try:
            os.makedirs(name=self.path + self.database_name, exist_ok=False)
            os.makedirs(name=self.path + self.database_name + self.table,
                        exist_ok=False)
            os.makedirs(name=self.path + self.database_name + self.object,
                        exist_ok=False)
            shutil.copyfile(self.mmdb_md, self.path +
                            self.database_name + self.mmdb_md)
            shutil.copyfile(self.table_md, self.path +
                            self.database_name + self.table + self.table_md)
            shutil.copyfile(self.table_md, self.path +
                            self.database_name + self.object + self.object_md)

        except FileExistsError:
            print('The directory already has a multimedia library or a \
                directory of the same name.')

    def drop_database(self):
        """Drop DataBase."""
        ask = str(input("Are you sure you want to continue?(yes/no)"))
        try:
            if ask == 'yes':
                shutil.rmtree(path=self.path + self.database_name,
                              ignore_errors=False)
            elif ask == 'no':
                print('Failed to delete database.')
            else:
                print("Your input is not one of the options.")
                assert False
        except FileExistsError:
            print('The database does not exist.')

    def rename_database(self):
        """Rename DataBase."""
        try:
            ask = str(input())
            if ask == 'yes':
                shutil.rmtree(path=self.path + self.database_name,
                              ignore_errors=False)
            elif ask == 'no':
                print('Failed to delete database.')
            else:
                assert False
        except FileExistsError:
            print('The database does not exist.')

    def show_database(self):
        """Show DataBase.

        搜尋指定目錄底下所有的多媒體資料庫。
        """
        try:
            for root, dirs, files in walk(self.path):
                if self.mmdb_md in files \
                        and self.table in dirs \
                        and self.object in dirs:
                    root_table = os.listdir(root + self.table)
                    root_object = os.listdir(root + self.object)
                    if self.table_md in root_table \
                            and self.object_md in root_object:
                        database_name = root.split('/')
                        print('資料庫:', database_name[-1])

        except FileExistsError:
            print('The database does not exist.')


class Table(object):
    u"""Create.

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
                         mode='a', newline='', encoding='utf8', **kwargs):
        """建立CSV.

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

    def create_table_yaml(self, name='Table.yaml',
                          mode='a', newline='', encoding='utf8', **kwargs):
        """建立YAML.

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
        with open(self.mmdb_path + self.mmdb_path_table + name,
                  mode=mode, newline=newline, encoding=encoding) as yamlfile:
            # 建立 CSV 檔寫入器
            yaml.dump(table, yamlfile)


class Date(object):
    u"""Insert.

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
        """儲存媒體資訊.

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
        """檔案、雜湊值與檔案資訊資料表.

        將檔案雜湊後得出的雜湊值與檔名搭配後存入YAML。
        """
        create = Table(mmdb_path=self.mmdb_path,
                       mpdlcache_path=self.mpdlcache_path)
        file_extension = HM.path_string_extraction(
            text=table, folder=False, file=False, file_extension=True)
        multimedias = self.check_database()
        for multimedia in multimedias:
            HM.multimedia_hash(
                input_path=self.mpdlcache_path + multimedia,
                output_path=self.mmdb_path + self.mmdb_path_object)
            media_hash = HM.hashfilename
            info_hash = self.save_info_yaml(
                hash_value=HM.hashfilename,
                media_path=self.mpdlcache_path + multimedia)
            if file_extension == ".csv":
                create.create_table_csv(save_path=table,
                                        hash=HM.hashfilename,
                                        info=info_hash,
                                        feature=None)
            elif file_extension == ".yaml":
                create.create_table_yaml(name=table,
                                         hash=media_hash,
                                         info=info_hash,
                                         feature=None)
            else:
                return False
        return True

    def check_database(self):
        """資料庫檢查.

        檢查資料表、物件以及暫存檔之間是否正確連結。
        會先檢查資料表與物件之間的關聯，再來會確定暫存檔是否已經進資料庫。
        階段一檢查:比對object名稱與資料表是否一致。
        階段二檢查:比對暫存與資料表。
        階段三檢查:回傳比對結果。

        快速檢查:不重新計算object雜湊值，比對資料表。
        慢速檢查:重新計算object雜湊值，比對資料表。
        """
        multimedias = list()
        mmdb_table_list = HM.scan_folder(
            path=self.mmdb_path + self.mmdb_path_table)
        if len(mmdb_table_list) <= 1 and "table.md" in mmdb_table_list:
            multimedias = HM.scan_folder(path=self.mpdlcache_path)
        elif mmdb_table_list and "table.md" not in mmdb_table_list:
            multimedias = HM.scan_folder(path=self.mpdlcache_path)

        for table in mmdb_table_list:
            table_file = self.mmdb_path + self.mmdb_path_table + table
            file_extension = HM.path_string_extraction(
                text=table_file,
                folder=False, file=False, file_extension=True)
            if file_extension == ".yaml":
                data = yaml.unsafe_load(
                    HM.read_file(
                        path=table_file, mode='r', encoding='utf8'))
                for row in data:
                    if row['info'] is not None:
                        info_object = self.mmdb_path + \
                            self.mmdb_path_object + row['info']
                        info_data = yaml.unsafe_load(
                            HM.read_file(
                                path=info_object, mode='r', encoding='utf8'))
                        name = info_data['name'] + \
                            info_data['info']['extension']
                        if name not in multimedias:
                            multimedias.append(name)
        return multimedias


if __name__ == '__main__':
    MMDB = Date()
    MMDB.multimedia_folder_hash()
