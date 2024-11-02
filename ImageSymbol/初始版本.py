from PIL import Image
import numpy as np


def image_to_ascii(image_path, new_width=100):
    # 打开图像并转换为灰度
    image = Image.open(image_path)
    image = image.convert("L")  # 转为灰度图

    # 计算新的高度以保持宽高比
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55用于调整高度

    # 缩放图像
    image = image.resize((new_width, new_height))

    # 将图像转换为 ndarray
    img_array = np.asarray(image)

    # 定义中文字符集，按照从密集到稀疏排列
    # 常用的中文字符，字符越密集，表示的内容越暗
    # ascii_chars = "█▓▒▒░ "  # 可以根据需要扩展或缩减字符
    ascii_chars = "@%#*+=-:. " * 4  # 多乘几遍来增加字符密度
    
    ascii_image = ""

    # 将像素值映射到 ASCII 字符
    for row in img_array:
        for pixel in row:
            ascii_image += ascii_chars[pixel // 51]  # 256/5 = 51，改变分割的值以适应字符数
        ascii_image += "\n"

    return ascii_image


def main():
    # 输入图像路径
    image_path = input("请输入图片路径: ")
    # 生成 ASCII 图像
    ascii_art = image_to_ascii(image_path)
    # 输出到控制台
    print(ascii_art)


if __name__ == "__main__":
    main()