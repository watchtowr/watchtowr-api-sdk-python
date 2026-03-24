# UnassignDomainFromBusinessUnitsRequest


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *float*                                                               | :heavy_check_mark:                                                    | The Domain asset's ID.                                                |
| `business_unit_ids`                                                   | List[*str*]                                                           | :heavy_check_mark:                                                    | List of comma-seperated business unit IDs to unassign from the asset. |
| `cascade_subdomain`                                                   | *str*                                                                 | :heavy_check_mark:                                                    | Cascade business units to domain's subdomains                         |
| `cascade_ip`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | Cascade business units to domain's ipaddresses                        |