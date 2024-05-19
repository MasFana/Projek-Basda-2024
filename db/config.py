from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # MEMBUAT PARSER
    parser = ConfigParser()
    # MEMBACA FILE CONFIG
    parser.read(filename)

    # MENDAPATKAN SECTION DENGAN DEFAULT POSTGRESQL
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section %s tidak ditemukan di file %s'.format(section, filename))

    return db