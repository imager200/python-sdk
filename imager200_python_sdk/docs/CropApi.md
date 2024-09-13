# imager200_python_sdk.CropApi

All URIs are relative to *https://api.imager200.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crop_async_get**](CropApi.md#crop_async_get) | **GET** /crop | 
[**crop_async_post**](CropApi.md#crop_async_post) | **POST** /crop | 
[**crop_sync_get**](CropApi.md#crop_sync_get) | **GET** /crop/sync | 
[**crop_sync_post**](CropApi.md#crop_sync_post) | **POST** /crop/sync | 


# **crop_async_get**
> InfoResponse crop_async_get(url, x0, x1, y0, y1)



  ![crop](https://api-docs.imager200.io/images/examples/crop_example.jpeg)

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
    api_instance = imager200_python_sdk.CropApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp,gif
    x0 = 56 # int | the x coordinate of the first point of the rectangle to crop.
    x1 = 56 # int | the x coordinate of the second point of the rectangle to crop.
    y0 = 56 # int | the y coordinate of the first point of the rectangle to crop.
    y1 = 56 # int | the y coordinate of the second point of the rectangle to crop.

    try:
        api_response = api_instance.crop_async_get(url, x0, x1, y0, y1)
        print("The response of CropApi->crop_async_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CropApi->crop_async_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp,gif | 
 **x0** | **int**| the x coordinate of the first point of the rectangle to crop. | 
 **x1** | **int**| the x coordinate of the second point of the rectangle to crop. | 
 **y0** | **int**| the y coordinate of the first point of the rectangle to crop. | 
 **y1** | **int**| the y coordinate of the second point of the rectangle to crop. | 

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

# **crop_async_post**
> InfoResponse crop_async_post(x0, x1, y0, y1, body)



  ![crop](https://api-docs.imager200.io/images/examples/crop_example.jpeg)

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
    api_instance = imager200_python_sdk.CropApi(api_client)
    x0 = 56 # int | the x coordinate of the first point of the rectangle to crop.
    x1 = 56 # int | the x coordinate of the second point of the rectangle to crop.
    y0 = 56 # int | the y coordinate of the first point of the rectangle to crop.
    y1 = 56 # int | the y coordinate of the second point of the rectangle to crop.
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp,gif

    try:
        api_response = api_instance.crop_async_post(x0, x1, y0, y1, body)
        print("The response of CropApi->crop_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CropApi->crop_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x0** | **int**| the x coordinate of the first point of the rectangle to crop. | 
 **x1** | **int**| the x coordinate of the second point of the rectangle to crop. | 
 **y0** | **int**| the y coordinate of the first point of the rectangle to crop. | 
 **y1** | **int**| the y coordinate of the second point of the rectangle to crop. | 
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp,gif | 

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

# **crop_sync_get**
> bytearray crop_sync_get(url, x0, x1, y0, y1)



  ![crop](https://api-docs.imager200.io/images/examples/crop_example.jpeg)

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
    api_instance = imager200_python_sdk.CropApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp,gif
    x0 = 56 # int | the x coordinate of the first point of the rectangle to crop.
    x1 = 56 # int | the x coordinate of the second point of the rectangle to crop.
    y0 = 56 # int | the y coordinate of the first point of the rectangle to crop.
    y1 = 56 # int | the y coordinate of the second point of the rectangle to crop.

    try:
        api_response = api_instance.crop_sync_get(url, x0, x1, y0, y1)
        print("The response of CropApi->crop_sync_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CropApi->crop_sync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp,gif | 
 **x0** | **int**| the x coordinate of the first point of the rectangle to crop. | 
 **x1** | **int**| the x coordinate of the second point of the rectangle to crop. | 
 **y0** | **int**| the y coordinate of the first point of the rectangle to crop. | 
 **y1** | **int**| the y coordinate of the second point of the rectangle to crop. | 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/bmp, image/gif, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response contains the image file |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crop_sync_post**
> bytearray crop_sync_post(x0, x1, y0, y1, body)



  ![crop](https://api-docs.imager200.io/images/examples/crop_example.jpeg)

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
    api_instance = imager200_python_sdk.CropApi(api_client)
    x0 = 56 # int | the x coordinate of the first point of the rectangle to crop.
    x1 = 56 # int | the x coordinate of the second point of the rectangle to crop.
    y0 = 56 # int | the y coordinate of the first point of the rectangle to crop.
    y1 = 56 # int | the y coordinate of the second point of the rectangle to crop.
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp,gif

    try:
        api_response = api_instance.crop_sync_post(x0, x1, y0, y1, body)
        print("The response of CropApi->crop_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CropApi->crop_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x0** | **int**| the x coordinate of the first point of the rectangle to crop. | 
 **x1** | **int**| the x coordinate of the second point of the rectangle to crop. | 
 **y0** | **int**| the y coordinate of the first point of the rectangle to crop. | 
 **y1** | **int**| the y coordinate of the second point of the rectangle to crop. | 
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp,gif | 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: image/bmp, image/gif, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response contains the image file |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

