import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:

    if norm_type == 'l1':
        ans = 0
        for i in range(arr.shape[0]):
            if arr.ndim == 1:
                ans += abs(arr[i])
            else:
                for j in range(arr.shape[1]):
                    ans += abs(arr[i, j])
        return float(ans)

    elif norm_type == 'l2':
        ans = 0
        for i in range(arr.shape[0]):
            if arr.ndim == 1:
                ans += arr[i] ** 2
            else:
                for j in range(arr.shape[1]):
                    ans += arr[i, j] ** 2
        return float(np.sqrt(ans))

    elif norm_type == 'linf':
        return float(np.max(np.abs(arr)))

    elif norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError("Array must be 2D")

        ans = 0
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                ans += arr[i, j] ** 2

        return float(np.sqrt(ans))

    else:
        raise ValueError("Invalid norm type")