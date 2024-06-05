# SpaceFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**id** | **str** |  | 
**original_mime_type** | **str** | The mimetype of the file | 
**space_id** | **str** |  | 
**path** | **str** | The path from the root of the Space | 
**status** | **str** | The processing status of the file. | 

## Example

```python
from tada_ai.models.space_file import SpaceFile

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceFile from a JSON string
space_file_instance = SpaceFile.from_json(json)
# print the JSON string representation of the object
print(SpaceFile.to_json())

# convert the object into a dict
space_file_dict = space_file_instance.to_dict()
# create an instance of SpaceFile from a dict
space_file_from_dict = SpaceFile.from_dict(space_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


