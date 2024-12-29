
# Algorithn conceuved while a patient at Byron Bay Hospital Tuckeroo

# Charles Thomas Wallace Truscott

# Byron Bay NSW 2481

# I love you Dad Mark William

# Thank you so much Guttag and Grumson and all at MITx

# Work in progress
class RubiksState(object):
    def __init__(self, tlf, blf, trf, brf, tlb, blb, trb, brb, moves):
        self.tlf = tlf
        self.blf = blf
        self.trf = trf
        self.brf = brf
        self.tlb = tlb
        self.blb = blb
        self.trb = trb
        self.brb = brb
        
        self.left_face = [self.tlb[1], self.tlf[1], self.blb[1], self.blf[1]]
        self.right_face = [self.trf[1], self.trb[1], self.brf[1], self.brb[1]]
        self.front_face = [self.tlf[2], self.trf[2], self.blf[2], self.brf[2]]
        self.back_face = [self.trb[2], self.tlb[2], self.brb[2], self.blb[2]]
        self.up_face  = [self.tlb[0], self.trb[0], self.tlf[0], self.trf[0]]
        self.down_face = [self.blf[0], self.brf[0], self.blb[0], self.brb[0]]
        self.orientation = [self.front_face, self.left_face, self.right_face, self.back_face, self.up_face, self.down_face]
        print("Front face: {}".format(self.front_face))
        print("Left Face: {}".format(self.left_face))
        print("Right Face: {}".format(self.right_face))
        print("Back Face: {}".format(self.back_face))
        print("Up face: {}".format(self.up_face))
        print("Down face:{}".format(self.down_face))
        self.moves = moves
    def L(self):
        """ TLF to TLB, TLB to BLB, BLB to BLF, BLF to TLF """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        ntlf[0], ntlf[1], ntlf[2] = tblf[2], tblf[1], tblf[0]
        nblf[0], nblf[1], nblf[2] = tblb[2], tblb[1], tblb[0]
        ntlb[0], ntlb[1], ntlb[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def L2(self):
        """ TLF to BLB, BLB to TLF, TLB to BLF, BLF to TLB """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        nblb[0], nblb[1], nblb[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = tblb[0], tblb[1], tblb[2]
        nblf[0], nblf[1], nblf[2] = ttlb[0], ttlb[1], ttlb[2]
        ntlb[0], ntlb[1], ntlb[2] = tblf[0], tblf[1], tblf[2]
        moves = self.moves.copy()
        moves.append('L2')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        return n
    def Linv(self):
        """ TLF to BLF, BLF to BLB, BLB to TLB, TLB to TLF """
        
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        nblf[0], nblf[1], nblf[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = tblf[2], tblf[1], tblf[0]
        ntlb[0], ntlb[1], ntlb[2] = tblb[2], tblb[1], tblb[0]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L inverse')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
        
        pass
    def R(self):
        """ TRF to TRB, TRB to BRB, BRB to BRF, BRF to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ntrb[2], ntrb[1], ntrb[0] = ttrf[0], ttrf[1], ttrf[2]
        nbrb[2], nbrb[1], nbrb[0] = ttrb[0], ttrb[1], ttrb[2]
        nbrf[2], nbrf[1], nbrf[0] = tbrb[0], tbrb[1], tbrb[2]
        ntrf[2], ntrf[1], ntrf[0] = tbrf[0], tbrf[1], tbrf[2]
        moves = self.moves.copy()
        moves.append('R')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def R2(self):
        """ TRF to BRB, BRB to TRF, BRF to TRB, TRB to BRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrb[0], nbrb[1], nbrb[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = tbrb[0], tbrb[1], tbrb[2]
        ntrb[0], ntrb[1], ntrb[2] = tbrf[0], tbrf[1], tbrf[2]
        nbrf[0], nbrf[1], nbrf[2] = ttrb[0], ttrb[1], ttrb[2]
        moves = self.moves.copy()
        moves.append('R2')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Rinv(self):
        """ TRF to BRF, BRF to BRB, BRB to TRB, TRB to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrf[0], nbrf[1], nbrf[2] = ttrf[2], ttrf[1], ttrf[0]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[2], tbrf[1], tbrf[0]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[2], tbrb[1], tbrb[0]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[2], ttrb[1], ttrb[0]
        moves = self.moves.copy()
        moves.append('R inverse')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
# From here below
    def U(self):
        """ TLF to TRF, TRF to TRB, TRB to TLB, TLB to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntrf[0], ntrf[1], ntrf[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttrf[0], ttrf[2], ttrf[1]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[0], ttlb[2], ttlb[1]
        moves = self.moves.copy()
        moves.append('U')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    def U2(self):
        """ TLF to TRB, TRB to TLF, TRF to TLB, TLB to TRF """
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ntrb[0], ntrb[1], ntrb[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = ttrb[0], ttrb[1], ttrb[2]
        ntlb[0], ntlb[1], ntlb[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = ttlb[0], ttlb[1], ttlb[2]
        moves = self.moves.copy()
        moves.append('U2')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    def Uinv(self):
        """ TLF to TLB, TLB to TRB, TRB to TRF, TRF to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntlb[0], ntlb[1], ntlb[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttlb[0], ttlb[2], ttlb[1]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[0], ttrf[2], ttrf[1]
        moves = self.moves.copy()
        moves.append('U inverse')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    
    def D(self):
        """ BLF to BRF, BRF to BRB, BRB to BLB, BLB to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nbrf[0], nbrf[1], nbrf[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[0], tbrf[2], tbrf[1]
        nblb[0], nblb[1], nblb[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tblb[0], tblb[2], tblb[1]
        moves = self.moves.copy()
        moves.append('D')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def D2(self):
        """ BLF to BRB, BRB to BLF, BRF to BLB, BLB to BRF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nbrb[0], nbrb[1], nbrb[2] = tblf[0], tblf[1], tblf[2]
        nblf[0], nblf[1], nblf[2] = tbrb[0], tbrb[1], tbrb[2]
        nblb[0], nblb[1], nblb[2] = tbrf[0], tbrf[1], tbrf[2]
        nbrf[0], nbrf[1], nbrf[2] = tblb[0], tblb[1], tblb[2]
        moves = self.moves.copy()
        moves.append('D2')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Dinv(self):
        """ BLF to BLB, BLB to BRB, BRB to BRF, BRF to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nblb[0], nblb[1], nblb[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tblb[0], tblb[2], tblb[1]
        nbrf[0], nbrf[1], nbrf[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tbrf[0], tbrf[2], tbrf[1]
        moves = self.moves.copy()
        moves.append('D inverse')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
# From here
    def F(self):
        """ TLF to BLF, BLF to BRF, BRF to TRF, TRF to TLF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        nblf[0], nblf[1], nblf[2] = ttlf[1], ttlf[0], ttlf[2]
        nbrf[0], nbrf[1], nbrf[2] = tblf[1], tblf[0], tblf[2]
        ntrf[0], ntrf[1], ntrf[2] = tbrf[1], tbrf[0], tbrf[2]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[1], ttrf[0], ttrf[2]
        moves = self.moves.copy()
        moves.append('F')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def F2(self):
        """ TLF to BRF, BRF to TLF, TRF to BLF, BLF to TRF """
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrf[0], nbrf[1], nbrf[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = tbrf[0], tbrf[1], tbrf[2]
        nblf[0], nblf[1], nblf[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = tblf[0], tblf[1], tblf[2]
        moves = self.moves.copy()
        moves.append('F2')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Finv(self):
        """ TLF to TRF, TRF to BRF, BRF to BLF, BLF to TLF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        ntrf[0], ntrf[1], ntrf[2] = ttlf[1], ttlf[0], ttlf[2]
        nbrf[0], nbrf[1], nbrf[2] = ttrf[1], ttrf[0], ttrf[2]
        nblf[0], nblf[1], nblf[2] = tbrf[1], tbrf[0], tbrf[2]
        ntlf[0], ntlf[1], ntlf[2] = tblf[1], tblf[0], tblf[2]
        moves = self.moves.copy()
        moves.append('F inverse')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def B(self):
        """ TLB to BLB, BLB to BRB, BRB to TRB, TRB to TLB """
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        nblb[0], nblb[1], nblb[2] = ttlb[1], ttlb[0], ttlb[2]
        nbrb[0], nbrb[1], nbrb[2] = tblb[1], tblb[0], tblb[2]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[1], tbrb[0], tbrb[2]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[1], ttrb[0], ttrb[2]
        moves = self.moves.copy()
        moves.append('B')
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def B2(self):
        """ TLB to BRB, BRB to TLB, TRB to BLB, BLB to TRB """
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrb[0], nbrb[1], nbrb[2] = ttlb[0], ttlb[1], ttlb[2]
        ntlb[0], ntlb[1], ntlb[2] = tbrb[0], tbrb[1], tbrb[2]
        nblb[0], nblb[1], nblb[2] = ttrb[0], ttrb[1], ttrb[2]
        ntrb[0], ntrb[1], ntrb[2] = tblb[0], tblb[1], tblb[2]
        moves = self.moves.copy()
        moves.append('B2')
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Binv(self):
        """ BLB to TLB, TLB to TRB, TRB to BRB, BRB to BLB"""
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        ntlb[1], ntlb[0], ntlb[2] = tblb[0], tblb[1], tblb[2] 
        ntrb[1], ntrb[0], ntrb[2] = ttlb[0], ttlb[1], ttlb[2]
        nbrb[1], nbrb[0], nbrb[2] = ttrb[0], ttrb[1], ttrb[2]
        nblb[1], nblb[0], nblb[2] = tbrb[0], tbrb[1], tbrb[2]

        moves = self.moves.copy()
        moves.append("B inverse")
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def is_solved(self):
        if self.blb == ['Y', 'O', 'B'] and self.tlb == ['W', 'O', 'B'] and self.brb == ['Y', 'R', 'B'] and self.trb == ['W', 'R', 'B'] and self.blf == ['Y', 'O', 'G'] and self.tlf == ['W', 'O', 'G'] and self.brf == ['Y', 'R', 'G'] and self.trf == ['W', 'R', 'G']:
            print('Solved: {}'.format(self.moves))
#            exit(1)
        if self.front_face == ['G', 'G', 'G', 'G'] and self.back_face == ['B', 'B', 'B', 'B'] and self.left_face == ['O', 'O', 'O', 'O'] and self.right_face == ['R', 'R', 'R', 'R'] and self.up_face == ['W', 'W', 'W', 'W'] and self.down_face == ['Y', 'Y', 'Y', 'Y']:
            return True
        else:
            return False
from queue import deque
import sys

def EncodeToMove(e, State):
	if e >> 18 == 1:
		print("B inverse")
		T = State.Binv()
		return T
	elif e >> 17 == 1:
		print("B2")
		T = State.B2()
		return T
	elif e >> 16 == 1:
		print("B")
		T = State.B()
		return T
	elif e >> 15 == 1:
		print("F inverse")
		T = State.Finv()
		return T
	elif e >> 14 == 1:
		print("F2")
		T = State.F2()
		return T
	elif e >> 13 == 1:
		print("F")
		T = State.F()
		return T
	elif e >> 12 == 1:
		print("D inverse")
		T = State.Dinv()
		return T
	elif e >> 11 == 1:
		print("D2")
		T = State.D2()
		return T
	elif e >> 10 == 1:
		print("D")
		T = State.D()
		return T
	elif e >> 9 == 1:
		print("U inverse")
		T = State.Uinv()
		return T
	elif e >> 8 == 1:
		print("U2")
		T = State.U2()
		return T
	elif e >> 7 == 1:
		print("U")
		T = State.U()
		return T
	elif e >> 6 == 1:
		print("R inverse")
		T = State.Rinv()
		return T
	elif e >> 5 == 1:
		print("R2")
		T = State.R2()
		return T
	elif e >> 4 == 1:
		print("R")
		T = State.R()
		return T
	elif e >> 3 == 1:
		print("L inverse")
		T = State.Linv()
		return T
	elif e >> 2 == 1:
		print("L2")
		T = State.L2()
		return T
	elif e >> 1 == 1:
		print("L")
		T = State.L()
		return T
	else:
		return State
def divconq(n, m, L):

	while m < len(L):
		print(L[n:m])
		n += 18
		m += 18
		
def Charles():
	s = 2 ** 18 + 1
#	rep = ""
	rep = []
	res = []
#	res = ""
	n = 0
	while n <= 18:
#		print(str(bin(2 **n)[2:]))
#		print(",")
#
		rep.append(2 ** n)
#		rep += str(bin(2 ** n)[2:])
#		rep += str(bin(2 ** n))
#		rep += ','
#		if n <= 17:
#			rep += ","
		n += 1
	n = 0
	while n <= 18 ** 2:
		res.append(rep)
		n += 18
#	while n <= 18:
#		print(str(bin(s)))
#		rep += str(bin(s))
#		res += str(bin(s))
#		s >>= 1
#		n += 1
#	print("Initial: {}".format(rep))
#	print("Consequentual: {}".format(res))
#	res = res.split(",")
#	print(res[0:17])
#	print(res[18: 2 * 18])
#	print(res[2 * 18: 3 * 18])
#	print("Charles Truscott Watters")
#	print("Trying divide and conquer trees")
#	print("I love you Tai, I love you Mark")
	State= RubiksState(["W", "O", "G"], ["Y", "O", "G"],  ["W", "R", "G"], ["O", "B", "Y"], ["W", "O", "B"], ["G", "Y", "R"], ["W", "R", "B"], ["Y", "R", "B"], [])
#	for e in res:
#		for m in e:
			
			
	s = State
	q = deque([])
	q.append(State)
	print(q)
	n = int.from_bytes(b'100000000000000000')
	while n >= 0:
#		print(n)
		d = EncodeToMove(n, State)
		print(d.moves)
		print(bin(n))
		print("\n'")
		n >>= 1
		if n <= 0:
			break
#	State = q.popleft()
#	for e in rep: 
#		print(State.moves)
#		q.append(EncodeToMove(e, State))
#	for elem in q:
#		print(elem, elem.moves)
#		n >>= 1
#		for l in res:
#			for e in l:
#				ct = EncodeToMove(e, State)
#				q.append(ct)
#				if ct.is_solved() == True:
#					solved = True
#	solved = False
#	while solved != True:
#		t = q.popleft()
#		for m in res:
#			for e in m:
#				q.append(EncodeToMove(e, t))
#		if t.is_solved() == True:
#			solved = True
Charles()