# UpdateOrganisationWhitelistIPDto


## Fields

| Field                                 | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `id`                                  | *float*                               | :heavy_check_mark:                    | IP address ID                         | 1                                     |
| `ip`                                  | *str*                                 | :heavy_check_mark:                    | IP address or CIDR range to whitelist | 192.168.1.1                           |
| `description`                         | *OptionalNullable[str]*               | :heavy_minus_sign:                    | Description of the IP address         | Office network                        |