import os
import shutil

def collect_images(source_dirs, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 支持的图片格式
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')
    
    for source_dir in source_dirs:
        # 遍历源目录及其所有子目录
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(image_extensions):
                    file_path = os.path.join(root, file)
                    # 创建输出文件的路径
                    output_file_path = os.path.join(output_dir, file)
                    
                    # 检查输出目录中是否已存在同名文件
                    if not os.path.exists(output_file_path):
                        shutil.copy(file_path, output_file_path)
                    else:
                        # 如果文件已存在，添加后缀以避免覆盖
                        base, extension = os.path.splitext(file)
                        new_name = f"{base}_copy{extension}"
                        output_file_path = os.path.join(output_dir, new_name)
                        shutil.copy(file_path, output_file_path)
                    
                    print(f"Copied: {file_path} -> {output_file_path}")

# 源目录列表
source_dirs = [
    ""
]

# 输出目录
output_dir = "collect_images"

# 执行图片收集
collect_images(source_dirs, output_dir)
