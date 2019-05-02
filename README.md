# tap-density

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from the [Density.io API](https://docs.density.io/v2/)
- Extracts the following resources:
  - [Doorways](https://docs.density.io/v2/#doorways-list)
  - [Links](https://docs.density.io/v2/#links-list)
  - [Spaces](https://docs.density.io/v2/#counts_and_events-list_spaces)
  - [Space Events](https://docs.density.io/v2/#counts_and_events-space_events)
  - [Space Counts](https://docs.density.io/v2/#counts_and_events-space_counts)
  - [Time Segments](https://docs.density.io/v2/#time_segments-list)
  - [Time Segment Groups](https://docs.density.io/v2/#time_segment_groups-list)
- Outputs the schema for each resource
- Loops through existing spaces and incrementally pulls data based on the input state for the **Space Events** and **Space Counts** endpoints, as these are the only endpoints that support date filtering at the time of writing

## Quick Start

1. Install

    ```bash
    pip install tap-density
    ```

2. Create the config file

   Create a JSON file called `config.json`. Its contents should look like:

   ```json
    {
        "start_date": "2019-03-01T00:00:00.000Z",
        "api_key": "<Density.io API Key>",
        "site": "<Density.io Site>"
    }
    ```

   The `start_date` specifies the date at which the tap will begin pulling data
   (for those resources that support this).

   The `api_key` is the API key for your Density.io site.

   The `site` parameter represents the name of your specific Density.io site (e.g. `{site}/spaces/`)

4. Run the Tap in Discovery Mode

    ```bash
    tap-density --config config.json --discover
    ```

   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode

    tap-density --config config.json --catalog catalog.json

---

Copyright &copy; 2019 Stitch
