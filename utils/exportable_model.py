from typing import Optional


class ExportableModel:

    def to_dict(self):
        return self.__dict__

