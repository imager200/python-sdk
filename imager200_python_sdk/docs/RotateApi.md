# imager200_python_sdk.RotateApi

All URIs are relative to *https://api.imager200.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rotate_async_get**](RotateApi.md#rotate_async_get) | **GET** /rotate | 
[**rotate_async_post**](RotateApi.md#rotate_async_post) | **POST** /rotate | 
[**rotate_sync_get**](RotateApi.md#rotate_sync_get) | **GET** /rotate/sync | 
[**rotate_sync_post**](RotateApi.md#rotate_sync_post) | **POST** /rotate/sync | 


# **rotate_async_get**
> InfoResponse rotate_async_get(url, angle=angle, background_color=background_color)



![rotate](https://api-docs.imager200.io/images/examples/rotate_example.jpeg)

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
    api_instance = imager200_python_sdk.RotateApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp,gif
    angle = 90 # float | rotation angle in degrees (optional) (default to 90)
    background_color = 'white' # str | the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')

    try:
        api_response = api_instance.rotate_async_get(url, angle=angle, background_color=background_color)
        print("The response of RotateApi->rotate_async_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RotateApi->rotate_async_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp,gif | 
 **angle** | **float**| rotation angle in degrees | [optional] [default to 90]
 **background_color** | **str**| the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]

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

# **rotate_async_post**
> InfoResponse rotate_async_post(body, angle=angle, background_color=background_color)



![rotate](https://api-docs.imager200.io/images/examples/rotate_example.jpeg)

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
    api_instance = imager200_python_sdk.RotateApi(api_client)
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp,gif
    angle = 90 # float | rotation angle in degrees (optional) (default to 90)
    background_color = 'white' # str | the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')

    try:
        api_response = api_instance.rotate_async_post(body, angle=angle, background_color=background_color)
        print("The response of RotateApi->rotate_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RotateApi->rotate_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp,gif | 
 **angle** | **float**| rotation angle in degrees | [optional] [default to 90]
 **background_color** | **str**| the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]

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

# **rotate_sync_get**
> bytearray rotate_sync_get(url, angle=angle, background_color=background_color)



![rotate](https://api-docs.imager200.io/images/examples/rotate_example.jpeg)

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
    api_instance = imager200_python_sdk.RotateApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp,gif
    angle = 90 # float | rotation angle in degrees (optional) (default to 90)
    background_color = 'white' # str | the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')

    try:
        api_response = api_instance.rotate_sync_get(url, angle=angle, background_color=background_color)
        print("The response of RotateApi->rotate_sync_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RotateApi->rotate_sync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp,gif | 
 **angle** | **float**| rotation angle in degrees | [optional] [default to 90]
 **background_color** | **str**| the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]

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

# **rotate_sync_post**
> bytearray rotate_sync_post(body, angle=angle, background_color=background_color)



![rotate](https://api-docs.imager200.io/images/examples/rotate_example.jpeg)

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
    api_instance = imager200_python_sdk.RotateApi(api_client)
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp,gif
    angle = 90 # float | rotation angle in degrees (optional) (default to 90)
    background_color = 'white' # str | the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')

    try:
        api_response = api_instance.rotate_sync_post(body, angle=angle, background_color=background_color)
        print("The response of RotateApi->rotate_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RotateApi->rotate_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp,gif | 
 **angle** | **float**| rotation angle in degrees | [optional] [default to 90]
 **background_color** | **str**| the color that should be used to fill the empty surfaces after rotating the image. Must be a valid color name (supported names are specified [here](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]

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

