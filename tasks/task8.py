import numpy as np


def array_factory(mode, shape, value=None):
    if mode == "zeros":
        return np.zeros(shape)
    elif mode == "ones":
        return np.ones(shape)
    elif mode == "full":
        return np.full(shape, value)
    elif mode == "identity":
        if isinstance(shape, tuple):
            shape = shape[0]
        return np.eye(shape)
    else:
        raise ValueError("Invalid mode specified.")


def secure_reshape_and_stack(data1, data2, new_shape):
    try:
        arr1 = np.array(data1)
        arr2 = np.array(data2)

        reshaped_arr1 = arr1.reshape(new_shape)
        combined_dataset = np.vstack((reshaped_arr1, arr2))

        return combined_dataset

    except ValueError as e:
        raise ValueError(f"Company-grade Error: {e}")


print("Array Factory (zeros):")
print(array_factory("zeros", (2, 3)))

print("\nArray Factory (full):")
print(array_factory("full", (2, 2), 7))

d1 = [1, 2, 3, 4, 5, 6]
d2 = [[7, 8, 9], [10, 11, 12]]
print("\nReshape and Stack Result:")
print(secure_reshape_and_stack(d1, d2, (2, 3)))