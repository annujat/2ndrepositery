from configparser import ConfigParser


def configs(section, key):
    conf = ConfigParser()
    conf.read("./ConfigurationFile/testingworld.cfg")
    return conf.get(section, key)

def elements(section,key):
    con = ConfigParser()
    con.read("./ConfigurationFile/testingworld.cfg")
    return con.get(section,key)
