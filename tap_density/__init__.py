import singer
import singer.utils
import tap_framework
import tap_density.client
import tap_density.streams

LOGGER = singer.get_logger()


class APIRunner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():

    args = singer.utils.parse_args(
        required_config_keys=['api_key', 'start_date'])

    APIClient = tap_density.client.Client(args.config)

    runner = APIRunner(
        args, APIClient, tap_density.streams.AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
