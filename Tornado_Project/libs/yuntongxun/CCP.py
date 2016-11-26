# coding:utf-8

from CCPRestSDK import REST
import ConfigParser

_accountSid= '8aaf070858862df301588a70f27501e7'; 
#说明：主账号，登陆云通讯网站后，可在"控制台-应用"中看到开发者主账号ACCOUNT SID。

_accountToken= 'dc1de428fe1f4ba2856cbb4e2a4e9836'; 
#说明：主账号Token，登陆云通讯网站后，可在控制台-应用中看到开发者主账号AUTH TOKEN。

_appId='8aaf070858862df301588a70f3d801ee'; 
#请使用管理控制台首页的APPID或自己创建应用的APPID.

_serverIP='sandboxapp.cloopen.com';
#说明：请求地址，生产环境配置成app.cloopen.com。

_serverPort='8883'; 
#说明：请求端口 ，生产环境为8883.

_softVersion='2013-12-26'; #说明：REST API版本号保持不变。 

class _CCP(object):
    def __init__(self):
        self.rest = REST(_serverIP, _serverPort, _softVersion) 
        self.rest.setAccount(_accountSid, _accountToken) 
        self.rest.setAppId(_appId)

    # 单例保证全局只有唯一的一个实例
    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def sendTemplateSMS(self, to, datas, tempId):
        return self.rest.sendTemplateSMS(to, datas, tempId)

ccp = _CCP.instance()

if __name__ == '__main__':
    ccp.sendTemplateSMS('15716640789', ['1234', 5], 1)