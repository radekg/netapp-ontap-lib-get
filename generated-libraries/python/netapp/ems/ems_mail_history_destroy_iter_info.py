from netapp.ems.ems_mail_history_info import EmsMailHistoryInfo
from netapp.netapp_object import NetAppObject

class EmsMailHistoryDestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against ems-mail-history object.
    were not deleted due to some error.
    due to some error.
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
    
    _ems_mail_history_key = None
    @property
    def ems_mail_history_key(self):
        """
        The keys for the ems-mail-history object to which the
        deletion applies.
        """
        return self._ems_mail_history_key
    @ems_mail_history_key.setter
    def ems_mail_history_key(self, val):
        if val != None:
            self.validate('ems_mail_history_key', val)
        self._ems_mail_history_key = val
    
    @staticmethod
    def get_api_name():
          return "ems-mail-history-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'ems-mail-history-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ems_mail_history_key': { 'class': EmsMailHistoryInfo, 'is_list': False, 'required': 'required' },
        }