from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topics: Topic):
        if topics not in self.topics:
            self.topics.append(topics)

    def add_document(self, documents: Document):
        if documents not in self.documents:
            self.documents.append(documents)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.__find_id(self.documents, document_id)

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.documents])

    def __find_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity
