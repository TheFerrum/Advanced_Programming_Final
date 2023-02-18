Report
Final Project
Handwritten Kazakh language character recognition
Temirlan Torebekov IT-2106
Useful links:
Video description - https://youtu.be/HQWtSRY-Upg
Google drive - https://drive.google.com/drive/folders/1CxC50jF_nMceU_bb2Vunhm85fog28agb?usp=sharing Github - https://github.com/TheFerrum/Advanced_Programming_Final
Telegram bot - @Kazakh_CNN_bot

Introduction
Image classification is one of the major paths of machine learning. Nowadays computers can recognise handwritten digits, english, spanish, german, and russian language letters. Therefore I decided to make handwritten kazakh language characters recognition. There are ready-made projects such as MNIST digit classification or A-Z character recognition [1]. Consequently I have been inspired by these projects. My project is similar to the previous works that described, but I worked with kazakh language characters and my aim is to train a model that recognises kazakh language characters.
Data and Methods
All the data is stored as images for separate classes, which are located at specific directory. In Kazakh language there are 42 characters, therefore all the directories are numbered from 0 to 41. Also train and validation data are separated. Directories have this structure
Each directory from train-dir includes approximately 245 images for training, and from val-dir includes 105 images for validation. I should mention that all data has been grayscaled, hence they have 1 color depth and they take less space in disk. Dataset is generated using ‘ImageDataGenerator’ to generate train and validation datasets to fit the ML model [2].
Here is some examples of the data:
ML model is CNN with three convolutional layers with filters 32, 64 and 128 and max pooling, also it includes two hidden dense layers with filters 64 and 128 with ‘relu’ activation function, and at last dense layer with filter 42 and activation function ‘softmax’. I trained the model in 5 epochs due to the avoid overfitting and eventual loss and accuracy turned out fine.

Results
After fitting the model summary output is below:
2606/2606 [==============================] - 15s 5ms/step - loss: 2.6505 - accuracy: 0.2483 - val_loss: 1.6725 - val_accuracy: 0.4949
Epoch 2/5
2606/2606 [==============================] - 13s 5ms/step - loss: 1.2190 - accuracy: 0.6281 - val_loss: 1.0411 - val_accuracy: 0.6834
Epoch 3/5
  
 2606/2606 [==============================] - 14s 5ms/step - loss: 0.7744 - accuracy: 0.7651 - val_loss: 0.7581 - val_accuracy: 0.7758
Epoch 4/5
2606/2606 [==============================] - 14s 6ms/step - loss: 0.5704 - accuracy: 0.8237 - val_loss: 0.6300 - val_accuracy: 0.8049
Epoch 5/5
2606/2606 [==============================] - 14s 5ms/step - loss: 0.4635 - accuracy: 0.8600 - val_loss: 0.6021 - val_accuracy: 0.8318

Discussion
As given in the graph above there is no overfitting or underfitting which is a good sign for training the model. Also I want to mention that loss and accuracy could be better if the dataset will be large enough. Because for every character there were only about 245 images which is fine for small datasets, but if the dataset was twice bigger the results would be much better.
Front-end is a telegram bot which takes a single photo from the user and preprocesses the image before sending it to the model. First of all the image is grayscaled, then the size is changed to 32x32, only after this preparation it goes to preprocessing which makes a numpy array and expands the shape. Only after all the preprocessing does it go to the model and make the prediction. After that prediction is sent to the user.
    
 Conclusion
All in all, the final project has reached its goal. ML model recognizes Kazakh language characters with 83 percent accuracy and 0.6 loss which has average size of training dataset. Personally, the final project was challenging but on the other hand more interesting and striking. Also the opportunity for extension is large, and I will try to improve the dataset with more images, handling errors and increasing accuracy.
References
[1] https://data-flair.training/blogs/handwritten-character-recognition-neural-network/
[2] https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/first_edition/5. 2-using-convnets-with-small-datasets.ipynb
   
