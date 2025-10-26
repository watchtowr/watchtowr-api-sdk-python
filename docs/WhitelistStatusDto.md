# WhitelistStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable whitelisting | 

## Example

```python
from watchtowr_api_sdk.models.whitelist_status_dto import WhitelistStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistStatusDto from a JSON string
whitelist_status_dto_instance = WhitelistStatusDto.from_json(json)
# print the JSON string representation of the object
print(WhitelistStatusDto.to_json())

# convert the object into a dict
whitelist_status_dto_dict = whitelist_status_dto_instance.to_dict()
# create an instance of WhitelistStatusDto from a dict
whitelist_status_dto_from_dict = WhitelistStatusDto.from_dict(whitelist_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


