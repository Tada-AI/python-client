# SearchQueryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**space_id** | **str** |  | [optional] 
**chunk_options** | [**SearchQueryChunkOptionsInput**](SearchQueryChunkOptionsInput.md) |  | [optional] 
**reranker** | [**SearchQueryRerankerOptionsInput**](SearchQueryRerankerOptionsInput.md) |  | [optional] 

## Example

```python
from tada_ai.models.search_query_input import SearchQueryInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQueryInput from a JSON string
search_query_input_instance = SearchQueryInput.from_json(json)
# print the JSON string representation of the object
print(SearchQueryInput.to_json())

# convert the object into a dict
search_query_input_dict = search_query_input_instance.to_dict()
# create an instance of SearchQueryInput from a dict
search_query_input_from_dict = SearchQueryInput.from_dict(search_query_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


