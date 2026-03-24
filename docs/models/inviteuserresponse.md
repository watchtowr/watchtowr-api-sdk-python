# InviteUserResponse


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `success`                                          | *bool*                                             | :heavy_check_mark:                                 | Success status                                     | true                                               |
| `invited_count`                                    | *float*                                            | :heavy_check_mark:                                 | Number of users invited                            | 2                                                  |
| `invited_emails`                                   | List[*str*]                                        | :heavy_check_mark:                                 | List of emails that were invited                   | [<br/>"john.doe@example.com",<br/>"jane.doe@example.com"<br/>] |