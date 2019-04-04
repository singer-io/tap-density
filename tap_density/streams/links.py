from tap_density.streams.base import BaseAPIStream


class LinksStream(BaseAPIStream):
    TABLE = 'links'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['id']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['created_at']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def get_url(self, bookmark_date, current_date):
        return ['{}/links'.format(self.config.get('site'))], [], False

    def get_params(self, bookmark_date, current_date):
        return {}
