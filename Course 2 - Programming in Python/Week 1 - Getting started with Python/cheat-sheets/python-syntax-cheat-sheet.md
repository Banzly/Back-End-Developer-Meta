# Python syntax cheat sheet

## Spacing

__Correct__

```python
#any ammount of whitespace on a single line is ok
x     =        1        +        2
```

```
3
```

__Incorrect__

```python
x = 1
+ 2
```

```
No Output
```

## Indentation

__Correct__

```python
def say_hello():
    print("Hello there!")

print(say_hello())
```

```
Hello there!
None
```

-----------

```python
def say_hello(): print("Hello there!")

print(say_hello())
```

```
Hello there!
None
```

__Incorrect__

```python
def say_hello():
print("Hello there!")
```

```
Error on line 2:
    print("Hello there!")
        ^
IndentationError: expected an indented block
```

-----------

```python
    def say_hello():
print("Hello there")
```
Output:
```
Error on line 1:
    def say_hello():
    ^
IndentationError: unexpected indent
```
