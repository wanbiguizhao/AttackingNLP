import torch 
from d2l import torch as d2l 

def show_relu():
    x=torch.arange(-8.0,8.0,0.1,requires_grad=True)
    y=torch.relu(x)
    d2l.plot(x.detach(),y.detach(),"X","relu(x)",figsize=(5,2.5))
    y.backward(torch.ones_like(x),retain_graph=True)
    d2l.plot(x.detach(),x.grad,'x','grad of relu',figsize=(5,2.5))

def showSigmoid():
    x=torch.arange(-8.0,8.0,0.1,requires_grad=True)
    y=torch.sigmoid(x)
    print(x.grad)
    d2l.plot(x.detach(), y.detach(), 'x', 'sigmoid(x)', figsize=(5, 2.5))
    #x.grad.data.zero_()
    x.grad.data.zero_()
    y.backward(torch.ones_like(x),retain_graph=True)
    x.grad.data.zero_()
    d2l.plot(x.detach(),x.grad,'x','grad of sigmoid',figsize=(5,2.5))
    print(x,x.grad)
if __name__=="__main__":
    #show_relu()
    showSigmoid()