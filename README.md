# 多媒體資料庫
參照Git運作方式，但不會一樣，但希望可以直接引用Git去執行這個，但因為Git並不是以SHA2或者SHA3甚至更高的去做關聯，因此會用Python做另外的檔案處理並交給Git協助備份的方式運作。  

此系統的目標就是不需要特別程式與軟體就可以存取與調閱資料庫，並且可以輕易的檢閱內容，因此 **文字編輯器的可讀性與媒體的完整性** 是這個資料庫的目標， **存取的效率與容量比** 並未成為此資料庫追求的目標，雖然也很重要但不是首要。

Python的擴充性成為此資料庫首選開發程式，同時也因為上述原因所以選用Python。

# 目錄結構
## 資料庫目錄結構
以下是資料庫的目錄結構，此結構會是多媒體在運作時方式。

```
__mmdb__ -|- table -|- table name.yaml -|- file hash
          |                             |- info hash
          |                             |- feature hash
          |- object -|- multimedia object
                     |- info object
                     |- feature object
```

## 暫存目錄結構
```
__mpdlcache__
```

# 多媒體資料庫結構
### 型態對應表
以下是Python型態對應YAML型態的表示方法，Python的型態作為「鍵值」(key)對應YAML的表示方式。

```YAML
none: [~, null]
bool: [true, false, on, off]
int: 42
float: 3.14159
list: [LITE, RES_ACID, SUS_DEXT]
dict: {hp: 13, sp: 5}
```

## 資料表
「資料表」(Table)

## 多媒體物件
「多媒體物件」(multimedia object)

## 資訊物件
「資訊物件」(info object)是用於紀錄多媒體的資訊，一個多媒體檔案只能對應一個資訊物件，因此資訊物件是針對多媒體格式紀錄，例如影片長度、解碼器、編碼器與容器等針對這個檔案內容，而非製作時間、作者與公司等相關紀錄，使用較為單一而明確。

### 資訊物件結構
#### Python
```python
{
    "id": str,
    "info": {
        "bit_rate": int,
        "duration": float,
        "size": int,
        "videos": [
            {
                "aspect_ratio": str,
                "bit_rate": int,
                "codec": str,
                "format": str,
                "framerate": float,
                "pixel_format": str,
                "resolution": (
                    int # Width,
                    int # Height
                )
            }
        ],
        "audios": [
            {
                "bit_rate": int,
                "channel_count": int,
                "channel_layout": str,
                "codec": str,
                "format": str,
                "sample_rate": int # Hz
            }
        ],
        "subtitles": [
            {
                "codec": str,
                "language": str
            }
        ],
        "chapters": [
            {
                "title": str,
                "start": float,
                "end": float,
            }
        ]
    }
}
```

#### YAML
```YAML
id: !!str
info:
  audios:
  - bit_rate: !!int
    channel_count: !!int
    channel_layout: !!str
    codec: !!str
    format: !!str
    sample_rate: !!int
  bit_rate: !!int
  chapters:
    - title: !!str
      start: !!float
      end: !!float
  duration: !!float
  extension: !!str
  size: !!int
  subtitles:
    - codec: !!str
      language: !!str
  videos:
  - aspect_ratio: !!str
    bit_rate: !!int
    codec: !!str
    format: !!str
    framerate: !!float
    pixel_format: !!str
    resolution: !!python/tuple
    - 720
    - 576
```

## 特徵物件
「特徵物件」(feature object)用於紀錄一個多媒體的特徵，類似於基本的製作時間、作者、公司與其他相關紀錄，這部份就相當開放，但基本上會有提供一些常用的方式。

### 特徵物件結構
```YAML
id:
  - !!str
  - multimedia hash value
number: null
serial number: null
name:
  - !!list
  - !!str
  - !!dirt
videotape:
  kind: !!str
  front view: !!str
  rear view: !!str
  right view: !!str
  left view: !!str
  bottom view: !!str
  top view: !!str
  cassette front view: !!str
  cassette rear view: !!str
  cassette right view: !!str
  cassette left view: !!str
  cassette bottom view: !!str
  cassette top view: !!str
dvd:
  - !!bool
  - null
mp2:
  - !!bool
  - null
mp4:
  - !!bool
  - null
google drive:
  - !!bool
  - null
hard drive:
  - !!bool
  - null
youtube:
  - !!bool
  - null
nas:
  - !!bool
  - null
remark:
  - !!list
  - !!str
  - !!dirt

```
