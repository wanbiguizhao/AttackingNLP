import torch 
from d2l import torch as d2l 

def show_relu():
    x=torch.arange(-8.0,8.0,0.1,requires_grad=True)
    y=torch.relu(x)
    d2l.plot(x.detach(),y.detach(),"X","relu(x)",figsize=(5,2.5))

if __name__=="__main__":
    show_relu()