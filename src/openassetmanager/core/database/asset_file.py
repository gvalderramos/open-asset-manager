from pprint import pprint
from typing import List, Generator
from pymongo.collection import Collection
from openassetmanager.core.database.model_base import ModelBase
from openassetmanager.core.database.documents import AssetFileDoc


class AssetFilesHandler(ModelBase):
    def __init__(self) -> None:
        super(AssetFilesHandler, self).__init__()
    
    @property
    def asset_collection(self) -> Collection:
        return self.db.asset_collection
    
    def find(self, *args) -> Generator[AssetFileDoc, None, None]:
        for doc in self.asset_collection.find(*args):
            asset = AssetFileDoc()
            asset.metadata = doc
            if asset.has_data:
                yield asset
    
    def find_one(self, *args) -> AssetFileDoc:
        doc = self.asset_collection.find_one(*args)
        asset = AssetFileDoc()
        asset.metadata = doc
        if asset.has_data:
            return asset

    def insert_one(self, file: AssetFileDoc) -> AssetFileDoc:
        if not isinstance(file, AssetFileDoc):
            raise RuntimeError("file_doc argument must be a AssetFileDoc instance")
        doc = self.asset_collection.insert_one(file.metadata)
        file.id = doc.inserted_id
        
        return file

    def insert_many(self, files: List[AssetFileDoc]) -> List[AssetFileDoc]:
        if not isinstance(files, (list, tuple)):
            raise RuntimeError("files argument must be a list of AssetFileDoc instances")

        ids = self.asset_collection.insert_many([f.metadata for f in files])
        for i, f in map(ids, files):
            f.id = i
        
        return files


if __name__ == "__main__":
    asset = AssetFilesHandler()
    # data = {
    #     "asset_name": "Character1",
    #     "file_name": "Character1.v001.ma",
    #     "file_type": "ma",
    #     "full_path": {
    #         "linux": "/mnt/server/ProjectX/asset/character/Character1/modeling/work/Character1.v001.ma",
    #         "mac": None,
    #         "win": None
    #     },
    #     "relative_path": "asset/character/Character1/work/Character1.v001.ma",
    #     "tags": [
    #         "character",
    #         "hero",
    #         "action",
    #         "human"
    #     ],
    #     "version": 1.0,
    #     "step": "modeling",
    #     "project": {
    #         "name": "ProjectX",
    #         "full_path": {
    #             "linux": "/mnt/server/ProjectX",
    #             "mac": None,
    #             "win": None
    #         },
    #         "tags": [
    #             "action",
    #             "scifi",
    #             "animation"
    #         ]
    #     }
    # }
    # f1 = AssetFileDoc()
    # f1.metadata = data
    # asset.insert_one(f1)
    # print(f1.id)
    for a in asset.find():
        pprint(a.metadata)