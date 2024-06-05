# SearchRecordChunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**markdown** | **str** | The markdown representation of the chunk | 
**score** | **object** | The score returned by the reranker. Between 0 and 1 | 

## Example

```python
from tada_ai.models.search_record_chunk import SearchRecordChunk

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRecordChunk from a JSON string
search_record_chunk_instance = SearchRecordChunk.from_json(json)
# print the JSON string representation of the object
print(SearchRecordChunk.to_json())

# convert the object into a dict
search_record_chunk_dict = search_record_chunk_instance.to_dict()
# create an instance of SearchRecordChunk from a dict
search_record_chunk_from_dict = SearchRecordChunk.from_dict(search_record_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


