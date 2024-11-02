from PIL import Image
import numpy as np


def rgbToAnsi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def imageToAscii(imagePath, newWidth=100):
    # 将图像转换为RGBA
    # image=Image.open()
    image = Image.open(imagePath).convert("RGBA")

    # 计算新的高度用于保持宽高比
    width, height = image.size
    aspectRatio = height / width
    newHeight = int(aspectRatio * newWidth * 0.55)

    # 缩放图像
    image = image.resize((newWidth, newHeight))
    imgArray = np.asarray(image)
    asciiImage = ""
    asciiChars = "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶"

    # 为每个像素生成字符及其颜色
    for row in imgArray:
        for pixel in row:
            r, g, b, a = pixel
            if a > 0:  # 只处理不透明的 像素
                # 根据亮度计算字符索引
                brightness = int((r + g + b) // 3)  # 计算平均亮度
                charIndex = brightness * (len(asciiChars) - 1) // 255  # 将255映射到字符数量范围
                asciiChar = asciiChars[charIndex]
                asciiImage += rgbToAnsi(r, g, b) + asciiChar  # 添加带颜色的字符
                # asciiChar = asciiChars[charIndex]
            else:
                asciiImage += " "  # 透明像素就用空格替代
        asciiImage += "\n"

    # 重置颜色
    asciiImage += "\003[0m"
    return asciiImage


def main():
    # 输入图像路径
    imagePath = input("请输入图片路径: ")
    # 生成 ASCII 图像

    # asciiArt = imageToAscii(imagePath)修正版本
    asciiArt = imageToAscii(imagePath)
    ascii(asciiArt)
    # 输出到控制台
    print(asciiArt)
    print("程序暂停，按回车继续...")
    input()


if __name__ == "__main__":
    main()
