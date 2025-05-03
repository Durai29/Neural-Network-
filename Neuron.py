inputs = [1,2,3,2.5]
weights = [[2.3,1.2,3.3,4.2],
           [0.3,2.1,3.4,4.1],
           [3.1,3.2,2.4,5.2]]
biases = [2.1,2.4,3.5]
output =[ inputs[0]*weights[0][0]+ inputs[1]*weights[0][1]+ inputs[2]*weights[0][2]+ inputs[3]*weights[0][3]+ biases[0],
          inputs[0]*weights[1][0]+ inputs[1]*weights[1][1]+ inputs[2]*weights[1][2]+ inputs[3]*weights[1][3]+ biases[1],
          inputs[0]*weights[2][0]+ inputs[1]*weights[2][1]+ inputs[2]*weights[2][2]+ inputs[3]*weights[2][3]+ biases[2]]
print(output)


