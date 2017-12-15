# secret-santa

## Example Usage:

```python
from secret_santa import secret_santa

matches = secret_santa(['joey', 'bob', 'henry', 'jll', 'anne', 'kelly', 'tim'])
for person in matches:
    print("{} giving to {} and receiving from {}"
        .format(person.name, person.send_to.name, person.receive_from.name))
```