class MyPyYaml:
    def load(self, string):
        root = None
        cursor = None
        for line in string.split('\n'):
            if len(line) == 0:
                continue
            if line[0] == '-':
                array_entry = line.split('-')[1]
                if type(cursor) != type([]):
                    cursor = []
                cursor.append(self.__strip_and_cast_value(array_entry))
            else:
                splitted = line.split(':')
                if len(splitted) == 1:
                    continue
                key, value = splitted
                if self.__begin_line(key):
                    if root == None:
                        root = dict()
                    cursor = root
                key = key.lstrip()
                if len(value) == 0:
                    cursor[key] = dict()
                    cursor = cursor[key]
                    continue
                cursor[key] = self.__strip_and_cast_value(value)
        if root == None:
            return cursor
        return root

    def __begin_line(self, line):
        return len(line) - len(line.lstrip()) == 0

    def __strip_and_cast_value(self, value):
        value = value.lstrip()
        try:
            value = int(value)
        except:
            pass
        return value
