# ServiceInformationCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**subject_common_name** | **str** | Subject Common Name | 
**subject_organisation** | **str** | Subject Organization | 
**subject_alt_names** | **List[str]** | Subject Alt Names | 
**subject_country** | **str** | Subject Country | 
**issuer_common_name** | **str** | Issuer CommonName | 
**issuer_organisation** | **str** | Issuer Organization | 
**issuer_country** | **str** | Issuer Country | 
**fingerprint** | **str** | Fingerprint | 
**serial_number** | **str** | Certificate serial number | 
**public_key_info_alg** | **str** | PublicKeyInfoAlg | 
**public_key_info_size** | **int** | PublicKeyInfoSize | 
**status** | **str** |  | 
**issued_by_status** | **str** | Trust provenance of the certificate issuer as classified upstream | 
**created_at** | **datetime** | Discovery date | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**not_before** | **datetime** | Certificate validity start | 
**not_after** | **datetime** | Certificate expiry | 
**last_seen_at** | **datetime** | Last time the certificate was observed on the linked port | 

## Example

```python
from watchtowr_api_sdk.models.service_information_certificate import ServiceInformationCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInformationCertificate from a JSON string
service_information_certificate_instance = ServiceInformationCertificate.from_json(json)
# print the JSON string representation of the object
print(ServiceInformationCertificate.to_json())

# convert the object into a dict
service_information_certificate_dict = service_information_certificate_instance.to_dict()
# create an instance of ServiceInformationCertificate from a dict
service_information_certificate_from_dict = ServiceInformationCertificate.from_dict(service_information_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


