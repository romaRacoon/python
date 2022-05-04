import struct


def main(data):
    A = struct.unpack_from('>hBHIq', data, offset=5)

    B = struct.unpack_from('>IdiB2IHbB4hBiH', data, offset=A[3])
    B6 = list(struct.unpack_from('>4h', data, offset=B[5]))

    C = struct.unpack_from('>3IqhQI7hBh3H', data, offset=B[0])

    D = []
    for i in range(3):
        tempTuple = struct.unpack_from('>bB', data, offset=C[i])
        tempDict = {}
        for j in range(len(tempTuple)):
            tempDict['D' + str(j + 1)] = tempTuple[j]
        D.append(tempDict)

    F2 = list(struct.unpack_from('>' + str(C[16]) + 'Q', data, offset=C[17]))

    G4 = list(struct.unpack_from('>' + str(B[4]) + 'I', data, offset=B[5]))

    return {'A1': A[0],
            'A2': A[1],
            'A3': A[2],
            'A4': {'B1': {'C1': D,
                          'C2': C[3],
                          'C3': C[4],
                          'C4': C[5],
                          'C5': C[6],
                          'C6': {'E1': [C[7],
                                        C[8],
                                        C[9],
                                        C[10],
                                        C[11],
                                        C[12],
                                        C[13]],
                                 'E2': C[14]},
                          'C7': {'F1': C[15],
                                 'F2': F2,
                                 'F3': C[18]}},
                   'B2': {'G1': B[1],
                          'G2': B[2],
                          'G3': B[3],
                          'G4': G4},
                   'B3': B[6],
                   'B4': B[7],
                   'B5': B[8],
                   'B6': [B[9], B[10], B[11], B[12]],
                   'B7': {'H1': B[13], 'H2': B[14], 'H3': B[15]}},
            'A5': A[4]}


# ТОЛЬКО ДЛЯ ТЕСТОВ, при отправлении на сайт полностью удалить print
# (так как он выходит за границу в 79 символов)
# print(main(b'OOFQ#\x10\t( `\x00\x00\x00y\x18\xb51\xddt;\xc8\xd6R\n\xf5\xb8\xde\xb7Rz\x86r'
#            b'\x1d>+\xce\x1dX\x95E\xc3\xd4\x02g\x00\x00\x00\x16\x00\x00\x00\x18'
#            b'\x00\x00\x00\x1a\xfd\x14\x8f0\xdd\xcfjZ\xdf{b\xf7\xd0_\xe3\xe8t\xa9t\xf6'
#            b'\x006\xb3P\xfdNS\xcfT\xd9\xb2\x9e\xd7V\xb4uh\x1b\t\x00\x02\x00\x1cEm\x16nP'
#            b'\x1a$\xd5\xd9\xf5\xaa\xe8\xcd\xfb"\rgsp\xb0\xc4\xe7\x00\x00\x00,\xbf\xed|'
#            b'\x1b\x0fr\x1c\x08 E\xf9\xdd+\x00\x00\x00\x05\x00\x00\x00e^I\xb2A.\xe8'
#            b'\xed\xb0\x87\xaa\x8e\xe4s\xd2$Hh\x80D'))

# A - >hBHIq
# B - >IdiB2IHbB4hBiH
# C - >3IqhQI7hBh3H
# D - >bB
# E - >7hB
# F - >h3H
# G - >diB2I
# H - >BiH
