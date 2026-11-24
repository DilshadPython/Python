# Technical Documentation: Object-Oriented Architecture & CPython Details

## 📊 Class Lifecycle & Method Dispatch Flowchart

```mermaid
flowchart TD
    Instantiation[Object Instantiation User name salary] --> Allocation[Memory Allocation __new__]
    Allocation --> Initialization[Instance Initialization __init__]
    Initialization --> Ready[Object Ready in RAM]

    Ready --> MethodCall{Method Invocation Type}
    MethodCall -->|instance.method()| InstanceMethod[Instance Method self passed implicitly]
    MethodCall -->|Class.factory()| ClassMethod[@classmethod cls passed implicitly]
    MethodCall -->|Class.utility()| StaticMethod[@staticmethod pure function execution]
    MethodCall -->|instance.property| PropertyMethod[@property getter/setter descriptor dispatch]
```

---

## 🔍 Attribute Introspection Matrix (`dir(object)`)

Calling `dir()` on class instances exposes the standard attributes and special dunder hooks:

```python
class Demo:
    pass

d = Demo()
print([attr for attr in dir(d) if not attr.startswith("__")])
```

- **`__class__`**: Points to instance's underlying class object.
- **`__dict__`**: Dictionary mapping dynamic instance attributes.
- **`__doc__`**: Class docstring documentation string.
- **`__mro__`**: Method Resolution Order tuple listing class inheritance search order.
