#多媒體資料庫
參照Git運作方式，但不會一樣，但希望可以直接引用Git去執行這個，但修改部份功能，會用Python做運作的方式，可以利用Python產生對應的資料。

## 目錄結構
資料庫結構
```
__mmdb__ --- table --- table name.yaml --- file hash
          |                             |- file name
          |- object --- multimedia object
                     |- info object
                     |- feature object
```
暫存目錄結構
```
__mpdlcache__
```
