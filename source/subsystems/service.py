from dataclasses import dataclass

@dataclass
class IService:
    @property
    def isDisabled(self) -> bool:
        return self._isDisabled

    @isDisabled.setter
    def isDisabled(self, condition: bool): self._isDisabled = condition  

    _name: str
    _isDisabled: bool = False
