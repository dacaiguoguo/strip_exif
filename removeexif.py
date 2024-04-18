import os
from PIL import Image

def strip_exif(image_path, output_path):
    with Image.open(image_path) as image:
        # Convert image to RGB to remove any other profiles (like ICC profiles)
        data = image.convert('RGB')
        # Save the image without EXIF data to the specified output path
        data.save(output_path, "JPEG" if image_path.lower().endswith('.jpg') else "PNG")

def process_directory(directory):
    output_directory = os.path.join(directory, "output")
    # 创建输出目录如果它不存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 遍历目录下所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.png')):
                file_path = os.path.join(root, file)
                output_path = os.path.join(output_directory, file)
                print(f"Processing {file_path} and saving to {output_path}...")
                strip_exif(file_path, output_path)


# 指定你要清除 EXIF 数据的目录
directory_path = "/path/of"
process_directory(directory_path)

# 压缩图片第一步 先清除 EXIF 数据 再 tinypng 压缩
