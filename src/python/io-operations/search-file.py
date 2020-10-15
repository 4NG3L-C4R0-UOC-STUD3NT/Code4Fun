import os

def search_file(directory = None, file = None):
    assert os.path.isdir(directory)
    current_path, directories, files = next(os.walk(directory))
    #print(files)
    if file in files:
        return os.path.join(directory, file)
    elif directories == '':
        return None
    else:
        for new_directory in directories:
            result = search_file(directory = os.path.join(directory, new_directory), file = file)
            if result:
                return result
        return None

print(search_file('F:/____Learning/____books/new/', 'Kubernetes on AWS - Ed Robinson.pdf'))
