# rime-koromaja
Rime 입력기용 한국어 로마자 입력 스키마  
Rime入力機用韓國語로마字入力스키마  
Korean romaja input schema for Rime IME  
Rime IME用韓国語ローマ字入力スキーマ  
中州韻輸入法引擎韓語羅馬輸入方案  
![gif](./img4md/demo.gif)

## How to install
1. Install [Rime IME](https://rime.im/download/)
2. Copy the following files into your Rime user directory and redeploy:
    * koromaja.schema.yaml
    * koromaja.dict.yaml
    * koromaja.hangul.dict.yaml
    * koromaja.hanja.dict.yaml
    * koromaja.user.dict.yaml
    * opencc/*

    or if your environment can use plum: `lazyfoxchan/rime-koromaja`

  You can reference: [Rime 中的數據文件分佈及作用 (Rime IME project official documentation)](https://github.com/rime/home/wiki/RimeWithSchemata#rime-%E4%B8%AD%E7%9A%84%E6%95%B8%E6%93%9A%E6%96%87%E4%BB%B6%E5%88%86%E4%BD%88%E5%8F%8A%E4%BD%9C%E7%94%A8)

## How to input

### Romaja input
Examples:
* `hangugfeo` or `hangugqeo` or `hangugEo` ➡ `한국어`
* `kareBangfi` or `kareBangqi` or`kareBangI` ➡ `카레빵이`
* `Gagg` or `Gakk` ➡ `깎`
* `xhxhxh` ➡ `ㅎㅎㅎ`
* `xJ` or `xZ` or `xC` or `xjj` or `xzz` or `xcc` ➡ `ㅉ`
* `xa` ➡ `ㅏ`

#### List of romaja
초성:
| Hangul | Only 초성 | ㄱ | ㄲ | ㅋ | ㄷ | ㄸ | ㅌ | ㅂ | ㅃ | ㅍ | ㅈ | ㅉ | ㅊ | ㅅ | ㅆ | ㅎ | ㄴ | ㅁ | ㅇ | ㄹ |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| Romaja | x + 초성 | g | G/K | k | d | D/T | t | b | B/P | p | j/z | J/Z/C | c | s | s | h | n | m | f/q or Shift + 중성 | r/l |

중성:
| Hangul | Only 중성 | ㅏ | ㅓ | ㅗ | ㅜ | ㅡ | ㅣ | ㅐ | ㅔ | ㅚ | ㅟ | ㅑ | ㅕ | ㅛ | ㅠ | ㅒ | ㅖ | ㅘ | ㅙ | ㅝ | ㅞ | ㅢ | ー |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| Romaja | x + 중성 | a | eo | o | u | eu | i | ae | e | oe | wi | ya | yeo | yo | yu | yae | ye | wa | wae | wo | we | ui | v |

종성:
| Hangul | Only 종성 | ㄱ | ㄲ | ㄳ | ㄴ | ㄵ | ㄶ | ㄷ | ㄹ | ㄺ | ㄻ | ㄼ | ㄽ | ㄾ | ㄿ | ㅀ | ㅁ | ㅂ | ㅄ | ㅅ | ㅆ | ㅇ | ㅈ | ㅊ | ㅋ | ㅌ | ㅍ | ㅎ |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| Romaja | x + 종성 | g | gg/kk | gs | n | nj | nh | d | r | rg | rm | rb | rs | rt | rp | rh | m | b | bs | s | ss | ng | j | c | k | t | p | h |

### Convertion
* While typing, press `Enter` to output hangul
  * `hangugfeo` + `Enter` ➡ `한국어`
* While typing, press `Shift` + `Enter` to output Latin characters
  * `hangugfeo` + `Shift` + `Enter` ➡ `hangugfeo`
* While typing, press `Space` to convert hanja
  * `hangugfeo` + `Space` ➡ `韓國語`

## License
Author: lazy fox chan  
License: [GNU Lesser General Public License v2.1](https://github.com/lazyfoxchan/rime-koromaja/blob/master/LICENSE)  
  
Hanja conversion dictionary was converted from [libhangul](https://github.com/libhangul/libhangul/tree/main/data/hanja) project  
More information about the original license and copyright can be found in the comments on the header line of `koromaja.hanja.dict.yaml`.
