import torch 
from torch import Tensor,nn
# from d2l import torch as d2l 

def corr2d(X:Tensor,K:Tensor):
    """计算二维互相关运算 """
    h,w=K.shape 
    Y = torch.zeros( (X.shape[0]-h +1, X.shape[1]-w+1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i,j]=((X[i:i+h,j:j+w])*K).sum() 
    return Y 
class Conv2D(nn.Module):
    def __init__(self,kernel_size) -> None:
        super().__init__()
        self.weight = nn.parameter(torch.rand(kernel_size))
        self.bias = nn.parameter(torch.zeros(1))
    
    def forward(self,x):
        return corr2d(x,self.weight)+ self.bias

def test_corr2d():
    X=torch.rand(3,3)
    K=torch.tensor([[0.0, 1.0], [2.0, 3.0]])
    print(corr2d(X,K))

def test_01():
    X=torch.ones((6,8))
    X[:,2:6]=0
    print(X)
    K = torch.tensor([[1.0,-1.0]])
    Y=corr2d(X,K)
    print(Y)
    X[2:5,:]=0
    Y=corr2d(X,K)
    print(Y)    


if __name__=="__main__":
    #show_relu()
    test_corr2d()
    test_01()