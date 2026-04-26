# PaginatedAdversaryIntel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdversaryIntel]**](AdversaryIntel.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_adversary_intel import PaginatedAdversaryIntel

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAdversaryIntel from a JSON string
paginated_adversary_intel_instance = PaginatedAdversaryIntel.from_json(json)
# print the JSON string representation of the object
print(PaginatedAdversaryIntel.to_json())

# convert the object into a dict
paginated_adversary_intel_dict = paginated_adversary_intel_instance.to_dict()
# create an instance of PaginatedAdversaryIntel from a dict
paginated_adversary_intel_from_dict = PaginatedAdversaryIntel.from_dict(paginated_adversary_intel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


