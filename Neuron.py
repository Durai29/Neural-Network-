import numpy as np

#inputs = [1,2,3,2.5]
inputs = [[1.0,2.0,3.0,2.5],    # Batch inputs
          [2.0,5.0,-1.0,2.0],
          [-1.5,2.7,3.3,-0.8]]

weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

weights2 = [[0.1,-0.14,0.5],
            [-0.5,0.12,-0.33],
            [-0.44,0.73,-0.13]]
biases2 = [-1,2,-0.5]

layer1_outputs = np.dot(np.array(inputs),np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs,np.array(weights2).T) + biases2

#for bias, layer_weights in zip(biases,weights):
#    sum_outputs = 0
#    for weight, input in zip(layer_weights, inputs):
#        sum_outputs += weight*input
#    sum_outputs += bias
#    layer_outputs.append(sum_outputs)

print(layer2_outputs)