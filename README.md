D-Link Dir-2150 stack overflow #2

Built-in web service 'anweb' contains stack overflow in action_handler() function.

When anweb receives a websocket request in the form sysutils:[STRING], it copies <string> to a 260 byte stack buffer.

```

$ cat /VERSION 
NAME:           DIR_2150_MT7621D
VERSION:        4.0.0
DATAMODEL:      2.40.0
SYSBUILDTIME:   Fri Jun  5 18:21:26 MSK 2020
VENDOR:         D-Link Russia
BUGS:           <support@dlink.ru>
SUMMARY:        Root filesystem image for DIR_2150_MT7621D

```

Debug session:
```
(gdb) target remote 192.168.0.1:4142
Remote debugging using 192.168.0.1:4142
warning: No executable has been specified and target does not support
determining executable automatically.  Try using the "file" command.
0x76f3ff84 in ?? ()
(gdb) c
Continuing.

Thread 8 received signal SIGSEGV, Segmentation fault.
[Switching to Thread 6542.6549]
0x61616161 in ?? ()
(gdb) bt
#0  0x61616161 in ?? ()
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
(gdb) i r
          zero       at       v0       v1       a0       a1       a2       a3
 R0   00000000 0047ac9b 00000000 ecfa204c ecfa204c 00000001 76fdb250 77106ffc 
            t0       t1       t2       t3       t4       t5       t6       t7
 R8   00000001 00000001 8553a1a8 0000fa80 00000001 c08f1238 00000000 7373656d 
            s0       s1       s2       s3       s4       s5       s6       s7
 R16  61616161 61616161 61616161 61616161 61616161 61616161 76067df0 76067df0 
            t8       t9       k0       k1       gp       sp       s8       ra
 R24  00000018 76fb5f08 00004000 00000000 76fe33f0 76067d00 000001a2 61616161 
        status       lo       hi badvaddr    cause       pc
      0100fc13 147bac00 0000e7ae 61616160 50800008 61616161 
          fcsr      fir      hi1      lo1      hi2      lo2      hi3      lo3
      00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 
        dspctl  restart
      00000000 00000000 
(gdb) 
```

