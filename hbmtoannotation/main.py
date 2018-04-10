import os
import sys
import xml.etree.ElementTree as ETree

from process_delegator import ProcessDelegator
from writer import Writer

path = os.path

arguments = sys.argv
arguments.pop(0)  # First argument is always the current file name
args_len = len(arguments)


def processHbm():
    # get root of the document i.e hibernate-mapping tag
    hibernate_mapping = ETree.parse(file_path).getroot()

    # get class tag
    clazz = hibernate_mapping.find('class')

    # get id tag
    id_column = clazz.find('id')

    process_delegator = ProcessDelegator("process_delegator")

    writer = Writer('java_file_writer', file_path[:file_path.rfind('/') + 1] + clazz.get('name') + '.java')

    writer.write(process_delegator.delegate(hibernate_mapping))

    writer.write(process_delegator.delegate(clazz))

    writer.write(process_delegator.delegate(id_column))

    for column in clazz.iter('property'):
        writer.write(process_delegator.delegate(column))

    writer.write(process_delegator.delegate('end'))

    writer.close()


if args_len > 0:

    file_path = path.abspath(arguments[0])

    # Check if argument is a file or a directory
    if not path.isfile(file_path):
        print(f"'{file_path} is not a file ")
        exit(0)

    processHbm()
