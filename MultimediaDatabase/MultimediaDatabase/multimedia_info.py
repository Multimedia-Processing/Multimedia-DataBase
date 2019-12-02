"""
多媒體資訊擷取.

將不同類型的媒體讀取資訊後儲存在物件區並搭配上資料表
"""


from MediaInfo import MediaInfo


INFO = MediaInfo(filename='../.temp/None.mp4')
INFO_DATA = INFO.getInfo()
print(INFO_DATA)
