# SearchQueryRerankerOptionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_reranker** | **bool** | Turns the reranker on or off. | [optional] [default to False]
**top_n** | **float** | The largest number of chunks to return from re-ranking | [optional] [default to 10]
**threshold** | **float** | The minimum threshold for a chunk | [optional] [default to 0.25]

## Example

```python
from tada_ai.models.search_query_reranker_options_input import SearchQueryRerankerOptionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQueryRerankerOptionsInput from a JSON string
search_query_reranker_options_input_instance = SearchQueryRerankerOptionsInput.from_json(json)
# print the JSON string representation of the object
print(SearchQueryRerankerOptionsInput.to_json())

# convert the object into a dict
search_query_reranker_options_input_dict = search_query_reranker_options_input_instance.to_dict()
# create an instance of SearchQueryRerankerOptionsInput from a dict
search_query_reranker_options_input_from_dict = SearchQueryRerankerOptionsInput.from_dict(search_query_reranker_options_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


