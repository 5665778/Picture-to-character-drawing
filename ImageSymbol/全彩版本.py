from PIL import Image
import numpy as np


def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def image_to_ascii(image_path, new_width=100):
    # 打开图像并转换为RGBA（包含透明度）
    image = Image.open(image_path).convert("RGBA")  # 保持原图的颜色信息

    # 计算新的高度以保持宽高比
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55用于调整高度

    # 缩放图像
    image = image.resize((new_width, new_height))
    img_array = np.asarray(image)

    ascii_image = ""

    # 定义字符集，字符比例由亮度决定
    ascii_chars = "█▓▒▒░░░ "

    # 为每个像素生成字符及其颜色
    for row in img_array:
        for pixel in row:
            r, g, b, a = pixel
            if a > 0:  # 只处理不透明的 像素
                brightness = (r + g + b) // 3  # 计算亮度
                ascii_char = ascii_chars[brightness // 26]
                ascii_image += rgb_to_ansi(r, g, b) + ascii_char  # 添加带颜色的字符
            else:
                ascii_image += " "  # 透明像素用空格替代
        ascii_image += "\n"

    ascii_image += "\033[0m"  # 重置颜色
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