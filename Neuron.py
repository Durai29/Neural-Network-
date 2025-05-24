import numpy as np

inputs = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

layer_outputs = np.dot(weights,inputs) + biases

#for bias, layer_weights in zip(biases,weights):
#    sum_outputs = 0
#    for weight, input in zip(layer_weights, inputs):
#        sum_outputs += weight*input
#    sum_outputs += bias
#    layer_outputs.append(sum_outputs)

print(layer_outputs)
