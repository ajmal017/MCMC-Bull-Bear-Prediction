def Prob_In_x_Days(Bull_Bear,x,Transition_Matrix):
	import numpy as np 
	from scipy import linalg

	A = np.linalg.matrix_power(Transition_Matrix,x)
	
	if Bull_Bear==0: 
		Mkt_Direction_Today=np.mat([0,1,0])
	elif Bull_Bear>0:
		Mkt_Direction_Today=np.mat([1,0,0])
	elif Bull_Bear<0:
		Mkt_Direction_Today=np.mat([0,0,1])
	
	return np.dot(Mkt_Direction_Today,A)



if __name__ == '__main__':
	import numpy as np 
	from scipy import linalg

	Transition_Matrix= np.mat([[.9,.075,.025], [.15,.8,.05],[.25,.25,.5]])

	p = Prob_In_x_Days(0.3,3,Transition_Matrix)
	print(p)
