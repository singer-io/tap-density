from tap_density.streams.base import BaseAPIStream
from dateutil.parser import parse


class SpacecountsStream(BaseAPIStream):
    TABLE = 'space_counts'
    # Endpoint does not provide us with an ID
    KEY_PROPERTIES = []
    BOOKMARK_PROPERTIES = ['timestamp']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['timestamp']
    INCLUSION = 'available'
    SELECTED = True
    API_METHOD = 'GET'

    def get_params(self, bookmark_date, current_date):
        return {'start_time': bookmark_date, 'end_time': current_date}

    def generate_urls(self, bookmark_date, current_date):

        response = self.client.make_request(
        url = '{}/spaces'.format(self.config.get('site')),
        method = self.API_METHOD,
        params = {}
        )

        spaces = [s['id'] for s in response['results']]
        spaces_created_at = [s['created_at'] for s in response['results']]
        space_urls = []

        for i, space in enumerate(spaces):
            # addressing issues with endpoint throwing up errors if we try to query count data before space creation
            if parse(self.get_params(bookmark_date, current_date)['end_time']) > parse(spaces_created_at[i]):
                space_urls.append('{}/spaces/{}/counts/'.format(self.config.get('site'),space))

        return space_urls, spaces

    def get_url(self, bookmark_date, current_date):
        space_urls = self.generate_urls(bookmark_date, current_date)[0]
        spaces = self.generate_urls(bookmark_date, current_date)[1]
        return space_urls, spaces, True
