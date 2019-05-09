#画像を表現するクラスをロード
from PIL import Image

# ファイルをグレースケールに変換
def convert_to_gray(img,filename,filetype):

    gray_img = img.convert('L')
    gray_img.save(filename + '_gry' + filetype)

# ファイルを白黒画像に変換
def convert_to_whiteblack(img,filename,filetype):

    wb_img = img.convert('L')
    wb_img.point(lambda x: 0 if x < 230 else x)   # 値が230以下は0になる
    wb_img.save(filename + '_wb' + filetype)

#画像をを開く
filename = 'minion'
filetype = '.jpg'
img = Image.open(filename + filetype)

#グレースケールに変換
convert_to_gray(img, filename, filetype)

#白黒に変換
convert_to_whiteblack(img, filename, filetype)
