# ImageMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_color** | **str** |  | [optional] 
**border_color** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**colorspace** | **str** |  | [optional] 
**compose** | **str** |  | [optional] 
**compression** | **str** |  | [optional] 
**depth_in_bits** | **float** |  | [optional] 
**dispose** | **str** |  | [optional] 
**endianness** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**gamma** | **float** |  | [optional] 
**geometry** | **str** |  | [optional] 
**intensity** | **str** |  | [optional] 
**interlace** | **str** |  | [optional] 
**iterations** | **float** |  | [optional] 
**matte_color** | **str** |  | [optional] 
**number_of_pixels** | **float** |  | [optional] 
**orientation** | **str** |  | [optional] 
**page_geometry** | **str** |  | [optional] 
**rendering_intent** | **str** |  | [optional] 
**size_in_bytes** | **float** |  | [optional] 
**tainted** | **str** |  | [optional] 
**transparent_color** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**units** | **str** |  | [optional] 

## Example

```python
from imager200_python_sdk.models.image_metadata import ImageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ImageMetadata from a JSON string
image_metadata_instance = ImageMetadata.from_json(json)
# print the JSON string representation of the object
print(ImageMetadata.to_json())

# convert the object into a dict
image_metadata_dict = image_metadata_instance.to_dict()
# create an instance of ImageMetadata from a dict
image_metadata_from_dict = ImageMetadata.from_dict(image_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


