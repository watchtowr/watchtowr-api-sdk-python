# SecurityPostureDashboardDto


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `required_actions`                                                           | [models.RequiredActionsDto](../models/requiredactionsdto.md)                 | :heavy_check_mark:                                                           | Top priority items requiring immediate attention                             |
| `hunt_overview`                                                              | [models.HuntOverviewDto](../models/huntoverviewdto.md)                       | :heavy_check_mark:                                                           | Hunt-related metrics and status                                              |
| `attack_surface_resiliency`                                                  | [models.AttackSurfaceResiliencyDto](../models/attacksurfaceresiliencydto.md) | :heavy_check_mark:                                                           | Long-term security resilience metrics                                        |
| `organization_summary`                                                       | [models.OrganizationSummaryDto](../models/organizationsummarydto.md)         | :heavy_check_mark:                                                           | Overall organization metrics and summary                                     |