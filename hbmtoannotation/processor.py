class Processor:
    def __init__(self, name):
        self.name = name

    def processRoot(self, element):
        return f"package {element.get('package')}\n"

    def processClass(self, element):
        return f"""
        @Entity
        @Table(name="{element.get('table')}")
        class {element.get('name')}
        {{
        """

    def processId(self, element):
        return f"""
        @Id
        @Column(name="{element.get('column')}")
        private {element.get('type')} {element.get('name')};

        """

    def processProperty(self, element):
        return f"""
        @Column(name="{element.get('column')}")
        private {element.get('type')} {element.get('name')};

        """

    def processEnd(self, element):
        if element == 'end':
            return '}'
