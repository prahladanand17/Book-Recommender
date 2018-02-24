import torch
import torch.nn as nn
import numpy as np
from Server.Recommender.model import *

def get_context(context, words):
    for k in context:
        indices = words[k]
    tensor = torch.LongTensor(indices)
    return Variable(tensor)

def get_context_data(text):
    data = []
    for i in range(3, len(text)-3):
        context = [text[i-3], text[i-2],
                   text[i-1], text[i+1],
                   text[i+2], text[i+3]]
        target = text[i]
        data.append(context, target)

    return data, context, target



def train(model, data, loss_function, optimizer, num_iter, context, target, words):
    for i in range(num_iter):
        total_loss = 0
        for context, target in data:
            context_vec = get_context(context, words)
            model.zero_grad()
            prob = model(context_vec)
            loss = loss_function(prob, Variable(torch.LongTensor(words[target])))
            loss.backward()
            optimizer.step()
            total_loss += loss.data





