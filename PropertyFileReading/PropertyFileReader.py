from configparser import ConfigParser

if __name__ == '__main__':
    cfg=ConfigParser()
    cfg.read('config.ini')

    ## Below method will print name of all sections in config file.
    print(cfg.sections())

    ## Below method will print all key and values in section  ConfigSection_1.
    print(cfg.items('ConfigSection_1'))

    ## Below method print all keys in section ConfigSection_1.
    print(list(cfg['ConfigSection_1'].keys()))

    ## To get the key values of ConfigSection_1.
    print(cfg.get('ConfigSection_1','cfg1'))
    print(cfg.getint('ConfigSection_1','cfg12'))
    print(cfg.getfloat('ConfigSection_1','cfg13'))
    print(cfg.getboolean('ConfigSection_1','cfg14'))

    print(cfg.items('DB_Details'))
    print(cfg.get('DB_Details','db_endpoint'))
    print(cfg.getint('DB_Details','db_port'))
    print(cfg.get('DB_Details','db_username'))
    print(cfg.get('DB_Details','db_password'))

    print(cfg.items('AWS_Details'))
    print(cfg.get('AWS_Details','accesskey'))
    print(cfg.get('AWS_Details','secretaccesskey'))
    print(cfg.get('AWS_Details','aws_region'))

    print(cfg.items('Proxy_Details'))
    print(cfg.get('Proxy_Details','proxy_endpoint'))
    print(cfg.getint('Proxy_Details','proxy_port'))
    print(cfg.get('Proxy_Details','proxy_user'))
    print(cfg.get('Proxy_Details','proxy_password'))

