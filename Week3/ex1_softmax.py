import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        return torch.exp(x)/torch.exp(x).sum()
    

class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        return torch.exp(x - torch.max(x).item())/torch.exp(x - torch.max(x).item()).sum()
    

if __name__ == "__main__":
    data = torch . Tensor ([1 , 2 , 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)
    stable_softmax = StableSoftmax()
    output = stable_softmax(data)
    print(output)