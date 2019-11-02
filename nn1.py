# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:59:14 2015

@author: nitin
"""
import math
import random
BIAS = -1
class Neuron:
    def __init__(self,n_inputs):
        self.n_inputs = n_inputs
        self.set_weights([random.uniform(0,1) for x in range(0,n_inputs +1)])

    def sum(self,inputs):
        return sum(val * self.weights[i] for i, val in enumerate(inputs))
        
    def set_weights(self,weights):
        self.weights = weights
    
    def __str__(self):
        return  'Weights : %s, Bias : %s' %(str(self.weights[:-1]),str(self.weights[-1]))
        
class NeuronLayer:
    def __init__(self,neurons,n_inputs):
        self.n_neurons = n_neurons
        self.neurons = [Neuron(n_inputs) for _ in range (0, self.n_neurons)]
        
    def __str__(self):
        return 'Layer:\n\t'+'\n\t'.join([str(neuron) for neuron in self.neurons])+''
        
class NeuralNetwork:
    def __init__(self, n_inputs, n_outputs, n_neurons_to_hl, n_hidden_layers):
        self.n_inputs = n_inputs
        self.n_outputs =n_outputs
        self.n_hidden_layers = n_hidden_layers
        self.n_neurons_to_hl = n_neurons_to_hl
        self._create_network()
        sefl._n_weights = None
    
    def _create_network(self):
        if self.n_hidden_layers>0:
            self.layers = [NeuronLayer(self.n_neurons_to_hl
            ,self.n_inputs)]

            self.layers += [NeuronLayer(self.n_neurons_to_hl,self.n_neurons_to_hl) for _ in range (0,self.n_hidden_layers)]
            self.layers += [NeuronLayer(self.n_outputs,self.n_neurons_to_hl)]
        else:
            self.layers =[NeuronLayer(self.n_outputs, self.n_inputs)]
            
    def get_weight(self):
        weights =[]
        for layer in self.layers:
            for neuron in layer.neurons:
                weights += neuron.weights
        return weights
    
    def n_weights(self):
        if not self._n_weights:
            self._n_weights = 0
            for layer in self.layers:
                for neuron in self.neurons:
                    self._n_weights += neuron.n_inputs+1
        return self._n_weights
        
    def set_weights(self, weights):
        assert len(weights) == self.n_weights,"Incorrect amount of weights."
        stop =0
        for layer in self.layers:
            for neuron in layer.neurons:
                start,stop = stop, stop + (neuron.n_inputs +1)
                neuron.set_weights(weights[start:stop])
        return self
        
    def update(self, inputs):
        assert len(inputs) == self.n_inputs, "incorrect amount of inputs"
        for layer in self.layers:
            output = []
            for neuron in layer.neurons:
                tot = neuron.sum(inputs) + neuron.weights[-1]*BIAS
                output.append(self.sigmoid(tot))
            inputs =outputs
        return outputs
        
    def sigmoid(self,activation,respponse =1):
        try:
            return 1/(1+math.e**(-activation/response))
        except OverflowError:
            return float("inf")
    def __str__(self):
        return '\n'.join([str(i+1)+''+str(layer) for i, layer in enumerate (self.layers)])