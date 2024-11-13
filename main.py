import openai
import os
import json
from prompt_send_openai import system_prompt_candidate, fn_candidate_analysis
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Cấu hình API key của OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"

# Đọc nội dung CV từ file text
def read_cv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Hàm gọi API OpenAI và phân tích CV
def analyze_cv(cv_text, system_prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": cv_text},
        ],
        functions=fn_candidate_analysis,
        function_call={"name": "AnalyzeCV"},
    )
    
    return response

# Chạy chương trình
if __name__ == "__main__":
    # Đọc CV và hệ thống prompt
    cv_file_path = "data/cv_1.txt"  
    prompt_file_path = "prompt.txt"  

    cv_content = read_cv(cv_file_path)
    system_prompt = system_prompt_candidate

    # Gọi hàm phân tích CV
    result = analyze_cv(cv_content, system_prompt)

    # Đặt tên file lưu kết quả, có thể dựa trên tên file CV
    output_file_path = f"results/{cv_file_path.split('/')[-1].split('.')[0]}_result.json"
    
    # Lưu kết quả vào file JSON
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    print(f"Kết quả đã được lưu vào file {output_file_path}")

