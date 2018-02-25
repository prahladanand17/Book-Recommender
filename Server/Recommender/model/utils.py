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



def train(model, data, loss_function, optimizer, num_iter, word_to_ix):
    for i in range(num_iter):
        total_loss = 0
        for context, target in data:
            context_vec = [word_to_ix[w] for w in context]
            context_var = Variable(torch.LongTensor(context_vec))
            target_vec = [word_to_ix[target]]
            target_var = Variable(torch.LongTensor(target_vec))
            model.zero_grad()
            prob = model(context_var)
            loss = loss_function(prob, target_var)
            loss.backward()
            optimizer.step()
            total_loss += loss.data





