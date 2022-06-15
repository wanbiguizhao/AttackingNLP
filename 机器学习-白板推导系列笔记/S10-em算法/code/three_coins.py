import  numpy as np

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

def em(y_list:list,pi=0.5,p=0.5,q=0.5):
    def calculate_y_i_from_coin1_p(y_i):
        print(pi,p,q)
        if y_i==1:
            return pi*p/(pi*p+(1-pi)*q)
        return pi*(1-p)/(pi*(1-p)+(1-pi)*(1-q))
         
    sum_head=sum(y_list)
    data_len=len(y_list)
    i=0
    while True:
        ui_list= [calculate_y_i_from_coin1_p(yi)  for yi in y_list ]
        pi_iter=sum(ui_list)/data_len
        p_iter=sum([ y_list[index]*ui_list[index] for index in range(data_len)])/sum(ui_list)
        q_iter=sum([ y_list[index]*(1-ui_list[index]) for index in range(data_len)])/(data_len - sum(ui_list))
        if np.linalg.norm([pi_iter-pi,p_iter-p,q_iter-q],ord=2)<0.00002:
            return [pi_iter,p_iter,q_iter]
        pi,p,q=pi_iter,p_iter,q_iter
        i+=1
        print(i)
        
    

if __name__=="__main__":
    print("hello")
    case_ans=simulateData(0.8,0.8,0.05,1000)
    print(case_ans,sum(case_ans)/len(case_ans),1-sum(case_ans)/len(case_ans))
    print(em(case_ans,0.2,0.8,0.01))