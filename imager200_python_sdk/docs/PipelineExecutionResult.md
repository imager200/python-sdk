# PipelineExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**failure_step** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size_in_megabytes** | **float** |  | [optional] 
**status** | [**PipelineStatus**](PipelineStatus.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from imager200_python_sdk.models.pipeline_execution_result import PipelineExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineExecutionResult from a JSON string
pipeline_execution_result_instance = PipelineExecutionResult.from_json(json)
# print the JSON string representation of the object
print(PipelineExecutionResult.to_json())

# convert the object into a dict
pipeline_execution_result_dict = pipeline_execution_result_instance.to_dict()
# create an instance of PipelineExecutionResult from a dict
pipeline_execution_result_from_dict = PipelineExecutionResult.from_dict(pipeline_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


