import  numpy as np
from sklearn.model_selection import GridSearchCV

def simulateData(pi :float,p:float,q:float,n):
    """
    three coin experiment
    coin 0 pi is head 1-pi is tail  
    coin 1 p
    coin 2 q
    n times round
    one round  toss coin 0 if head toss coin 1 else coin 2  and record coin x head or tail 
    repeat n
    Args:
        pi (float): _description_
        p (float): _description_
        q (float): _description_
        n (int ): _description_
    """
    def bernoulli(px):
        """
        px in [0,1.0)
        random float x in [0,1.0)
        if x<px return 1 
        else return 0

        Args:
            px (_type_): _description_
        """
        x=np.random.uniform(0,1)
        if x<px:
            return 1
        return 0
    ans=[]
    for i in range(n):
        if bernoulli(pi)==1:
            ans.append(bernoulli(p))
        else:
            ans.append(bernoulli(q))
    return ans 
    # 均匀分布
def calculate_y_i_from_coin1_p(y_i,pi,p,q):
    #print(pi,p,q)
    # 计算观察的结果，是来源于y_i的地方
    return (pi*p**y_i*(1-p)**(1-y_i))/(pi*p**y_i*(1-p)**(1-y_i)+(1-pi)*q**y_i*(1-q)**(1-y_i) )
    # if y_i==1:
    #     return pi*p/(pi*p+(1-pi)*q)
    # return pi*(1-p)/(pi*(1-p)+(1-pi)*(1-q))
def em(y_list:list,pi=0.5,p=0.5,q=0.5):
    sum_head=sum(y_list)
    data_len=len(y_list)
    i=0
    while True:
        ui_list= [calculate_y_i_from_coin1_p(yi,pi,p,q)  for yi in y_list ]
        pi_iter=sum(ui_list)/data_len
        p_iter=sum([ y_list[index]*ui_list[index] for index in range(data_len)])/sum(ui_list)
        q_iter=sum([ y_list[index]*(1-ui_list[index]) for index in range(data_len)])/(data_len - sum(ui_list))
        if np.linalg.norm([pi_iter-pi,p_iter-p,q_iter-q],ord=2)<(1e-10)/data_len or i>data_len*10:
            return [pi_iter,p_iter,q_iter]
        pi,p,q=pi_iter,p_iter,q_iter
        i+=1
        print(i)
        
def test_case():
    origin_pi=0.5
    origin_p=0.6
    origin_q=0.5
    case_ans=simulateData(origin_pi,origin_p,origin_q,20000)
    print("\n",sum(case_ans)/len(case_ans),1-sum(case_ans)/len(case_ans))
    origin_ui_list=[calculate_y_i_from_coin1_p(yi,origin_pi,origin_p,origin_q)  for yi in case_ans]
    calculate_pi,calculate_p,calculate_q=em(case_ans,0.5,0.9,0.1)
    print(calculate_pi,calculate_p,calculate_q)
    
    calculate_ui_list=[calculate_y_i_from_coin1_p(yi,calculate_pi,calculate_p,calculate_q)  for yi in case_ans]
    print(np.linalg.norm(np.array(calculate_ui_list)-np.array(origin_ui_list),ord=2),np.mean(np.array(calculate_ui_list)-np.array(origin_ui_list)))

    # 使用网格搜索遍历参数,以后再尝试吧
    param_grid = [

    ]
    # todo 使用机器学习进行训练，然后看看能否找到参数。猜测是不行的，需要使用序列模型才可以的。
    # 
    # em 的结果并不一定准确


if __name__=="__main__":
    print("hello")
    # case_ans=simulateData(0.5,0.5,0.5,1000)
    # original=[]
    # print(case_ans,sum(case_ans)/len(case_ans),1-sum(case_ans)/len(case_ans))
    # print(em(case_ans,0.2,0.8,0.01))
    test_case()