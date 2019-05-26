# Model deveopment over different iterations

  * 1st iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/1st_iteration.ipynb
  * 2nd iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/2nd_iteration.ipynb
  * 3rd iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/3rd_iteration.ipynb
  * 4th iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/4th_iteration.ipynb

# Architectural Basics

## Image Normalization,
## 3x3 Convolutions,
## Kernels and how do we decide the number of kernels?
## How many layers,
## Receptive Field,
## Position of MaxPooling,
## MaxPooling,
## 1x1 Convolutions,
## Batch Normalization,
## Concept of Transition Layers,
## Position of Transition Layer,
## The distance of MaxPooling from Prediction,
## The distance of Batch Normalization from Prediction,
## SoftMax,
## Adam vs SGD
## When to add validation checks
## How do we know our network is not going well, comparatively, very early
## When do we introduce DropOut, or when do we know we have some overfitting
## DropOut
## Batch Size, and effects of batch size
## LR schedule and concept behind it
## Learning Rate,
## Number of Epochs and when to increase them,










## MaxPooling: 
  Max pooling is a sample-based discretization process. The objective is to down-sample an input representation (image, hidden-layer output matrix, etc.), reducing its dimensionality and allowing for assumptions to be made about features contained in the sub-regions binned.



## 1x1 Convolutions:

MaxPooling can be used to down sample the content of feature maps, reducing their width and height but number of feature maps remains same and generally it increases with the hidden layers.

To address this problem, a 1×1 convolutional layer can be used that offers a channel-wise pooling, often called feature map pooling or a projection layer.


## 3x3 Convolutions

While designing the network, we need to take a decision on the size of the matrix (Kernel).

Choosing 3 * 3 has advantages: 

Computationally efficient:
  If we apply 3x3 kernel twice, we have actually used (3x3 + 3x3) weights. But in case if we used 5*5 we have used 25 weights.

More linear features:
  Due to the larger number of layers, it learns complex, more non-linear features.
  

## Receptive Field

## SoftMax

Learning Rate

Kernels and how do we decide the number of kernels?

Batch Normalization

Image Normalization

Position of MaxPooling

Concept of Transition Layers

Position of Transition Layer

Number of Epochs and when to increase them

DropOut

When do we introduce DropOut, or when do we know we have some overfitting

The distance of MaxPooling from Prediction

The distance of Batch Normalization from Prediction

When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

How do we know our network is not going well, comparatively, very early

Batch Size, and effects of batch size

When to add validation checks

LR schedule and concept behind it

Adam vs SGD

etc (you can add more if we missed it here)
