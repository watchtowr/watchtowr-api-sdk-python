# OrganizationSummaryDto


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `attack_surface`                                             | [models.AttackSurfaceDto](../models/attacksurfacedto.md)     | :heavy_check_mark:                                           | Attack surface metrics                                       |
| `open_findings`                                              | [models.OpenFindingsDto](../models/openfindingsdto.md)       | :heavy_check_mark:                                           | Breakdown of findings by severity level                      |
| `mttr_metrics`                                               | [models.MttrMetricsDto](../models/mttrmetricsdto.md)         | :heavy_check_mark:                                           | Mean Time To Remediation metrics                             |
| `findings_summary`                                           | [models.FindingsSummaryDto](../models/findingssummarydto.md) | :heavy_check_mark:                                           | Historical and categorized finding metrics                   |