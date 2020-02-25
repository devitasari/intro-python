def vocalSeeker(board):
    count = 0
    kamus = ('a','i','u','e','o','A','I','U','E','O')
    output = ''
    for i in board:
        for j in i:
            for k in kamus:
                if j == k:
                    output += k
                    count += 1
    return 'vocal ditemukan %d dan kumpulan vokal adalah %s' %(count, output)
            

print(vocalSeeker([
  ['*', '*', '*', 10],
  ['*', '*', -5, -10, '*', 100],
  ['a', 'A', 'o', 'b'] 
]))