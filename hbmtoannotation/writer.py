# class to create and write java file
class Writer:
    def __init__(self, name, java_file_path):
        self.name = name
        self.java_file = open(java_file_path, 'w')

    def write(self, string):
        self.java_file.write(string)

    def close(self):
        self.java_file.close()
