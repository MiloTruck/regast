from regast.core.core import Core

class Type(Core):
    @property
    def storage_size(self):
        raise NotImplementedError(f"Unable to compute storage_size of {self.__class__.__name__}")

    @property
    def is_dynamic(self) -> bool:
        return False