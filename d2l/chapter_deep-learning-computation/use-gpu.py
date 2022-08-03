import torch
from torch import nn

print(torch.device('cpu'), torch.device('cuda'), torch.device('cuda:1'))
print(torch.cuda.device_count())

x = torch.tensor([1, 2, 3])
x.device
print(x.device)

def try_gpu(i=0):  #@save
    """如果存在，则返回gpu(i)，否则返回cpu()"""
    if torch.cuda.device_count() >= i + 1:
        return torch.device(f'cuda:{i}')
    return torch.device('cpu')
X = torch.ones(2, 3, device=try_gpu())
print(X)
