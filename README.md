# Gexa

Gexa as the name suggests converts hand gestures into Alexa voice commands.Hence people who cannot speak can just use their hand gestures to interact with  Alexa.

First Step :
Initially we took a hand gesture recognition dataset from kaggle and trained a convolutional neural networks model with one convolutional layer and 2 linear layers to classify the hand gesture into appropriate label.

Second Step:
In the next step, we used the trained model to convert the real time hand gestures from live feed (laptop camera) into appropriate alexa commands .The alexa commands will get triggered and played as audio whenever the model recognizes a new hand gesture from live feed.

So our Gexa takes Alexa one step closer to serving the people who cannot speak.

Example Hand Gesture

![alt text](https://github.com/Charan1010/Gexa/blob/master/hand_ges.png)
