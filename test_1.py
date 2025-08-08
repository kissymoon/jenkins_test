import os

from openai import OpenAI
import json


class DeepSeekChat:
    def __init__(self,
                 api_key="",
                 base_url=""
                 ):
                 self.client = OpenAI(api_key=api_key, base_url=base_url)
                 self.system_prompt = """

                 """

    def get_response(self, model, user_message):
        # 多轮对话文件
        json_path = f"json/{model.name}.json"
        os.makedirs(os.path.dirname(json_path), exist_ok=True)

        # 处理多轮对话
        message_list = [{"role": "system", "content": self.system_prompt},]

        if os.path.exists(json_path):  # 文件存在 → 读取
            with open(json_path, "r", encoding="utf-8") as f:
                json_message = json.load(f)
                json_message.pop(0)
                for i in json_message:
                    message_list.append(i)

        message_list.append({"role": "user", "content": user_message})

        # 请求
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=message_list,
            stream=False
        )
        get_deep = response.choices[0].message.content

        # 存储多轮对话
        message_list.append({"role": "assistant", "content": get_deep})
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(message_list, f, indent=4)

        return get_deep


# json_path = "json/+1 (202) 555-1234.json"
# os.makedirs(os.path.dirname(json_path), exist_ok=True)
# if not os.path.exists(json_path):
#     with open(json_path, "w", encoding="utf-8") as f:
#         json.dump([], f, indent=4)
#
# ds = DeepSeekChat()
# while True:
#     with open("json/+1 (202) 555-1234.json", "r", encoding="utf-8") as f:
#         json_list = json.load(f)
#     input1 = input("请输入：")
#     ds.get_response("+1 (202) 555-1234", input1, json_list)
