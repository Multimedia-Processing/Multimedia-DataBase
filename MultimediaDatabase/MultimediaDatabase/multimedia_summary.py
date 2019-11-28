"""
多媒體檔案摘要製作.

將各種數位媒體使用密碼學的雜湊函式的計算，將計算結果雜湊值作為檔案名稱且不包含副檔名，解
決因為媒體重複性質高造成的問題。
"""


import os
from hashlib import sha256
import csv


class HashMultimedia():
    """
    雜湊多媒體檔案類別.

    提供讀取、寫入、輸出等自動化操作，並提供API使用.
    """

    def __init__(self, encoding=None, mode="rb", size=-1):
        """
        初始化類別.

        選擇自己喜歡的雜湊函數，提供其他函式使用。
        """
        self.encoding = encoding
        self.mode = mode
        self.size = size
        self.hashfilename = None
        self.filename = None

    @classmethod
    def read_file(cls, path='./.temp/None.mp4',
                  encoding=None, mode='rb', size=-1):
        """
        讀取文件檔案並計算雜湊值.

        指定檔案路徑，將裡面的內容依照參數回傳。
        """
        with open(path, mode=mode, encoding=encoding) as text:
            return text.read(size)

    def save_file(self, text,
                  path='./.mmdb/object/', encoding=None, mode='wb'):
        """
        雜湊二進位檔案後存檔.

        針對輸入的文字雜湊儲存成雜湊值名稱檔案。
        輸入文字、存檔路徑、編碼格式轉成沒有檔名為雜湊值且沒有副檔名。
        """
        self.hashfilename = sha256(text).hexdigest()
        with open(path + self.hashfilename,
                  mode=mode, encoding=encoding) as file:
            file.write(text)

    @classmethod
    def scan_folder(cls, path='./.temp/'):
        """
        掃描目錄底下的檔案名稱並回傳.

        針對指定的目錄位置底下掃描檔案，回傳序列。
        """
        multimedias = os.listdir(path)
        return multimedias

    @classmethod
    def remove_file(cls, path="./.temp/None.mp4"):
        """
        刪除指定路徑的目錄內檔案.

        預設是.temp目錄底下刪除。
        """
        os.remove(path)

    def remove_folder(self, path="./.temp/"):
        """
        刪除指定路徑的目錄內檔案.

        預設是.temp目錄底下刪除。
        """
        multimedias = self.scan_folder(path=path)
        for multimedia in multimedias:
            self.remove_file(path + multimedia)

    def multimedia_hash(self, input_path='./.temp/None.mp4',
                        output_path='./.mmdb/object/'):
        """
        雜湊指定的多媒體.

        讀取指定的多媒體時會以二進位的方式讀取，並將檔案以雜湊函數計算後的雜湊值製作成
        檔名，並同時取消副檔名。
        """
        self.mode = 'rb'
        multimedia = self.read_file(path=input_path,
                                    encoding=self.encoding,
                                    mode=self.mode,
                                    size=self.size)
        self.mode = 'wb'
        self.save_file(text=multimedia,
                       path=output_path,
                       encoding=self.encoding,
                       mode=self.mode)
        filename = ""
        i = -1
        while input_path[i] != "/":
            i -= 1
        filename = input_path[i + 1:]

        print(filename, self.hashfilename)

    def multimedia_folder_hash(self, input_path='./.temp/',
                               output_path='./.mmdb/object/'):
        """
        自動化目錄雜湊.

        指定路徑讀取目錄底下檔案再指定目錄轉出以檔案雜湊值為檔名的檔案.
        """
        multimedias = self.scan_folder(path=input_path)
        for multimedia in multimedias:
            self.multimedia_hash(input_path=input_path + multimedia,
                                 output_path=output_path)

    def multimedia_folder_hash_csv(self, input_path='./.temp/',
                                   output_path='./.mmdb/object/',
                                   save_path='./.mmdb/info/info.csv'):
        """
        檔案與雜湊值對應CSV.

        將檔案雜湊後得出的雜湊值與檔名搭配後存入CSV檔
        """
        multimedias = self.scan_folder(path=input_path)
        for multimedia in multimedias:
            self.multimedia_hash(input_path=input_path + multimedia,
                                 output_path=output_path)

            with open(save_path,
                      mode='a', newline='', encoding='utf8') as csvfile:
                # 建立 CSV 檔寫入器g
                writer = csv.writer(csvfile)

                # 寫入一列資料
                writer.writerow([self.filename, self.hashfilename])


HM = HashMultimedia()

HM.multimedia_folder_hash_csv()
