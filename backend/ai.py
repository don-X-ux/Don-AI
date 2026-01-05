import openai

# 🔑 Thay bằng API KEY của bạn
openai.api_key = "YOUR_API_KEY"


def chat_ai(user_message: str) -> str:
    """
    Hàm gửi tin nhắn người dùng tới AI
    và nhận câu trả lời
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Bạn là một AI thông minh, trả lời rõ ràng, "
                        "chi tiết, dễ hiểu, có thể giải quyết câu hỏi phức tạp."
