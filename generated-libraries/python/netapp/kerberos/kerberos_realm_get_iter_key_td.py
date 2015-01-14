from netapp.netapp_object import NetAppObject

class KerberosRealmGetIterKeyTd(NetAppObject):
    """
    Key typedef for table kerbrealm
    """
    
    _key_0 = None
    @property
    def key_0(self):
        """
        Field configname
        """
        return self._key_0
    @key_0.setter
    def key_0(self, val):
        if val != None:
            self.validate('key_0', val)
        self._key_0 = val
    
    @staticmethod
    def get_api_name():
          return "kerberos-realm-get-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-0',
        ]
    
    def describe_properties(self):
        return {
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
