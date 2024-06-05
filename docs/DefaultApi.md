# tada_ai.DefaultApi

All URIs are relative to _http://localhost_

| Method                                                                               | HTTP request                                    | Description |
| ------------------------------------------------------------------------------------ | ----------------------------------------------- | ----------- |
| [**search_controller_search_chunks**](DefaultApi.md#search_controller_search_chunks) | **POST** /api/search                            |
| [**space_file_controller_download**](DefaultApi.md#space_file_controller_download)   | **GET** /api/space-files/{spaceFileId}/download |
| [**space_file_controller_find**](DefaultApi.md#space_file_controller_find)           | **GET** /api/space-files/{spaceFileId}          |
| [**spaces_controller_create**](DefaultApi.md#spaces_controller_create)               | **POST** /api/spaces                            |
| [**spaces_controller_find**](DefaultApi.md#spaces_controller_find)                   | **GET** /api/spaces/{spaceId}                   |
| [**spaces_controller_find_many**](DefaultApi.md#spaces_controller_find_many)         | **GET** /api/spaces                             |
| [**spaces_controller_space_files**](DefaultApi.md#spaces_controller_space_files)     | **GET** /api/spaces/{spaceId}/files             |
| [**spaces_controller_upload**](DefaultApi.md#spaces_controller_upload)               | **POST** /api/spaces/{spaceId}/files            |

# **search_controller_search_chunks**

> SearchResultDto search_controller_search_chunks(search_query_input)

### Example

```python
import tada_ai
from tada_ai.models.search_query_input import SearchQueryInput
from tada_ai.models.search_result_dto import SearchResultDto
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): api-key
configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)
    search_query_input = tada_ai.SearchQueryInput() # SearchQueryInput |

    try:
        api_response = api_instance.search_controller_search_chunks(search_query_input)
        print("The response of DefaultApi->search_controller_search_chunks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_controller_search_chunks: %s\n" % e)
```

### Parameters

| Name                   | Type                                        | Description | Notes |
| ---------------------- | ------------------------------------------- | ----------- | ----- |
| **search_query_input** | [**SearchQueryInput**](SearchQueryInput.md) |             |

### Return type

[**SearchResultDto**](SearchResultDto.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description             | Response headers |
| ----------- | ----------------------- | ---------------- |
| **200**     | Returns a search record | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_file_controller_download**

> space_file_controller_download(space_file_id)

### Example

```python
import tada_ai
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): api-key
configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)
    space_file_id = 'space_file_id_example' # str |

    try:
        api_instance.space_file_controller_download(space_file_id)
    except Exception as e:
        print("Exception when calling DefaultApi->space_file_controller_download: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
| ----------------- | ------- | ----------- | ----- |
| **space_file_id** | **str** |             |

### Return type

void (empty response body)

### Authorization

[API Key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | The file&#39;s content                     | -                |
| **403**     | You are not authorized to take this action | -                |
| **404**     | SpaceFile not found                        | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_file_controller_find**

> SpaceFile space_file_controller_find(space_file_id)

### Example

```python
import tada_ai
from tada_ai.models.space_file import SpaceFile
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)
    space_file_id = 'space_file_id_example' # str |

    try:
        api_response = api_instance.space_file_controller_find(space_file_id)
        print("The response of DefaultApi->space_file_controller_find:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->space_file_controller_find: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
| ----------------- | ------- | ----------- | ----- |
| **space_file_id** | **str** |             |

### Return type

[**SpaceFile**](SpaceFile.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | SpaceFile not found                        | -                |
| **403**     | You are not authorized to take this action | -                |
| **404**     | SpaceFile not found                        | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_controller_create**

> Space spaces_controller_create(create_manual_space_input)

### Example

```python
import tada_ai
from tada_ai.models.create_manual_space_input import CreateManualSpaceInput
from tada_ai.models.space import Space
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): api-key
configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)
    create_manual_space_input = tada_ai.CreateManualSpaceInput() # CreateManualSpaceInput |

    try:
        api_response = api_instance.spaces_controller_create(create_manual_space_input)
        print("The response of DefaultApi->spaces_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->spaces_controller_create: %s\n" % e)
```

### Parameters

| Name                          | Type                                                    | Description | Notes |
| ----------------------------- | ------------------------------------------------------- | ----------- | ----- |
| **create_manual_space_input** | [**CreateManualSpaceInput**](CreateManualSpaceInput.md) |             |

### Return type

[**Space**](Space.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Returns a search record                    | -                |
| **403**     | You are not authorized to take this action | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_controller_find**

> Space spaces_controller_find(space_id)

### Example

```python
import tada_ai
from tada_ai.models.space import Space
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): api-key
configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)
    space_id = 'space_id_example' # str |

    try:
        api_response = api_instance.spaces_controller_find(space_id)
        print("The response of DefaultApi->spaces_controller_find:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->spaces_controller_find: %s\n" % e)
```

### Parameters

| Name         | Type    | Description | Notes |
| ------------ | ------- | ----------- | ----- |
| **space_id** | **str** |             |

### Return type

[**Space**](Space.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Get a specific space                       | -                |
| **403**     | You are not authorized to take this action | -                |
| **404**     | No space found for the given spaceId       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_controller_find_many**

> List[Space] spaces_controller_find_many()

### Example

```python
import tada_ai
from tada_ai.models.space import Space
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): api-key
configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)

    try:
        api_response = api_instance.spaces_controller_find_many()
        print("The response of DefaultApi->spaces_controller_find_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->spaces_controller_find_many: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Space]**](Space.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Lists all spaces                           | -                |
| **403**     | You are not authorized to take this action | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_controller_space_files**

> List[SpaceFile] spaces_controller_space_files(space_id)

### Example

```python
import tada_ai
from tada_ai.models.space_file import SpaceFile
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): api-key
configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)
    space_id = 'space_id_example' # str |

    try:
        api_response = api_instance.spaces_controller_space_files(space_id)
        print("The response of DefaultApi->spaces_controller_space_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->spaces_controller_space_files: %s\n" % e)
```

### Parameters

| Name         | Type    | Description | Notes |
| ------------ | ------- | ----------- | ----- |
| **space_id** | **str** |             |

### Return type

[**List[SpaceFile]**](SpaceFile.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | All files within the space                 | -                |
| **403**     | You are not authorized to take this action | -                |
| **404**     | No space found for the given spaceId       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_controller_upload**

> SpaceFile spaces_controller_upload(space_id, file)

### Example

```python
import tada_ai
from tada_ai.models.space_file import SpaceFile
from tada_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tada_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): api-key
configuration = tada_ai.Configuration(
    access_token = os.environ["TADA_AI_API_KEY"]
)

# Enter a context with an instance of the API client
with tada_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tada_ai.DefaultApi(api_client)
    space_id = 'space_id_example' # str |
    file = None # bytearray | File upload (expected formats: PDF, DOCX, etc.). Content Type and the name are read off of the file

    try:
        api_response = api_instance.spaces_controller_upload(space_id, file)
        print("The response of DefaultApi->spaces_controller_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->spaces_controller_upload: %s\n" % e)
```

### Parameters

| Name         | Type          | Description                                                                                         | Notes |
| ------------ | ------------- | --------------------------------------------------------------------------------------------------- | ----- |
| **space_id** | **str**       |                                                                                                     |
| **file**     | **bytearray** | File upload (expected formats: PDF, DOCX, etc.). Content Type and the name are read off of the file |

### Return type

[**SpaceFile**](SpaceFile.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **201**     | Successfully created space file            | -                |
| **403**     | You are not authorized to take this action | -                |
| **404**     | No space found for the given spaceId       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
