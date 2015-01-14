from netapp.security.security_login_role_info import SecurityLoginRoleInfo
from netapp.netapp_object import NetAppObject

class SecurityLoginRoleDeleteIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against security login role object.
    were not deleted due to some error.
    deleted due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the deletion operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _security_key = None
    @property
    def security_key(self):
        """
        The keys for the security login role object to which the
        deletion applies.
        """
        return self._security_key
    @security_key.setter
    def security_key(self, val):
        if val != None:
            self.validate('security_key', val)
        self._security_key = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the operation caused an error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    @staticmethod
    def get_api_name():
          return "security-login-role-delete-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'security-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'security_key': { 'class': SecurityLoginRoleInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
