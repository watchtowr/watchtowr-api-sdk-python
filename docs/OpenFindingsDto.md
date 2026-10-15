# OpenFindingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **int** | Count of critical findings | 
**high** | **int** | Count of high severity findings | 
**medium** | **int** | Count of medium severity findings | 
**low** | **int** | Count of low severity findings | 
**info** | **int** | Count of informational findings | 
**total** | **int** | Total count of all open findings | 

## Example

```python
from watchtowr_api_sdk.models.open_findings_dto import OpenFindingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenFindingsDto from a JSON string
open_findings_dto_instance = OpenFindingsDto.from_json(json)
# print the JSON string representation of the object
print(OpenFindingsDto.to_json())

# convert the object into a dict
open_findings_dto_dict = open_findings_dto_instance.to_dict()
# create an instance of OpenFindingsDto from a dict
open_findings_dto_from_dict = OpenFindingsDto.from_dict(open_findings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


