from bot.storage import StateStorage
from bot.states import State


class FSMContext:

    def __init__(self, user_vk_id):
        self.user_vk_id = user_vk_id
        self.storage = StateStorage(user_vk_id)

    async def get_data(self) -> dict:
        return self.storage.get_data()

    async def update_data(self, **data) -> None:
        self.storage.update_data(**data)

    async def get_state(self) -> str:
        return self.storage.get_current_state()

    async def set_state(self, state: State) -> None:
        self.storage.set_state(state)

    async def get_current(self) -> None:
        return self.storage.get_current_state()

    async def start(self) -> None:
        self.storage.alloc()

    async def finish(self) -> None:
        self.storage.free()
