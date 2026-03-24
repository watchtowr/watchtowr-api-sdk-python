# HostnameBusinessUnitIDsDTO


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `business_unit_ids`                               | List[*str*]                                       | :heavy_check_mark:                                | List of business unit IDs to assign the asset to. | [<br/>1,<br/>2,<br/>3<br/>]                       |
| `cascade_subdomain`                               | *bool*                                            | :heavy_check_mark:                                | Cascade business units to domain's subdomains     |                                                   |
| `cascade_ip`                                      | *bool*                                            | :heavy_check_mark:                                | Cascade business units to domain's ipaddresses    |                                                   |