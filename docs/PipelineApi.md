# imager200_python_sdk.PipelineApi

All URIs are relative to *https://api.imager200.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_get**](PipelineApi.md#pipeline_get) | **GET** /pipeline/{name} | 
[**pipeline_get_status**](PipelineApi.md#pipeline_get_status) | **GET** /pipeline/{execution_id}/status | 
[**pipeline_post**](PipelineApi.md#pipeline_post) | **POST** /pipeline/{name} | 


# **pipeline_get**
> SuccessResponse pipeline_get(url, name)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
from imager200_python_sdk.models.success_response import SuccessResponse
from imager200_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.imager200.io
# See configuration.py for a list of all supported configuration parameters.
configuration = imager200_python_sdk.Configuration(
    host = "https://api.imager200.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with imager200_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = imager200_python_sdk.PipelineApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp
    name = 'name_example' # str | the name of the pipeline

    try:
        api_response = api_instance.pipeline_get(url, name)
        print("The response of PipelineApi->pipeline_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->pipeline_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp | 
 **name** | **str**| the name of the pipeline | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pipeline will be applied to the image based on the stored configuration. The result will be stored according to the post operation configured in the pipeline |  -  |
**400** | invalid pipeline definition (pipeline is new and not yet configured) |  -  |
**404** | pipeline does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_get_status**
> PipelineExecutionResult pipeline_get_status(execution_id)



returns the current status of a pipeline

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
from imager200_python_sdk.models.pipeline_execution_result import PipelineExecutionResult
from imager200_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.imager200.io
# See configuration.py for a list of all supported configuration parameters.
configuration = imager200_python_sdk.Configuration(
    host = "https://api.imager200.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with imager200_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = imager200_python_sdk.PipelineApi(api_client)
    execution_id = 'execution_id_example' # str | the execution id obtained from the pipeline creation response

    try:
        api_response = api_instance.pipeline_get_status(execution_id)
        print("The response of PipelineApi->pipeline_get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->pipeline_get_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| the execution id obtained from the pipeline creation response | 

### Return type

[**PipelineExecutionResult**](PipelineExecutionResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_post**
> SuccessResponse pipeline_post(name, body)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
from imager200_python_sdk.models.success_response import SuccessResponse
from imager200_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.imager200.io
# See configuration.py for a list of all supported configuration parameters.
configuration = imager200_python_sdk.Configuration(
    host = "https://api.imager200.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with imager200_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = imager200_python_sdk.PipelineApi(api_client)
    name = 'name_example' # str | the name of the pipeline
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp,gif (depending on operations)

    try:
        api_response = api_instance.pipeline_post(name, body)
        print("The response of PipelineApi->pipeline_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->pipeline_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the name of the pipeline | 
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp,gif (depending on operations) | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pipeline will be applied to the image based on the stored configuration. The result will be stored according to the post operation configured in the pipeline |  -  |
**400** | invalid pipeline definition (pipeline is new and not yet configured) |  -  |
**404** | pipeline does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

