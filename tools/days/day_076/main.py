from days.day_076.files.helpers import *


def day_076():
    title("NUMPY")

    # Create new ndarray from scatch
    my_array = np.array([1.1, 9.2, 8.1, 4.7])
    nls(f"1-Dimensional Array (VECTOR) with .shape:\n{my_array.shape}")
    # Can be accessed by index (my_array[2] will return 8.1)

    # Show dimensions of an array
    nls(f"Show Dimensions of array with .ndim:\n{my_array.ndim}")

    array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

    nls(f"array_2d (MATRIX) has {array_2d.ndim} dimensions")
    nls(f"Its shape is {array_2d.shape}")
    nls(f"It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns")
    nls(array_2d)

    nls(f"Third value in Second Row={array_2d[1,2]}")
    nls(f"All Values in first row={array_2d[0,:]}")

    nls("========== N-Dimensional Arrays (TENSORS) ==========")
    mystery_array = np.array(
        [
            [[0, 1, 2, 3], [4, 5, 6, 7]],
            [[7, 86, 6, 98], [5, 1, 0, 4]],
            [[5, 36, 32, 48], [97, 0, 27, 18]],
        ]
    )
    nls(f"Mystery Array has {mystery_array.ndim} dimensions")
    nls(f"Mystery Array's shape is {mystery_array.shape}")

    # Axis 0: 3rd element. Axis 1: 2nd Element. Axis 3: 4th Element
    nls(
        f"Last item of last element of last array: {mystery_array[2, 1, 3]}\n(Axis 0: 3rd element. Axis 1: 2nd Element. Axis 3: 4th Element)"
    )

    # Retrieve all the elements on the 3rd axis that are at
    # position 2 on the first axis and position 1 on the second axis.
    nls(
        f"Retrieve all the elements on the 3rd axis that are at\nposition 2 on the first axis and position 1 on the second axis.\n{mystery_array[2, 1, :]}"
    )

    # All the first elements on axis number 3
    nls(f"All the first elements on axis number 3:\n{mystery_array[:, :, 0]}")

    # Use arange to create a vector `a` with values ranging from 10 to 29
    a = np.arange(10, 30)
    nls(f"Use arange to create a vector `a` with values ranging from 10 to 29\n{a}")

    # last 3 values
    nls(f"Last 3 values:\n{a[-3:]}")

    # interval of values
    nls(f"interval of values:\n{a[3:6]}")

    # all the values except the first 12
    nls(f"all the values except the first 12:\n{a[12:]}")

    # every second value (all the even numbers)
    nls(f"every second value (all the even numbers):\n{a[::2]}")

    # reverse order
    nls(f"Reversed:\n{a[::-1]}")  # or np.flip(a)

    # Print out all the indices of the non-zero elements in this array [6,0,9,0,0,5,0]
    b = np.array([6, 0, 9, 0, 0, 5, 0])
    nz_indices = np.nonzero(b)
    nz_indices  # note this is a tuple
    nls(
        f"Indices of non-zero elements in this array (b) [6,0,9,0,0,5,0]\nnp.nonzero(b):\n{nz_indices}"
    )
    nls(f"Z:\n{nz_indices}")

    # Use NumPy to generate a 3x3x3 array with random numbers
    z = np.random.random((3, 3, 3))
    nls(f"Shape of Z (3x3x3 Array with random numbers):\n{z.shape}")
    nls(f"Z:\n{z}")

    # Use .linspace()` to create a vector `x` of size 9 with values spaced out evenly between 0 to 100 (both included).
    x = np.linspace(0, 100, num=9)
    nls(
        f"Shape of X (.linspace to create vector x of size 9 with values evenly split between 0 and 100 inclusive):\n{x.shape}"
    )
    nls(f"X:\n{x}")

    # Use .linspace() to create another vector `y` of size 9 with values between -3 to 3 (both included).
    # Then plot `x` and `y` on a line chart using Matplotlib.
    y = np.linspace(start=-3, stop=3, num=9)
    nls(
        f"Y (.linspace() to create another vector `y` of size 9 with values between -3 to 3 (both included)):\n{y}"
    )

    # Plot em
    plt.plot(x, y)
    plt.show()

    # Use NumPy to generate an array called `noise` with shape 128x128x3 that has random values. Then use Matplotlib's .imshow() to display the array as an image.
    noise = np.random.random((128, 128, 3))
    nls(f"Noise shape:\n{noise.shape}")
    plt.imshow(noise)
    plt.show()

    nls(f"adding np.arrays ([4, 5, 2, 7] and [2, 1, 3, 3])")
    v1 = np.array([4, 5, 2, 7])
    v2 = np.array([2, 1, 3, 3])
    nls(v1 + v2)

    # Python Lists vs ndarrays
    nls("compared to adding the same python lists")
    list1 = [4, 5, 2, 7]
    list2 = [2, 1, 3, 3]
    nls(list1 + list2)

    nls(f"Unlike python lists, can multiply:\n{v1*v2}")

    array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    nls(f"ARRAY: {array_2d}")
    print(f"Dimensions: {array_2d.ndim}")
    print(f"Shape: {array_2d.shape}")
    print(f"PLus 10 (array_2d +10\n{array_2d + 10}")
    print(f"Times 5 (array_2d *5\n{array_2d * 5}")

    nls("Operation is run on all elements.")

    nls("=========== MULTIPLYING MATRICES ===========")
    a1 = np.array([[1, 3], [0, 1], [6, 2], [9, 7]])

    b1 = np.array([[4, 1, 3], [5, 8, 5]])

    print(f"{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.")
    print(f"{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.")
    print("Dimensions of result: (4x2)*(2x3)=(4x3)")

    c = np.matmul(a1, b1)
    print(f"Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.")
    nls(f"C:\n{c}")

    nls(a1 @ b1)  # another way of matmul

    nls("=========== IMAGES ===========")

    img = misc.face()
    nls(img)
    nls(f"Img Type:\n{type(img)}")
    nls(f"Img Shape:\n{img.shape}")
    nls(f"Img Ndim:\n{img.ndim}")
    plt.imshow(img)
    plt.show()

    nls("Black and white ver")
    # Divide all the values by 255 to convert them to sRGB, where all the values are between 0 and 1.
    sRGB_array = img / 255

    # Next, multiply the sRGB array by the `grey_vals` to convert the image to grey scale.
    grey_vals = np.array([0.2126, 0.7152, 0.0722])
    img_gray = sRGB_array @ grey_vals
    # img_gray = np.matmul(sRGB_array, grey_vals)

    # Finally use Matplotlib's [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) together with the colormap parameter set to gray `cmap=gray` to look at the results
    plt.imshow(img_gray, cmap="gray")
    plt.show()

    plt.imshow(img_gray)
    plt.show()

    # 1) You flip the grayscale image upside down
    a1
    np.flip(a1)
    plt.imshow(np.flip(img_gray), cmap="gray")
    plt.show()
    # 2) Rotate the colour image
    print(a1)
    print("a1 array rotated:")
    np.rot90(a1)
    plt.imshow(np.rot90(img))
    plt.show()
    # 3) Invert (i.e., solarize) the colour image. To do this you need to converting all the pixels to their "opposite" value, so black (0) becomes white (255).
    solar_img = 255 - img
    plt.imshow(solar_img)
    plt.show()

    image_file = os.path.join(os.path.dirname(__file__), "files", "psycho.jpg")
    my_img = Image.open(image_file)

    img_array = np.array(my_img)
    img_array.ndim
    img_array.shape
    plt.imshow(img_array)
    plt.show()
    plt.imshow(255 - img_array)
    plt.show()
