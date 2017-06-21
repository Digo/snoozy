# Snoozy
Defines a decoration to remove the boiler-plate for lazy attributes.

## Usage
Just attach the annotation to the properties in a class

```python
import snoozy

class Foo:
    @snoozy.lazy_property
    def bar(self):
        return 'bar'
```