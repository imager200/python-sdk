# BlendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpha** | **float** |  | [optional] 
**image1** | **str** |  | 
**image2** | **str** |  | 
**mode** | **str** |  | [optional] [default to 'rts']
**target_format** | **str** |  | [optional] [default to 'jpeg']

## Example

```python
from imager200_python_sdk.models.blend_request import BlendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlendRequest from a JSON string
blend_request_instance = BlendRequest.from_json(json)
# print the JSON string representation of the object
print(BlendRequest.to_json())

# convert the object into a dict
blend_request_dict = blend_request_instance.to_dict()
# create an instance of BlendRequest from a dict
blend_request_from_dict = BlendRequest.from_dict(blend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


