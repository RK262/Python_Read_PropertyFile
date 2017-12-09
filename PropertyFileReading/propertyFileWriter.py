from configparser import ConfigParser

if __name__ == '__main__':
    cfg=ConfigParser()

    ### Write to Config File all key value pair at a time.###
    cfg['ConfigSection_1']={'cfg1':'one','cfg12':'123','cfg13':'23.34','cfg14':'true'}

    ### Write to Config File one by one.###
    cfg['DB_Details']={}
    cfg['DB_Details']['DB_EndPoint']='myEndPoint'
    cfg['DB_Details']['DB_Port']='3306'
    cfg['DB_Details']['DB_Username']='uname'
    cfg['DB_Details']['DB_Password']='pw@123'

    cfg['AWS_Details']={}
    cfg['AWS_Details']['AccessKey']='myAccessKey'
    cfg['AWS_Details']['SecretAccessKey']='secretAccessKey'
    cfg['AWS_Details']['AWS_Region']='myregion'

    cfg['Proxy_Details']={}
    cfg['Proxy_Details']['Proxy_EndPoint']='proxyHost'
    cfg['Proxy_Details']['Proxy_Port']='9090'
    cfg['Proxy_Details']['Proxy_User']='puser'
    cfg['Proxy_Details']['Proxy_Password']='pw'

    with open('config.ini','w') as configFile:
        cfg.write(configFile)



