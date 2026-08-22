## 🚀 Time Complexity and Space Complexity

### 1. Basic Concepts

**Time Complexity** describes how the running time of an algorithm
grows as the input size $n$ increases.

**Space Complexity** describes how much additional memory an algorithm
requires as the input size $n$ increases.

In algorithm analysis, we usually focus on the asymptotic growth rate
and use Big-O notation.

$
T(n) = O(f(n))
$

For space complexity, we usually consider the **auxiliary space**,
i.e., the additional memory used by the algorithm excluding the input itself.

$
S(n) = O(f(n))
$

------------------------------------------------

### 2. Examples of Time and Space Complexity

#### $O(1)$ Time Complexity

Consider accessing the first element of an array:

```python
def get_first(arr):
    return arr[0]
```

Only one operation is required regardless of the input size.

Therefore,

$
\boxed{T(n)=O(1)}
$

If no additional memory proportional to $n$ is required,

$
\boxed{S(n)=O(1)}
$

------------------------------------------------

### $O(n)$ Time Complexity

Consider finding the maximum element:

```python
def find_max(arr):
    max_val = arr[0]

    for x in arr:
        if x > max_val:
            max_val = x

    return max_val
```

The algorithm potentially examines every element once.

Therefore,

$
\boxed{T(n)=O(n)}
$

Only a constant number of variables are used:

$
\boxed{S(n)=O(1)}
$

------------------------------------------------

### $O(n^2)$ Time Complexity

Consider two nested loops:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The outer loop executes $n$ times and the inner loop executes $n$ times
for each iteration of the outer loop.

Thus,

$
T(n)=n\times n=n^2
$

and therefore,

$
\boxed{T(n)=O(n^2)}
$

If no additional data structure is created,

$
\boxed{S(n)=O(1)}
$

------------------------------------------------

### $O(\log n)$ Time Complexity

Binary Search is a classic example.

At each step, the search space is reduced by half:

$
n \rightarrow \frac{n}{2} \rightarrow \frac{n}{4} \rightarrow \cdots \rightarrow 1
$

The number of steps is approximately

$
\log_2 n
$

Therefore,

$
\boxed{T(n)=O(\log n)}
$

For an iterative implementation, only a constant number of variables
are required:

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

$
\boxed{S(n)=O(1)}
$

```python
def binary_search(nums, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, right)
    else:
        return binary_search(nums, target, left, mid - 1)
```

For a recursive implementation, the recursion depth is $O(\log n)$:

$
\boxed{S(n)=O(\log n)}
$

------------------------------------------------

### $O(n\log n)$ Time Complexity

Merge Sort is a typical example.

The input is repeatedly divided into two halves:

$
n \rightarrow \frac{n}{2} \rightarrow \frac{n}{4} \rightarrow \cdots
$

The number of levels is

$
O(\log n)
$

At each level, a total of $O(n)$ elements are processed.

Therefore,

$
\boxed{T(n)=O(n\log n)}
$

Merge Sort usually requires an additional temporary array:

$
\boxed{S(n)=O(n)}
$

------------------------------------------------

### $O(2^n)$ Time Complexity

A naive recursive Fibonacci implementation is a classic example:

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)
```

The recursion generates many repeated subproblems:

$
\text{fib}(n)
\rightarrow
\text{fib}(n-1),\text{fib}(n-2)
$

and each subproblem generates additional subproblems.

The time complexity is approximately

$
\boxed{T(n)=O(2^n)}
$

This becomes extremely inefficient as $n$ increases.

================================================================

## 🚀 Space Complexity

### $O(1)$ Space Complexity

Consider:

```python
def sum_array(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

Only a constant number of variables are used:

$
\text{total},\quad x
$

Therefore,

$
\boxed{S(n)=O(1)}
$

The input array itself is not counted as auxiliary space.

------------------------------------------------

### $O(n)$ Space Complexity

Consider creating another array:

```python
def double_array(arr):
    result = []

    for x in arr:
        result.append(x * 2)

    return result
```

If the input contains $n$ elements, the output array also contains
$O(n)$ elements.

Therefore,

$
\boxed{S(n)=O(n)}
$

Another common example is using a hash set:

```python
def has_duplicate(arr):
    seen = set()

    for x in arr:
        if x in seen:
            return True

        seen.add(x)

    return False
```

In the worst case, the set stores $n$ elements:

$
\boxed{S(n)=O(n)}
$

------------------------------------------------

### $O(n^2)$ Space Complexity

Consider an $n\times n$ matrix:

```python
matrix = [[0] * n for _ in range(n)]
```

The matrix contains
$
n\times n=n^2
$
elements.

Therefore,

$
\boxed{S(n)=O(n^2)}
$

More generally, an $(m\times n)$ matrix requires

$
\boxed{S(m,n)=O(mn)}
$

------------------------------------------------

### Recursion and Space Complexity

Recursive function calls consume memory on the call stack.

For example:

```python
def countdown(n):
    if n == 0:
        return

    countdown(n - 1)
```

The recursion depth is
$
n
$

Therefore,

$
\boxed{S(n)=O(n)}
$

Even though no explicit array or list is created, recursion itself
requires additional memory.

------------------------------------------------

### Recursive vs. Iterative Binary Search}

Recursive Binary Search:

$
\boxed{T(n)=O(\log n)}
$

$
\boxed{S(n)=O(\log n)}
$

because the recursion depth is $O(\log n)$.

Iterative Binary Search:

$
\boxed{T(n)=O(\log n)}
$

$
\boxed{S(n)=O(1)}
$

Thus, an iterative implementation can reduce the auxiliary space
complexity.
