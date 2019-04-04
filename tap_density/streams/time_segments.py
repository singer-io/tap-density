from tap_density.streams.base import BaseAPIStream


class TimesegmentsStream(BaseAPIStream):
    TABLE = 'time_segments'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['id']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['id']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def get_url(self, bookmark_date, current_date):
        return ['{}/time_segments'.format(self.config.get('site'))], [], False

    def get_params(self, bookmark_date, current_date):
        return {}
