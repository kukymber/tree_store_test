from collections import defaultdict

class TreeStore:
    def __init__(self, items):
        self.items = items
        self.items_dict = {item['id']: item for item in items}
        self.children_dict = defaultdict(list)
        for item in items:
            self.children_dict[item['parent']].append(item)

    def getAll(self):
        return self.items

    def getItem(self, id):
        return self.items_dict.get(id, None)

    def getChildren(self, id):
        return self.children_dict.get(id, [])

    def getAllParents(self, id):
        parents = []
        current_item = self.getItem(id)
        while current_item and current_item['parent'] in self.items_dict:
            parents.append(current_item)
            parent_id = current_item['parent']
            current_item = self.items_dict.get(parent_id, None)
        return parents

if __name__ == "__main__":
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)
    print(ts.getAll())
    print(ts.getItem(7))
    print(ts.getChildren(4))
    print(ts.getAllParents(7))
