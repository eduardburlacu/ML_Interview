import numpy as np

def max_pool(
        image: np.ndarray,
        kernel_size: int,
        stride:int,
) -> np.ndarray:
    """
    Perform average pooling on a 2D image.

    :param image: 2D NumPy array representing the image
    :param kernel_size: Size of the pooling kernel
    :param stride: Size of translation
    :param pad: the pad sequence
    :return: 2D NumPy array representing the pooled image
    """
    if len(image.shape) == 2:
        image = image[None, :, :]

    c, h, w = image.shape

    h_out = 1 + (h - kernel_size) //stride
    w_out = 1 + (w - kernel_size) // stride
    out = np.zeros((c, h_out, w_out))
    for u in range(h_out):
        for v in range(w_out):
            out [:, u, v] = np.max(
                image[:,stride * u: stride * u + kernel_size,stride * v: stride * v + kernel_size],
                axis=(1, 2)
            )
    if c==1:
        return out[0]
    return out

if __name__=='__main__':
    image = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])
    print(max_pool(image, 2, 2))
    # [[6 8]
    #  [14 16]]
    print(max_pool(image, 2, 1))
    # [[6 7 8]
    #  [10 11 12]
    #  [14 15 16]]
    image = np.array([
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]],
        [[31, 32, 33, 34],
         [35, 36, 37, 38],
         [39, 40, 41, 42],
         [43, 44, 45, 46]]]
    )
    print(max_pool(image, 2, 2))
    # [[ 6  8]
    #  [36 38]]

