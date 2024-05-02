require 'tinify'

Tinify.key = "gTMl0Bt2nr6KTHk4vWzkDjvrj8ZgNgZz" # 替换为你的 API 密钥 
# # 4yXgJN7B6X4zFf7MFCNLr4ysbSvlMn3n 

def compress_image(file_path)
  source = Tinify.from_file(file_path)
  source.to_file(file_path)  # 压缩并替换原文件
end

def compress_images_in_directory(directory)
  Dir.glob("#{directory}/*.{png,jpg,jpeg}").each do |file_path|
    puts "Compressing: #{file_path}"
    compress_image(file_path)
  rescue Tinify::Error => e  # 捕捉并处理可能的异常
    puts "Error compressing #{file_path}: #{e.message}"
  end
end

# 调用函数，指定要压缩的文件夹路径
compress_images_in_directory("/path/to/your/images")
