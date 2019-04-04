from tap_density.streams.base import BaseAPIStream


class SpaceeventsStream(BaseAPIStream):
    TABLE = 'space_events'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['timestamp']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['timestamp']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def generate_urls(self,bookmark_date, current_date):

        response = self.client.make_request(
        url = '{}/spaces'.format(self.config.get('site')),
        method = self.API_METHOD,
        params = {}
        )

        spaces = [s['id'] for s in response['results']]
        space_urls = []

        for space in spaces:
            space_urls.append('{}/spaces/{}/events/'.format(self.config.get('site'),space))

        return space_urls, spaces


    def get_url(self, bookmark_date, current_date):
        space_urls = self.generate_urls(bookmark_date, current_date)[0]
        spaces = self.generate_urls(bookmark_date, current_date)[1]
        return space_urls, spaces, True

    def get_params(self, bookmark_date, current_date):
        return {'start_time': bookmark_date, 'end_time': current_date}
