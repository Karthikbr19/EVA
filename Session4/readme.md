# Model development over different iterations

  * 1st iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/1st_iteration.ipynb
  * 2nd iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/2nd_iteration.ipynb
  * 3rd iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/3rd_iteration.ipynb
  * 4th iteration - https://github.com/Karthikbr19/EVA/blob/master/Session4/4th_iteration.ipynb

# Architectural Basics

## Image Normalization:
   To begin with convolution operation normalize the images first.
   
## 3x3 Convolutions:
   Start the convolution operation and generally use the 3x3 convolution, no need of 5x5 or 7x7 convolutions.   
   
## Kernels and how do we decide the number of kernels?
   Based type/size of the input, identify the number of kernels required. If it is a small image no need to require larger number of kernels. 

## How many layers:
   While doing the convolutions we need to predefined idea about how many layers need to be there before the dense/full connected layer and it depends slightly on the receptive field.
   
## Receptive Field:
   Before the fully connected layer is built at each and every step identify the receptive field at each layer, ideally last layer receptive filed need to be size of the input. 
   
## When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

## MaxPooling,
   After building a vanilla network or a basic model, now we need to concentrating on the reducing the number of parameters in the model and maxpooling makes an important role in it

## Position of MaxPooling:
   Maxpooling will be generally done as the network learns, generally after a couple of convolutions.
   
## 1x1 Convolutions: 
   Maxpooling reduces the height and width of the image, but channel reduction will be done by the 1x1 convolutions.

## Batch Normalization: 
   We normalize the input layer by adjusting and scaling the activations. Batch normalization reduces the amount by what the hidden unit values shift around (covariance shift). 
   
## Concept of Transition Layers: 
   When model becomes it is highly impractical to write each layer, instead we make blocks and reuse it with different filters. And layers between two dense blocks will be placed, which consists of Batch Normalization, 1x1 Convolution &
Average pooling

## Position of Transition Layer:
   Layers between two dense blocks will be placed.

## The distance of MaxPooling from Prediction:
   Maxpooling wil be done before 2-3 layers from prediction.

## The distance of Batch Normalization from Prediction: 
   Batch Normalization wil certainly not done before the prediction layer.

## SoftMax: 

## Adam vs SGD

## When to add validation checks
   After completing the model architecture, when we train the model we add the validation checks.
   
## How do we know our network is not going well, comparatively, very early. 
   After 3-4 epochs if the model accuracy is not increasing as expected.  
   
## When do we introduce DropOut, or when do we know we have some overfitting.
   When we train accuracy is more than the validation accuracy.
  

## DropOut:
   When the model is overfitting, we regularize it using the DropOut. 
   
## Batch Size, and effects of batch size:
   Batch size is a term used in machine learning and refers to the number of training examples utilized in one iteration.
      
   Generally large batch size, leads to a higher accuracy.

## Learning Rate:
   The learning rate or step size in machine learning is a hyperparameter which determines to what extent newly acquired information overrides old information.

## LR schedule and concept behind it
   In training the network, it is good to reduce the learning rate as the number of training epochs increases. And this is achieved using learning rate scheduler.

## Number of Epochs and when to increase them
   The number of epochs is a hyperparameter that defines the number times that the learning algorithm will work through the entire training dataset. 









