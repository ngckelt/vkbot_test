
class State:

    def __set_name__(self, owner, name):
        self.name = name

    def get_state(self) -> str:
        return self.name



