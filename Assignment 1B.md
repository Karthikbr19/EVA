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



| Input     | Kernel | output    |
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
| 167 x 167 | 3 x 3  | 165 x 165 |
| 167 x 167 | 3 x 3  | 165 x 165 |
| 167 x 167 | 3 x 3  | 165 x 165 |
| 167 x 167 | 3 x 3  | 165 x 165 |
| 167 x 167 | 3 x 3  | 165 x 165 |
| 167 x 167 | 3 x 3  | 165 x 165 |
| 167 x 167 | 3 x 3  | 165 x 165 |
|           |        |           |
|           |        |           |
|           |        |           |
|           |        |           |
|           |        |           |
|           |        |           |
|           |        |           |