import torch
from torch import conv2d, nn,Tensor

def comp_conv2d(conv2d,X:Tensor):
    X=X.reshape((1,1)+X.shape)
    Y=conv2d(X)
    return Y.reshape(Y.shape[2:])

def padding():
    conv2d = nn.Conv2d(1,1,kernel_size=3,padding=1)
    X=torch.rand(size=(8,8))
    print(comp_conv2d(conv2d,X).shape)

if __name__=="__main__":
    #show_relu()
    padding()
    