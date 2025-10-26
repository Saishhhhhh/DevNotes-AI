# Numpy Notes

## 01 Creating NumPy Array

## 01 Creating NumPy Arrays

Welcome to your first dive into NumPy! NumPy (Numerical Python) is a fundamental library for numerical computing in Python. It provides high-performance multidimensional array objects and tools for working with these arrays. If you're dealing with large datasets or complex mathematical operations, NumPy is your go-to library.

Let's explore how to create and manipulate these powerful arrays step-by-step.

---

### 🔹 Setting Up NumPy

Before we can use NumPy, we need to ensure it's installed and imported.

#### 1. Installing NumPy

While often pre-installed in environments like Google Colab or Anaconda, it's good practice to know how to install it.

```python
!pip install numpy
```

**Explanation:**
• This command uses `pip`, Python's package installer, to download and install the NumPy library into your environment. The `!` prefix allows you to run shell commands directly from a Jupyter Notebook or similar interactive environment.

#### 2. Importing NumPy

Once installed, you need to import it into your Python script or notebook to start using its functionalities.

```python
import numpy as np
```

**Explanation:**
• `import numpy as np` is the standard convention. It imports the NumPy library and assigns it the alias `np`. This means instead of typing `numpy.array()`, you can simply type `np.array()`, making your code cleaner and easier to read.

---

### 🔹 Creating Arrays from Python Lists

The most straightforward way to create a NumPy array is by converting a standard Python list or tuple.

#### 1. Creating a 1-Dimensional Array

```python
arr = np.array([1,3,4])
arr
```

**Expected Output:**
```
array([1, 3, 4])
```

**Explanation:**
• We pass a Python list `[1, 3, 4]` to the `np.array()` function.
• NumPy then converts this list into a 1-dimensional array (also known as a vector).
• When you print `arr`, NumPy displays the array with its elements.

#### 2. Creating a 2-Dimensional Array (Matrix)

NumPy can easily handle multi-dimensional data structures, like matrices.

```python
myarr = np.array([[1,2,3],[4,5,6],[7,8,9]])
myarr
```

**Expected Output:**
```
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

**Explanation:**
• Here, we pass a list of lists to `np.array()`. Each inner list represents a row in the matrix.
• This creates a 2-dimensional array, which is essentially a table of numbers.

---

### 🔹 Array Creation Functions

NumPy provides several convenient functions to create arrays with specific initial values or patterns, without needing to manually define all elements.

#### 1. `np.zeros()`: All Zeros Array

Creates an array filled with zeros.

```python
np.zeros((3,4))
```

**Expected Output:**
```
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```

**Explanation:**
• The argument `(3,4)` is a tuple specifying the `shape` of the array: 3 rows and 4 columns.
• By default, `np.zeros()` creates arrays with a `float` data type (notice the decimal points).

#### 2. `np.ones()`: All Ones Array

Creates an array filled with ones.

```python
np.ones((3,5))
```

**Expected Output:**
```
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
```

**Explanation:**
• Similar to `np.zeros()`, `np.ones()` takes a shape tuple.
• It fills the specified shape with `1.0` (float) values.

#### 3. `np.full()`: Custom Value Array

Creates an array filled with a specified constant value.

```python
np.full((4,6), 7)
```

**Expected Output:**
```
array([[7, 7, 7, 7, 7, 7],
       [7, 7, 7, 7, 7, 7],
       [7, 7, 7, 7, 7, 7],
       [7, 7, 7, 7, 7, 7]])
```

**Explanation:**
• The first argument `(4,6)` is the desired shape (4 rows, 6 columns).
• The second argument `7` is the value with which to fill the array.
• The `dtype` will be inferred from the fill value (here, `int`).

#### 4. `np.eye()`: Identity Matrix

Creates an identity matrix, which is a square matrix with ones on the main diagonal and zeros elsewhere.

```python
np.eye(3)   #Identity Matrix
```

**Expected Output:**
```
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

**Explanation:**
• The argument `3` specifies the dimension of the square matrix (a 3x3 identity matrix).
• This is particularly useful in linear algebra.

#### 5. `np.arange()`: Range-Based Array

Similar to Python's built-in `range()` function, but it returns a NumPy array.

```python
np.arange(1,10,2)  #(like range)
```

**Expected Output:**
```
array([1, 3, 5, 7, 9])
```

**Explanation:**
• `np.arange(start, stop, step)`:
    • `start`: The starting value (inclusive).
    • `stop`: The ending value (exclusive).
    • `step`: The step size between values.
• This creates a 1-dimensional array with values from 1 up to (but not including) 10, incrementing by 2.

#### 6. `np.linspace()`: Evenly Spaced Array

Creates an array with a specified number of evenly spaced values over a given interval.

```python
np.linspace(0,1,5) #evenly spaced array from given number to given number and also we have to specify the total elements in the array
```

**Expected Output:**
```
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
```

**Explanation:**
• `np.linspace(start, stop, num)`:
    • `start`: The starting value (inclusive).
    • `stop`: The ending value (inclusive).
    • `num`: The total number of elements to generate.
• This creates an array of 5 evenly spaced numbers between 0 and 1 (inclusive). It's great for plotting functions or creating data points.

---

### 🔹 Understanding Array Attributes

NumPy arrays come with several useful attributes that provide information about their structure and data. Let's look at some key ones using our `myarr` example.

```python
myarr = np.array([[1,2,3],[4,5,6],[7,8,9]])
myarr
```

**Expected Output:**
```
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

#### 1. `myarr.shape`: Array Dimensions

```python
myarr.shape  #kiti by kiti cha array
```

**Expected Output:**
```
(3, 3)
```

**Explanation:**
• The `shape` attribute returns a tuple indicating the size of the array in each dimension.
• For `myarr`, it's a 3x3 array (3 rows, 3 columns).

#### 2. `myarr.size`: Total Number of Elements

```python
myarr.size
```

**Expected Output:**
```
9
```

**Explanation:**
• The `size` attribute returns the total number of elements in the array.
• For a 3x3 array, `3 * 3 = 9` elements.

#### 3. `myarr.ndim`: Number of Dimensions

```python
myarr.ndim  #dimension of array
```

**Expected Output:**
```
2
```

**Explanation:**
• The `ndim` attribute returns the number of dimensions (axes) of the array.
• `myarr` is a 2-dimensional array. A 1D array would have `ndim=1`, and a scalar would have `ndim=0`.

#### 4. `myarr.dtype`: Data Type of Elements

```python
myarr.dtype
```

**Expected Output:**
```
dtype('int32')
```

**Explanation:**
• The `dtype` attribute tells you the data type of the elements stored in the array.
• NumPy arrays are homogeneous, meaning all elements in an array must be of the same data type. Here, it inferred `int32` (32-bit integer) because all elements were integers.

---

### 🔹 Managing Data Types (`dtype`)

NumPy is very efficient because it stores data in specific, optimized data types. You can control these types.

#### 1. Specifying `dtype` During Creation

You can explicitly set the data type when creating an array.

```python
myarr2 = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype='float32')   #Giving my own data type to array
myarr2
```

**Expected Output:**
```
array([[1., 2., 3.],
       [4., 5., 6.],
       [7., 8., 9.]], dtype=float32)
```

**Explanation:**
• By adding `dtype='float32'`, we tell NumPy to store the numbers as 32-bit floating-point numbers. Notice the `.` after each number in the output, indicating they are floats.

```python
myarr2.dtype
```

**Expected Output:**
```
dtype('float32')
```

**Explanation:**
• Confirming the data type of `myarr2`.

#### 2. Changing `dtype` of an Existing Array

You can convert an array to a different data type using the `astype()` method.

```python
myarr2.astype('float64')   #changing the existing data type of the array
```

**Expected Output:**
```
array([[1., 2., 3.],
       [4., 5., 6.],
       [7., 8., 9.]])
```

**Explanation:**
• `astype('float64')` converts the array elements to 64-bit floating-point numbers.
• **Important Note:** `astype()` returns a *new* array with the specified `dtype`. It does **not** modify the original array in-place. If you want to update the array, you need to assign the result back: `myarr2 = myarr2.astype('float64')`.

```python
myarr2.dtype
```

**Expected Output:**
```
dtype('float32')
```

**Explanation:**
• As explained above, `myarr2` itself was not modified by the previous `astype()` call, so its `dtype` remains `float32`.

---

### 🔹 Reshaping and Flattening Arrays

NumPy allows you to change the shape of an array without changing its data, and to convert multi-dimensional arrays into 1-dimensional ones.

First, let's create a new array for demonstration.

```python
myarr3 = np.array([[1,2,3],[4,5,6],[7,8,9],[11,12,13]])
myarr3.shape
```

**Expected Output:**
```
(4, 3)
```

**Explanation:**
• We have a 2D array `myarr3` with 4 rows and 3 columns. Total elements: `4 * 3 = 12`.

#### 1. `reshape()`: Changing Array Dimensions

The `reshape()` method allows you to change the shape of an array, provided the new shape has the same total number of elements as the original.

```python
reshaped = myarr3.reshape((3,4))
reshaped
```

**Expected Output:**
```
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 11, 12, 13]])
```

**Explanation:**
• We take `myarr3` (shape `(4,3)`, 12 elements) and reshape it into `(3,4)` (3 rows, 4 columns, also 12 elements).
• The elements are filled row by row from the original array.
• **Note:** `reshape()` also returns a *new* array with the desired shape. The original `myarr3` remains unchanged.

```python
myarr3
```

**Expected Output:**
```
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [11, 12, 13]])
```

**Explanation:**
• This confirms that `myarr3` still retains its original shape `(4,3)`.

#### 🔹 Important: Reshaping with Incompatible Dimensions

If you try to reshape an array into a shape that doesn't match the total number of elements, NumPy will raise an error.

```python
myarr3.reshape(2,7)
```

**Expected Output (Error):**
```
ValueError: cannot reshape array of size 12 into shape (2,7)
```

**Explanation:**
• `myarr3` has `12` elements (`4 * 3`).
• Trying to reshape it to `(2,7)` would require `2 * 7 = 14` elements. Since `12 != 14`, NumPy throws a `ValueError`. Always ensure `product(new_shape) == product(original_shape)`.

#### 2. `flatten()`: Converting to a 1D Array

The `flatten()` method returns a copy of the array collapsed into one dimension.

```python
myarr3.flatten() #converting to 1D array
```

**Expected Output:**
```
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 11, 12, 13])
```

**Explanation:**
• This converts our 2D `myarr3` into a single, 1-dimensional array, preserving the order of elements (row by row).
• Like `reshape()`, `flatten()` returns a *copy* of the array; the original array remains unchanged.

---

### Key Takeaways from Creating NumPy Arrays:

*   **`np.array()`**: The primary way to create arrays from Python lists.
*   **Specialized Creation Functions**: `np.zeros()`, `np.ones()`, `np.full()`, `np.eye()`, `np.arange()`, and `np.linspace()` are powerful for generating arrays with specific patterns.
*   **Array Attributes**: `shape`, `size`, `ndim`, and `dtype` provide essential information about your arrays.
*   **Data Types (`dtype`)**: NumPy arrays are homogeneous. You can specify `dtype` during creation or convert it using `astype()`. Remember `astype()` returns a new array.
*   **Reshaping**: `reshape()` allows you to change the dimensions of an array, provided the total number of elements remains constant.
*   **Flattening**: `flatten()` transforms any array into a 1-dimensional array.

You've now learned the foundational steps to create and understand the basic structure of NumPy arrays. This knowledge is crucial for all advanced operations you'll perform with NumPy!

## 02 Indexing And Slicing

Welcome to the second topic in our NumPy journey! After learning how to create NumPy arrays, the next crucial step is understanding how to access and manipulate their elements. This is where **indexing** and **slicing** come into play.

🔹 **Indexing** allows you to select individual elements from an array using their position.
🔹 **Slicing** allows you to select a *range* of elements, creating a sub-array (or "view") from the original.
🔹 NumPy's indexing and slicing capabilities are powerful and highly optimized, making data extraction very efficient.

Let's dive into the details!

### Initializing Our Arrays

We'll start by creating a 2D NumPy array and then flatten it to demonstrate indexing and slicing on a 1D array first, which is often easier to grasp.

```python
import numpy as np

# Create a 2D NumPy array
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[11,12,13]])
arr
```
**Output:**
```
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [11, 12, 13]])
```

Now, let's create a 1D version of this array using the `flatten()` method.

```python
# Flatten the 2D array into a 1D array
flat = arr.flatten()
flat
```
**Output:**
```
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 11, 12, 13])
```
🔹 The `flatten()` method creates a **new 1D array** (a copy) from the original multidimensional array. This is different from `ravel()`, which can return a view. For now, `flatten()` ensures we have a simple 1D array to work with.

### Basic Indexing: Accessing Single Elements

Just like Python lists, you can access individual elements in a NumPy array using square brackets `[]` and their zero-based index.

```python
# Access the element at index 0 (the first element)
flat[0]
```
**Output:**
```
1
```
🔹 Remember that indexing in Python (and NumPy) starts from `0`. So, `flat[0]` refers to the very first element.

### Slicing 1D Arrays

Slicing allows you to extract a portion of an array. The syntax is `[start:end:step]`.

*   **`start`**: The index where the slice begins (inclusive). If omitted, it defaults to `0`.
*   **`end`**: The index where the slice ends (exclusive). If omitted, it defaults to the end of the array.
*   **`step`**: The increment between elements (e.g., `2` for every second element). If omitted, it defaults to `1`.

Let's look at various slicing examples:

#### 1. `[start:end]` - A Specific Range

```python
# Get elements from index 3 up to (but not including) index 6
flat[3:6]
```
**Output:**
```
array([4, 5, 6])
```
🔹 Here, we get elements at indices 3, 4, and 5. The element at index 6 is excluded.

#### 2. `[:end]` - From the Beginning to a Specific Index

```python
# Get elements from the beginning (index 0) up to (but not including) index 5
flat[:5]  # same as flat[0:5]
```
**Output:**
```
array([1, 2, 3, 4, 5])
```
🔹 When `start` is omitted, slicing begins from index `0`.

#### 3. `[start:]` - From a Specific Index to the End

```python
# Get elements from index 3 to the end of the array
flat[3:] # same as flat[3: array ki length]
```
**Output:**
```
array([ 4,  5,  6,  7,  8,  9, 11, 12, 13])
```
🔹 When `end` is omitted, slicing continues until the last element of the array.

#### 4. `[::step]` - Every Nth Element

```python
# Get every second element from the entire array
flat[::2]  #every 2nd element
```
**Output:**
```
array([ 1,  3,  5,  7,  9, 12])
```
🔹 This selects elements at index 0, 2, 4, etc.

#### Key Takeaway on Slicing:
Slicing is a powerful way to extract subsets of your data. It's concise and efficient for selecting ranges of elements.

### 🔹 Important Concept: Views vs. Copies in Slicing

This is one of the most crucial concepts to understand when working with NumPy arrays. Unlike standard Python lists where slicing creates a new copy, **NumPy array slices typically return a *view* of the original array, not a copy.**

*   **View**: A view is essentially a reference to the original array's data. If you modify the view, the original array will also be modified.
*   **Copy**: A copy is an independent new array with its own data. Modifying a copy will not affect the original array.

Let's demonstrate this with an example:

```python
# Our original flat array
flat
```
**Output:**
```
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 11, 12, 13])
```

```python
# Create a slice 'b' from 'flat'
# Here slicing doesnt make a new array from flat and store in b, instead it just gives a view of flat array to b
b = flat[3:7]
b
```
**Output:**
```
array([4, 5, 6, 7])
```
🔹 `b` now holds a view of elements at indices 3, 4, 5, and 6 from `flat`.

Now, let's modify an element in `b`:

```python
# Modify the first element of 'b'
b[0] = 44
b
```
**Output:**
```
array([44,  5,  6,  7])
```
🔹 Notice that `b` has been updated. Now, let's see what happened to our original `flat` array:

```python
# Check the original 'flat' array
flat
```
**Output:**
```
array([ 1,  2,  3, 44,  5,  6,  7,  8,  9, 11, 12, 13])
```
🔹 **Surprise!** The original `flat` array was also modified. The element at index 3 (which was `4`) is now `44`. This is because `b` was a view, sharing the same underlying data as `flat`.

#### How to Create an Explicit Copy

If you need a completely independent array (a copy) from a slice, you must explicitly use the `.copy()` method:

```python
# Create a slice 'a' from 'flat' using .copy()
a = flat[3:7].copy()    #and if you need to make a copy...use this copy function
a
```
**Output:**
```
array([44,  5,  6,  7])
```
🔹 `a` now holds a *copy* of the elements from `flat` at indices 3 through 6.

Now, let's modify an element in `a`:

```python
# Modify the first element of 'a'
a[0] = 4
a
```
**Output:**
```
array([ 4,  5,  6,  7])
```
🔹 `a` has been updated. Let's check the original `flat` array:

```python
# Check the original 'flat' array
flat
```
**Output:**
```
array([ 1,  2,  3, 44,  5,  6,  7,  8,  9, 11, 12, 13])
```
🔹 As you can see, `flat` remains unchanged. This confirms that `a` is an independent copy.

#### Key Takeaway on Views vs. Copies:
🔹 Always be mindful whether your slicing operation is creating a view or a copy. If you intend to modify the subset of data without affecting the original array, **always use `.copy()` explicitly.**

### Advanced Indexing (Fancy Indexing)

NumPy offers more advanced ways to index arrays, often referred to as "fancy indexing." This includes using arrays of integers or boolean arrays as indices.

#### 1. Integer Array Indexing (Selecting Specific Non-Contiguous Elements)

You can pass a list or array of integers to select elements at those specific, non-sequential indices.

```python
# Create a new array for demonstration
arr = np.array([1,54,23,53,2,3,34,5,6])

# Select elements at indices 1, 4, and 6
arr[[1,4,6]]   #selection of indices
```
**Output:**
```
array([54,  2, 34])
```
🔹 This allows you to pick out elements at arbitrary positions, creating a new array with just those selected elements. The order of indices in the list determines the order of elements in the resulting array.

#### 2. Boolean Array Indexing (Filtering Elements Based on a Condition)

You can use a boolean array (an array of `True`/`False` values) of the same shape as the array you're indexing to select elements where the corresponding boolean value is `True`. This is incredibly useful for filtering data based on conditions.

```python
# Create another array for demonstration
arr2 = np.array([10,20,30,40,50])

# Select elements from arr2 that are greater than 25
arr2[arr2 > 25]    #the array will have elements bigger than 25 only
```
**Output:**
```
array([30, 40, 50])
```
**Explanation:**
1.  `arr2 > 25` evaluates to a boolean array: `array([False, False, True, True, True])`.
2.  When this boolean array is used to index `arr2`, only the elements where the boolean array has `True` at the corresponding position are selected.

#### Key Takeaway on Advanced Indexing:
🔹 **Integer array indexing** is great for picking specific, non-contiguous elements.
🔹 **Boolean array indexing** is perfect for filtering arrays based on conditions, making it very powerful for data analysis.

### Summary

In this section, we explored the essential techniques for accessing and manipulating elements within NumPy arrays:

*   **Basic Indexing:** Accessing single elements using their zero-based index.
*   **Slicing:** Extracting ranges of elements using `[start:end:step]`.
*   **Views vs. Copies:** Understanding that NumPy slices usually return a *view* (modifications affect the original) and how to explicitly create a *copy* using `.copy()`.
*   **Advanced Indexing (Fancy Indexing):**
    *   **Integer Array Indexing:** Selecting elements at specific, non-contiguous indices.
    *   **Boolean Array Indexing:** Filtering elements based on a condition, returning only those that satisfy it.

Mastering indexing and slicing is fundamental to effective data manipulation with NumPy. These techniques form the backbone of many data processing tasks.

