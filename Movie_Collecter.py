class TreeNode:
    def __init__(self, title):
        self.title = title
        self.left = None
        self.right = None

class MovieCollection:
    def __init__(self):
        self.root = None

    def display_tree(self):
        self._display_tree(self.root, 0)

    def _display_tree(self, node, level):
        if node is not None:
            self._display_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.title)
            self._display_tree(node.left, level + 1)

    def insert(self, title):
        if self.root is None:
            self.root = TreeNode(title)
        else:
            result = self.check_insert(self.root, title)
            if result is False:
                print(f"Error: Movie '{title}' already exists in the collection.")

    def check_insert(self, node, title):
        if title == node.title:
            return False
        elif title < node.title:
            if node.left is None:
                node.left = TreeNode(title)
            else:
                return self.check_insert(node.left, title)
        else:
            if node.right is None:
                node.right = TreeNode(title)
            else:
                return self.check_insert(node.right, title)

        return True

    def search(self, title):
        return self.check_search(self.root, title)

    def check_search(self, node, title):
        if node is None:
            return False
        if title == node.title:
            return True
        elif title < node.title:
            return self.check_search(node.left, title)
        else:
            return self.check_search(node.right, title)

    def delete(self, title):
        self.root = self.check_delete_delete(self.root, title)

    def check_delete(self, node, title):
        if node is None:
            return node

        if title < node.title:
            node.left = self.check_delete_delete(node.left, title)
        elif title > node.title:
            node.right = self.check_delete_delete(node.right, title)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.find_min(node.right)
            node.title = temp.title
            node.right = self.check_delete_delete(node.right, temp.title)

        return node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def create(self, movie_list):
        for movie in movie_list:
            self.insert(movie)

# Example Usage
movie_collection = MovieCollection()
movies = ["Inception", "The Dark Knight", "Pulp Fiction", "Forrest Gump", "The Godfather","Avatar","Godzilla","The Avatar"]
movie_collection.create(movies)

# Search
print(movie_collection.search("Pulp Fiction"))  # Output: True
print(movie_collection.search("Avatar"))       # Output: False

# Delete
movie_collection.delete("Pulp Fiction")
print(movie_collection.search("Pulp Fiction"))  # Output: False

movie_collection.display_tree()

