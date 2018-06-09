import sys
import numpy as np

def nmi(result1, result2):
  start1 = min(result1)
  start2 = min(result2)
  _i = max(result1) - start1 + 1
  _j = max(result2) - start2 + 1
  n = len(result1)
  confusion = np.zeros((_i, _j))
  
  for i, j in zip(result1, result2):
    confusion[i - start1][j - start2] += 1
  
  nmi1 = 0.
  nmi2 = 0.
  nmi3 = 0.
  Nj = np.zeros((_j,))
  for j in range(_j):
    Nj[j] = sum(confusion[:, j])
    nmi3 += Nj[j] * np.log(Nj[j] / n)

  for row in confusion:
    Ni = sum(row)
    nmi2 += Ni * np.log(Ni / n)
    for j, Nij in enumerate(row):
      if Nij != 0:
        nmi1 -= 2 * Nij * np.log(Nij * n / Ni / Nj[j])
  
  return nmi1 / (nmi2 + nmi3)

def main():
  with open(sys.argv[1], 'r') as f:
    result1 = list(map(lambda x: int(x.split('	')[1]), f.read().split('\n')[:-1]))
  with open(sys.argv[2], 'r') as f:
    result2 = list(map(lambda x: int(x.split('	')[1]), f.read().split('\n')))
  
  if len(result1) != len(result2):
    print("len(result1) = {} is not equal to len(result2) = {}".format(len(result1), len(result2)))
    #return -1
  
  print('nmi = {}'.format(nmi(result1, result2)))
  
if __name__ == "__main__":
  main()
