import numpy as np 
from scipy import linalg
from tdadata import Hist_Data,Mkt_Direction_Today
from transition_matrix import Transition_Matrix
import random

def Prob_In_x_Days(Mkt_Direction_Today,x,Transition_Matrix):

	A = np.linalg.matrix_power(Transition_Matrix,x)

	if Mkt_Direction_Today>-0.4 and Mkt_Direction_Today<0.4: 
		mkt_dir=np.mat([0,1,0])
	elif Mkt_Direction_Today>0.4:
		mkt_dir=np.mat([1,0,0])
	elif Mkt_Direction_Today<-0.4:
		mkt_dir=np.mat([0,0,1])
	
	p = np.dot(mkt_dir,A).tolist()
	return p

def MCMC_Pred(reps,hist_months,pred_days):
	close = Hist_Data(hist_months)
	t= Transition_Matrix(close,hist_months)

	dists = []
	for i in range(1,pred_days):
		dists.append(Prob_In_x_Days(Mkt_Direction_Today(),i,t))

	sum=0
	for i in range(reps):
		sum+=MC_Estimation(dists)
	
	avg=float(sum)/reps
	print(avg)
	return avg

def MC_Estimation(dists):
	p = 0
	for d in dists:
		r=random.random()
		if r<d[0][0]:
			p-=0.75
		elif r>d[0][0] and r<(d[0][0]+d[0][1]):
			p+=random.uniform(-0.2,0.2)
		else:
			p+=0.4
	return p

if __name__ == '__main__':
	MCMC_Pred(1000,6,2)

