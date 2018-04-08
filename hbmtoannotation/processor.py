class Processor:
    def __init__(self, name):
        self.name = name

    def processRoot(self, element):
        return 'package ' + element.get('package') + ';\n'

    def processClass(self, element):
        result = '@Entity' + '\n'
        result += '@Table(name="' + element.get('table') + '")' + '\n'
        result += 'class ' + element.get('name') + '\n'
        result += '{' + '\n'
        return result
    
    def processId(self, element):
        result = '@Id' + '\n'
        result += '@Column(name="' + element.get('column') + '")' + '\n'
        result += 'private ' + element.get('type') + ' ' + element.get('name') + ';\n'
        return result
    
    def processProperty(self, element):
        result = '@Column(name="' + element.get('column') + '")' + '\n'
        result += 'private ' + element.get('type') + ' ' + element.get('name') + ';\n'
        return result

    def processEnd(self, element):
        if element == 'end':
            return '}'