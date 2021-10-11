def factorial(n):
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  return n * factorial(n - 1)


import opcode
RETURN_VALUE = 83
JUMP_FORWARD, JUMP_ABSOLUTE = 110, 113
FALSE_BRANCH_JUMPS = (111, 114) # JUMP_IF_FALSE_OR_POP, POP_JUMP_IF_FALSE

def find_blocks(meth_co):
  blocks = {}
  code = meth_co.co_code
  finger_start_block = 0
  i, length = 0, len(code)
  while i < length:
    op = ord(code[i])
    i += 1
    if op == RETURN_VALUE: # We force finishing the block after the return,
                           # dead code might still exist after though...
      blocks[finger_start_block] = {
        'length': i - finger_start_block - 1,
        'exit': True
      }
      finger_start_block = i
    elif op >= opcode.HAVE_ARGUMENT:
      oparg = ord(code[i]) + (ord(code[i+1]) << 8)
      i += 2
      if op in opcode.hasjabs: # Absolute jump to oparg
        blocks[finger_start_block] = {
          'length': i - finger_start_block
        }
        if op == JUMP_ABSOLUTE: # Only uncond absolute jump
          blocks[finger_start_block]['conditions'] = {
            'uncond': oparg
          }
        else:
          false_index, true_index = (oparg, i) if op in FALSE_BRANCH_JUMPS else (i, oparg)
          blocks[finger_start_block]['conditions'] = {
            'true': true_index,
            'false': false_index
          }
        finger_start_block = i
      elif op in opcode.hasjrel:
        # Essentially do the same...
        pass

  return blocks

def to_dot(blocks):
  cache = {}

  def get_node_id(idx, buf):
    if idx not in cache:
      cache[idx] = 'node_%d' % idx
      buf.append('%s [label="Block Index %d"];' % (cache[idx], idx))
    return cache[idx]

  buffer = ['digraph CFG {']
  buffer.append('entry [label="CFG Entry"]; ')
  buffer.append('exit  [label="CFG Implicit Return"]; ')

  for block_idx in blocks:
    node_id = get_node_id(block_idx, buffer)
    if block_idx == 0:
      buffer.append('entry -> %s;' % node_id)
    if 'conditions' in blocks[block_idx]:
      for cond_kind in blocks[block_idx]['conditions']:
        target_id = get_node_id(blocks[block_idx]['conditions'][cond_kind], buffer)
        buffer.append('%s -> %s [label="%s"];' % (node_id, target_id, cond_kind))
    if 'exit' in blocks[block_idx]:
      buffer.append('%s -> exit;' % node_id)

  buffer.append('}')
  return '\n'.join(buffer)