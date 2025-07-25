# ServiceListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**port_id** | **float** | Port ID | 
**ip** | **str** | IP Address | 
**hostname** | **str** | Hostname | 
**port** | **float** | Port number | [optional] 
**type** | **str** | Port Protocol | [optional] 
**country** | **str** | Country code | [optional] 
**banner** | **str** | Banner | [optional] 
**service** | **str** | Service | [optional] 
**source** | **str** | Asset source | [optional] 
**last_seen** | **datetime** | Last seen date Range | 
**technologies** | [**List[Technology]**](Technology.md) | Technology list | 
**service_types** | [**List[ServiceType]**](ServiceType.md) | Service types | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) | Business Units | 
**is_concerning** | **bool** | Whether the discovered network service is concerning | 

## Example

```python
from watchtowr_api_sdk.models.service_listing import ServiceListing

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceListing from a JSON string
service_listing_instance = ServiceListing.from_json(json)
# print the JSON string representation of the object
print(ServiceListing.to_json())

# convert the object into a dict
service_listing_dict = service_listing_instance.to_dict()
# create an instance of ServiceListing from a dict
service_listing_from_dict = ServiceListing.from_dict(service_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


