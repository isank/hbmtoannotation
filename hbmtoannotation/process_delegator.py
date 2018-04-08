from processor import Processor


class ProcessDelegator:
    def __init__(self, name):
        self.name = name
        self.hbm_processor = Processor('hbm_processor')

    def delegate(self, element):
        if element == 'end':
            return self.hbm_processor.processEnd(element)
        if element.tag == 'hibernate-mapping':
            return self.hbm_processor.processRoot(element)
        if element.tag == 'class':
            return self.hbm_processor.processClass(element)
        if element.tag == 'id':
            return self.hbm_processor.processId(element)
        if element.tag == 'property':
            return self.hbm_processor.processProperty(element)
