from datetime import datetime


class DocBase(object):
    __setted_data = False

    def __getitem__(self, key):
        return self.metadata.get(key)
    
    def __str__(self):
        return f"{repr(self)}: {self.metadata}"

    def get(self, key):
        return self.metadata.get(key)

    @classmethod
    def __data_changed(cls, value):
        cls.__setted_data = value
    
    @property
    def metadata(self):
        data = {}
        for key, value in self.__dict__.items():
            if key.startswith("_") or key == "metaclass":
                continue

            if issubclass(type(value), DocBase):
                value = value.metadata

            data.update({key: value})
        return data

    @metadata.setter
    def metadata(self, data):
        if not isinstance(data, dict):
            raise RuntimeError("Data argument must be a dictionary")
        
        for key in self.__dict__.keys():
            if key.startswith("_") or key == "metaclass":
                continue
            
            v = data.get(key)
            
            if not v:
                continue
            elif issubclass(type(getattr(self, key)), DocBase):
                getattr(self, key).metaclass = v
            else:
                setattr(self, key, v)
                self.__data_changed(True)
    
    @property
    def has_data(self):
        return self.__setted_data


class FullPathDoc(DocBase):
    def __init__(self) -> None:
        super(FullPathDoc, self).__init__()

        self.linux = None
        self.mac = None
        self.win = None


class ProjectDoc(DocBase):
    def __init__(self) -> None:
        super(ProjectDoc, self).__init__()

        self.name = ""
        self.full_path = FullPathDoc()
        self.tags = []


class AssetFileDoc(DocBase):
    def __init__(self) -> None:
        super(AssetFileDoc, self).__init__()
        self._id = None

        self.asset_name = ""
        self.file_name = ""
        self.file_type = ""
        self.full_path = FullPathDoc()
        self.relative_path = ""
        self.tags = []
        self.version = 0.0
        self.step = ""
        self.project = ProjectDoc()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, i):
        self._id = i
