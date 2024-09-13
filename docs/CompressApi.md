# imager200_python_sdk.CompressApi

All URIs are relative to *https://api.imager200.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compress_async_get**](CompressApi.md#compress_async_get) | **GET** /compress | 
[**compress_async_post**](CompressApi.md#compress_async_post) | **POST** /compress | 
[**compress_sync_get**](CompressApi.md#compress_sync_get) | **GET** /compress/sync | 
[**compress_sync_post**](CompressApi.md#compress_sync_post) | **POST** /compress/sync | 


# **compress_async_get**
> InfoResponse compress_async_get(url, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)



This endpoint compresses the image according to the parameters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
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
    api_instance = imager200_python_sdk.CompressApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png
    jpeg_quality = 95 # int | defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) (optional) (default to 95)
    png_optimization_level = 3 # int | defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. (optional) (default to 3)
    progressive_jpeg = True # bool | It toggles the generation of a progressive JPEG. A \"false\" value generates a baseline JPEG (optional) (default to True)

    try:
        api_response = api_instance.compress_async_get(url, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)
        print("The response of CompressApi->compress_async_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompressApi->compress_async_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png | 
 **jpeg_quality** | **int**| defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) | [optional] [default to 95]
 **png_optimization_level** | **int**| defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. | [optional] [default to 3]
 **progressive_jpeg** | **bool**| It toggles the generation of a progressive JPEG. A \&quot;false\&quot; value generates a baseline JPEG | [optional] [default to True]

### Return type

[**InfoResponse**](InfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - the temporary url of an image in case a post operation id is not provided <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compress_async_post**
> InfoResponse compress_async_post(body, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)



This endpoint compresses the image according to the parameters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
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
    api_instance = imager200_python_sdk.CompressApi(api_client)
    body = None # bytearray | image binary data, acceptable formats: jpeg,png
    jpeg_quality = 95 # int | defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) (optional) (default to 95)
    png_optimization_level = 3 # int | defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. (optional) (default to 3)
    progressive_jpeg = True # bool | It toggles the generation of a progressive JPEG. A \"false\" value generates a baseline JPEG (optional) (default to True)

    try:
        api_response = api_instance.compress_async_post(body, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)
        print("The response of CompressApi->compress_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompressApi->compress_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png | 
 **jpeg_quality** | **int**| defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) | [optional] [default to 95]
 **png_optimization_level** | **int**| defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. | [optional] [default to 3]
 **progressive_jpeg** | **bool**| It toggles the generation of a progressive JPEG. A \&quot;false\&quot; value generates a baseline JPEG | [optional] [default to True]

### Return type

[**InfoResponse**](InfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - the temporary url of an image in case a post operation id is not provided <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compress_sync_get**
> bytearray compress_sync_get(url, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)



This endpoint compresses the image according to the parameters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
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
    api_instance = imager200_python_sdk.CompressApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png
    jpeg_quality = 95 # int | defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) (optional) (default to 95)
    png_optimization_level = 3 # int | defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. (optional) (default to 3)
    progressive_jpeg = True # bool | It toggles the generation of a progressive JPEG. A \"false\" value generates a baseline JPEG (optional) (default to True)

    try:
        api_response = api_instance.compress_sync_get(url, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)
        print("The response of CompressApi->compress_sync_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompressApi->compress_sync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png | 
 **jpeg_quality** | **int**| defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) | [optional] [default to 95]
 **png_optimization_level** | **int**| defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. | [optional] [default to 3]
 **progressive_jpeg** | **bool**| It toggles the generation of a progressive JPEG. A \&quot;false\&quot; value generates a baseline JPEG | [optional] [default to True]

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response contains the image file |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compress_sync_post**
> bytearray compress_sync_post(body, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)



This endpoint compresses the image according to the parameters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import imager200_python_sdk
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
    api_instance = imager200_python_sdk.CompressApi(api_client)
    body = None # bytearray | image binary data, acceptable formats: jpeg,png
    jpeg_quality = 95 # int | defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) (optional) (default to 95)
    png_optimization_level = 3 # int | defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. (optional) (default to 3)
    progressive_jpeg = True # bool | It toggles the generation of a progressive JPEG. A \"false\" value generates a baseline JPEG (optional) (default to True)

    try:
        api_response = api_instance.compress_sync_post(body, jpeg_quality=jpeg_quality, png_optimization_level=png_optimization_level, progressive_jpeg=progressive_jpeg)
        print("The response of CompressApi->compress_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompressApi->compress_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png | 
 **jpeg_quality** | **int**| defines the jpeg quality level (the higher is the value, the better quality of the image). Only applied if the image is of type jpeg. (uses MozJPEG behind the curtains) | [optional] [default to 95]
 **png_optimization_level** | **int**| defines the png optimization level (higher value means a smaller size and longer compression time). Only applied if image is of type png. | [optional] [default to 3]
 **progressive_jpeg** | **bool**| It toggles the generation of a progressive JPEG. A \&quot;false\&quot; value generates a baseline JPEG | [optional] [default to True]

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response contains the image file |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

