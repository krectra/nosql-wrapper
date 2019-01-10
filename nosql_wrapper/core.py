from .constants import required_fields


class BaseDBWrapper(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.client = None

    def get_required(self):
        """ Retrieve required fields for specific DB
        :return:
        """

        # Retrieves class name to reference required fields
        db_name = self.__class__.__name__

        for field_name in required_fields[db_name]:
            setattr(self, field_name, self.kwargs.get(field_name))