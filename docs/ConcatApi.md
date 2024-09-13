# imager200_python_sdk.ConcatApi

All URIs are relative to *https://api.imager200.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**concat_async_post**](ConcatApi.md#concat_async_post) | **POST** /concat | 
[**concat_sync_post**](ConcatApi.md#concat_sync_post) | **POST** /concat/sync | 


# **concat_async_post**
> InfoResponse concat_async_post(payload)



__image 2__:   ![concat](https://api-docs.imager200.io/images/examples/concat_candidate.png)  __result__:  ![concat_result](https://api-docs.imager200.io/images/examples/concat_example.jpeg)  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
from imager200_python_sdk.models.concat_request import ConcatRequest
from imager200_python_sdk.models.info_response import InfoResponse
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
    api_instance = imager200_python_sdk.ConcatApi(api_client)
    payload = imager200_python_sdk.ConcatRequest() # ConcatRequest | request

    try:
        api_response = api_instance.concat_async_post(payload)
        print("The response of ConcatApi->concat_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConcatApi->concat_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ConcatRequest**](ConcatRequest.md)| request | 

### Return type

[**InfoResponse**](InfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - the temporary url of an image in case a post operation id is not provided <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **concat_sync_post**
> bytearray concat_sync_post(payload)



__image 2__:   ![concat](https://api-docs.imager200.io/images/examples/concat_candidate.png)  __result__:  ![concat_result](https://api-docs.imager200.io/images/examples/concat_example.jpeg)  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
from imager200_python_sdk.models.concat_request import ConcatRequest
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
    api_instance = imager200_python_sdk.ConcatApi(api_client)
    payload = imager200_python_sdk.ConcatRequest() # ConcatRequest | request

    try:
        api_response = api_instance.concat_sync_post(payload)
        print("The response of ConcatApi->concat_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConcatApi->concat_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ConcatRequest**](ConcatRequest.md)| request | 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/bmp, image/gif, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response contains the image file |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

