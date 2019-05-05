# Assignmnet 1B

## What are Channels and Kernels (according to EVA)?

### Kernel
- A kernel or a filter is mathematically a matrix which runs over the input to extract the features. 
- The basic feature extractions are blurring, sharpening, embossing, edge detection. 
- Mathematically it can be used set[matrix] of learnable weights. These weights of the kernels are randomly assigned at the start, and during training they get updated automatically. 
- A kernel slides over the image, performs convolution and produces feature map as the output. The feature maps are useful for performing the learning tasks such as detection and classification better.

### Channels: 

There is no exact definition which can explain the channels in neural network. But following points can used to conceptualize the "channels".
1) Channels are also defined as depth of an input.
​	i.e For an image, there will be 3 channels Red,Green,Blue.
2) Channels are the outcome of convolutions.
​	A kernel slides over the image, performs convolution and produces feature map as the output. 
3) Below explained in detail with an ex: 

- 	If the input has one channel such as a grayscale image, then a 3×3 filter will be applied in 3x3x1 blocks.
- 	If the input image has three channels for red, green, and blue, then a 3×3 filter will be applied in 3x3x3 blocks.
- 	If the input is a block of feature maps from another convolutional or pooling layer and has the depth of 64, then the 3×3 filter will be applied in 3x3x64 blocks to create the single values to make up the single output feature map.



Blur Kernel :

$\begin{bmatrix}0.0625 & 0.125 & 0.0625\\
​                0.0625 & 0.25 & 0.0625\\
​                0.0625 & 0.125 & 0.0625\\
\end{bmatrix}$



|                Original Image                 |                     Blurred Image                     |
| :-------------------------------------------: | :---------------------------------------------------: |
| ![](https://image.ibb.co/bTFGuS/einstein.jpg) | ![](https://image.ibb.co/dsMZg7/blurred_einstein.jpg) |


As it can be seen above, by applying gaussian filter, we were able to blur the image. Similarly, there are different filters available for performing tasks such as edge detection,sharpening,etc.

Previously, research used to spend a lot of time handcrafting these filters which can perform various tasks such as curve detection, noise removal, etc. After that, the feature maps produced by this filter will be used for classification,etc.

Handcrafting of kernels is no more required due to advancement in the field of deep learning. The kernels are initialzed with random weights. During the neural network training, these values of the filter which are called "weights" are learned. At every layer , we can mention number of filters to be learned. The initial filters learn to detect small edges,lines, etc. The latter filter learns to detect bigger things such as face,eye,etc. as they have a bigger receptive field.



## Why should we only (well mostly) use 3x3 Kernels?

While designing the network, we need to take a decision on the size of the matrix (Kernel).
​	i.e Which size kernel will gives a better performance?

Several factors needs to be taken into account : 

1) If we choose really small kernel we might end up increasing the number of layers. That will increase the computation time.

2) If we choose a bigger kernel we might end up in loosing too much information during convolution. 

People used to all different sizes of kernels over the years and now its widely accepted that 3*3 is the right size for the kernel.

### 3 * 3 Advantages 

1) Computationally efficient: 

​	If we apply 3x3 kernel twice, we have actually used (3x3 + 3x3) weights. But in case if we used 5*5 we have used 25 weights.  

2) More linear features:

​	Due to the larger number of layers, it learns complex, more non-linear features.



![3 * 3 kernel](https://cdn-images-1.medium.com/max/1600/1*7S266Kq-UCExS25iX_I_AQ.png)
Computational part :
In general when 3*3 kernel is applied on the layer of n*n, the resultant layer is (n-2)*(n-2).



## How many times do we need to perform 3x3 convolution operation to reach 1x1 from 199x199?



| Input     | Filter | output    |
| --------- | ------ | --------- |
| 199 x 199 | 3 x 3  | 197 x 197 |
| 197 x 197 | 3 x 3  | 195 x 195 |
| 195 x 195 | 3 x 3  | 193 x 193 |
| 193 x 193 | 3 x 3  | 191 x 191 |
| 191 x 191 | 3 x 3  | 189 x 189 |
| 189 x 189 | 3 x 3  | 187 x 187 |
| 187 x 187 | 3 x 3  | 185 x 185 |
| 185 x 185 | 3 x 3  | 183 x 183 |
| 183 x 183 | 3 x 3  | 181 x 181 |
| 181 x 181 | 3 x 3  | 179 x 179 |
| 179 x 179 | 3 x 3  | 177 x 177 |
| 177 x 177 | 3 x 3  | 175 x 175 |
| 175 x 175 | 3 x 3  | 173 x 173 |
| 173 x 173 | 3 x 3  | 171 x 171 |
| 171 x 171 | 3 x 3  | 169 x 169 |
| 169 x 169 | 3 x 3  | 167 x 167 |
| 167 x 167 | 3 x 3  | 165 x 165 |
| 165 x 165 | 3 x 3  | 163 x 163 |
| 163 x 163 | 3 x 3  | 161 x 161 |
| 161 x 161 | 3 x 3  | 159 x 159 |
| 159 x 159 | 3 x 3  | 157 x 157 |
| 157 x 157 | 3 x 3  | 155 x 155 |
| 167 x 167 | 3 x 3  | 165 x 165 |
| 165 x 165 | 3 x 3  | 163 x 163 |
| 163 x 163 | 3 x 3  | 161 x 161 |
| 159 x 159 | 3 x 3  | 157 x 157 |
| 157 x 157 | 3 x 3  | 155 x 155 |
| 155 x 155 | 3 x 3  | 153 x 153 |
| 153 x 153 | 3 x 3  | 151 x 151 |
| 151 x 151 | 3 x 3  | 149 x 149 |
| 149 x 149 | 3 x 3  | 147 x 147 |
| 147 x 147 | 3 x 3  | 145 x 145 |
| 145 x 145 | 3 x 3  | 143 x 143 |
| 143 x 143 | 3 x 3  | 141 x 141 |
| 141 x 141 | 3 x 3  | 139 x 139 |
| 139 x 139 | 3 x 3  | 137 x 137 |
| 137 x 137 | 3 x 3  | 135 x 135 |
| 135 x 135 | 3 x 3  | 133 x 133 |
| 133 x 133 | 3 x 3  | 131 x 131 |
| 131 x 131 | 3 x 3  | 129 x 129 |
| 129 x 129 | 3 x 3  | 127 x 127 |
| 127 x 127 | 3 x 3  | 125 x 125 |
| 125 x 125 | 3 x 3  | 123 x 123 |
| 123 x 123 | 3 x 3  | 121 x 121 |
| 121 x 121 | 3 x 3  | 119 x 119 |
| 119 x 119 | 3 x 3  | 117 x 117 |
| 117 x 117 | 3 x 3  | 115 x 115 |
| 115 x 115 | 3 x 3  | 113 x 113 |
| 113 x 113 | 3 x 3  | 111 x 111 |
| 111 x 111 | 3 x 3  | 109 x 109 |
| 109 x 109 | 3 x 3  | 107 x 107 |
| 129 x 129 | 3 x 3  | 127 x 127 |
| 127 x 127 | 3 x 3  | 125 x 125 |
| 125 x 125 | 3 x 3  | 123 x 123 |
| 123 x 123 | 3 x 3  | 121 x 121 |
| 121 x 121 | 3 x 3  | 119 x 119 |
| 119 x 119 | 3 x 3  | 117 x 117 |
| 117 x 117 | 3 x 3  | 115 x 115 |
| 115 x 115 | 3 x 3  | 113 x 113 |
| 113 x 113 | 3 x 3  | 109 x 109 |
| 109 x 109 | 3 x 3  | 107 x 107 |
| 107 x 107 | 3 x 3  | 105 x 105 |
| 105 x 105 | 3 x 3  | 103 x 103 |
| 103 x 103 | 3 x 3  | 101 x 101 |
| 101 x 101 | 3 x 3  | 99 x 99 |
|  101 x 101  | 3 x 3  |  99 x 99 |
|  99 x 99  | 3 x 3  |  97 x 97 |
|  97 x 97  | 3 x 3  |  95 x 95 |
|  95 x 95  | 3 x 3  |  93 x 93 |
|  93 x 93  | 3 x 3  |  91 x 91 |
|  91 x 91  | 3 x 3  |  89 x 89 |
|  89 x 89  | 3 x 3  |  87 x 87 |
|  87 x 87  | 3 x 3  |  85 x 85 |
|  85 x 85  | 3 x 3  |  83 x 83 |
|  83 x 83  | 3 x 3  |  81 x 81 |
|  81 x 81  | 3 x 3  |  79 x 79 |
|  79 x 79  | 3 x 3  |  77 x 77 |
|  77 x 77  | 3 x 3  |  75 x 75 |
|  75 x 75  | 3 x 3  |  73 x 73 |
|  73 x 73  | 3 x 3  |  71 x 71 |
|  71 x 71  | 3 x 3  |  69 x 69 |
|  69 x 69  | 3 x 3  |  67 x 67 |
|  67 x 67  | 3 x 3  |  65 x 65 |
|  65 x 65  | 3 x 3  |  63 x 63 |
|  63 x 63  | 3 x 3  |  61 x 61 |
|  61 x 61  | 3 x 3  |  59 x 59 |
|  59 x 59  | 3 x 3  |  57 x 57 |
|  57 x 57  | 3 x 3  |  55 x 55 |
|  55 x 55  | 3 x 3  |  53 x 53 |
|  53 x 53  | 3 x 3  |  51 x 51 |
|  51 x 51  | 3 x 3  |  49 x 49 |
|  49 x 49  | 3 x 3  |  47 x 47 |
|  47 x 47  | 3 x 3  |  45 x 45 |
|  45 x 45  | 3 x 3  |  43 x 43 |
|  43 x 43  | 3 x 3  |  41 x 41 |
|  41 x 41  | 3 x 3  |  39 x 39 |
|  39 x 39  | 3 x 3  |  37 x 37 |
|  37 x 37  | 3 x 3  |  35 x 35 |
|  35 x 35  | 3 x 3  |  33 x 33 |
|  33 x 33  | 3 x 3  |  31 x 31 |
|  31 x 31  | 3 x 3  |  29 x 29 |
|  29 x 29  | 3 x 3  |  27 x 27 |
|  27 x 27  | 3 x 3  |  25 x 25 |
|  25 x 25  | 3 x 3  |  23 x 23 |
|  23 x 23  | 3 x 3  |  21 x 21 |
|  21 x 21  | 3 x 3  |  19 x 19 |
|  19 x 19  | 3 x 3  |  17 x 17 |
|  17 x 17  | 3 x 3  |  15 x 15 |
|  15 x 15  | 3 x 3  |  13 x 13 |
|  13 x 13  | 3 x 3  |  11 x 11 |
|  11 x 11  | 3 x 3  |  9 x 9 |
|  9 x 9  | 3 x 3  |  7 x 7 |
|  7 x 7  | 3 x 3  |  5 x 5 |
|  5 x 5  | 3 x 3  |  3 x 3 |
|  3 x 3  | 3 x 3  |  1 x 1 |
