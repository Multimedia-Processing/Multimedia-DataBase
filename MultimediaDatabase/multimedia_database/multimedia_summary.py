"""
多媒體檔案摘要製作.

將各種數位媒體使用密碼學的雜湊函式的計算，將計算結果雜湊值作為檔案名稱且不包含副檔名，解
決因為媒體重複性質高造成的問題。
"""


import os
from hashlib import sha256


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
        self.save = True

    @classmethod
    def read_file(cls, path='../__mpdlcache__/None.mp4',
                  encoding=None, mode='rb', size=-1):
        """
        讀取文件檔案.

        指定檔案路徑，將裡面的內容依照參數回傳。
        """
        with open(path, mode=mode, encoding=encoding) as text:
            return text.read(size)

    def save_file(self, text, path='../__mmdb__/object/',
                  encoding=None, mode='wb'):
        """
        雜湊二進位檔案後存檔.

        針對輸入的文字雜湊儲存成雜湊值名稱檔案。
        輸入文字、存檔路徑、編碼格式轉成沒有檔名為雜湊值且沒有副檔名。
        """
        self.hashfilename = sha256(text).hexdigest()
        with open(path + self.hashfilename,
                  mode=mode, encoding=encoding) as file:
            if self.save is True:
                if mode == 'wb':
                    file.write(text)
                else:
                    file.write(text.decode('utf8'))

    @classmethod
    def scan_folder(cls, path='../__mpdlcache__/'):
        """
        掃描目錄底下的檔案名稱並回傳.

        針對指定的目錄位置底下掃描檔案，回傳序列。
        """
        multimedias = os.listdir(path)
        return multimedias

    @classmethod
    def remove_file(cls, path="../__mpdlcache__/None.mp4"):
        """
        刪除指定路徑的目錄內檔案.

        預設是__mpdlcache__目錄底下刪除。
        """
        os.remove(path)

    def remove_folder(self, path="../__mpdlcache__/"):
        """
        刪除指定路徑的目錄內檔案.

        預設是__mpdlcache__目錄底下刪除。
        """
        multimedias = self.scan_folder(path=path)
        for multimedia in multimedias:
            self.remove_file(path + multimedia)

    def multimedia_hash(self, input_path='../__mpdlcache__/None.mp4',
                        output_path='../__mmdb__/object/',
                        file=True,
                        folder=False):
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
        self.filename = self.path_string_extraction(
            text=input_path, folder=folder, file=file
        )
        print(self.filename, self.hashfilename, '\n')

    def multimedia_folder_hash(self, input_path='../__mpdlcache__/',
                               output_path='../__mmdb__/object/'):
        """
        自動化目錄雜湊.

        指定路徑讀取目錄底下檔案再指定目錄轉出以檔案雜湊值為檔名的檔案.
        """
        multimedias = self.scan_folder(path=input_path)
        for multimedia in multimedias:
            self.multimedia_hash(input_path=input_path + multimedia,
                                 output_path=output_path)

    @classmethod
    def path_string_extraction(cls, text='abcd/efgh.mp4',
                               folder=False, file=True, file_extension=True):
        """
        針對路徑擷取指定的檔名.

        將輸入的路徑依照參數去控制檔名的擷取方式。
        folder:True=有路徑，False=沒路徑
        file:True=有檔名，False=沒檔名
        file_extension:True=有副檔名，False=沒副檔名
        """
        no_folder = -1
        while text[no_folder] != "/" and "/" in text:
            no_folder -= 1

        no_extension = -1
        while text[no_extension] != "." and "." in text:
            no_extension -= 1

        if folder is True and "/" in text:
            name_folder = text[:no_folder + 1]
        else:
            name_folder = ""

        if file is True:
            name_file = text[no_folder + 1:no_extension]
        else:
            name_file = ""

        if file_extension is True and "." in text:
            name_file_extension = text[no_extension:]
        else:
            name_file_extension = ""

        name = name_folder + name_file + name_file_extension
        return name


if __name__ == '__main__':
    HM = HashMultimedia()
