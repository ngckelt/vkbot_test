import os
import json

from bot.settings import STORAGE_DIR

CURRENT_STATE = "current_state"


class StateStorage:

    def __init__(self, user_vk_id):
        self.user_vk_id = user_vk_id
        if not self.exists():
            self.alloc()

    def alloc(self) -> None:
        os.makedirs(f"{STORAGE_DIR}/{self.user_vk_id}/", exist_ok=True)
        with open(f"{STORAGE_DIR}/{self.user_vk_id}/{self.user_vk_id}.json", "w") as f:
            f.write(json.dumps({}))

    def free(self) -> None:
        os.remove(f"{STORAGE_DIR}/{self.user_vk_id}/{self.user_vk_id}.json")

    def exists(self) -> bool:
        return os.path.exists(f"{STORAGE_DIR}/{self.user_vk_id}/{self.user_vk_id}.json")

    def update_data(self, **data) -> None:
        current_data = self.get_data()
        for key, val in data.items():
            current_data[key] = val
        with open(f"{STORAGE_DIR}/{self.user_vk_id}/{self.user_vk_id}.json", "w") as f:
            f.write(json.dumps(current_data))

    def get_data(self) -> dict:
        with open(f"{STORAGE_DIR}/{self.user_vk_id}/{self.user_vk_id}.json") as f:
            data = json.loads(f.read())
        return data

    def get_current_state(self) -> str:
        if self.exists():
            data = self.get_data()
            return data.get(CURRENT_STATE)

    def set_state(self, state) -> None:
        self.update_data(current_state=state.get_state())



