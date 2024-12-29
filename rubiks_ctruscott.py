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

Divide and conquer - work in progress

Front face: ['G', 'G', 'G', 'Y']
Left Face: ['O', 'O', 'Y', 'O']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'O', 'G', 'Y']
[131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1] [262144]
B2
Front face: ['G', 'G', 'G', 'Y']
Left Face: ['R', 'O', 'R', 'O']
Right Face: ['R', 'Y', 'B', 'O']
Back Face: ['R', 'B', 'B', 'B']
Up face: ['Y', 'G', 'W', 'W']
Down face:['Y', 'O', 'W', 'W']
B2
Front face: ['G', 'G', 'G', 'Y']
Left Face: ['R', 'O', 'R', 'O']
Right Face: ['R', 'Y', 'B', 'O']
Back Face: ['R', 'B', 'B', 'B']
Up face: ['Y', 'G', 'W', 'W']
Down face:['Y', 'O', 'W', 'W']
['B2']
B
Front face: ['G', 'G', 'G', 'Y']
Left Face: ['W', 'O', 'W', 'O']
Right Face: ['R', 'Y', 'B', 'G']
Back Face: ['B', 'B', 'R', 'B']
Up face: ['R', 'R', 'W', 'W']
Down face:['Y', 'O', 'O', 'Y']
B
Front face: ['G', 'G', 'G', 'Y']
Left Face: ['W', 'O', 'W', 'O']
Right Face: ['R', 'Y', 'B', 'G']
Back Face: ['B', 'B', 'R', 'B']
Up face: ['R', 'R', 'W', 'W']
Down face:['Y', 'O', 'O', 'Y']
['B']
F inverse
Front face: ['G', 'G', 'Y', 'G']
Left Face: ['O', 'Y', 'Y', 'O']
Right Face: ['W', 'R', 'W', 'R']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'O', 'O']
Down face:['B', 'R', 'G', 'Y']
F inverse
Front face: ['G', 'G', 'Y', 'G']
Left Face: ['O', 'Y', 'Y', 'O']
Right Face: ['W', 'R', 'W', 'R']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'O', 'O']
Down face:['B', 'R', 'G', 'Y']
['F inverse']
F2
Front face: ['Y', 'G', 'G', 'G']
Left Face: ['O', 'B', 'Y', 'R']
Right Face: ['O', 'R', 'O', 'R']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'O', 'Y']
Down face:['W', 'W', 'G', 'Y']
F2
Front face: ['Y', 'G', 'G', 'G']
Left Face: ['O', 'B', 'Y', 'R']
Right Face: ['O', 'R', 'O', 'R']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'O', 'Y']
Down face:['W', 'W', 'G', 'Y']
['F2']
F
Front face: ['G', 'Y', 'G', 'G']
Left Face: ['O', 'W', 'Y', 'W']
Right Face: ['O', 'R', 'Y', 'R']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'R', 'B']
Down face:['O', 'O', 'G', 'Y']
F
Front face: ['G', 'Y', 'G', 'G']
Left Face: ['O', 'W', 'Y', 'W']
Right Face: ['O', 'R', 'Y', 'R']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'R', 'B']
Down face:['O', 'O', 'G', 'Y']
['F']
D inverse
Front face: ['G', 'G', 'B', 'R']
Left Face: ['O', 'O', 'G', 'Y']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'B', 'Y', 'O']
Up face: ['W', 'W', 'W', 'W']
Down face:['O', 'Y', 'Y', 'G']
D inverse
Front face: ['G', 'G', 'B', 'R']
Left Face: ['O', 'O', 'G', 'Y']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'B', 'Y', 'O']
Up face: ['W', 'W', 'W', 'W']
Down face:['O', 'Y', 'Y', 'G']
['D inverse']
D2
Front face: ['G', 'G', 'B', 'R']
Left Face: ['O', 'O', 'B', 'R']
Right Face: ['R', 'R', 'Y', 'O']
Back Face: ['B', 'B', 'G', 'Y']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'G', 'O', 'Y']
D2
Front face: ['G', 'G', 'B', 'R']
Left Face: ['O', 'O', 'B', 'R']
Right Face: ['R', 'R', 'Y', 'O']
Back Face: ['B', 'B', 'G', 'Y']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'G', 'O', 'Y']
['D2']
D
Front face: ['G', 'G', 'Y', 'O']
Left Face: ['O', 'O', 'B', 'R']
Right Face: ['R', 'R', 'G', 'Y']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['G', 'Y', 'Y', 'O']
D
Front face: ['G', 'G', 'Y', 'O']
Left Face: ['O', 'O', 'B', 'R']
Right Face: ['R', 'R', 'G', 'Y']
Back Face: ['B', 'B', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['G', 'Y', 'Y', 'O']
['D']
U inverse
Front face: ['R', 'R', 'G', 'Y']
Left Face: ['G', 'G', 'Y', 'O']
Right Face: ['B', 'B', 'B', 'R']
Back Face: ['O', 'O', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'O', 'G', 'Y']
U inverse
Front face: ['R', 'R', 'G', 'Y']
Left Face: ['G', 'G', 'Y', 'O']
Right Face: ['B', 'B', 'B', 'R']
Back Face: ['O', 'O', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'O', 'G', 'Y']
['U inverse']
U2
Front face: ['B', 'B', 'G', 'Y']
Left Face: ['R', 'R', 'Y', 'O']
Right Face: ['O', 'O', 'B', 'R']
Back Face: ['G', 'G', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'O', 'G', 'Y']
U2
Front face: ['B', 'B', 'G', 'Y']
Left Face: ['R', 'R', 'Y', 'O']
Right Face: ['O', 'O', 'B', 'R']
Back Face: ['G', 'G', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'O', 'G', 'Y']
['U2']
U
Front face: ['O', 'O', 'G', 'Y']
Left Face: ['B', 'B', 'Y', 'O']
Right Face: ['G', 'G', 'B', 'R']
Back Face: ['R', 'R', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'O', 'G', 'Y']
U
Front face: ['O', 'O', 'G', 'Y']
Left Face: ['B', 'B', 'Y', 'O']
Right Face: ['G', 'G', 'B', 'R']
Back Face: ['R', 'R', 'B', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'O', 'G', 'Y']
['U']
R inverse
Front face: ['G', 'W', 'G', 'W']
Left Face: ['O', 'O', 'Y', 'O']
Right Face: ['R', 'R', 'R', 'B']
Back Face: ['Y', 'B', 'O', 'R']
Up face: ['W', 'B', 'W', 'B']
Down face:['Y', 'G', 'G', 'Y']
R inverse
Front face: ['G', 'W', 'G', 'W']
Left Face: ['O', 'O', 'Y', 'O']
Right Face: ['R', 'R', 'R', 'B']
Back Face: ['Y', 'B', 'O', 'R']
Up face: ['W', 'B', 'W', 'B']
Down face:['Y', 'G', 'G', 'Y']
['R inverse']
R2
Front face: ['G', 'B', 'G', 'B']
Left Face: ['O', 'O', 'Y', 'O']
Right Face: ['R', 'B', 'R', 'R']
Back Face: ['Y', 'B', 'G', 'R']
Up face: ['W', 'O', 'W', 'Y']
Down face:['Y', 'W', 'G', 'W']
R2
Front face: ['G', 'B', 'G', 'B']
Left Face: ['O', 'O', 'Y', 'O']
Right Face: ['R', 'B', 'R', 'R']
Back Face: ['Y', 'B', 'G', 'R']
Up face: ['W', 'O', 'W', 'Y']
Down face:['Y', 'W', 'G', 'W']
['R2']
R
Front face: ['G', 'O', 'G', 'Y']
Left Face: ['O', 'O', 'Y', 'O']
Right Face: ['B', 'R', 'R', 'R']
Back Face: ['W', 'B', 'W', 'R']
Up face: ['W', 'G', 'W', 'Y']
Down face:['Y', 'B', 'G', 'B']
R
Front face: ['G', 'O', 'G', 'Y']
Left Face: ['O', 'O', 'Y', 'O']
Right Face: ['B', 'R', 'R', 'R']
Back Face: ['W', 'B', 'W', 'R']
Up face: ['W', 'G', 'W', 'Y']
Down face:['Y', 'B', 'G', 'B']
['R']
L inverse
Front face: ['W', 'G', 'W', 'Y']
Left Face: ['Y', 'O', 'O', 'O']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'G', 'B', 'Y']
Up face: ['R', 'W', 'B', 'W']
Down face:['G', 'O', 'G', 'Y']
L inverse
Front face: ['W', 'G', 'W', 'Y']
Left Face: ['Y', 'O', 'O', 'O']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'G', 'B', 'Y']
Up face: ['R', 'W', 'B', 'W']
Down face:['G', 'O', 'G', 'Y']
['L inverse']
L2
Front face: ['R', 'G', 'B', 'Y']
Left Face: ['O', 'Y', 'O', 'O']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'G', 'B', 'G']
Up face: ['Y', 'W', 'G', 'W']
Down face:['W', 'O', 'W', 'Y']
L2
Front face: ['R', 'G', 'B', 'Y']
Left Face: ['O', 'Y', 'O', 'O']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'G', 'B', 'G']
Up face: ['Y', 'W', 'G', 'W']
Down face:['W', 'O', 'W', 'Y']
['L2']
L
Front face: ['Y', 'G', 'G', 'Y']
Left Face: ['O', 'O', 'O', 'Y']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'W', 'B', 'W']
Up face: ['G', 'W', 'G', 'W']
Down face:['R', 'O', 'B', 'Y']
L
Front face: ['Y', 'G', 'G', 'Y']
Left Face: ['O', 'O', 'O', 'Y']
Right Face: ['R', 'R', 'B', 'R']
Back Face: ['B', 'W', 'B', 'W']
Up face: ['G', 'W', 'G', 'W']
Down face:['R', 'O', 'B', 'Y']
['L']
[]
B inverse
Front face: ['G', 'G', 'G', 'Y']
Left Face: ['G', 'O', 'Y', 'O']
Right Face: ['R', 'W', 'B', 'W']
Back Face: ['B', 'R', 'B', 'B']
Up face: ['Y', 'O', 'W', 'W']
Down face:['Y', 'O', 'R', 'R']
B inverse
Front face: ['G', 'G', 'G', 'Y']
Left Face: ['G', 'O', 'Y', 'O']
Right Face: ['R', 'W', 'B', 'W']
Back Face: ['B', 'R', 'B', 'B']
Up face: ['Y', 'O', 'W', 'W']
Down face:['Y', 'O', 'R', 'R']
['B inverse']
[<__main__.RubiksState object at 0x75d4376990>, <__main__.RubiksState object at 0x75d4332c50>, <__main__.RubiksState object at 0x75d4376cd0>, <__main__.RubiksState object at 0x75d4377010>, <__main__.RubiksState object at 0x75d4377350>, <__main__.RubiksState object at 0x75d4377690>, <__main__.RubiksState object at 0x75d4377a10>, <__main__.RubiksState object at 0x75d4377d50>, <__main__.RubiksState object at 0x75d43840d0>, <__main__.RubiksState object at 0x75d4384410>, <__main__.RubiksState object at 0x75d4384710>, <__main__.RubiksState object at 0x75d4384a50>, <__main__.RubiksState object at 0x75d4384e90>, <__main__.RubiksState object at 0x75d43853d0>, <__main__.RubiksState object at 0x75d431bc10>, <__main__.RubiksState object at 0x75d4385c50>, <__main__.RubiksState object at 0x75d4385e50>, <__main__.RubiksState object at 0x75d42cf7d0>, <__main__.RubiksState object at 0x75d4386550>]

[Program finished]
"""
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
		

def wrap(L, R, State):
		i, j = 0, 0
		temp = []
		while i < len(L):
			l = EncodeToMove(L[i], State)
			temp.append(EncodeToMove(L[i], State))
			print(l.moves)
			i += 1
		while j < len(R):
			r = EncodeToMove(R[j], State)
			temp.append(EncodeToMove(R[j], State))
			print(r.moves)
			j += 1
		return temp
def divconq(n, m, L, State):
#	print(L)
	if L == None:
		L = []
	if len(L) <= 18:
		return L[:]
	left = L[len(L)//18:]
	right = L[:len(L) // 18]
#	left = L[len(L)//18:][len(L[0]) // 18:]
#	right = L[:len(L) // 18][:len(L[0]) // 18]
	print(left, right)
	left_subtree = divconq(0, 0, left, State)
	right_subtree = divconq(0, 0, right, State)
	return wrap(left_subtree, right_subtree, State)

#	while m < len(L):
#		print(L[n:m])
#		n += 18
#		m += 18


def caller(State):
	elems = [2 ** x for x in range(18, -1, -1)]
	elems *= 10
	divconq(0, 0, elems, State)
	
def Charles():
	rep = []
	res = []
	n = 0
	while n <= 18:
		rep.append(2 ** n)
#		rep += str(bin(2 ** n)[2:])
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

	s = State
	q = deque([])
	q.append(State)
	elems = [2 ** x for x in range(18, -1, -1)]
#	elems *= 10
	tt = divconq(0, 0, elems, State)
	print(tt)

Charles()