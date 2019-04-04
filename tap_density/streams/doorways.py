from tap_density.streams.base import BaseAPIStream


class DoorwaysStream(BaseAPIStream):
    TABLE = 'doorways'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['updated_at']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['updated_at']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def get_url(self, bookmark_date, current_date):
        return ['{}/doorways'.format(self.config.get('site'))], [], False

    def get_params(self, bookmark_date, current_date):
        return {}
