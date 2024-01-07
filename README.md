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

# The first load method.
# It is the most efficient and suitable for working even with large arrays.
# Since it loads data from the file sequentially when loading.
with open("document.rsv", "rb") as file:
    data = rsv.load(file)

# The second load method.
# It is suitable for working with small arrays.
# Since it loads the entire file into memory at once and only then parses it.
with open("document.rsv", "rb") as file:
    data = rsv.load_split(file)

```