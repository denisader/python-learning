# Practice Exercises — Concepts

### List Comprehension

- one-line syntax for creating lists by transforming and/or filtering elements from an iterable 
- replaces multi-line `for` loops with a readable `[expression for item in iterable if condition]` pattern.
### Lambda Functions

- anonymous functions defined inline with the `lambda` keyword
- commonly used as throwaway functions for `sorted()`, `map()`, or `filter()` 
- instead of defining a full `def` block.
### Custom Iterator

- any object that implements `__iter__()` and `__next__()`
- lets you control exactly how values are produced one at a time, raising `StopIteration` when done
- useful for sequences that are expensive to compute or infinite in nature.
### Decorators

- a function that wraps another function to extend its behavior without modifying its code
- the `@decorator` syntax is syntactic sugar for reassigning the function through the wrapper
### Generators

- functions that use `yield` instead of `return` to produce values lazily, one at a time
- the function's state is paused between yields, making generators memory-efficient for large or infinite sequences
### Context Managers

- objects that define `__enter__()` and `__exit__()` to manage setup and teardown of resources (files, connections, locks)
- used with the `with` statement, they guarantee cleanup even if an exception occurs.
### *args & **kwargs

- `*args` collects extra positional arguments into a tuple
- `**kwargs` collects extra keyword arguments into a dictionary
- they let a function accept any number and type of arguments
### Inheritance & Method Overriding

- subclass method "overrides" the parent's version, and `super()` can be used to still call the original
### Encapsulation

- hiding internal state by prefixing attributes with double underscores (`__attr`), which triggers name mangling
- access is then only possible through controlled methods, protecting the object's integrity

### Property Decorators

- `@property` turns a method into a read-only attribute
- pairing it with `@attr.setter` allows controlled writes with validation
- this gives the clean syntax of attribute access with the safety of getter/setter methods.
### Callable Objects (`__call__`)

- implementing `__call__` makes an instance callable like a function
- useful for objects that need to carry state between calls