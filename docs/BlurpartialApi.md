# imager200_python_sdk.BlurpartialApi

All URIs are relative to *https://api.imager200.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blurpartial_async_get**](BlurpartialApi.md#blurpartial_async_get) | **GET** /blurpartial | 
[**blurpartial_async_post**](BlurpartialApi.md#blurpartial_async_post) | **POST** /blurpartial | 
[**blurpartial_sync_get**](BlurpartialApi.md#blurpartial_sync_get) | **GET** /blurpartial/sync | 
[**blurpartial_sync_post**](BlurpartialApi.md#blurpartial_sync_post) | **POST** /blurpartial/sync | 


# **blurpartial_async_get**
> InfoResponse blurpartial_async_get(url, x0, x1, y0, y1, sigma=sigma)



 Blurs a fraction of the image defined by the rectangle (x0, y0, x1, y1)  ![blur_partial](https://api-docs.imager200.io/images/examples/blur_partial_example.jpeg)

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
    api_instance = imager200_python_sdk.BlurpartialApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp
    x0 = 56 # int | defines the x coordinate of the first point of the rectangle to blur
    x1 = 56 # int | defines the x coordinate of the second point of the rectangle to blur
    y0 = 56 # int | defines the y coordinate of the first point of the rectangle to blur
    y1 = 56 # int | defines the y coordinate of the second point of the rectangle to blur.
    sigma = 10 # float | controls the strength of the blur (optional) (default to 10)

    try:
        api_response = api_instance.blurpartial_async_get(url, x0, x1, y0, y1, sigma=sigma)
        print("The response of BlurpartialApi->blurpartial_async_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlurpartialApi->blurpartial_async_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp | 
 **x0** | **int**| defines the x coordinate of the first point of the rectangle to blur | 
 **x1** | **int**| defines the x coordinate of the second point of the rectangle to blur | 
 **y0** | **int**| defines the y coordinate of the first point of the rectangle to blur | 
 **y1** | **int**| defines the y coordinate of the second point of the rectangle to blur. | 
 **sigma** | **float**| controls the strength of the blur | [optional] [default to 10]

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

# **blurpartial_async_post**
> InfoResponse blurpartial_async_post(x0, x1, y0, y1, body, sigma=sigma)



 Blurs a fraction of the image defined by the rectangle (x0, y0, x1, y1)  ![blur_partial](https://api-docs.imager200.io/images/examples/blur_partial_example.jpeg)

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
    api_instance = imager200_python_sdk.BlurpartialApi(api_client)
    x0 = 56 # int | defines the x coordinate of the first point of the rectangle to blur
    x1 = 56 # int | defines the x coordinate of the second point of the rectangle to blur
    y0 = 56 # int | defines the y coordinate of the first point of the rectangle to blur
    y1 = 56 # int | defines the y coordinate of the second point of the rectangle to blur.
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp
    sigma = 10 # float | controls the strength of the blur (optional) (default to 10)

    try:
        api_response = api_instance.blurpartial_async_post(x0, x1, y0, y1, body, sigma=sigma)
        print("The response of BlurpartialApi->blurpartial_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlurpartialApi->blurpartial_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x0** | **int**| defines the x coordinate of the first point of the rectangle to blur | 
 **x1** | **int**| defines the x coordinate of the second point of the rectangle to blur | 
 **y0** | **int**| defines the y coordinate of the first point of the rectangle to blur | 
 **y1** | **int**| defines the y coordinate of the second point of the rectangle to blur. | 
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp | 
 **sigma** | **float**| controls the strength of the blur | [optional] [default to 10]

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

# **blurpartial_sync_get**
> bytearray blurpartial_sync_get(url, x0, x1, y0, y1, sigma=sigma)



 Blurs a fraction of the image defined by the rectangle (x0, y0, x1, y1)  ![blur_partial](https://api-docs.imager200.io/images/examples/blur_partial_example.jpeg)

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
    api_instance = imager200_python_sdk.BlurpartialApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp
    x0 = 56 # int | defines the x coordinate of the first point of the rectangle to blur
    x1 = 56 # int | defines the x coordinate of the second point of the rectangle to blur
    y0 = 56 # int | defines the y coordinate of the first point of the rectangle to blur
    y1 = 56 # int | defines the y coordinate of the second point of the rectangle to blur.
    sigma = 10 # float | controls the strength of the blur (optional) (default to 10)

    try:
        api_response = api_instance.blurpartial_sync_get(url, x0, x1, y0, y1, sigma=sigma)
        print("The response of BlurpartialApi->blurpartial_sync_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlurpartialApi->blurpartial_sync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp | 
 **x0** | **int**| defines the x coordinate of the first point of the rectangle to blur | 
 **x1** | **int**| defines the x coordinate of the second point of the rectangle to blur | 
 **y0** | **int**| defines the y coordinate of the first point of the rectangle to blur | 
 **y1** | **int**| defines the y coordinate of the second point of the rectangle to blur. | 
 **sigma** | **float**| controls the strength of the blur | [optional] [default to 10]

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/bmp, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response contains the image file |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blurpartial_sync_post**
> bytearray blurpartial_sync_post(x0, x1, y0, y1, body, sigma=sigma)



 Blurs a fraction of the image defined by the rectangle (x0, y0, x1, y1)  ![blur_partial](https://api-docs.imager200.io/images/examples/blur_partial_example.jpeg)

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
    api_instance = imager200_python_sdk.BlurpartialApi(api_client)
    x0 = 56 # int | defines the x coordinate of the first point of the rectangle to blur
    x1 = 56 # int | defines the x coordinate of the second point of the rectangle to blur
    y0 = 56 # int | defines the y coordinate of the first point of the rectangle to blur
    y1 = 56 # int | defines the y coordinate of the second point of the rectangle to blur.
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp
    sigma = 10 # float | controls the strength of the blur (optional) (default to 10)

    try:
        api_response = api_instance.blurpartial_sync_post(x0, x1, y0, y1, body, sigma=sigma)
        print("The response of BlurpartialApi->blurpartial_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlurpartialApi->blurpartial_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x0** | **int**| defines the x coordinate of the first point of the rectangle to blur | 
 **x1** | **int**| defines the x coordinate of the second point of the rectangle to blur | 
 **y0** | **int**| defines the y coordinate of the first point of the rectangle to blur | 
 **y1** | **int**| defines the y coordinate of the second point of the rectangle to blur. | 
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp | 
 **sigma** | **float**| controls the strength of the blur | [optional] [default to 10]

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: image/bmp, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response contains the image file |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

