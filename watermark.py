import os
import sys
from PIL import Image, ImageDraw, ImageFont

def add_watermark_to_image(image_path, watermark_path, output_dir):
    # Kiểm tra xem output_dir có tồn tại không, nếu không thì tạo mới
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Đọc ảnh từ đường dẫn
    image = Image.open(image_path)

    # Tạo một vùng làm việc mới có kích thước bằng với ảnh
    watermark_layer = Image.new("RGBA", image.size)

    # Đọc watermark từ đường dẫn
    watermark = Image.open(watermark_path)
    # Scale watermark cho phù hợp kích thước ảnh gốc
    watermark = watermark.resize(image.size, Image.LANCZOS)
    # Tạo mask từ watermark
    mask = watermark.convert("L").point(lambda x: min(x, 55))
    # Chèn watermark vào layer
    watermark_layer.paste(watermark, (0, 0), mask=mask)

    # Ghép ảnh gốc với watermark_layer
    watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark_layer)

    # Tạo tên file đầu ra
    output_filename = os.path.basename(image_path)
    output_path = os.path.join(output_dir, output_filename)

    # Lưu ảnh đã đánh dấu vào output_dir
    watermarked_image.convert(image.mode).save(output_path)

if __name__ == "__main__":
    # Kiểm tra số lượng tham số dòng lệnh
    if len(sys.argv) != 4:
        print("Usage: python watermarker.py input_dir output_dir watermark.png")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    watermark_path = sys.argv[3]

    # Lặp qua tất cả các file ảnh trong thư mục input_dir
    for filename in os.listdir(input_dir):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(input_dir, filename)
            add_watermark_to_image(image_path, watermark_path, output_dir)
