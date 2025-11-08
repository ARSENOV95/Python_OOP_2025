from project.category import Category
from project.topic import Topic

class Document:
    def __init__(self,id_: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags: list = []

    @classmethod
    def from_instances(cls,id: int, category: Category, topic: Topic, file_name: str):
        return cls(id,category.id,topic.id,file_name)