# imager200_python_sdk.TextApi

All URIs are relative to *https://api.imager200.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_async_get**](TextApi.md#text_async_get) | **GET** /text | 
[**text_async_post**](TextApi.md#text_async_post) | **POST** /text | 
[**text_sync_get**](TextApi.md#text_sync_get) | **GET** /text/sync | 
[**text_sync_post**](TextApi.md#text_sync_post) | **POST** /text/sync | 


# **text_async_get**
> InfoResponse text_async_get(url, text, color=color, font=font, size=size, x=x, y=y)



![text](https://api-docs.imager200.io/images/examples/text_example.jpeg)

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
    api_instance = imager200_python_sdk.TextApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp,gif
    text = 'text_example' # str | the text to be added.
    color = 'white' # str | defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')
    font = 'calibri' # str | defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) (optional) (default to 'calibri')
    size = 12 # float | the text size in pixels. (optional) (default to 12)
    x = 50 # int | the x coordinate in pixels of the point where the text will be added. (optional) (default to 50)
    y = 50 # int | the y coordinate in pixels of the point where the text will be added. (optional) (default to 50)

    try:
        api_response = api_instance.text_async_get(url, text, color=color, font=font, size=size, x=x, y=y)
        print("The response of TextApi->text_async_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->text_async_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp,gif | 
 **text** | **str**| the text to be added. | 
 **color** | **str**| defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]
 **font** | **str**| defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) | [optional] [default to &#39;calibri&#39;]
 **size** | **float**| the text size in pixels. | [optional] [default to 12]
 **x** | **int**| the x coordinate in pixels of the point where the text will be added. | [optional] [default to 50]
 **y** | **int**| the y coordinate in pixels of the point where the text will be added. | [optional] [default to 50]

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

# **text_async_post**
> InfoResponse text_async_post(text, body, color=color, font=font, size=size, x=x, y=y)



![text](https://api-docs.imager200.io/images/examples/text_example.jpeg)

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
    api_instance = imager200_python_sdk.TextApi(api_client)
    text = 'text_example' # str | the text to be added.
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp,gif
    color = 'white' # str | defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')
    font = 'calibri' # str | defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) (optional) (default to 'calibri')
    size = 12 # float | the text size in pixels. (optional) (default to 12)
    x = 50 # int | the x coordinate in pixels of the point where the text will be added. (optional) (default to 50)
    y = 50 # int | the y coordinate in pixels of the point where the text will be added. (optional) (default to 50)

    try:
        api_response = api_instance.text_async_post(text, body, color=color, font=font, size=size, x=x, y=y)
        print("The response of TextApi->text_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->text_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| the text to be added. | 
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp,gif | 
 **color** | **str**| defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]
 **font** | **str**| defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) | [optional] [default to &#39;calibri&#39;]
 **size** | **float**| the text size in pixels. | [optional] [default to 12]
 **x** | **int**| the x coordinate in pixels of the point where the text will be added. | [optional] [default to 50]
 **y** | **int**| the y coordinate in pixels of the point where the text will be added. | [optional] [default to 50]

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

# **text_sync_get**
> bytearray text_sync_get(url, text, color=color, font=font, size=size, x=x, y=y)



![text](https://api-docs.imager200.io/images/examples/text_example.jpeg)

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
    api_instance = imager200_python_sdk.TextApi(api_client)
    url = 'url_example' # str | image url, supported formats jpeg,png,bmp,gif
    text = 'text_example' # str | the text to be added.
    color = 'white' # str | defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')
    font = 'calibri' # str | defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) (optional) (default to 'calibri')
    size = 12 # float | the text size in pixels. (optional) (default to 12)
    x = 50 # int | the x coordinate in pixels of the point where the text will be added. (optional) (default to 50)
    y = 50 # int | the y coordinate in pixels of the point where the text will be added. (optional) (default to 50)

    try:
        api_response = api_instance.text_sync_get(url, text, color=color, font=font, size=size, x=x, y=y)
        print("The response of TextApi->text_sync_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->text_sync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| image url, supported formats jpeg,png,bmp,gif | 
 **text** | **str**| the text to be added. | 
 **color** | **str**| defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]
 **font** | **str**| defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) | [optional] [default to &#39;calibri&#39;]
 **size** | **float**| the text size in pixels. | [optional] [default to 12]
 **x** | **int**| the x coordinate in pixels of the point where the text will be added. | [optional] [default to 50]
 **y** | **int**| the y coordinate in pixels of the point where the text will be added. | [optional] [default to 50]

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

# **text_sync_post**
> bytearray text_sync_post(text, body, color=color, font=font, size=size, x=x, y=y)



![text](https://api-docs.imager200.io/images/examples/text_example.jpeg)

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
    api_instance = imager200_python_sdk.TextApi(api_client)
    text = 'text_example' # str | the text to be added.
    body = None # bytearray | image binary data, acceptable formats: jpeg,png,bmp,gif
    color = 'white' # str | defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. (optional) (default to 'white')
    font = 'calibri' # str | defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) (optional) (default to 'calibri')
    size = 12 # float | the text size in pixels. (optional) (default to 12)
    x = 50 # int | the x coordinate in pixels of the point where the text will be added. (optional) (default to 50)
    y = 50 # int | the y coordinate in pixels of the point where the text will be added. (optional) (default to 50)

    try:
        api_response = api_instance.text_sync_post(text, body, color=color, font=font, size=size, x=x, y=y)
        print("The response of TextApi->text_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->text_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| the text to be added. | 
 **body** | **bytearray**| image binary data, acceptable formats: jpeg,png,bmp,gif | 
 **color** | **str**| defines the color of the text. Must be a valid color name (supported names are specified here  [https://www.w3schools.com/colors/colors_names.asp](https://www.w3schools.com/colors/colors_names.asp)) or hexadecimal code. | [optional] [default to &#39;white&#39;]
 **font** | **str**| defines the font type name. Possible values can be found [here](https://api-docs.imager200.io/fonts_example/). (More fonts can be added on request) | [optional] [default to &#39;calibri&#39;]
 **size** | **float**| the text size in pixels. | [optional] [default to 12]
 **x** | **int**| the x coordinate in pixels of the point where the text will be added. | [optional] [default to 50]
 **y** | **int**| the y coordinate in pixels of the point where the text will be added. | [optional] [default to 50]

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

