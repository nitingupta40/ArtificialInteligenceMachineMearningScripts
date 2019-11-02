# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:51:02 2015

@author: nitin
"""

def SGD(self, training_data,  epochs, mini_batch_size, eta, test_data = None):
if test_data: n_test = len(test_data):
n = len(training_data)
for j in xrange(epochs):
    random.shuffle(training_data)
    mini_batches = [training_data[k:k+mini_batch_size]
        for k in xrange(0, n,mini_batch_size)]:
    for mini_batch in mini_batches:
        self.update_mini_batch(mini_batch, eta)
    if test_data:
        print "Epoch {0}:{1}c/c{2}".format(j, self.evaluate(test_data),n_test)
    else:
        print "Epoch {0} complete"..format(j)