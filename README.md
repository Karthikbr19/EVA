# Assignmnet 1B

## Kernel
- A kernel or a filter is mathematically a matrix which runs over the input to extract the features. 
- The basic feature extractions are blurring, sharpening, embossing, edge detection. 
- Mathematically it can be used set[matrix] of learnable weights. These weights of the kernels are randomly assigned at the start, and during training they get updated automatically. 
- A kernel slides over the image, performs convolution and produces feature map as the output. The feature maps are useful for performing the learning tasks such as detection and classification better.

## Channels: 

There is no exact definition which can explain the channels in neural network. But following points can used to conceptualize the "channels".
1) Channels are also defined as depth of an input.
​	i.e For an image, there will be 3 channels Red,Green,Blue.
2) Channels are the outcome of convolutions.
​	A kernel slides over the image, performs convolution and produces feature map as the output. 
3) Below explained in detail with an ex: 

- ​	If the input has one channel such as a grayscale image, then a 3×3 filter will be applied in 3x3x1 blocks.
- ​	If the input image has three channels for red, green, and blue, then a 3×3 filter will be applied in 3x3x3 blocks.
- ​	If the input is a block of feature maps from another convolutional or pooling layer and has the depth of 64, then the 3×3 filter will be applied in 3x3x64 blocks to create the single values to make up the single output feature map.

In image processing, filter/kernels are used to extract important features from an image. A kernel slides over the image, performs convolution and produces feature map as the output. The feature maps are useful for performing the learning tasks such as detection and classification better.

Kernels can be used for tasks such as blurring,sharpening, edge detection.Let's apply a 3x3 blur kernel to a greyscale image.

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



## 3x3 convolution

We need to take a decision on the size of the matrix or say Kernel.
What size kernel will give better performance ?
There are multiple factors that needs to be taken into account : 
1) If we choose really small kernel we might end up increasing the number of layers. That will increase the computation time.
2) So the solution of the first problem is choose a bigger kernel. But we don't want to loose much information during convolution. If we take really big size kernel, we might end up loosing too much of information.
People used to all different sizes of kernels over the years and now its widely accepted that 3*3 is the right size for the kernel.
Its gives better performance than any other size kernels.

![3 * 3 kernel](https://cdn-images-1.medium.com/max/1600/1*7S266Kq-UCExS25iX_I_AQ.png)
Computational part :
When 3*3 kernel is applied on the layer of n*n, the resulatant layer is (n-2)*(n-2).
For example, if we have a image of an order 300*300, and we apply the filter of 3*3 on it. The resultant layer will be of the order 298*298 , then 296*296 and so on.
