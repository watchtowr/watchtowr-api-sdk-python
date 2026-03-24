# KillSwitchForbiddenError


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `message`                                                 | *str*                                                     | :heavy_check_mark:                                        | Error message                                             | Administrator or User role required to manage kill switch |
| `error`                                                   | *str*                                                     | :heavy_check_mark:                                        | Error code                                                | KILL_SWITCH_FORBIDDEN                                     |
| `status_code`                                             | *float*                                                   | :heavy_check_mark:                                        | HTTP status code                                          | 403                                                       |