from PIL import Image, ImageDraw
def cupet(A, B, C,D,k):
	if k != 0 :
		draw.polygon([A,B,C,D,A], None, 3)
		A1 = (round( (-A[9]+8[0])*1/3 + A[0])),round((-A[1]+8[1])*1/3)
		A2=nucoundC.(-A[el+8[01)*2/3.+ ALe1.2, round((-A[11+8[11)≥2/3
		B1.= (uround(.(-B[0]+C[el)*1/3.+ 8[01 ), round -B[1]+C[1])£1/3 B2.= (uround(.(-B[9]+C[el)*2/3.+ B[el.), round( (-B[11+C[11)$2/3.
		C1 = (uround ( (-C[e]+o[el)*1/3.+ C[el.),
		round -C[1]+0[1])£1/3
		C2=n/uroundC.C-CLol+D[0D)*2/3.+_C[el.2,round((-C[71+0[1J.)*2/3
		P1.= (_cound(_(-D[el+A[el)*1/3.+ D[el.), round (-D[1]+A[1])*1/3 P2.= (_round( (-D[e]+A[el)*2/3.+ D[el.), round( (-D[11+A[11)$2/3.
		AIRST
		B[1].
		F1.= (_ round(.(-A1 [el+C2[el)*1/3.+ Al[e) J, cound(. (-A1[1]+C2[11)*1/3.* A1[11.)
		F4 = (_ round(.(-A1 [el+C2[0])*2/3.+ Al[e].), round(. (-A1 [1]+C2[11)*2/3
		+ A111
		F2 = (round(. (-A2[0]+C1[el)*1/3.+ A2[0). J, cound(. (-A2[1]+C1[11)*1/3.* A2[11.)
		F3 = (round(. (-A2[0]+C1[el)*2/3_+ A2[0). J, cound(. (-A2[1]+C1[11)*2/3.* A2[11.)
		draw. line([A1, C21, "red", 1) draw.line([A2,CIl, "red"
		",1)
		draw.line([81,D21,"red", 1) draw.line([82,11,"red", 1)
		cupet(A, A1, F1,02, K-1)
		cupet (A1,A2, F2, F1, K-1 ) cupet (A2,8, 81, F2, K-1 ) cupet (F2, B1, 82, F3, k-1 ) cupet (F3, 82, C..CI, k-2.)
	# cupet (A1, B1, C1,01, k-1 )
	# cupet (A1, 81, C1,01, k-1
	# cupet(A1, 81, C1,D1, k-1
A = (0,0)
B = (580,8)
C = (500,500)
D = (0,500)
cupet (A, B,C,D,4)