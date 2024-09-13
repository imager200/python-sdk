# ConcatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concat_mode** | **str** | Defines whether the result image will be resized to the smaller one or the larger one in case both images have different dimensions. It has not effect if images have the same dimensions. | [optional] [default to 'none']
**direction** | **str** | This parameter defines how the images will be concatenated. horizontal means that the images will concatenated one beside the other from left to right. vertical means that images will be concatenated one on the top of the other | [optional] [default to 'hor']
**image1** | **str** |  | [optional] 
**image2** | **str** |  | [optional] 
**target_format** | **str** |  | [optional] [default to 'jpeg']

## Example

```python
from imager200_python_sdk.models.concat_request import ConcatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConcatRequest from a JSON string
concat_request_instance = ConcatRequest.from_json(json)
# print the JSON string representation of the object
print(ConcatRequest.to_json())

# convert the object into a dict
concat_request_dict = concat_request_instance.to_dict()
# create an instance of ConcatRequest from a dict
concat_request_from_dict = ConcatRequest.from_dict(concat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


