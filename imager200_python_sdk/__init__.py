# coding: utf-8

# flake8: noqa

"""
    imager200 API

      Welcome to imager200! the API for image processing and image workflow automation.        You can find detailed specification of each endpoint and usage examples.      All endpoints  have synchronous (`/{endpoint}/sync`) and asynchronous (`/{endpoint}`) versions. Synchronous endpoints returns the result image in the body of the response (and thus the response is suspended until the processing is finished). The asynchronous endpoint returns immediately and processes the image asap. The image is stored according to the provided `post operation` configuration or stored in our temporary storage where the `Location` header specifies the exact location. More details on post operations can be found on the getting started [guides](/getting-started)    Most endpoints (except `/blend`, `/concat`) allow to send the image either in the body of the request (POST endpoints) or send only the url of the image (GET endpoints) to be downloaded and processed by the API.     Therefore there are 4 possibilities for most endpoints `GET /{endpoint}?url={imageUrl}`, `GET /{endpoint}/sync?url={imageUrl}`, `POST /{endpoint}/sync`, `POST /{endpoint}`    If you find some outdated or inacurate information. Please let us know anytime at [contact@imager200.io](mailto:contact@imager200.io)  ## Authentication:  All API requests need to have an `X-Imager-Key` header with your provided API key as a value otherwise 401 will be returned.   Your API key can be obtained from the [control panel](https://panel.imager200.io) once you sign up. More details can be found on the getting started [guides](/getting-started).  It's possible to test the API without registration using the guest API key, which can be found above the Authorize section below. Note that the guest API key expires every 10 mins and is only used for testing purposes. For a permanent API key, a sign up is needed.    ## Common headers:  | Name | Description | | ---- | ----------- | | X-Imager-Key | Contains the API key. should be part of every request  | | X-PostOp-Id | Optional. Only used in async endpoints. It contains the post operation id that should be applied after processing the image | | X-Upload-File-Name  | Optional. Can be used to give the stored image a name instead of a random / the configured one. The value in this header takes precedence over the file naming convention configured in the post operation. **The value should contain the file name only without extension.**  | | X-Imgur-Title  | **Available in case an imgur post operation is used.** Optional header to set the image title in imgur. The value in the header takes precedence over the stored configuration. | | X-Imgur-Description  | **Available in case an imgur post operation is used.** Optional header to set the image description in imgur. The value in the header takes precedence over the stored configuration. | | X-GPhoto-Description  | **Available in case a google photo post operation is used.** Optional header to set the image description in google photo. |  ## Common Responses:  | Status | Description | | ------ | ----------- | | 402 | indicates that something is wrong with your subscription: either your subscription payment is past due or you have exceeded the maximum allowed requests by your plan.  | | 503 | error that indicates an unreachable service (usually the authentication server) | | 401 | indicates that your API key is wrong or missing | | 400 | validation error specific to the endpoint parameters. Can also indicate that the `X-PostOp-Id` value is not found or the image format is not valid or unsupported | | 201 | returned by async endpoints to indicate that requests has been received and being processed. It does not necessarily mean the success of the operation.  | | 200 | returned by sync endpoints. Means that the request has succeeded and the result is in the response body. |  ## Mime types:  When submitting an image to an endpoint, the content type can be of type `application/octet-stream` or `image/*`.  ## Post Operations:  Because many post operations require the OAuth flow for obtaining the access token to the storage provider API, the creation of post operations can only be done manually through the [control panel](https://panel.imager200.io).  The current integrations are available:  * Dropbox  * Google Drive  * Google Photos  * Google Cloud storage (suspended temporarily because of Google verification)  * AWS S3  * SCP (secure copy)  * Microsoft OneDrive  * Microsoft Azure Storage  * imgur  * http (send the image to a defined http address)  The getting started [guides](/getting-started) contains detailed usage examples and video demos for each post operation.   ## Pipelines:  pipelines can be invoked throught the API, but can only be created through the [control panel](https://panel.imager200.io). The getting started [guides](/getting-started) describes the pipelines inner workings in details.   ## Limits  For security measures and for avoiding server overload, endpoints have the following limits:  - Max image width: 4096 pixels - Max image height: 4096 pixels - Max image size: 20MB - Requests per second: 15 - Max connections from one host: 10  If you need an increase in the limits, please let us know by creating a ticket from the control panel.  ## Reference image:  This image will be used in all the examples for the endpoints below.   ![reference_image](https://api-docs.imager200.io/images/examples/jpeg_image.jpg)  

    The version of the OpenAPI document: 1.0
    Contact: contact@imager200.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from imager200_python_sdk.api.blend_api import BlendApi
from imager200_python_sdk.api.blur_api import BlurApi
from imager200_python_sdk.api.blurhash_api import BlurhashApi
from imager200_python_sdk.api.blurpartial_api import BlurpartialApi
from imager200_python_sdk.api.brightness_api import BrightnessApi
from imager200_python_sdk.api.compress_api import CompressApi
from imager200_python_sdk.api.concat_api import ConcatApi
from imager200_python_sdk.api.contrast_api import ContrastApi
from imager200_python_sdk.api.convert_api import ConvertApi
from imager200_python_sdk.api.crop_api import CropApi
from imager200_python_sdk.api.equalize_api import EqualizeApi
from imager200_python_sdk.api.grayscale_api import GrayscaleApi
from imager200_python_sdk.api.imageinfo_api import ImageinfoApi
from imager200_python_sdk.api.pipeline_api import PipelineApi
from imager200_python_sdk.api.resize_api import ResizeApi
from imager200_python_sdk.api.rotate_api import RotateApi
from imager200_python_sdk.api.text_api import TextApi

# import ApiClient
from imager200_python_sdk.api_response import ApiResponse
from imager200_python_sdk.api_client import ApiClient
from imager200_python_sdk.configuration import Configuration
from imager200_python_sdk.exceptions import OpenApiException
from imager200_python_sdk.exceptions import ApiTypeError
from imager200_python_sdk.exceptions import ApiValueError
from imager200_python_sdk.exceptions import ApiKeyError
from imager200_python_sdk.exceptions import ApiAttributeError
from imager200_python_sdk.exceptions import ApiException

# import models into sdk package
from imager200_python_sdk.models.blend_request import BlendRequest
from imager200_python_sdk.models.concat_request import ConcatRequest
from imager200_python_sdk.models.error_response import ErrorResponse
from imager200_python_sdk.models.image_metadata import ImageMetadata
from imager200_python_sdk.models.info_response import InfoResponse
from imager200_python_sdk.models.pipeline_execution_result import PipelineExecutionResult
from imager200_python_sdk.models.pipeline_status import PipelineStatus
from imager200_python_sdk.models.success_response import SuccessResponse
