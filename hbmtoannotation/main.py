import xml.etree.ElementTree as ETree
from process_delegator import ProcessDelegator
from writer import Writer


def readHbm():
    # ask user for hbm file's absolute path
    hbm_file_path = raw_input("Please provide hbm file path\n")
    return hbm_file_path


def parseHbm(hbm_file_path):
    return ETree.parse(hbm_file_path)


def processHbm():
    hbm_file = readHbm()

    hbm = parseHbm(hbm_file)

    # get root of the document i.e hibernate-mapping tag
    hibernate_mapping = hbm.getroot()

    # get class tag
    clazz = hibernate_mapping.find('class')

    # get id tag
    id_column = clazz.find('id')

    process_delegator = ProcessDelegator("process_delegator")

    writer = Writer('java_file_writer', hbm_file[:hbm_file.rfind('/') + 1] + clazz.get('name') + '.java')

    writer.write(process_delegator.delegate(hibernate_mapping))

    writer.write(process_delegator.delegate(clazz))

    writer.write(process_delegator.delegate(id_column))

    for column in clazz.iter('property'):
        writer.write(process_delegator.delegate(column))

    writer.write(process_delegator.delegate('end'))

    writer.close()


if __name__ == "__main__":
    processHbm()
