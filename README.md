# Chase 2018 Job Interview Coding Challenges

Install: `brew install python3`
New: `make new`
Run latest: `make`

## Python Tricks

### Slices

```python
"foobar"[:1] == "f"
"foobar"[1:] == "oobar"
```

### Dicts

Can take MULTIPLE arguments as the key

```python
d[a, b, c] = 'foobar'
d.get((a, b, c)) == 'foobar'
```

The function `items` is awesome.

```python
d = dict(f=0, o=1, b=3)
d.items() == [('b', 3), ('o', 1), ('f', 0)]
```

### Sets

- Declare: `{1, 2, 3}`  
- Union: `{1, 2, 3} | {4, }`, but use `results = set(); results.add()`

### Types

```python
isinstance(item, (list, tuple))
if type(foo) == list
```

### Iterables

```python
[(i, char) for i, char in enumerate("foobar")]
    == [(0, 'f'), (1, 'o'), (2, 'o'), (3, 'b'), (4, 'a'), (5, 'r')]
```

### Regex

- Replace: `re.sub(pattern, repl, str)`
- Groups: `re.sub(r'tzinfo=<(.*)>', r'tzinfo=pytz.timezone("\1")', repr(v))`
- List matches: `re.findall(pattern, str)`

### Sorting

```python
sorted([{'k':2}, {'k':3}, {'k':1}], key=lambda x: x.get('k'), reverse=False)
```

### Binary

- Int to binary string: `bin(10) == '0b1010'`, `bin(10)[2:] == '1010'`.
- Binary string to int: `int('11111111', 2)`.

But be careful - the results are not fixed width!

## Data Structures

### Matrix

- Don't use x/y for variable names. Use row and column.
- Remember that `m[row][col]` is the right order.

### Stacks/Queues

- Emulate a stack - `list.append` and `list.pop`.
- Emulate a queue - `deque.append` and `deque.popleft`.

```python
[1, 2, 3].pop() == 3
[1, 2, 3].pop(0) == 1
```

### Trees/Graphs

- A trie is great for storing words for quick prefix lookup.
- Implement a depth first search using a queue.
- Two find the shortest distance between two nodes in a graph, run a breadth
  first search from each one in parallel.
- It's common to need to track whether a node has been visited in a graph.
- For some problems it may be expedient to model a graph as a hash table of
  edges.

## Algorithms

### Recursion / Dynamic Programming

- Recursion - bottom up, top down, half and half
- To get big-O, draw a tree with number of nodes
- DP == recursion + memoization
