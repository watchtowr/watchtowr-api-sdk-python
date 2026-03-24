# ClientBusinessUnitDetail


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `id`                                             | *float*                                          | :heavy_check_mark:                               | ID                                               | 1                                                |
| `name`                                           | *str*                                            | :heavy_check_mark:                               | Name                                             | Singapore Business Unit                          |
| `description`                                    | *str*                                            | :heavy_check_mark:                               | Description                                      | Singapore based assets                           |
| `type`                                           | *str*                                            | :heavy_check_mark:                               | Business unit type                               | DEPARTMENT                                       |
| `parent_id`                                      | *Optional[float]*                                | :heavy_minus_sign:                               | Parent business unit ID                          | 1                                                |
| `user_ids`                                       | List[*float*]                                    | :heavy_minus_sign:                               | Array of user IDs assigned to this business unit | [<br/>1,<br/>2,<br/>3<br/>]                      |
| `created_at`                                     | [models.CreatedAt](../models/createdat.md)       | :heavy_check_mark:                               | Created At                                       | 2022-02-13T02:10:00.000000Z                      |
| `updated_at`                                     | [models.UpdatedAt](../models/updatedat.md)       | :heavy_check_mark:                               | Updated At                                       | 2022-02-13T02:10:00.000000Z                      |