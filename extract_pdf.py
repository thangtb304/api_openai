from pdfminer.high_level import extract_text
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Đường dẫn file PDF
file_name="CV_1.pdf"
file_path = f"data/{file_name}"

def extract_text_pdfminer(pdf_path):
    # Trích xuất văn bản từ file PDF
    text = extract_text(pdf_path)
    return text

# Hàm lưu văn bản vào file .txt
def save_extracted_text(text, pdf_name):
    # Tạo thư mục 'extract' nếu chưa tồn tại
    output_dir = "extract"
    os.makedirs(output_dir, exist_ok=True)
    # Lấy tên file không có phần mở rộng
    pdf_name = os.path.splitext(os.path.basename(pdf_name))[0]
    # Đường dẫn lưu file
    output_path = os.path.join(output_dir, f"{os.path.splitext(pdf_name)[0]}.txt")
    
    # Lưu văn bản vào file .txt
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Văn bản đã được lưu tại: {output_path}")

# Gọi hàm để trích xuất văn bản
pdf_text = extract_text_pdfminer(file_path)
save_extracted_text(pdf_text, file_name)
print(pdf_text)
