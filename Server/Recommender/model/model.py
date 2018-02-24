import torch
from torch.autograd import Variable
import torch.nn as nn
import numpy as np

class CBOW(torch.nn.Module):
    def __init__(self, vocab, embedding_dimension):
        super(CBOW, self).__init__()

        self.embeddings = nn.Embedding(vocab, embedding_dimension)
        self.model = nn.Sequential(nn.Linear(embedding_dimension, 150),
                                   nn.ReLU(),
                                   nn.Linear(150, embedding_dimension),
                                   nn.LogSoftmax)

    def forward(self, input):
        embedding = sum(self.embeddings(input)).view(1,-1)
        out = self.model(embedding)
        return out

    def get_embed(self, words, word):
        word = Variable(torch.LongTensor(words[word]))
        return self.embeddings(word).view(1,-1)





