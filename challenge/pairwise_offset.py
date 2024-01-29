def pairwise_offsetV2(sequence, fillvalue= "*", offset= 0):
  if not offset:
    return [(a, a) for a in sequence]
  
  it = []

  for i in range(offset):
    if i < len(sequence):
        it.append((sequence[i], fillvalue))
        continue
    it.append((fillvalue, fillvalue))
  
  count = 0
  if offset < len(sequence):
    for e in range(offset, len(sequence)):
      it.append((sequence[e], sequence[count]))
      count += 1
  for r in range(count, len(sequence)):
    it.append((fillvalue, sequence[r]))

  return it



def pairwise_offset(sequence, fillvalue= "*", offset= 0):
  it = []

  seq = [fillvalue] * offset + list(sequence)
  for i in range(len(seq)):
    if i < len(sequence):
      pair = (sequence[i], seq[i])
    else:
      pair = (fillvalue, seq[i])
    
    it.append(pair)

  return it