


from __future__ import division
import neuro
import sys
import numpy as np

#gets rgb data from neurotain.csv file, the training set
data=open("neurotrain.csv")
data= data.read()
data= data.split("\n")
for i in range(0, len(data)):
    if len(data[i]) == 0:
            del(data[i])
            continue
    data[i]= data[i].split(",")
    data[i][0]= float(data[i][0])
    data[i][1]= float(data[i][1])
    data[i][2]= float(data[i][2])
    data[i][3]= float(data[i][3])
    
#splits the data by columns so that rgb will be inputs and the last value is the desired targets
red, green, blue, targets =  zip(*data)
inputs= zip(red, green, blue)
inputs= list(inputs)
targets= list(targets)
#this loop makes the targets list a list of lists to fit what the neuro network is expecting
#also the input values are divided by 255 to fit the 0 to 1 scale the neuro network is expecting
for i in range(0, len(inputs)):
    inputs[i] = list(inputs[i])
    targets[i]= [targets[i]]
    inputs[i][0]= inputs[i][0]/255
    inputs[i][1]=inputs[i][1]/255
    inputs[i][2]=inputs[i][2]/255

#print(targets)
#number of repetitions to train the network
reps=7500
print "Blue-Predictor Neural Network "
val_r=raw_input("\tEnter red value: ")
val_g=raw_input("\tEnter green value: ")
val_b=raw_input("\tEnter blue value: ")
#converts user input to float and I kept seperate values for each, one to push through neuro network and on for printing
val_r=float(val_r)
val_red= val_r/255
val_g=float(val_g)
val_green= val_g/255
val_b= float(val_b)
val_blue = val_b/255
#print(val_red, val_green, val_blue)

network=[] #makes an empty list to contain the neural net
#sets up the network to accommodate the size of your inputs
network=neuro.setup_network(inputs)
#trains the network for some number of repetitions on your
#training input and targets
neuro.train(network, inputs, targets, reps)
#your input to the neural network has to be in the form of
#a list of input values
test_input=[val_red, val_green, val_blue]
#predicts the outcome based on the input
pred=neuro.predict(network, test_input)
#the predicted blueness of the rgb entered 
pred=np.round(pred)
#prints the input and output of predicted blueness
print "The network thinks red value",int(val_r),"&& green value",int(val_g),"&& blue value",int(val_b),"is",
if(int(pred)==1):
    print "a blue color"
else:
    print "not a blue color"

