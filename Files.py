from abc import ABC, abstractmethod
import Users


class File(ABC):
    """
    Abstract class for files.
    name: name of the file.
    """
    @abstractmethod
    def __init__(self, name: str):
        self.name = name


class Directory(File):
    """
    Class for directories.
    name: name of the directory.
    """

    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.files = []

    def add_file(self, file) -> None:
        """
        Add a file to the directory.
        :param file: File to add.
        :return: None.
        """
    
        if file not in self.files:
            self.files.append(file)
        
    def delete_file(self, file_name: str):
        """
        Receives file's name and delete it if it is exist.
        :param file_name: File's name.
        :return: If delete file.
        """
        for file in self.files:
            if file.get_name() == file_name:
                self.files.remove(file)
                return True
        return False

    def __str__(self) -> str:
        """
        Return a string representation of the directory.
        :return: String representation of the directory.
        and the files in it.
        """
        ret = f"{self.name}:\n"
        for file in self.files:
            ret += file.__str__() + ", "

        return ret

    def get_file(self, file_name: str):
        """
        Receives file's name and return it if it is exist.
        :param file_name: File's name.
        :return: One of the possible types of file if it is exist. Else, None.
        """
        for file in self.files:
            if file.get_name() == file_name:
                return file
        return None


class Readable_file(File):
    """
    Class for readable files (Image or txt) .
    name: name of the file.
    content: content of the file.
    """

    def __init__(self, name: str, size: int, creator: Users.User, content):
        super().__init__(name)
        self.size = size
        self.creator = creator
        self.content = content
        
    def read(self, user: Users.User):
        """
        Return the content of the file if user  creat the file.
        :return: The content of the file.
        """
        if user == self.creator or isinstance(user, Users.Admin):
            return self.content
        else:
            return None

    def __str__(self) -> str:
        """ Return a string representation of the file.
        :return: String representation of the file.
        """
        return f"{self.name}: {self.content}"


class Text_file(Readable_file):
    """
    Class for text files.
    name: name of the file.
    content: content of the file.
    """
    def __init__(self, name: str, size: int, creator: Users.User, content):
        super().__init__(name, size, creator, content)

    def count(self, word: str) -> int:
        """ Return the number of the word in the file.
        :return: The number of the word in the file.
        """
        return self.content.count(word)


class Image_file(Readable_file):
    """
        Class for Image files.
        name: name of the file.
        content: content of the file.
        """
    def __init__(self, name: str, size: int, creator: Users.User, content):
        super().__init__(name, size, creator, content)

    def get_dimensions(self):
        """ Return the dimensions of the image.
        :return: The dimensions of the image.
        """
        return self.content.get_dimensions()
