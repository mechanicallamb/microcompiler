Instructions

4-bit opcode

  0000  nop - no-op
  0001  str - store
  0010  ld - load 
  0011  mv - move regA to regD
  0100  wr - write reg C to memory_addr[regA]
  0101  add - add register C and A, store into register D
  0110  addi - add constnat C and reg A, store into register D
  0111  subi - subtract const C from reg A, store into register D
  1000  sub - subtract reg C from reg A, store into registe D
  1001  lrs - logical right shift reg A by 1 and store in register D
  1010  not - not register const A store into register D
  1011  and - and reg A and reg C
  1100  compz - compare const C with 0
  1101  compc - compare register A with const C
  1110  compr - compare register A with register C
  1111  brif - branch if condition true
