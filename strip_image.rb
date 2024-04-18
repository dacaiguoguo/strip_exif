require 'mini_magick'
require 'fileutils'
require 'find'

def strip_exif(image_path, output_path)
  image = MiniMagick::Image.open(image_path)
  image.strip
  image.write(output_path)
end

def process_directory(directory)
  output_directory = File.join(directory, "output")
  FileUtils.mkdir_p(output_directory) unless Dir.exists?(output_directory)

  Find.find(directory) do |path|
    if path.downcase.end_with?('.jpg', '.png')
      output_path = File.join(output_directory, File.basename(path))
      puts "Processing #{path} and saving to #{output_path}..."
      strip_exif(path, output_path)
    end
  end
end

# 指定你要清除 EXIF 数据的目录
directory_path = "/path/of"
process_directory(directory_path)


require 'tinify'
Tinify.key = "gTMl0Bt2nr6KTHk4vWzkDjvrj8ZgNgZz" # 替换为你的 API 密钥 
# 4yXgJN7B6X4zFf7MFCNLr4ysbSvlMn3n 
# 9W6NwNzPJ8qzWCz3q0BlBfM2DBYJBffY
def compress_image(image_path, output_path)
  source = Tinify.from_file(image_path)
  source.to_file(output_path)
end

# 在 process_directory 函数中调用 compress_image
