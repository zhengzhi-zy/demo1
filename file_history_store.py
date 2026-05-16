import json
import os

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import message_to_dict, BaseMessage, messages_from_dict

def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(self.storage_path, session_id)
        os.makedirs(self.storage_path, exist_ok=True)

    def add_message(self, message: BaseMessage) -> None:  # 修复1：参数是单个message，不是列表
        all_messages = list(self.messages)
        all_messages.append(message)  # 修复2：用 append，不是 extend

        new_messages = [message_to_dict(m) for m in all_messages]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f, ensure_ascii=False)

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)
