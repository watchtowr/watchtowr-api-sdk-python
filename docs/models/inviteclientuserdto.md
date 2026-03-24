# InviteClientUserDto


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `email`                                                  | *str*                                                    | :heavy_check_mark:                                       | Email address of the user to invite                      | john.doe@example.com                                     |
| `role_type`                                              | [models.RoleType](../models/roletype.md)                 | :heavy_check_mark:                                       | Role type for the user                                   | USER                                                     |
| `business_unit_ids`                                      | List[*float*]                                            | :heavy_minus_sign:                                       | Business Unit IDs to assign (required for BU_USER roles) | [<br/>1,<br/>2<br/>]                                     |