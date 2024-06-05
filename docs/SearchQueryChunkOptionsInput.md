# SearchQueryChunkOptionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_min_word_count** | **float** | Will attempt to keep the minimum chunk size to less than the provided amount. NOTE: This is not guaranteed. Please validate if your system requires a minimum or maximum size. | [optional] [default to 50]
**requested_max_word_count** | **float** | Will attempt to keep the maximum chunk size to less than the provided amount. NOTE: This is not guaranteed. Please validate if your system requires a minimum or maximum size. | [optional] [default to 1500]

## Example

```python
from tada_ai.models.search_query_chunk_options_input import SearchQueryChunkOptionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQueryChunkOptionsInput from a JSON string
search_query_chunk_options_input_instance = SearchQueryChunkOptionsInput.from_json(json)
# print the JSON string representation of the object
print(SearchQueryChunkOptionsInput.to_json())

# convert the object into a dict
search_query_chunk_options_input_dict = search_query_chunk_options_input_instance.to_dict()
# create an instance of SearchQueryChunkOptionsInput from a dict
search_query_chunk_options_input_from_dict = SearchQueryChunkOptionsInput.from_dict(search_query_chunk_options_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


