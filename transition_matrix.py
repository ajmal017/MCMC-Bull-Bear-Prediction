import numpy as np 
from scipy import linalg
from tdadata import Hist_Data,Mkt_Direction_Today

def Transition_Matrix(close,months):
	
	#creates list of % change values
	p = []
	for i in range(len(close)-1):
		p.append(( (close[i+1]-close[i])/close[i])*100)

	#creates the transition matrix 
	tm = [[0,0,0],[0,0,0],[0,0,0]]
	bull_count=float(0)
	stagnant_count=float(0)
	bear_count=float(0)

	for i in range(1,len(close)-1):
		if p[i-1]>0.4:
			bull_count+=1
			if p[i]>0.4:
				tm[0][0]+=1
			elif p[i]<0.4 and p[i]>-0.4:
				tm[0][1]+=1
			else:
				tm[0][2]+=1
		elif p[i-1]<0.4 and p[i-1]>-0.4:
			stagnant_count+=1
			if p[i]>0.4:
				tm[1][0]+=1
			elif p[i]<0.4 and p[i]>-0.4:
				tm[1][1]+=1
			else:
				tm[1][2]+=1
		else:
			bear_count+=1
			if p[i]>0.4:
				tm[2][0]+=1
			elif p[i]<0.4 and p[i]>-0.4:
				tm[2][1]+=1
			else:
				tm[2][2]+=1

	for i in range(3):
		tm[0][i]=tm[0][i]/bull_count
		tm[1][i]=tm[1][i]/stagnant_count
		tm[2][i]=tm[2][i]/bear_count

	return np.mat(tm)
	

if __name__ == '__main__':
	close = Hist_Data(3)
	Transition_Matrix= Transition_Matrix(close,3)
	print(Transition_Matrix)
