"""
檔案摘要製作.

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

    def __init__(self, hash_function=None):
        """
        初始化類別.

        選擇自己喜歡的雜湊函數，提供其他函式使用。
        """
        if hash_function is None:
            self.hash_function = sha256()
        else:
            self.hash_function = hash_function

    def save_file(self, text, path='../.temp/', encoding='utf8'):
        """
        雜湊文字存檔.

        針對輸入的文字雜湊儲存成雜湊值名稱檔案。
        輸入文字、存檔路徑、編碼格式轉成沒有檔名為雜湊值且沒有副檔名。
        """
        hash_function = self.hash_function
        filename = hash_function(text.encode(encoding)).hexdigest()
        file = open(path + filename, 'w', encoding=encoding)
        file.write(text)

    @classmethod
    def read_file(cls, path='./None.mp4', encoding='utf8', mode='r', size=-1):
        """
        讀取文件檔案並計算雜湊值.

        指定檔案路徑，將裡面的內容依照參數回傳。
        """
        text = open(path, mode=mode, encoding=encoding)
        return text.read(size)

    @classmethod
    def remove_multimedia(cls, path="./.temp/"):
        """
        刪除指定路徑的目錄內檔案.

        預設是.temp目錄底下刪除。
        """
        multimedia_list = os.listdir(path)
        for multimediafile in multimedia_list:
            os.remove(path + multimediafile)

    def read_multimedia(self, path='./.temp/',
                        encoding=None, mode="rb", size=1):
        """
        讀取指定檔案或指定路徑底下的多媒體.

        讀取指定的多媒體時會因為每一種使用的編碼都不同，因此會使用二進位的方式讀取，來
        解決這個問題，但因為可能檔案過於龐大，因此會需要一些方式解決。
        """
        multimedia = list()
        if path[-1:] == "/":
            multimedias = os.listdir(path)
            for media in multimedias:
                media = self.read_file(path=path + media,
                                       encoding=encoding, mode=mode, size=size)
                multimedia.append(media)
        else:
            multimedia.append(media)
        return multimedia
