# rsv.py
# Description
A module for reading and writing an [RSV](https://github.com/Stenway/RSV-Challenge) document file.

# Using
```python
import rsv

sample_data = [
    ["Name", "Description", None],
    [],
    [None, ":)"]
]

with open("document.rsv", "wb") as file:
    rsv.dump(sample_data, file)

with open("document.rsv", "rb") as file:
    data = rsv.load(file)
```