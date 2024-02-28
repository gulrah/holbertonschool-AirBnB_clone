import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path: str = "file.json"
    __objects: dict[str, object] = {}

    def all(self) -> dict[str, object]:
        return self.__objects

    def new(self, obj) -> None:
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self) -> None:
        with open(self.__file_path, "w") as fd:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, fd)

    def reload(self) -> None:
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as fd:
                self.__objects = {k: BaseModel(**v) for k, v in json.load(fd).items()}
