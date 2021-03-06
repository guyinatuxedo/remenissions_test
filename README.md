
# Remenissions Test Cases

So this repo contains the testcases used for Remenissions. There are two types of testcases, one that is a ctf challenge, the other that are binaries that I have written the source code for.

## CTF Challenges

#### 0-bof_var:

```
csaw18_boi					 
hackucf_bof1				
hackucf_bof2				 
protostar_stack0			
protostar_stack1			
MattE_bof1					
MattE_bof2					
tamu20_bbpwn				
dawg20_onlockdown			
cuctf19_bof1				
inctf17_overflow1			
icectf15_overflow1			
easyctf15-buffering			
auburn20-turkey				
hackcon19_babybof			
hackcon18_warchange			
tamu17_pwn1					
angstrumctf16_overflow1		
```

#### 1-bof_func

```
247ctf_hidden             
icectf16_smashing-profit  
sharky20_giveme0
angstrum20_no-canary      
nctf19_babypwn            
sunshine19-ret2mania
castors20_abcbof          
nctf19_oneshot-onekill    
tamu17_pwn2
castors20_babybof         
newark20-bufover          
tamu17_pwn4
csaw16_warmup             
pico13_rop1               
tamu18_pwn1
csaw18_getit              
pico13_rop2               
tamu18_pwn2
easyctfiv-rop1            
pico18_bof1               
tjctf20_seashells
encrypt19_pwn0            
pico19_overflow1          
tu16-bbys-first-elf
encrypt19_pwn1            
protostar_stack4          
tu19_thefirst
hackcon18-bof             
redpwn19_hardmode         
utc_pwn2
hackcon19-q1              
redpwn20_coffer0          
zero_free-flag
hackucf_ret               
redpwn20_coffer1
hsctf19-return-to-sender  
redpwn20_coffer2
b01lers20_oracle
cuctf20_baby-bof
```

#### 2-bof_shellcode

```
bsidesvc15_sushi			
hackcon18_seashells			
tamu18_pwn3					
tu19_shellme32				
csaw17_pilot				
hackucf_superstack			
tamu19_pwn3					
tu19_shellme64				
esecurity18_pwn01			
sniperoj_pwn100				
tu18_shellaeasy				
umdctf20_easy-right			
```

#### 3 - indirect_call

```
protostar_stack3			
hackucf_bof3				
Matte_bof3					
```

#### 04 - CallInput

```
angstrom16_shellcode		
bsidessf_easyshell			
bsidessf_easyshell64	
bsidessf18_runit			
open16_tyro-shellcode
pioc18_shellcode
pico19_handy-shellcode		
tctf_turtlesh3lls			
tctf_turtlesh3lls-3		
```

#### 05-Ret2Static

```
dcquals19_speedrun1 		
```

#### 06 - Ret2Libc

```
pico18_got-2-learn-libc		
csaw19_babyboi				
MattEctf_Rop1				
MattEctf_Rop2				
fireshell19_leakless		
hs19_combo-chain-lite		
encrypt19_pwn3				
encrypt19_pwn2				
xmas19_sn0wverflow			
redpwn20_library			
csaw20_rop
```

#### 07	-	Remote Libc ID

```
247ctf_hidden 				
247ctf_hidden-parameters	
247ctf_executable-stack 	
247ctf_non-executable-stack 
```

#### 07	-	Local Libc ID

```
angstrum20_no-canary
pico19_overflow
encrypt19_pwn0
csaw18_getit
pioc18_bof1
csaw19_babyboi
utc_pwn2
MattECtf-rop2
fireshell19_leakless
encrypt19_pwn2
encrypt19_pwn3
xmas19_sn0wverflow
redpwn19_zipline (not duplicate)	
```
	
#### 08	-	FmtString

```
angstrum16_format1			
protostar_format4
encrypt19_pwn4				
backdoor17_bbpwn			
ractf_nra
redpwn19_rot26
tamu17_pwn3					
```

## Unit Testing

#### 0.) Overflow Vars

```
00	-	Basic Test
01	-	Basic Test w no mitigations
02	-	Overwrite  Three Vars, two equal, one not equal
03	-	Overwrite Var, with one var past where you can write, one within your reach
04	- 	Overwrtite six vars, one equal, one not equal, one less than, one greater 
than, one less than or equal to, one greater than or equal to
05	-	^ that one, but no mitigations	
06	-	Repeated Cmps against single variable 
07	-	More Repeated Cmps against single variable
08	-	Nested cmps
09	-	Basic test with strcpy (argv input)
10	-	REMOVED
11	-	Basic test with fscanf
12	-	Basic test with strncpy (argv input)
```

#### 1.) Call Func

```
00	-	Basic Test
01 	-	Basic Test no mitigations
02	-	Basic Test of Import System
03	-	Overflow with one var, call func
04	-	Overflow with three vars, call func
05	-	Baic test with multiple win funcs
06	-	Baic test with multiple false win funcs, one win func
07	-	Basic Test w pie infoleak
08	-	Basic Test of Import System w pie infoleak (x64 only)
09	-	Overflow with one var, call func w pie infoleak
10	-	Overflow with three vars, call func w pie infoleak (x64 only)
11	-	Baic test with multiple false win funcs, one win func w pie infoleak
12	-	Basic Test with argv input
13	-	Test correct bofFunc, multiple stack variable checks
14	-	Test correct bofFuncWInfoleak, multiple stack variable checks
15	-	Test correct bofSystem, multiple stack variable checks
16	-	Test correct bofSystemWInfoleak, multiple stack variable checks
```

#### 2.) Call Shellcode

```
00	- 	Basic Test
01	-	Basic Test no mitigations
02	-	Basic test with scanf
03	-	Basic test, infoleak points to start of input plus offset
04	-	Have to place shellcode ahead of stack variable
05	- 	Have to place shellcode between two stack variables
06	- 	Have to place shellcode between two stack variables, no mitigations
07	-	Have to place shellcode after return address, infoleak points to start of input plus offset
08	-	Have to place shellcode in place of variables with cmps against them (cmps not critical)
09	-	Pie Infoleak and libc
10	-	Multiple infoleaks, with pie / stack
```

#### 3.) Call Indirect

```
00	-	Basic test, overwrite indirect pointer to winfunc
01	-	Basic test no mitigations
02	-	Basic test w pie inofleak, pie enabled
03	-	Basic test w libc infoleak, pie enabled (x64 only)
04	-	Indirect ptr on stack is compared
05	-	cmp to get to indirect ptr
06	-	Mutliple indirect ptrs
07	-	Multiple indirect ptrs, compares to get to them, and cmps against indirect ptrs
08	-	multiple false win funcs, one real win func
09	-	Overwrite ptr to shellcode on the stack
```

#### 4.) Call Input

```
00	-	Call Input off from Stack
01	-	Call Input from allocated Space
02	-	Call Input off from stack with offset
03	-	Call Input from allocated Space with offset
```

#### 5.) Return 2 Statically Compiled Binary

```
00	-	Basic Test
```


#### 6.) Return 2 Libc
```
00	-	Basic Test
01	-	Basic Test No Pie
02	-	Basic test with single variable cmp
03	-	Only have 8 byte write over return address
04	-	Basic Test w/puts infoleak
05	-	Ret2Libc w/ puts infoleak
06	-	Basic test with single variable cmp
07	-	Basic Test
```

#### 7.) Local Libc Id
```
00.)	-	Basic Test
01.)	-	Basic Test in Sub Function
02.)	-	Basic Test with var check
03.)	-	Basic Test
```
#### 8.) Fmt String
```
00.)		-	got overwrite to winfunc
01.)		-	got overwrite to winfunc, no binary mitigations
02.)		-	got overwrite to winfunc, with string prepended to input before printed
03.)		-	got overwrite to winfunc, with string prepended to input before printed that does not align to new stack spot
04.)		-	GOT Overwrite to winfunc, PIE enabled, PIE Infoleak provided
05.)		-	GOT Overwrite to libc system w Libc Infoleak provided
06.)		-	GOT overwrite to imported system
07.)		-	GOT overwrite to imported system, PIE enabled, PIE Infoleak provided
08.)		-	Return Address overwrite to winFunc, stack infoleak provided, in sub function
09.)		-	Return Address overwrite to shellcode on the stack, stack infoleak provided, NX disabled, in sub function
10.)		-	Got overwrite to shellcode on the stack, stack infoleak provided, in sub function
11.)		-	for x86, Return Address overwrite to winFunc (9 but from main), libc infoleak provided, in sub function, for x64 got overwrite to onegadget
12.)		-	for x86, Got overwrite to shellcode on the stack, stack infoleak provided (10 but from main), stack infoleak provided, for x64 got overwrite to onegadget (11 but puts instead of fflush)	
13.)		-	Got overwrite to shellcode on the stack, stack infoleak provided (10 from main, x64 and x86 both)
14.)		-	got overwrite to WinFunc, for x86 the size of your payload is small enough that it only allows for 2 writes, for x64 the got address you're writing to has already been resolved and must have some of the higher bytes zeroed out, multiple false winFuncs both
15.)		-	got overwrite to WinFunc, PIE enabled, PIE Infoleak provided, for x86 the size of your payload is small enough that it only allows for 2 writes, for x64 the got address you're writing to has already been resolved and must have some of the higher bytes zeroed out, multiple false winFuncs both
16.)		-	got overwrite to system, for x86 the size of your payload is small enough that it only allows for 2 writes
17.)		-	got overwrite to system, PIE enabled, PIE Infoleak provided, for x86 the size of your payload is small enough that it only allows for 2 writes
18.)		-	return address overwrite to stack shellcode, stack infoleak provided, nx disabled,  for x86 the size of your payload is small enough that it only allows for 2 writes
19.)		-	return address overwrite to winFunc, stack infoleak provided, nx disabled,  for x86 the size of your payload is small enough that it only allows for 2 writes	
20.)		-	got overwrite to stack shellcode, stack infoleak provided, nx disabled,  for x86 the size of your payload is small enough that it only allows for 2 writes	 
21.)		-	GOT Overwrite to libc system w Libc Infoleak provided, for x86 the size of your payload is small enough that it only allows for 2 writes
22.)		-	Got overwrite to shellcode, NX Disabled, leverage fmt string to do got overwrite for infinite loop, then use fmt string to get stack infoleak from saved base ptr in sub function
23.)		-	Target with looped input to fmt string, PIE enabled, leverage format string for PIE infoleak, then got overwrite to winfunc
24.)		-	Target with looped input to fmt string, libc provided, leverage format stirng for libc infoleak, that got overwrite printf to system
```
