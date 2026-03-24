# Values

Values object for ipRange asset type. Must contain both cidr and asn fields. Required when type is ipRange.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `cidr`                                     | *str*                                      | :heavy_check_mark:                         | CIDR for IP Range (e.g., "192.168.1.0/24") | 192.168.1.0/24                             |
| `asn`                                      | *str*                                      | :heavy_check_mark:                         | ASN for IP Range (e.g., "AS16509")         | AS16509                                    |