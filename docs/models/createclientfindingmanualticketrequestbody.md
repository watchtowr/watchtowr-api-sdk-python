# CreateClientFindingManualTicketRequestBody


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `board_name`                                    | *str*                                           | :heavy_check_mark:                              | Name of the external board or ticketing system. | Acme Jira Board                                 |
| `issue_link`                                    | *str*                                           | :heavy_check_mark:                              | URL of the manually created ticket.             | https://example.atlassian.net/browse/ABC-123    |