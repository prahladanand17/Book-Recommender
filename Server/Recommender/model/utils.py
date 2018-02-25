import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
from Server.Recommender.model import *


def get_context_data(text):
    data = []
    for i in range(3, len(text)-3):
        context = [text[i-3], text[i-2],
                   text[i-1], text[i+1],
                   text[i+2], text[i+3]]
        target = text[i]
        data.append((context, target))

        return data, context, target



def train(model, data, loss_function, optimizer, num_iter, context, target, word_to_ix):
    for i in range(num_iter):
        total_loss = 0
        for context, target in data:
            context_vec = [word_to_ix[w] for w in context]
            context_var = Variable(torch.LongTensor(context_vec))
            model.zero_grad()
            prob = model(context_var)
            loss = loss_function(prob, torch.max(target, 1)[1])
            loss.backward()
            optimizer.step()
            total_loss += loss.data





