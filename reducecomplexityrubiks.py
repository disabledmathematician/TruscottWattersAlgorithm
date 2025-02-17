# -*- coding: utf-8 -*-
"""
New paradigm Rubik's Cube Solving algorithm

Charles Thomas Wallace Truscott
(Computational Thinking with Python MITx, Using Python for Research Harvard T.H. Chan School of Medicine)

"If I had six hours to chop down a tree, I would spend the first four sharpening the axe" - Benjamin Franklin

Thank you so much Byron Central Hospital, John Flynn Private Hospital, Gold Coast University Hospital.

Very proud of my optimal, dynamic programming, matrix computation algorithm to solve the 2 x 2 Rubik's cube. 

Copyright Charles Truscott, 2024 December

Suffolk Park / Byron Bay, NSW 2481

I love you Tai, I love you Mark - beloved father. I love you Rodney.

Thank you so much United States Department of Defence, Offensive Security, MIT faculty.

I have been on the Centrelink Disability pension for 12 years because of Schizophrenia, and a brain injury, sleep disorder and memory disorder.

I recently walked into an employment agency and I was very tickled pink to put MITx and HarvardX on the resume.

I may get my dream tech career here in Byron Bay, but there is not circumstantially the industry locally to need to hire a full-wage programmer, data scientist or cybersecurity consultant.

I may be the only one in the nation or globally working on this problem on Christmas Eve 2024.

Very excited to return to society after forced disappearance.

Thank you General Michael Hayden CIA NSA ODNI

Thank you Carl Joseph Truscott former Assistant Director General of the United States Secret Service, BATF


"""

""" Efforts to store the states and moves of states in a key-value pair, such as a resizable 'Rubik's move' adjacency list """


import itertools
# n = RubiksState([], [], [], [], [], [], [], [])
# n = RubiksState(['W', 'O', 'G'], ['B', 'O', 'Y'], ['W', 'R', 'G'], ['O', 'Y', 'G'], ['W', 'O', 'B'], ['B', 'R', 'Y'], ['W', 'R', 'B'], ['R', 'Y', 'G'], [])
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
#        print("Front face: {}".format(self.front_face))
#        print("Left Face: {}".format(self.left_face))
#        print("Right Face: {}".format(self.right_face))
#        print("Back Face: {}".format(self.back_face))
#        print("Up face: {}".format(self.up_face))
#        print("Down face:{}".format(self.down_face))
        self.moves = moves
        if self.is_solved():
        	print("SOLVED: {}".format(self.moves))
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
def Charles():
    States = deque([])
#    n = RubiksState(['O', 'B', 'Y'], ['R', 'B', 'Y', ], ['O', 'G', 'Y'], ['R', 'G', 'Y'], ['O', 'B', 'W'], ['R', 'B', 'W'], ['O', 'G', 'W'], ['R', 'G', 'W'], [])
    all_states = [n for n in itertools.permutations([['G', 'G', 'G', 'G'], ['B', 'B', 'B', 'B'], ['O', 'O', 'O', 'O'], ['R', 'R', 'R', 'R'], ['W', 'W', 'W', 'W'], ['Y', 'Y', 'Y', 'Y']])]
    n = RubiksState(["W", "O", "G"], ["Y", "B", "O"],  ["O", "G", "Y"], ["W", "G", "R"], ["W", "B", "R"], ["Y", "B", "R"], ["Y", "R", "G"], ["Y", "W", "O"], [])
    initial_state = n.orientation
#    print(all_states)
#    sys.exit(1)
    #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
    moves = [lambda s: s.L(), lambda s: s.Linv(), lambda s: s.R(), lambda s: s.Rinv(), lambda s: s.U(), lambda s: s.Uinv(), lambda s: s.D(), lambda s: s.F(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.Binv()]
 #   moves = [lambda s: s.L(), lambda s: s.L2(), lambda s: s.Linv(), lambda s: s.R(), lambda s: s.R2(), lambda s: s.Rinv(), lambda s: s.U(), lambda s: s.U2(), lambda s: s.Uinv(), lambda s: s.D(), lambda s: s.D2(), lambda s: s.Dinv(), lambda s: s.F(), lambda s: s.F2(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.B2(), lambda s: s.Binv()]
    States.append(n)
    d = {}
    for move in moves:
    	d[move(States[0])] = []
  #  print(d)
    for k in d:
    	for move in moves:
	    	d[k].append(move(k))
#    print(d)
    for k in d:
    	print(d[k], k.moves)
    	for e in d[k]:
    		print(e.moves)
 #   c = 0
#    solved = False
#    print(States)
#    d = {}
#    for move in moves:
#        print(move(States[0]))
#        d[move] = move(States[0])
#    for move in moves:
#        States.append(move(States[0]))
#    print(States)
 #   print(d)
#    Trying a memoisation approach. 
#: s.F2(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.B2(), lambda s: s.Binv()]

#    States.append(n)

#    c = 0

#    solved = False
# 	   for k in d:
# 	   	print(k, d[k].orientation)
#	    	for move in moves:
#    			n = move(d[k])
#    			d[move] = n
#   	 	if d[k].is_solved() == True:
#    			print("Solved")
#    			break
 #   print(len(d))
  #  while solved != True:

#    Trying a memoisation approach. 

#    while solved != True:

#        state = States.popleft()

#        for move in moves:

#            t = move(state)

#            print(t.moves)

#            States.append(t)

#        if state.orientation in all_states:

#            solved = True

#            print("Initial State:\nFront Face: {}\nLeft Face: {}\nRight Face: {}\nBack Face: {}\nUp Face: {}\nDown Face:{}".format(n.front_face, n.left_face, n.right_face, n.back_face, n.up_face, n.down_face))

#            print("Solved State: Front Face: {}, Left Face: {}, Right Face:{} Back Face: {}, Up face: {}, Down face: {}\n".format(state.front_face, state.left_face, state.right_face, state.back_face, state.up_face, state.down_face))

#            print("********")

#            print("Moves: {}".format(state.moves))

#            print("*******")

#            print("Charles Truscott Watters, Byron Bay NSW 2481")

#        if state.is_solved() == True:

#            solved = True

#            print("Initial State:\nFront Face: {}\nLeft Face: {}\nRight Face: {}\nBack Face: {}\nUp Face: {}\nDown Face:{}".format(n.front_face, n.left_face, n.right_face, n.back_face, n.up_face, n.down_face))

#            print("Solved State: Front Face: {}, Left Face: {}, Right Face:{} Back Face: {}
Charles()

""" [<__main__.RubiksState object at 0x73135fc890>, <__main__.RubiksState object at 0x73135fcd10>, <__main__.RubiksState object at 0x73135fd190>, <__main__.RubiksState object at 0x73135fd610>, <__main__.RubiksState object at 0x73135fd990>, <__main__.RubiksState object at 0x73135fdd50>, <__main__.RubiksState object at 0x73135fe0d0>, <__main__.RubiksState object at 0x73135fe450>, <__main__.RubiksState object at 0x73135fe7d0>, <__main__.RubiksState object at 0x73135feb10>, <__main__.RubiksState object at 0x73135fee90>] ['L']
['L', 'L']
['L', 'L inverse']
['L', 'R']
['L', 'R inverse']
['L', 'U']
['L', 'U inverse']
['L', 'D']
['L', 'F']
['L', 'F inverse']
['L', 'B']
['L', 'B inverse']
[<__main__.RubiksState object at 0x73135ff310>, <__main__.RubiksState object at 0x73135ff790>, <__main__.RubiksState object at 0x73135ffc10>, <__main__.RubiksState object at 0x73136000d0>, <__main__.RubiksState object at 0x7313600450>, <__main__.RubiksState object at 0x7313600810>, <__main__.RubiksState object at 0x7313600b90>, <__main__.RubiksState object at 0x7313600f10>, <__main__.RubiksState object at 0x7313601290>, <__main__.RubiksState object at 0x73136015d0>, <__main__.RubiksState object at 0x7313601950>] ['L inverse']
['L inverse', 'L']
['L inverse', 'L inverse']
['L inverse', 'R']
['L inverse', 'R inverse']
['L inverse', 'U']
['L inverse', 'U inverse']
['L inverse', 'D']
['L inverse', 'F']
['L inverse', 'F inverse']
['L inverse', 'B']
['L inverse', 'B inverse']
[<__main__.RubiksState object at 0x7313601dd0>, <__main__.RubiksState object at 0x7313602250>, <__main__.RubiksState object at 0x73136026d0>, <__main__.RubiksState object at 0x7313602b50>, <__main__.RubiksState object at 0x7313602ed0>, <__main__.RubiksState object at 0x7313603290>, <__main__.RubiksState object at 0x7313603610>, <__main__.RubiksState object at 0x7313603990>, <__main__.RubiksState object at 0x7313603d10>, <__main__.RubiksState object at 0x7313608090>, <__main__.RubiksState object at 0x7313608410>] ['R']
['R', 'L']
['R', 'L inverse']
['R', 'R']
['R', 'R inverse']
['R', 'U']
['R', 'U inverse']
['R', 'D']
['R', 'F']
['R', 'F inverse']
['R', 'B']
['R', 'B inverse']
[<__main__.RubiksState object at 0x7313608890>, <__main__.RubiksState object at 0x7313608d10>, <__main__.RubiksState object at 0x7313609190>, <__main__.RubiksState object at 0x7313609610>, <__main__.RubiksState object at 0x7313609990>, <__main__.RubiksState object at 0x7313609d50>, <__main__.RubiksState object at 0x731360a0d0>, <__main__.RubiksState object at 0x731360a450>, <__main__.RubiksState object at 0x731360a7d0>, <__main__.RubiksState object at 0x731360ab10>, <__main__.RubiksState object at 0x731360ae90>] ['R inverse']
['R inverse', 'L']
['R inverse', 'L inverse']
['R inverse', 'R']
['R inverse', 'R inverse']
['R inverse', 'U']
['R inverse', 'U inverse']
['R inverse', 'D']
['R inverse', 'F']
['R inverse', 'F inverse']
['R inverse', 'B']
['R inverse', 'B inverse']
[<__main__.RubiksState object at 0x731360b310>, <__main__.RubiksState object at 0x731360b790>, <__main__.RubiksState object at 0x731360bc10>, <__main__.RubiksState object at 0x731360c0d0>, <__main__.RubiksState object at 0x731360c450>, <__main__.RubiksState object at 0x731360c810>, <__main__.RubiksState object at 0x731360cb90>, <__main__.RubiksState object at 0x731360cf10>, <__main__.RubiksState object at 0x731360d290>, <__main__.RubiksState object at 0x731360d5d0>, <__main__.RubiksState object at 0x731360d950>] ['U']
['U', 'L']
['U', 'L inverse']
['U', 'R']
['U', 'R inverse']
['U', 'U']
['U', 'U inverse']
['U', 'D']
['U', 'F']
['U', 'F inverse']
['U', 'B']
['U', 'B inverse']
[<__main__.RubiksState object at 0x731360ddd0>, <__main__.RubiksState object at 0x731360e250>, <__main__.RubiksState object at 0x731360e6d0>, <__main__.RubiksState object at 0x731360eb50>, <__main__.RubiksState object at 0x731360eed0>, <__main__.RubiksState object at 0x731360f290>, <__main__.RubiksState object at 0x731360f610>, <__main__.RubiksState object at 0x731360f990>, <__main__.RubiksState object at 0x731360fd10>, <__main__.RubiksState object at 0x7313610090>, <__main__.RubiksState object at 0x7313610410>] ['U inverse']
['U inverse', 'L']
['U inverse', 'L inverse']
['U inverse', 'R']
['U inverse', 'R inverse']
['U inverse', 'U']
['U inverse', 'U inverse']
['U inverse', 'D']
['U inverse', 'F']
['U inverse', 'F inverse']
['U inverse', 'B']
['U inverse', 'B inverse']
[<__main__.RubiksState object at 0x7313610890>, <__main__.RubiksState object at 0x7313610d10>, <__main__.RubiksState object at 0x7313611190>, <__main__.RubiksState object at 0x7313611610>, <__main__.RubiksState object at 0x7313611990>, <__main__.RubiksState object at 0x7313611d50>, <__main__.RubiksState object at 0x73136120d0>, <__main__.RubiksState object at 0x7313612450>, <__main__.RubiksState object at 0x73136127d0>, <__main__.RubiksState object at 0x7313612b10>, <__main__.RubiksState object at 0x7313612e90>] ['D']
['D', 'L']
['D', 'L inverse']
['D', 'R']
['D', 'R inverse']
['D', 'U']
['D', 'U inverse']
['D', 'D']
['D', 'F']
['D', 'F inverse']
['D', 'B']
['D', 'B inverse']
[<__main__.RubiksState object at 0x7313613310>, <__main__.RubiksState object at 0x7313613790>, <__main__.RubiksState object at 0x7313613c10>, <__main__.RubiksState object at 0x731361c0d0>, <__main__.RubiksState object at 0x731361c450>, <__main__.RubiksState object at 0x731361c810>, <__main__.RubiksState object at 0x731361cb90>, <__main__.RubiksState object at 0x731361cf10>, <__main__.RubiksState object at 0x731361d290>, <__main__.RubiksState object at 0x731361d5d0>, <__main__.RubiksState object at 0x731361d950>] ['F']
['F', 'L']
['F', 'L inverse']
['F', 'R']
['F', 'R inverse']
['F', 'U']
['F', 'U inverse']
['F', 'D']
['F', 'F']
['F', 'F inverse']
['F', 'B']
['F', 'B inverse']
[<__main__.RubiksState object at 0x731361ddd0>, <__main__.RubiksState object at 0x731361e250>, <__main__.RubiksState object at 0x731361e6d0>, <__main__.RubiksState object at 0x731361eb50>, <__main__.RubiksState object at 0x731361eed0>, <__main__.RubiksState object at 0x731361f290>, <__main__.RubiksState object at 0x731361f610>, <__main__.RubiksState object at 0x731361f990>, <__main__.RubiksState object at 0x731361fd10>, <__main__.RubiksState object at 0x731339c090>, <__main__.RubiksState object at 0x731339c410>] ['F inverse']
['F inverse', 'L']
['F inverse', 'L inverse']
['F inverse', 'R']
['F inverse', 'R inverse']
['F inverse', 'U']
['F inverse', 'U inverse']
['F inverse', 'D']
['F inverse', 'F']
['F inverse', 'F inverse']
['F inverse', 'B']
['F inverse', 'B inverse']
[<__main__.RubiksState object at 0x731339c890>, <__main__.RubiksState object at 0x731339cd10>, <__main__.RubiksState object at 0x731339d190>, <__main__.RubiksState object at 0x731339d610>, <__main__.RubiksState object at 0x731339d990>, <__main__.RubiksState object at 0x731339dd50>, <__main__.RubiksState object at 0x731339e0d0>, <__main__.RubiksState object at 0x731339e450>, <__main__.RubiksState object at 0x731339e7d0>, <__main__.RubiksState object at 0x731339eb10>, <__main__.RubiksState object at 0x731339ee90>] ['B']
['B', 'L']
['B', 'L inverse']
['B', 'R']
['B', 'R inverse']
['B', 'U']
['B', 'U inverse']
['B', 'D']
['B', 'F']
['B', 'F inverse']
['B', 'B']
['B', 'B inverse']
[<__main__.RubiksState object at 0x731339f310>, <__main__.RubiksState object at 0x731339f790>, <__main__.RubiksState object at 0x731339fc10>, <__main__.RubiksState object at 0x73133a00d0>, <__main__.RubiksState object at 0x73133a0450>, <__main__.RubiksState object at 0x73133a0810>, <__main__.RubiksState object at 0x73133a0b90>, <__main__.RubiksState object at 0x73133a0f10>, <__main__.RubiksState object at 0x73133a1290>, <__main__.RubiksState object at 0x73133a15d0>, <__main__.RubiksState object at 0x73133a1950>] ['B inverse']
['B inverse', 'L']
['B inverse', 'L inverse']
['B inverse', 'R']
['B inverse', 'R inverse']
['B inverse', 'U']
['B inverse', 'U inverse']
['B inverse', 'D']
['B inverse', 'F']
['B inverse', 'F inverse']
['B inverse', 'B']
['B inverse', 'B inverse']

17 February 2025. I love you Dad. Mark William Watters + Charles + Tai 

"""