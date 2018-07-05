# Overall Progress
|percentage|in_progress|new|assigned|closed|total|
|:---:|:---:|:---:|:---:|:---:|:---:|
|100%|0|0|0|47|47|
# By Category
## version
|version|closed|progress|total|
|:---:|:---:|:---:|:---:|
| |3|3/3|3|
|4.11|44|44/44|44|
## severity
|severity|closed|progress|total|
|:---:|:---:|:---:|:---:|
|critical|1|1/1|1|
|minor|1|1/1|1|
|normal|39|39/39|39|
|blocker|6|6/6|6|
## owner
|owner|closed|progress|total|
|:---:|:---:|:---:|:---:|
| |6|6/6|6|
|Chris Johns <chrisj@…>|1|1/1|1|
|Sebastian Huber|13|13/13|13|
|Joel Sherrill|2|2/2|2|
|Chris Johns|22|22/22|22|
|chrisj@…|2|2/2|2|
|Amar Takhar|1|1/1|1|
## component
|component|closed|progress|total|
|:---:|:---:|:---:|:---:|
|build|3|3/3|3|
|lib/block|1|1/1|1|
|doc|6|6/6|6|
|arch/arm|2|2/2|2|
|config|1|1/1|1|
|tool/gcc|5|5/5|5|
|score|5|5/5|5|
|lib/dl|2|2/2|2|
|tool/rsb|13|13/13|13|
|fs/fat|5|5/5|5|
|shell|1|1/1|1|
|tool|3|3/3|3|
## type
|type|closed|progress|total|
|:---:|:---:|:---:|:---:|
|enhancement|3|3/3|3|
|project|1|1/1|1|
|infra|1|1/1|1|
|defect|42|42/42|42|
## priority
|priority|closed|progress|total|
|:---:|:---:|:---:|:---:|
|highest|3|3/3|3|
|normal|40|40/40|40|
|high|3|3/3|3|
|low|1|1/1|1|
## reporter
|reporter|closed|progress|total|
|:---:|:---:|:---:|:---:|
|Mario Gruber|1|1/1|1|
|Patrick Gauvin|1|1/1|1|
|slemstick|2|2/2|2|
|Joel Sherrill|3|3/3|3|
|Chris Johns|21|21/21|21|
|Steen Palm|1|1/1|1|
|Ben|2|2/2|2|
|Adit|1|1/1|1|
|mw|1|1/1|1|
|Linda Huxley|1|1/1|1|
|mholm|1|1/1|1|
|Jeffrey Hill|1|1/1|1|
|Sebastian Huber|10|10/10|10|
|Pavel|1|1/1|1|
# Tickets
## [2677](https://devel.rtems.org/ticket/2677)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Joel Sherrill|normal|closed|build|wontfix| |2677| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Any host, such as OX S, with a case insensitive file system does not build. PCI.c includes PCI.h. There must be a pci.h somewhere now.
```

* **summary**
```text
PowerPC BSP score603e PCI.c is broken on case insensitive file system
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2677#comment:1|Joel Sherrill|status changed; owner set|https://devel.rtems.org/ticket/2677#comment:1|owner set to Joel Sherrill status changed from new to assigned I will try to fix this but the BSP should have been removed on master. Should I look for other files with upper case letters in their name?|Mon, 28 Mar 2016 03:15:56 GMT|Ticket|
|https://devel.rtems.org/ticket/2677#comment:2|Chris Johns| |https://devel.rtems.org/ticket/2677#comment:2|Replying to joel.sherrill: I will try to fix this but the BSP should have been removed on master. Too late for 4.11. Should I look for other files with upper case letters in their name? Not 4.11. For 4.11 any simple hack to avoid this would be good.|Mon, 28 Mar 2016 04:03:39 GMT|Ticket|
|https://devel.rtems.org/ticket/2677#comment:3|Joel Sherrill| |https://devel.rtems.org/ticket/2677#comment:3|The file is installed as bsp/PCI.h and the shared infrastructure is installed as bsp/pci.h. It is used just enough where reworking code to avoid it for a deprecated BSP isn't worth it. I am testing a patch now to rename it to bsp/pciimpl.h. But at the moment, I am going back to relax and enjoy my team with honey, lemon and fresh mint. I caught something from someone last week and passed it along to Michele. :(|Mon, 28 Mar 2016 19:08:15 GMT|Ticket|
|https://devel.rtems.org/ticket/2677#comment:4|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2677#comment:4|milestone changed from 4.11.1 to 4.11.2|Thu, 26 Jan 2017 07:16:00 GMT|Ticket|
|https://devel.rtems.org/ticket/2677#comment:5|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2677#comment:5|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2677#comment:6|Joel Sherrill|status changed; resolution set|https://devel.rtems.org/ticket/2677#comment:6|status changed from assigned to closed resolution set to wontfix This BSP has been removed from the RTEMS source tree.|Thu, 13 Jul 2017 13:42:18 GMT|Ticket|
|https://devel.rtems.org/ticket/2677#comment:7|Chris Johns|component changed|https://devel.rtems.org/ticket/2677#comment:7|component changed from unspecified to build|Mon, 12 Feb 2018 03:57:08 GMT|Ticket|
## [3183](https://devel.rtems.org/ticket/3183)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|arch/arm|fixed|build|3183| |4.11.3|Steen Palm|defect| | |
* **description**
```text
I have built release 4.11.2 of RTEMS for ERC32, and it can successfully run the hello example using the SPARC gdb.

I'm now trying to build RTEMS for ARM using RSB 4.11.2, but RSB fails after it has built the kernel, while it is making a hello example test. The strange thing is that RSB is attempting to use a file that is part of the RTEMS built for ERC32 - a file that does not exist.  The prefix for the ERC32 RTEMS is /home/smile/dev/rtems/4.11/erc32 and /home/smile/dev/rtems/4.11/arm for the ARM RTEMS.

Used build command:  ../source-builder/sb-set-builder --prefix=$HOME/dev/rtems/4.11/arm 4.11/rtems-arm

Extract from the log file rsb-report-arm-rtems4.11-kernel-4.11.2-1.txt:
...
make  all-am
make[5]: Entering directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites/samples'
BSP Testsuite Data: all tests
Making all in hello
make[6]: Entering directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites/samples/hello'
arm-rtems4.11-gcc -B../../../../../nds/lib/ -specs bsp_specs -qrtems -DHAVE_CONFIG_H -I. -I../../../../../../../rtems-4.11.2/c/src/../../testsuites/samples/hello -I..     -mcpu=arm9tdmi -O2 -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs -MT init.o -MD -MP -MF .deps/init.Tpo -c -o init.o ../../../../../../../rtems-4.11.2/c/src/../../testsuites/samples/hello/init.c
mv -f .deps/init.Tpo .deps/init.Po
arm-rtems4.11-gcc -B../../../../../nds/lib/ -specs bsp_specs -qrtems -mcpu=arm9tdmi -O2 -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs    -mcpu=arm9tdmi   -o hello.exe init.o 
arm-rtems4.11-nm -g -n hello.exe > hello.num arm-rtems4.11-size hello.exe
   text	   data	    bss	    dec	    hex	filename
 145504	   2384	4043392	4191280	 3ff430	hello.exe
arm-rtems4.11-objcopy -O binary hello.exe hello.bin ../../../../../nds/build-tools/ndstool -c hello.nds -9 hello.bin -7 /home/smile/dev/rtems/4.11/erc32/sparc-rtems4.11/erc32/lib/coproc.bin
Cannot open file '/home/smile/dev/rtems/4.11/erc32/sparc-rtems4.11/erc32/lib/coproc.bin'.
Nintendo DS rom tool compiled for rtems - Oct 10 2017 by Rafael Vuijk, Dave Murphy, Alexei Karpenko
Makefile:626: recipe for target 'hello.exe' failed
make[6]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites/samples/hello'
make[6]: *** [hello.exe] Error 1
make[5]: *** [all-local] Error 1
make[4]: *** [all] Error 2
make[3]: *** [all-recursive] Error 1
make[2]: *** [all-recursive] Error 1
Makefile:583: recipe for target 'all-local' failed
make[5]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites/samples'
Makefile:245: recipe for target 'all' failed
make[4]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites/samples'
Makefile:313: recipe for target 'all-recursive' failed
make[3]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites'
Makefile:424: recipe for target 'all-recursive' failed
make[2]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds'
make[1]: *** [all-recursive] Error 1
Makefile:286: recipe for target 'all-recursive' failed
make[1]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c'
make: *** [all-recursive] Error 1
Makefile:410: recipe for target 'all-recursive' failed shell cmd failed: /bin/sh -ex  /home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/doit
error: building arm-rtems4.11-kernel-4.11.2-1

```

* **summary**
```text
Build of RTEMS 4.11.2 using RSB fails for ARM
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3183#comment:1|Steen Palm| |https://devel.rtems.org/ticket/3183#comment:1|I forgot to mention that the platform is Debian 8.|Thu, 12 Oct 2017 08:00:23 GMT|Ticket|
|https://devel.rtems.org/ticket/3183#comment:2|Chris Johns| |https://devel.rtems.org/ticket/3183#comment:2|As a work around please add --without-rtems as an option to the RSB set builder command. You will then need to build RTEMS yourself and you can select the specific BSP you are interested in.|Thu, 12 Oct 2017 15:52:03 GMT|Ticket|
|https://devel.rtems.org/ticket/3183#comment:3|Chris Johns|status, component changed; owner, milestone set|https://devel.rtems.org/ticket/3183#comment:3|owner set to Chris Johns status changed from new to assigned component changed from admin to arch/arm milestone set to 4.11.3|Tue, 06 Feb 2018 00:41:37 GMT|Ticket|
|https://devel.rtems.org/ticket/3183#comment:4|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3183#comment:4|status changed from assigned to closed resolution set to fixed This fix resolves the RSB side of things, the kernel is now not build by default with the following change so this error is avoided: ​https://git.rtems.org/rtems-source-builder/commit/?h=4.11&id=49033ffc66f75d10ba47df166be77827d0069b56 The underlying bug in the BSP is still present and if it is a problem a new ticket can be created.|Wed, 07 Feb 2018 03:12:28 GMT|Ticket|
## [3024](https://devel.rtems.org/ticket/3024)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|lib/dl|fixed|dl04, dl05, depcomp, CXXDEPMOD|3024| |4.11.3|Pavel|defect| | |
* **description**
```text
Building rtems-4.11.2-rc4 with "--enable-tests" option fails with error from depcomp:
"depcomp: Variables source, object and depmode must be set"

The reason (in my opinion) is empty CXXDEPMODE variable in Makefiles generated for dl04 and dl05.

I changed it to depmode=gcc for dl04 and depmode=gcc3 for dl05 just to check, it helped.

But I don't know the right value for this variable.

target  - i386-rtems4.11
bsp     - pc486
version - rtems-4.11.2-rc4 (version downloaded by rtems-source-builder-4.11.2-rc4)
```

* **summary**
```text
dl04, dl05 build failes
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3024#comment:1|Joel Sherrill|owner, status changed|https://devel.rtems.org/ticket/3024#comment:1|owner changed from joel.sherrill@… to Chris Johns status changed from new to assigned Changing own to chrisj since he owns the dl tests and has been hacking on the Makefiles lately. The script depcomp is at the top of a bootstrapped source tree and is documented as part of automake. Hopefully the documentation pointers saved someone some time.|Tue, 23 May 2017 15:47:28 GMT|Ticket|
|https://devel.rtems.org/ticket/3024#comment:2|Chris Johns|milestone changed|https://devel.rtems.org/ticket/3024#comment:2|milestone changed from 4.11.3 to 4.11.2|Wed, 24 May 2017 00:06:42 GMT|Ticket|
|https://devel.rtems.org/ticket/3024#comment:3|Chris Johns|milestone changed|https://devel.rtems.org/ticket/3024#comment:3|milestone changed from 4.11.2 to 4.11.3|Tue, 11 Jul 2017 00:37:09 GMT|Ticket|
|https://devel.rtems.org/ticket/3024#comment:4|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/3024#comment:4|status changed from assigned to closed resolution set to fixed In 2ed53cb9/rtems: testsuite/dl: Add C++ by default for DL tests which use C++. Add AM C++ support to the testsuite configure.ac script. Fix the dependences in the DL tests. Closes #3024.|Tue, 22 Aug 2017 23:49:20 GMT|Ticket|
|https://devel.rtems.org/ticket/3024#comment:5|Sebastian Huber|component changed|https://devel.rtems.org/ticket/3024#comment:5|component changed from testing to unspecified|Tue, 10 Oct 2017 06:46:55 GMT|Ticket|
|https://devel.rtems.org/ticket/3024#comment:6|Chris Johns|component changed|https://devel.rtems.org/ticket/3024#comment:6|component changed from unspecified to lib/dl|Mon, 12 Feb 2018 03:54:22 GMT|Ticket|
## [3094](https://devel.rtems.org/ticket/3094)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|tool|fixed| |3094| |4.11.3|Sebastian Huber|defect| | |
* **description**
```text
Some architectures like ARM encode the short enum option state in the object file and the linker checks that this option is consistent for all objects of an executable.  In case applications use -fno-short-enums, then this leads to linker warnings.  Use the enum __packed attribute for the relevant enums to avoid the -fshort-enums compiler option.  This attribute is at least available on GCC, LLVM/clang and the Intel compiler.
```

* **summary**
```text
ARM: Back port Newlib patch to avoid warnings with -fno-short-enums
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3094#comment:1|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/3094#comment:1|status changed from assigned to closed resolution set to fixed In 50908d2/rtems-source-builder: ARM: Avoid warnings with -fno-short-enums Close #3094.|Fri, 11 Aug 2017 05:16:41 GMT|Ticket|
## [3075](https://devel.rtems.org/ticket/3075)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|minor|Sebastian Huber|low|closed|doc|fixed|interrupt lock acquire|3075| |4.11.3|Jeffrey Hill|defect| | |
* **description**
```text

I suspect that in this section it should indicate that the second argument is "rtems_interrupt_level * level" instead of "rtems_interrupt_level level". Furthermore, perhaps it should state that the function is caching some type of opaque context inside of "level" to be restored when the lock is released. Also, perhaps a better argument name would be "pPrvCtx"? The documentation might also divulge additional _functional_ details about what occurs on an SMP system. Does it prevent interrupts from running on all CPUs simultaneously when the lock is acquired? It does say something about an SMP lock, but that perhaps is an implementation detail, and not a functional description of what the function does.

{{{
7.4.8 INTERRUPT_LOCK_ACQUIRE - Acquire an ISR Lock
CALLING SEQUENCE:

void rtems_interrupt_lock_acquire(
  rtems_interrupt_lock *lock,
  rtems_interrupt_level level
);
}}}

```

* **summary**
```text
rtems_interrupt_lock_acquire interface documentation issue in the "RTEMS C Users Guide"
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3075#comment:1|Gedare|owner, status changed|https://devel.rtems.org/ticket/3075#comment:1|owner changed from chrisj@… to Sebastian Huber status changed from new to assigned|Thu, 13 Jul 2017 22:10:43 GMT|Ticket|
|https://devel.rtems.org/ticket/3075#comment:2|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/3075#comment:2|In f776fe6/rtems-docs: c-user: Fix interrupt lock documentation Update #3075.|Fri, 14 Jul 2017 05:53:00 GMT|Ticket|
|https://devel.rtems.org/ticket/3075#comment:3|Sebastian Huber|milestone set|https://devel.rtems.org/ticket/3075#comment:3|milestone set to 4.11.3|Fri, 14 Jul 2017 05:53:23 GMT|Ticket|
|https://devel.rtems.org/ticket/3075#comment:4|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/3075#comment:4|status changed from assigned to closed resolution set to fixed In eecec5f/rtems-docs: c-user: Fix interrupt lock documentation Close #3075.|Fri, 14 Jul 2017 05:55:52 GMT|Ticket|
|https://devel.rtems.org/ticket/3075#comment:5|Sebastian Huber| |https://devel.rtems.org/ticket/3075#comment:5|If it is still unclear, then please re-open the ticket.|Fri, 14 Jul 2017 06:00:17 GMT|Ticket|
|https://devel.rtems.org/ticket/3075#comment:6|Sebastian Huber|component changed|https://devel.rtems.org/ticket/3075#comment:6|component changed from Documentation to doc|Tue, 10 Oct 2017 06:06:29 GMT|Ticket|
## [2439](https://devel.rtems.org/ticket/2439)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool/gcc|fixed| |2439| |4.11.3|Chris Johns|defect|3262| |
* **description**
```text
Building 4.11/rtems-arm with the RSB fails with (error report attached):

{{{
/Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/build/./gcc/xgcc -B/Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/build/./gcc/ -nostdinc -B/Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/build/arm-rtems4.11/newlib/ -isystem /Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/build/arm-rtems4.11/newlib/targ-include -isystem /Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/gcc-4.9.3/newlib/libc/include -B/Users/chris/development/rtems/4.11/arm-rtems4.11/bin/ -B/Users/chris/development/rtems/4.11/arm-rtems4.11/lib/ -isystem /Users/chris/development/rtems/4.11/arm-rtems4.11/include -isystem /Users/chris/development/rtems/4.11/arm-rtems4.11/sys-include    -g -O2 -mthumb -O2 -I../../../../gcc-4.9.3/libgcc/../newlib/libc/sys/rtems/include -g -O2 -DIN_GCC  -DCROSS_DIRECTORY_STRUCTURE  -W -Wall -Wno-narrowing -Wwrite-strings -Wcast-qual -Wstrict-prototypes -Wmissing-prototypes -Wold-style-definition  -isystem ./include   -fno-inline -g -DIN_LIBGCC2 -fbuilding-libgcc -fno-stack-protector -Dinhibit_libc  -fno-inline -I. -I. -I../../.././gcc -I../../../../gcc-4.9.3/libgcc -I../../../../gcc-4.9.3/libgcc/. -I../../../../gcc-4.9.3/libgcc/../gcc -I../../../../gcc-4.9.3/libgcc/../include  -DHAVE_CC_TLS  -o _arm_unorddf2_s.o -MT _arm_unorddf2_s.o -MD -MP -MF _arm_unorddf2_s.dep -DSHARED -DL_arm_unorddf2 -xassembler-with-cpp -c ../../../../gcc-4.9.3/libgcc/config/arm/lib1funcs.S
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S: Assembler messages:
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:567: Error: invalid constant (ff) after fixup
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:673: Error: invalid constant (ff) after fixup
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:689: Error: invalid constant (fd) after fixup
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:875: Error: invalid constant (ff) after fixup
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:912: Error: invalid constant (fd) after fixup
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:985: Error: invalid constant (fd) after fixup
}}}
```

* **summary**
```text
GCC 4.9.3 ARM build fails on OS X 10.11 (El Capitan)
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2439#comment:1|Chris Johns|summary changed|https://devel.rtems.org/ticket/2439#comment:1|summary changed from ARM build fails on OS X 10.11 (Ll Capitan) to GCC 4.9.3 ARM build fails on OS X 10.11 (Ll Capitan)|Mon, 02 Nov 2015 00:06:00 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:2|Amar Takhar|summary changed|https://devel.rtems.org/ticket/2439#comment:2|summary changed from GCC 4.9.3 ARM build fails on OS X 10.11 (Ll Capitan) to GCC 4.9.3 ARM build fails on OS X 10.11 (El Capitan)|Mon, 02 Nov 2015 02:47:10 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:3|Chris Johns| |https://devel.rtems.org/ticket/2439#comment:3|The ARM target does not build on Yosemite or El Capitan with Xcode 7.1 command line tools and the problem still exists in El Capitan with Xcode 7.1 and the 7.2 beta command line tools. It appears to be a bug in clang in Xcode building tc-arm.c in binutils. I have raise a bug report with Apple with a small test case.|Wed, 04 Nov 2015 23:31:42 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:4|Joel Sherrill| |https://devel.rtems.org/ticket/2439#comment:4|Did you ask about this on the binutils and clang lists? It might actually get more traction on the public side.|Thu, 05 Nov 2015 00:59:15 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:5|Chris Johns| |https://devel.rtems.org/ticket/2439#comment:5|I raised a bug report and it has been fixed in binutils and should be released in 2.26.|Wed, 11 Nov 2015 00:11:22 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:6|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2439#comment:6|milestone changed from 4.11.1 to 4.11.2|Thu, 26 Jan 2017 07:16:00 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:7|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2439#comment:7|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:04:45 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:8|Sebastian Huber|component changed|https://devel.rtems.org/ticket/2439#comment:8|component changed from GCC to tool/gcc|Tue, 10 Oct 2017 05:58:26 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:9|Chris Johns|blocking set|https://devel.rtems.org/ticket/2439#comment:9|blocking set to 3262|Tue, 23 Jan 2018 03:03:54 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:10|Chris Johns| |https://devel.rtems.org/ticket/2439#comment:10|Testing the latest RSB for this ticket with the latest MacOS (High Sierra) with the latest Xcode (9.2) and it's command line tools fails with: /usr/bin/c++ -O2 -pipe -fbracket-depth=1024 -I/opt/work/chris/rtems/rsb/rtems-source-builder.git/rtems/build/tmp/sb-chris/4.11/rtems-arm.bset/opt/work/rtems/4.11/include -c -DIN_GCC_FRONTEND -g -O2 -DIN_GCC -DCROSS_DIRECTORY_STRUCTURE -fno-exceptions -fno-rtti -fasynchronous-unwind-tables -W -Wall -Wno-narrowing -Wwrite-strings -Wcast-qual -Wmissing-format-attribute -pedantic -Wno-long-long -Wno-variadic-m acros -Wno-overlength-strings -DHAVE_CONFIG_H -I. -Ic -I../../gcc-4.9.3/gcc -I../../gcc-4.9.3/gcc/c -I../../gcc-4.9.3/gcc/../include -I../../gcc-4.9.3/gcc/../libcpp/include -I/opt/work/chris/rtems/rsb/rtems-source-builder.git/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin17.3.0-1/build/./gmp -I/opt/work/chris/rtems/rsb/rtems-source-builder.git/rtems/build/arm-rtems4.11-gcc-4.9 .3-newlib-2.2.0.20150423-x86_64-apple-darwin17.3.0-1/gcc-4.9.3/gmp -I/opt/work/chris/rtems/rsb/rtems-source-builder.git/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin17.3.0-1/build/./mpfr -I/opt/work/chris/rtems/rsb/rtems-source-builder.git/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin17.3.0-1/gcc-4.9.3/mpfr -I/opt/work/chris/rtems/rsb/rtems-sourc e-builder.git/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin17.3.0-1/gcc-4.9.3/mpc/src -I../../gcc-4.9.3/gcc/../libdecnumber -I../../gcc-4.9.3/gcc/../libdecnumber/dpd -I../libdecnumber -I../../gcc-4.9.3/gcc/../libbacktrace -o c/c-objc-common.o -MT c/c-objc-common.o -MMD -MP -MF c/.deps/c-objc-common.TPo ../../gcc-4.9.3/gcc/c/c-objc-common.c clang: warning: treating 'c' input as 'c++' when in C++ mode, this behavior is deprecated [-Wdeprecated] In file included from ../../gcc-4.9.3/gcc/c/c-objc-common.c:33: In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/new:89: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/exception:173:5: error: no member named 'fancy_abort' in namespace 'std::__1'; did you mean simply 'fancy_abort'? _VSTD::abort(); ^~~~~~~ /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/__config:392:15: note: expanded from macro '_VSTD' #define _VSTD std::_LIBCPP_NAMESPACE ^ ../../gcc-4.9.3/gcc/system.h:685:13: note: 'fancy_abort' declared here extern void fancy_abort (const char *, int, const char *) ATTRIBUTE_NORETURN; ^ 1 error generated.|Tue, 23 Jan 2018 05:10:15 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:11|Chris Johns|status changed; owner set|https://devel.rtems.org/ticket/2439#comment:11|owner set to Chris Johns status changed from new to accepted|Thu, 25 Jan 2018 05:51:43 GMT|Ticket|
|https://devel.rtems.org/ticket/2439#comment:12|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2439#comment:12|status changed from accepted to closed resolution set to fixed ARM is building on MacOS: ​https://lists.rtems.org/pipermail/build/2018-February/000447.html|Wed, 07 Feb 2018 05:12:32 GMT|Ticket|
### attachments
|guid|creator|title|link|description|attachment_link|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2439|Chris Johns|attachment set|https://devel.rtems.org/ticket/2439|attachment set to rsb-report-arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1.txt RSB report.|https://devel.rtems.org/attachment/ticket/2439/rsb-report-arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1.txt|Mon, 02 Nov 2015 00:05:09 GMT|Ticket|
|https://devel.rtems.org/ticket/2439|Chris Johns|attachment set|https://devel.rtems.org/ticket/2439|attachment set to gcc-4.9.3-macos-xcode9.diff Fixes for MacOS (High Sierra) and Xocde 9.2 command line tools.|https://devel.rtems.org/attachment/ticket/2439/gcc-4.9.3-macos-xcode9.diff|Tue, 23 Jan 2018 22:09:36 GMT|Ticket|
## [2987](https://devel.rtems.org/ticket/2987)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|fs/fat|fixed| |2987| |4.11.3|slemstick|defect| | |
* **description**
```text
msdos_dir_read(..) uses a conversion function, convert_handler->utf16_to_utf8, to convert LFN directory entry names in utf16 format to utf8. 

However, the conversion handler sets the string length of the output utf8 string as well. That variable: **string_size** in msdos_dir_read(..) is never re-initialised in the search algorithm. When the volume becomes sufficiently fragmented, de-allocated LFN directory entry checksums will cause the filename search algorithm to fail, effectively breaking the current attempt to concatenate directory entry filename chunks, but the output string size is now much shorter (10 characters, where it should be **sizeof(tmp_dirent.d_name)**). Consequently, msdos_dir_read(..) will continue to parse directory entries with a much smaller output string size. 

The end result is that attempts to read file names from a directory will output truncated file names (for example, readdir() will "work" as normal but the output filenames are too short). Any attempt to open these truncated file names will, of course, fail. 
```

* **summary**
```text
fat: msdos_dir_read(..) doesn't reset conversion output string length
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2987#comment:1|Gedare| |https://devel.rtems.org/ticket/2987#comment:1|Please remove the spurious whitespace changes, add "Closes #2987." Into the commit message, and format a friendly short commit message that specifies the rtems subsystem first, e.g. "libfs/dosfs: ..." Please see Developer/Git|Tue, 11 Apr 2017 00:43:35 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:2|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2987#comment:2|milestone changed from 4.12 to 4.12.0|Thu, 11 May 2017 07:31:02 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:3|Sebastian Huber| |https://devel.rtems.org/ticket/2987#comment:3|Without a real name I cannot apply this patch.|Mon, 12 Jun 2017 07:32:58 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:4|Sebastian Huber|status changed; owner set|https://devel.rtems.org/ticket/2987#comment:4|owner set to Sebastian Huber status changed from new to assigned|Thu, 24 Aug 2017 09:56:36 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:5|Sebastian Huber|component, summary changed|https://devel.rtems.org/ticket/2987#comment:5|component changed from General to filesystem summary changed from msdos_dir_read(..) doesn't reset conversion output string length to fat: msdos_dir_read(..) doesn't reset conversion output string length|Thu, 24 Aug 2017 10:03:56 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:6|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/2987#comment:6|In 34dda604/rtems: dosfs: Fix msdos_dir_read() Set a proper name buffer length for each converter invocation. Update #2987.|Wed, 06 Sep 2017 11:22:03 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:7|Sebastian Huber|version, milestone changed|https://devel.rtems.org/ticket/2987#comment:7|version changed from 4.12 to 4.11 milestone changed from 4.12.0 to 4.11.3|Wed, 06 Sep 2017 11:24:30 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:8|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/2987#comment:8|status changed from assigned to closed resolution set to fixed In e1c3dc09/rtems: dosfs: Fix msdos_dir_read() Set a proper name buffer length for each converter invocation. Close #2987.|Wed, 06 Sep 2017 11:24:52 GMT|Ticket|
|https://devel.rtems.org/ticket/2987#comment:9|Sebastian Huber|component changed|https://devel.rtems.org/ticket/2987#comment:9|component changed from fs to fs/fat|Tue, 10 Oct 2017 06:50:58 GMT|Ticket|
### attachments
|guid|creator|title|link|description|attachment_link|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2987|slemstick|attachment set|https://devel.rtems.org/ticket/2987|attachment set to 0001-Fix-issue-that-msdos_dir_read-didn-t-reset-an-output.patch|https://devel.rtems.org/attachment/ticket/2987/0001-Fix-issue-that-msdos_dir_read-didn-t-reset-an-output.patch|Sun, 09 Apr 2017 10:33:41 GMT|Ticket|
## [2988](https://devel.rtems.org/ticket/2988)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|critical|chrisj@…|highest|closed|doc|fixed| |2988| |4.11.3|Chris Johns|defect| | |
* **description**
```text
The link on docs.rtems.org to the latest release is broken. I suspect an issue in the catalogue Javascript code.
```

* **summary**
```text
Documentation link to the 4.11 release is broken.
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2988#comment:1|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2988#comment:1|milestone changed from 4.11.2 to 4.11.3 Moved to 4.11.3 and will fix once #3031 is fixed.|Tue, 11 Jul 2017 00:38:21 GMT|Ticket|
|https://devel.rtems.org/ticket/2988#comment:2|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2988#comment:2|status changed from assigned to closed resolution set to fixed Fixed. ​https://git.rtems.org/chrisj/rtems-admin.git/commit/?id=7eed3cecc3d6f729550468d973641d13e9ce7956|Mon, 04 Sep 2017 03:40:17 GMT|Ticket|
|https://devel.rtems.org/ticket/2988#comment:3|Sebastian Huber|component changed|https://devel.rtems.org/ticket/2988#comment:3|component changed from Documentation to doc|Tue, 10 Oct 2017 06:06:29 GMT|Ticket|
|https://devel.rtems.org/ticket/2988#comment:4|Danxue Huang| |https://devel.rtems.org/ticket/2988#comment:4|This is for test purpose. NVM :D|Tue, 29 May 2018 03:47:12 GMT|Ticket|
## [3105](https://devel.rtems.org/ticket/3105)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|config|fixed| |3105| |4.11.3|Sebastian Huber|defect| | |
* **description**
```text
The unlimited objects option is available for POSIX key value pairs. This flag must be removed for the memory size configuration.
```

* **summary**
```text
Invalid memory size configuration for POSIX keys
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3105#comment:1|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/3105#comment:1|In e0660391/rtems: confdefs: Fix POSIX keys configuration Remove the OBJECTS_UNLIMITED_OBJECTS flag for the memory size configuration. Update #3105.|Tue, 22 Aug 2017 06:02:41 GMT|Ticket|
|https://devel.rtems.org/ticket/3105#comment:2|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/3105#comment:2|status changed from assigned to closed resolution set to fixed In 492c95e/rtems: confdefs: Fix POSIX keys configuration Remove the OBJECTS_UNLIMITED_OBJECTS flag for the memory size configuration. Close #3105.|Tue, 22 Aug 2017 14:13:58 GMT|Ticket|
## [3164](https://devel.rtems.org/ticket/3164)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|score|fixed| |3164| |4.11.3|Sebastian Huber|defect| | |
* **summary**
```text
aio_cancel() does not destroy the corresponding condition variables
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3164#comment:1|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/3164#comment:1|In dcdd329/rtems: posix: Fix aio_cancel() Update #3164.|Wed, 04 Oct 2017 07:25:50 GMT|Ticket|
|https://devel.rtems.org/ticket/3164#comment:2|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/3164#comment:2|status changed from assigned to closed resolution set to fixed In c139a70/rtems: posix: Fix aio_cancel() Close #3164.|Wed, 04 Oct 2017 07:26:55 GMT|Ticket|
## [2910](https://devel.rtems.org/ticket/2910)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|doc|fixed| |2910| |4.11.3|Joel Sherrill|defect| | |
* **description**
```text

This section of the RSB has "+sb_check+" which I assume is supposed to be italics or bold.

https://docs.rtems.org/branches/master/rsb/hosts.html#mavericks

Also the formatting of the sentence on xz in the same section is odd.
```

* **summary**
```text
RSB docs for Mavericks has Incorrect Formatting Markup
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2910#comment:1|Sebastian Huber|owner, status, milestone changed|https://devel.rtems.org/ticket/2910#comment:1|owner changed from Chris Johns to Needs Funding status changed from new to assigned milestone changed from 4.11.2 to Indefinite|Wed, 15 Feb 2017 13:44:44 GMT|Ticket|
|https://devel.rtems.org/ticket/2910#comment:2|Joel Sherrill|owner, milestone changed|https://devel.rtems.org/ticket/2910#comment:2|owner changed from Needs Funding to Chris Johns milestone changed from Indefinite to 4.11.2|Wed, 15 Feb 2017 14:05:49 GMT|Ticket|
|https://devel.rtems.org/ticket/2910#comment:3|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2910#comment:3|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2910#comment:4|Sebastian Huber|component changed|https://devel.rtems.org/ticket/2910#comment:4|component changed from Documentation to doc|Tue, 10 Oct 2017 06:06:29 GMT|Ticket|
|https://devel.rtems.org/ticket/2910#comment:5|Chris Johns|status changed|https://devel.rtems.org/ticket/2910#comment:5|status changed from assigned to accepted|Mon, 05 Feb 2018 04:54:44 GMT|Ticket|
|https://devel.rtems.org/ticket/2910#comment:6|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/2910#comment:6|status changed from accepted to closed resolution set to fixed In 739e0f9/rtems-docs: rsb: Minor fixes. Close #2910|Mon, 05 Feb 2018 23:22:15 GMT|Ticket|
|https://devel.rtems.org/ticket/2910#comment:7|Chris Johns <chrisj@…>| |https://devel.rtems.org/ticket/2910#comment:7|In 739e0f9/rtems-docs: rsb: Minor fixes. Close #2910|Fri, 16 Feb 2018 02:17:18 GMT|Ticket|
## [3161](https://devel.rtems.org/ticket/3161)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|score|fixed| |3161| |4.11.3|Sebastian Huber|defect| | |
* **description**
```text
The I2C EEPROM driver must send the MSB of the address bytes first.
```

* **summary**
```text
I2C EEPROM driver uses incorrect address format
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3161#comment:1|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/3161#comment:1|In 2e1d595/rtems: i2c: Send MSB of address first for EEPROMs Update #3161.|Mon, 02 Oct 2017 11:41:17 GMT|Ticket|
|https://devel.rtems.org/ticket/3161#comment:2|Sebastian Huber|status changed; resolution set|https://devel.rtems.org/ticket/3161#comment:2|status changed from assigned to closed resolution set to fixed [8ca15e26ba98f172ee1396f34269ca664925427d/rtems]|Mon, 02 Oct 2017 11:47:47 GMT|Ticket|
## [2578](https://devel.rtems.org/ticket/2578)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|blocker|Chris Johns|high|closed|tool|wontfix| |2578| |4.11.3|Mario Gruber|defect| | |
* **description**
```text
Building rtems-tools for Cxc builds:

{{{
git checkout -b 4.11 origin/4.11 \
 && source-builder/sb-check \
 && cd rtems \
 && ../source-builder/sb-set-builder \
 --log=rsb-powerpc-rtems4.11-mingw.txt \
 --prefix=/opt/powerpc-rtems4.11-mingw \
 --host=i686-w64-mingw32 \
 --bset-tar-files \
 4.11/rtems-powerpc
}}}

dies at configuring package rtems-tools-4.11-1:

{{{
config: tools/rtems-tools-4.11-1.cfg
package: rtems-tools-4.11-1
...
+ echo ==> %build:
==> %build:
+ pwd
+ build_top=/tmp/rtems-source-builder/rtems/build/rtems-tools-4.11-1
+ test x86_64-linux-gnu != i686-w64-mingw32
+ RT_HOST=-host=i686-w64-mingw32
+ cd rtems-tools-4.11
+ ./waf configure -host=i686-w64-mingw32 
+ --prefix=/opt/powerpc-rtems4.11-mingw
waf [commands] [options]

Main commands (example: ./waf build -j4)
  build    : executes the build
  clean    : cleans the project
...
+ ./waf
The project was not configured: run "waf configure" first!
shell cmd failed: /bin/sh -ex  /tmp/rtems-source-builder/rtems/build/rtems-tools-4.11-1/doit
error: building rtems-tools-4.11-1
  See error report: rsb-report-rtems-tools-4.11-1.txt
}}}

This is due to the -host command line argument, which is missing a hyphen.

I sent a patch to the mailing list:

https://lists.rtems.org/pipermail/devel/2016-January/013348.html
```

* **summary**
```text
rtems-tools configure fails for Cxc builds
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2578#comment:1|Mario Gruber|status changed; owner set|https://devel.rtems.org/ticket/2578#comment:1|owner set to Sebastian Huber status changed from new to assigned|Thu, 18 Feb 2016 08:36:58 GMT|Ticket|
|https://devel.rtems.org/ticket/2578#comment:2|Chris Johns|owner changed|https://devel.rtems.org/ticket/2578#comment:2|owner changed from Sebastian Huber to Chris Johns|Sun, 27 Mar 2016 00:48:40 GMT|Ticket|
|https://devel.rtems.org/ticket/2578#comment:3|Chris Johns|priority, milestone changed|https://devel.rtems.org/ticket/2578#comment:3|priority changed from normal to high milestone changed from 4.11.1 to 4.11|Sun, 27 Mar 2016 00:51:58 GMT|Ticket|
|https://devel.rtems.org/ticket/2578#comment:4|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2578#comment:4|milestone changed from 4.11 to 4.11.2|Thu, 26 Jan 2017 07:05:05 GMT|Ticket|
|https://devel.rtems.org/ticket/2578#comment:5|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2578#comment:5|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2578#comment:6|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2578#comment:6|status changed from assigned to closed resolution set to wontfix I am going to close this ticket. We are now building Windows tools on Windows so the need for Cxc build is not as important as it was. Building on Windows ensures we have the correct DLL set for the tools.|Tue, 23 Jan 2018 21:37:54 GMT|Ticket|
## [3068](https://devel.rtems.org/ticket/3068)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal| |normal|closed|tool/gcc|wontfix| |3068| |4.11.3|Chris Johns|defect| | |
* **description**
```text
C++ sample fails to build:
{{{
moxie-rtems4.11-g++ -B../../../../../moxiesim/lib/ -specs bsp_specs -qrtems -Os -g -ffunction-sections -fdata-sections -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs  -Wl,--gc-sections     -o cxx_iostream.exe init.o
init.o: In function `__static_initialization_and_destruction_0':
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/lib/gcc/moxie-rtems4.11/4.9.3/include/c++/iostream:74: undefined reference to `__dso_handle'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/libstdc++.a(atomicity.o): In function `get_atomic_mutex':
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/libstdc++-v3/src/c++98/atomicity.cc:33: undefined reference to `__dso_handle'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/libstdc++.a(locale.o): In function `get_locale_cache_mutex':
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/libstdc++-v3/src/c++98/../../../../../gcc-4.9.3/libstdc++-v3/src/c++98/locale.cc:36: undefined reference to `__dso_handle'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/libstdc++.a(system_error.o): In function `__static_initialization_and_destruction_0':
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/libstdc++-v3/src/c++11/../../../../../gcc-4.9.3/libstdc++-v3/src/c++11/system_error.cc:65: undefined reference to `__dso_handle'
gmake[6]: Leaving directory '/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-kernel-4.11.2-1/moxie-rtems4.11-kernel-4.11.2-1-4.11.2/build/moxie-rtems4.11/c/moxiesim/testsuites/samples/iostream'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/libstdc++-v3/src/c++11/../../../../../gcc-4.9.3/libstdc++-v3/src/c++11/system_error.cc:66: undefined reference to `__dso_handle'
gmake[5]: Leaving directory '/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-kernel-4.11.2-1/moxie-rtems4.11-kernel-4.11.2-1-4.11.2/build/moxie-rtems4.11/c/moxiesim/testsuites/samples'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/libstdc++.a(eh_alloc.o):/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/libstdc++-v3/libsupc++/../../../../gcc-4.9.3/libstdc++-v3/libsupc++/eh_alloc.cc:96: more undefined references to `__dso_handle' follow
gmake[4]: Leaving directory '/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-kernel-4.11.2-1/moxie-rtems4.11-kernel-4.11.2-1-4.11.2/build/moxie-rtems4.11/c/moxiesim/testsuites/samples'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/../../../../moxie-rtems4.11/bin/ld: cxx_iostream.exe: hidden symbol `__dso_handle' isn't defined
gmake[3]: Leaving directory '/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-kernel-4.11.2-1/moxie-rtems4.11-kernel-4.11.2-1-4.11.2/build/moxie-rtems4.11/c/moxiesim/testsuites'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/../../../../moxie-rtems4.11/bin/ld: final link failed: Bad value
}}}
```

* **summary**
```text
RTEMS 4.11.2 Moxie build fails
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3068#comment:1|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3068#comment:1|status changed from new to closed resolution set to wontfix If you want Moxie support use master.|Mon, 05 Feb 2018 05:42:57 GMT|Ticket|
|https://devel.rtems.org/ticket/3068#comment:2|Chris Johns|component changed|https://devel.rtems.org/ticket/3068#comment:2|component changed from unspecified to tool/gcc|Mon, 12 Feb 2018 03:58:04 GMT|Ticket|
## [2460](https://devel.rtems.org/ticket/2460)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal| |normal|closed|arch/arm|duplicate| |2460| |4.11.3|Adit|defect| | |
* **description**
```text
This bug pertains to the ARM Generic Interrupt Controller (GIC) register utility functions in 

{{{c/src/lib/libbsp/arm/shared/include/arm-gic.h}}}

The following routines all use the macro {{{GIC_ID_TO_TWO_BITS_REG_OFFSET(id)}}}:

{{{
gic_id_get_handling_mode
gic_id_set_handling_mode
gic_id_get_trigger_mode
gic_id_set_trigger_mode
}}}

These routines set the {{{GIC_ICFGRn}}} set of registers. These registers have 2-bit bit fields. Let's take the trigger mode routines as an example of the bug, but it applies to the handling mode as well. The GIC specification from ARM states that for a particular interrupt ID ''m'' the register ''n'' and bit field ''F'' is found by:

''n = m DIV 16''
''F = m MOD 16''

And the bit location in register ''n'' is defined as ''[2F+1:2F]''. However, the macro  {{{GIC_ID_TO_TWO_BITS_REG_OFFSET(id)}}} and the routines that use it, set bits ''[F+1:F]''.

I have tested this by using the set_trigger_mode routine to set an interrupt to be edge triggered, but the correct bit does not get set, and the interrupt still behaves in a level triggered fashion. When I adjust the macro to have a {{{<< 1}}} it works correctly.

If someone can verify my logic at least, then I can submit a tested patch.
```

* **summary**
```text
arm-gic.h - GIC_ID_TO_TWO_BITS_REG_OFFSET(id) incorrectly defined
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2460#comment:1|Sebastian Huber| |https://devel.rtems.org/ticket/2460#comment:1|Yes, please send a patch to devel(at)rtems.org and add "Close #2460." to the commit message.|Tue, 10 Nov 2015 07:16:01 GMT|Ticket|
|https://devel.rtems.org/ticket/2460#comment:2|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2460#comment:2|milestone changed from 4.11.1 to 4.11.2|Thu, 26 Jan 2017 07:16:00 GMT|Ticket|
|https://devel.rtems.org/ticket/2460#comment:3|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2460#comment:3|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:04:45 GMT|Ticket|
|https://devel.rtems.org/ticket/2460#comment:4|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2460#comment:4|milestone changed from 4.11.3 to Indefinite Requires funding.|Mon, 05 Feb 2018 04:40:23 GMT|Ticket|
|https://devel.rtems.org/ticket/2460#comment:5|Sebastian Huber|status, milestone changed; resolution set|https://devel.rtems.org/ticket/2460#comment:5|status changed from new to closed resolution set to duplicate milestone changed from Indefinite to 4.11.3 Duplicate of #3002.|Mon, 05 Feb 2018 07:48:15 GMT|Ticket|
|https://devel.rtems.org/ticket/2460#comment:6|Sebastian Huber|component changed|https://devel.rtems.org/ticket/2460#comment:6|component changed from bsps to arch/arm|Mon, 05 Feb 2018 07:59:59 GMT|Ticket|
### attachments
|guid|creator|title|link|description|attachment_link|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2460|Adit|attachment set|https://devel.rtems.org/ticket/2460|attachment set to 0001-Fixes-GIC_ID_TO_TWO_BITS_REG_OFFSET-macro-in-arm-gic.patch|https://devel.rtems.org/attachment/ticket/2460/0001-Fixes-GIC_ID_TO_TWO_BITS_REG_OFFSET-macro-in-arm-gic.patch|Wed, 11 Nov 2015 04:42:44 GMT|Ticket|
## [3074](https://devel.rtems.org/ticket/3074)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool/rsb|fixed| |3074| |4.11.3|Chris Johns|defect| | |
* **description**
```text
RTEMS 4.11.2 Released Tools version is wrong:
{{{
$ /opt/work/rtems/4.11/bin/arm-rtems4.11-gcc --version
arm-rtems4.11-gcc (GCC) 4.9.3 20150626 (RTEMS 4.11, RSB no-repo, Newlib 2.2.0.20150423)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
}}}

The RSB field should be `4.11.2`.
```

* **summary**
```text
gcc version report for released tools is wrong.
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3074#comment:1|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/3074#comment:1|status changed from assigned to closed resolution set to fixed In 3822803/rtems-source-builder: gcc: Use the RSB release for released tools. Using the RSB release version for the gcc version string means the tools have a version string that matches the release. Close #3074|Wed, 07 Feb 2018 21:54:15 GMT|Ticket|
## [3119](https://devel.rtems.org/ticket/3119)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|blocker|Chris Johns|highest|closed|doc|fixed| |3119| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Back port the master (4.12) fix.
```

* **summary**
```text
Docs failed to build PDF with the latest Sphinx.
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3119#comment:1|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/3119#comment:1|status changed from assigned to closed resolution set to fixed In ba143e0/rtems-docs: pdf: Update the RTEMS style to work recent Sphinx versions. Closes #3119.|Sun, 03 Sep 2017 05:40:24 GMT|Ticket|
|https://devel.rtems.org/ticket/3119#comment:2|Sebastian Huber|component changed|https://devel.rtems.org/ticket/3119#comment:2|component changed from Documentation to doc|Tue, 10 Oct 2017 06:06:29 GMT|Ticket|
## [3067](https://devel.rtems.org/ticket/3067)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal| |normal|closed|tool/gcc|wontfix| |3067| |4.11.3|Chris Johns|defect| | |
* **description**
```text
CPU Top does not build:
{{{
m32c-rtems4.11-gcc --pipe -DHAVE_CONFIG_H   -I.. -I../../cpukit/../../../m32csim/lib/include   -g -O0 -MT monitor/mon-queue.o -MD -MP -MF $depbase.Tpo -c -o monitor/mon-queue.o ../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/monitor/mon-queue.c &&\
mv -f $depbase.Tpo $depbase.Po
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c: In function 'print_memsize':
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:159:20: warning: integer overflow in expression [-Woverflow]
   if (size > (1024 * 1024))
                    ^
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:161:40: warning: integer overflow in expression [-Woverflow]
                           size / (1024 * 1024), label);
                                        ^
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:161:32: warning: division by zero [-Wdiv-by-zero]
                           size / (1024 * 1024), label);
                                ^
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c: In function 'rtems_cpuusage_top_thread':
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:309:33: warning: cast to pointer from integer of different size [-Wint-to-pointer-cast]
   rtems_cpu_usage_data*  data = (rtems_cpu_usage_data*) arg;
                                 ^
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c: In function 'rtems_cpu_usage_top_with_plugin':
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:617:36: warning: cast from pointer to integer of different size [-Wpointer-to-int-cast]
     id, rtems_cpuusage_top_thread, (rtems_task_argument) &data
                                    ^
depbase=`echo monitor/mon-driver.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
m32c-rtems4.11-gcc --pipe -DHAVE_CONFIG_H   -I.. -I../../cpukit/../../../m32csim/lib/include   -g -O0 -MT monitor/mon-driver.o -MD -MP -MF $depbase.Tpo -c -o monitor/mon-driver.o ../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/monitor/mon-driver.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo monitor/mon-itask.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
m32c-rtems4.11-gcc --pipe -DHAVE_CONFIG_H   -I.. -I../../cpukit/../../../m32csim/lib/include   -g -O0 -MT monitor/mon-itask.o -MD -MP -MF $depbase.Tpo -c -o monitor/mon-itask.o ../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/monitor/mon-itask.c &&\
mv -f $depbase.Tpo $depbase.Po
In file included from ../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/dummy/default-configuration.c:113:0:
../../cpukit/../../../m32csim/lib/include/rtems/confdefs.h: At top level:
../../cpukit/../../../m32csim/lib/include/rtems/confdefs.h:1483:46: warning: cast from pointer to integer of different size [-Wpointer-to-int-cast]
   #define CONFIGURE_INIT_TASK_ARGUMENTS     ((rtems_task_argument) &bsp_boot_cmdline)
                                              ^
../../cpukit/../../../m32csim/lib/include/rtems/confdefs.h:1514:7: note: in expansion of macro 'CONFIGURE_INIT_TASK_ARGUMENTS'
       CONFIGURE_INIT_TASK_ARGUMENTS
       ^
../../cpukit/../../../m32csim/lib/include/rtems/confdefs.h:1515:5: error: initializer element is not constant
     }
     ^
../../cpukit/../../../m32csim/lib/include/rtems/confdefs.h:1515:5: error: (near initialization for 'Initialization_tasks[0].argument')
}}}
```

* **summary**
```text
RTEMS 4.11.2 M32C build fails
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3067#comment:1|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3067#comment:1|status changed from new to closed resolution set to wontfix If you want M32C support use master.|Mon, 05 Feb 2018 05:42:28 GMT|Ticket|
|https://devel.rtems.org/ticket/3067#comment:2|Chris Johns|component changed|https://devel.rtems.org/ticket/3067#comment:2|component changed from unspecified to tool/gcc|Mon, 12 Feb 2018 03:57:48 GMT|Ticket|
## [2671](https://devel.rtems.org/ticket/2671)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Joel Sherrill|normal|closed|tool/rsb|wontfix| |2671| |4.11.3|Joel Sherrill|defect| | |
* **description**
```text
I recall needing to sync the binutils and gcc. Checking an old install for 4.11, I noticed that the gcc seems to match what is configured but the binutils is older (2.25).

[joel@rtbf64c ~]$ ~/rtems-4.11-work/tools/4.11/bin/moxie-rtems4.11-as --version
GNU assembler (GNU Binutils) 2.25
Copyright (C) 2014 Free Software Foundation, Inc.
This program is free software; you may redistribute it under the terms of
the GNU General Public License version 3 or later.
This program has absolutely no warranty.
This assembler was configured for a target of `moxie-rtems4.11'.
[joel@rtbf64c ~]$ ~/rtems-4.11-work/tools/4.11/bin/moxie-rtems4.11-gcc --version
moxie-rtems4.11-gcc (GCC) 4.9.3 20150626 (RTEMS 4.11, RSB 075ed1c8e2363ec7fcfcaec6b648222597009f20, Newlib 2.2.0.20150423)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.



Error below:

/home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-linux-gnu-1/build/./gcc/xgcc -B/home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-linux-gnu-1/build/./gcc/ -nostdinc -B/home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-linux-gnu-1/build/moxie-rtems4.11/newlib/ -isystem /home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-linux-gnu-1/build/moxie-rtems4.11/newlib/targ-include -isystem /home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-linux-gnu-1/gcc-4.9.3/newlib/libc/include -B/home/joel/rtems-4.11-work/tools/4.11/moxie-rtems4.11/bin/ -B/home/joel/rtems-4.11-work/tools/4.11/moxie-rtems4.11/lib/ -isystem /home/joel/rtems-4.11-work/tools/4.11/moxie-rtems4.11/include -isystem /home/joel/rtems-4.11-work/tools/4.11/moxie-rtems4.11/sys-include    -g -O2 -mel -O2 -I../../../../gcc-4.9.3/libgcc/../newlib/libc/sys/rtems/include -g -O2 -DIN_GCC  -DCROSS_DIRECTORY_STRUCTURE  -W -Wall -Wno-narrowing -Wwrite-strings -Wcast-qual -Wstrict-prototypes -Wmissing-prototypes -Wold-style-definition  -isystem ./include   -g -DIN_LIBGCC2 -fbuilding-libgcc -fno-stack-protector -Dinhibit_libc  -I. -I. -I../../.././gcc -I../../../../gcc-4.9.3/libgcc -I../../../../gcc-4.9.3/libgcc/. -I../../../../gcc-4.9.3/libgcc/../gcc -I../../../../gcc-4.9.3/libgcc/../include  -DHAVE_CC_TLS -DUSE_EMUTLS -o _ashldi3.o -MT _ashldi3.o -MD -MP -MF _ashldi3.dep -DL_ashldi3 -c ../../../../gcc-4.9.3/libgcc/libgcc2.c -fvisibility=hidden -DHIDE_EXPORTS
/tmp/cctmIP4r.s: Assembler messages:
/tmp/cctmIP4r.s:26: Error: unknown opcode sub.l $r1,$r2
Makefile:463: recipe for target '_negdi2.o' failed
make[4]: *** [_negdi2.o] Error 1
make[4]: *** Waiting for unfinished jobs....
/tmp/ccaQiOcs.s: /tmp/ccWFtIrs.s: Assembler messages:
Assembler messages:
/tmp/ccaQiOcs.s:22: Error: unknown opcode sub.l $r3,$r2
/tmp/ccWFtIrs.s:44: Error: unknown opcode mul.l $r12,$r6
/tmp/ccWFtIrs.s:46: Error: unknown opcode mul.l $r4,$r1
/tmp/ccWFtIrs.s:49: Error: unknown opcode mul.l $r8,$r1
/tmp/ccWFtIrs.s:52: Error: unknown opcode mul.l $r3,$r6
/tmp/ccWFtIrs.s:56: Error: unknown opcode add.l $r6,$r3
/tmp/ccWFtIrs.s:61: Error: unknown opcode add.l $r3,$r6
/tmp/ccWFtIrs.s:68: Error: unknown opcode add.l $r1,$r4
/tmp/ccWFtIrs.s:75: Error: unknown opcode add.l $r1,$r4
/tmp/ccWFtIrs.s:89: Error: unknown opcode mul.l $r0,$r4
/tmp/ccWFtIrs.s:93: Error: unknown opcode mul.l $r2,$r4
/tmp/ccWFtIrs.s:95: Error: unknown opcode add.l $r0,$r2
/tmp/ccWFtIrs.s:99: Error: unknown opcode add.l $r0,$r12
/tmp/ccWFtIrs.s:100: Error: unknown opcode add.l $r1,$r2
Makefile:463: recipe for target '_muldi3.o' failed
make[4]: *** [_muldi3.o] Error 1
make[4]: *** [_lshrdi3.o] Error 1

```

* **summary**
```text
moxie tools fail to build on 4.11
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2671#comment:1|Joel Sherrill| |https://devel.rtems.org/ticket/2671#comment:1|The following is sufficient to get a toolset built. diff --git a/rtems/config/4.11/rtems-moxie.bset b/rtems/config/4.11/rtems-moxie.bset index 0473f02..c8f764e 100644 --- a/rtems/config/4.11/rtems-moxie.bset +++ b/rtems/config/4.11/rtems-moxie.bset @@ -22,7 +22,7 @@ 4.11/rtems-autotools devel/expat-2.1.0-1 devel/dtc-1.4.1-1 -tools/rtems-binutils-2.26-1 +tools/rtems-binutils-2.25-1 tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1 tools/rtems-gdb-7.9-1 tools/rtems-tools-4.11-1|Mon, 21 Mar 2016 14:54:34 GMT|Ticket|
|https://devel.rtems.org/ticket/2671#comment:2|Joel Sherrill| |https://devel.rtems.org/ticket/2671#comment:2|moxie/moxiesim built but didn't run: Starting program: /home/joel/rtems-4.11-work/rtems-testing/rtems/ticker-executables/moxie-moxiesim-ticker.ralf sim-core.c:476: assertion failed - (addr & (nr_bytes - 1)) == 0 Aborted (core dumped) But at least the tools build. I will confirm status on the master once I get time.|Mon, 21 Mar 2016 15:27:18 GMT|Ticket|
|https://devel.rtems.org/ticket/2671#comment:3|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2671#comment:3|milestone changed from 4.11 to 4.11.2|Thu, 26 Jan 2017 07:05:37 GMT|Ticket|
|https://devel.rtems.org/ticket/2671#comment:4|Chris Johns|owner, status changed|https://devel.rtems.org/ticket/2671#comment:4|owner changed from Chris Johns to Joel Sherrill status changed from new to assigned I suggest you create a patch and apply to the RSB to resolve this. Please close the ticket in the commit. Thanks.|Tue, 21 Mar 2017 04:07:24 GMT|Ticket|
|https://devel.rtems.org/ticket/2671#comment:5|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2671#comment:5|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2671#comment:6|Chris Johns| |https://devel.rtems.org/ticket/2671#comment:6|If you want Moxie support use master.|Mon, 05 Feb 2018 05:45:16 GMT|Ticket|
|https://devel.rtems.org/ticket/2671#comment:7|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2671#comment:7|status changed from assigned to closed resolution set to wontfix|Mon, 05 Feb 2018 05:45:26 GMT|Ticket|
## [3289](https://devel.rtems.org/ticket/3289)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool/rsb|fixed| |3289| |4.11.3|Chris Johns|enhancement| | |
* **description**
```text
To help the long term support of the 4.11 branch back port the RSB changes to support mailing list posting of builds.
```

* **summary**
```text
RSB backport changes to support mailing list posting of builds.
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3289#comment:1|Chris Johns|status changed|https://devel.rtems.org/ticket/3289#comment:1|status changed from assigned to accepted|Mon, 05 Feb 2018 04:33:55 GMT|Ticket|
|https://devel.rtems.org/ticket/3289#comment:2|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3289#comment:2|status changed from accepted to closed resolution set to fixed|Mon, 05 Feb 2018 23:17:12 GMT|Ticket|
## [3107](https://devel.rtems.org/ticket/3107)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|blocker|Chris Johns|highest|closed|tool/gcc|fixed|GCC FreeBSD|3107| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Building GCC breaks on FreeBDS 11.1. See https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=212465 for details.
```

* **summary**
```text
Building gcc-4.9.3 is broken on FreeBSD 11.1
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3107#comment:1|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/3107#comment:1|status changed from assigned to closed resolution set to fixed In bb43afd/rtems-source-builder: Building gcc-4.9.3 is broken on FreeBSD 11.1 Reference the patch for the FreeBSD port. See ticket: ​https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=212465 Closes #3107.|Wed, 23 Aug 2017 01:08:53 GMT|Ticket|
|https://devel.rtems.org/ticket/3107#comment:2|Sebastian Huber|component changed|https://devel.rtems.org/ticket/3107#comment:2|component changed from GCC to tool/gcc|Tue, 10 Oct 2017 05:58:26 GMT|Ticket|
## [3031](https://devel.rtems.org/ticket/3031)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|blocker|Amar Takhar|normal|closed|doc|fixed| |3031|Joel@…|4.11.3|Chris Johns|infra| | |
* **description**
```text
Giving jails such as docs and sync access to an area of the TrueNAS storage would make building and moving of the docs from sync to the docs website much simpler.

Currently I build the docs on a server in Sydney, copy them to the RTEMS FTP server using an ssh key and docs.rtems.org picks up the copy. I like to make the whole process local to the RTEMS servers and not rely on gear here with my dodgy connection and me needing to monitor it.
```

* **summary**
```text
Give docs.rtems.org and sync.rtems.org jails access to the TrueNAS storage.
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3031#comment:1|Joel Sherrill|cc set|https://devel.rtems.org/ticket/3031#comment:1|cc Joel@… added|Wed, 07 Jun 2017 06:58:09 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:2|Amar Takhar| |https://devel.rtems.org/ticket/3031#comment:2|OK I will look into this Tonight or Friday (2017-06-09). I'll try to get it done quickly tonight but that will depend on what time I get home.|Wed, 07 Jun 2017 11:45:10 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:3|Chris Johns| |https://devel.rtems.org/ticket/3031#comment:3|How is this going?|Thu, 15 Jun 2017 02:27:38 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:4|Amar Takhar| |https://devel.rtems.org/ticket/3031#comment:4|Sigh, thanks for the reminder. I need to setup auto-reminders for trac to harass me. I need to fix something in the switch to give this machine access to the VLAN I am away tomorrow (2016-06-15) but I will be back Friday (2016-06-16). I will take care of this then and have entered it into my calendar.|Thu, 15 Jun 2017 02:34:32 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:5|Chris Johns| |https://devel.rtems.org/ticket/3031#comment:5|Hey no problem, and thanks. Let me know how it goes.|Thu, 15 Jun 2017 02:35:56 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:6|Amar Takhar| |https://devel.rtems.org/ticket/3031#comment:6|FYI an update I'm almost done this just took some time to clean up a few VLANs on the switch.|Mon, 19 Jun 2017 19:00:38 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:7|Chris Johns|severity, milestone changed|https://devel.rtems.org/ticket/3031#comment:7|severity changed from major to blocker milestone changed from 4.11.2 to 4.11.3 I cannot wait any longer and will release RTEMS 4.11.2. Moving this to 4.11.3 and making it a blocker issue.|Tue, 11 Jul 2017 00:35:11 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:8|Chris Johns|owner, status changed|https://devel.rtems.org/ticket/3031#comment:8|owner changed from chrisj@… to Amar Takhar status changed from new to assigned Assign to Amar.|Tue, 11 Jul 2017 00:35:41 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:9|Amar Takhar| |https://devel.rtems.org/ticket/3031#comment:9|Huh, I thought I did this already I will look at it in the morning. Sorry.|Tue, 11 Jul 2017 02:23:30 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:10|Amar Takhar| |https://devel.rtems.org/ticket/3031#comment:10|I think all I need to do is attach the share, it's late here I will do it in the morning.|Tue, 11 Jul 2017 02:24:07 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:11|Amar Takhar| |https://devel.rtems.org/ticket/3031#comment:11|This is done please check to make sure it works.|Tue, 11 Jul 2017 12:30:19 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:12|Chris Johns| |https://devel.rtems.org/ticket/3031#comment:12|Replying to Amar Takhar: This is done please check to make sure it works. Thank you. I will take a look over this week.|Tue, 11 Jul 2017 23:43:30 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:13|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3031#comment:13|status changed from assigned to closed resolution set to fixed|Sun, 03 Sep 2017 05:37:17 GMT|Ticket|
|https://devel.rtems.org/ticket/3031#comment:14|Sebastian Huber|component changed|https://devel.rtems.org/ticket/3031#comment:14|component changed from Documentation to doc|Tue, 10 Oct 2017 06:06:29 GMT|Ticket|
## [3092](https://devel.rtems.org/ticket/3092)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|score|fixed| |3092| |4.11.3|Sebastian Huber|defect| | |
* **summary**
```text
ARM: Test spcontext01 fails on Cortex-R4
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3092#comment:1|Sebastian Huber|summary changed|https://devel.rtems.org/ticket/3092#comment:1|summary changed from Test spcontext01 fails on Cortex-R5 to ARM: Test spcontext01 fails on Cortex-R5|Thu, 10 Aug 2017 06:10:33 GMT|Ticket|
|https://devel.rtems.org/ticket/3092#comment:2|Sebastian Huber|summary changed|https://devel.rtems.org/ticket/3092#comment:2|summary changed from ARM: Test spcontext01 fails on Cortex-R5 to ARM: Test spcontext01 fails on Cortex-R4|Thu, 10 Aug 2017 06:21:47 GMT|Ticket|
|https://devel.rtems.org/ticket/3092#comment:3|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/3092#comment:3|status changed from assigned to closed resolution set to fixed In 5cc276e/rtems: arm: Fix CPU context validation for Cortex-R4 Do not touch the FPSCR[QC] bit since this is DNM/RAZ on Cortex-R4. Close #3092.|Thu, 10 Aug 2017 06:24:11 GMT|Ticket|
## [2610](https://devel.rtems.org/ticket/2610)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool|wontfix| |2610| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Building unhex.c on Windows gives the following error:

{{{
gcc -DHAVE_CONFIG_H -I. -I/c/opt/rtems/kernel/rtems.git/tools/build     -g -O2 -MT rtems-bin2c.o -MD -MP -MF .deps/rtems-bin2c.Tpo -c -o rtems-bin2c.o /c/opt/rtems/kernel/rtems.git/tools/build/rtems-bin2c.c
In file included from C:/opt/rtems/kernel/rtems.git/tools/build/unhex.c:36:0:
C:/opt/rtems/kernel/rtems.git/tools/build/unhex.c: In function 'error':
C:/opt/rtems/kernel/rtems.git/tools/build/unhex.c:687:16: warning: '_errno' redeclared without dllimport attribute: previous dllimport ignored [-Wattributes]
     extern int errno;
                ^
}}}
```

* **summary**
```text
unhex.c does not build on MSYS2
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2610#comment:1|Chris Johns| |https://devel.rtems.org/ticket/2610#comment:1|This is a warning and not fatal. I think it should still be cleaned up.|Tue, 23 Feb 2016 05:22:17 GMT|Ticket|
|https://devel.rtems.org/ticket/2610#comment:2|Chris Johns|priority, severity, milestone changed|https://devel.rtems.org/ticket/2610#comment:2|priority changed from highest to normal severity changed from critical to normal milestone changed from 4.11 to 4.11.1|Tue, 23 Feb 2016 05:22:50 GMT|Ticket|
|https://devel.rtems.org/ticket/2610#comment:3|Chris Johns|status changed|https://devel.rtems.org/ticket/2610#comment:3|status changed from new to accepted|Wed, 24 Feb 2016 03:15:50 GMT|Ticket|
|https://devel.rtems.org/ticket/2610#comment:4|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2610#comment:4|milestone changed from 4.11.1 to 4.11.2|Thu, 26 Jan 2017 07:16:00 GMT|Ticket|
|https://devel.rtems.org/ticket/2610#comment:5|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2610#comment:5|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2610#comment:6|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2610#comment:6|status changed from accepted to closed resolution set to wontfix I am closing this ticket. The tool can be fixed on master.|Wed, 07 Feb 2018 03:00:35 GMT|Ticket|
## [3093](https://devel.rtems.org/ticket/3093)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| |normal|Sebastian Huber|normal|closed|score|fixed| |3093| |4.11.3|Sebastian Huber|enhancement| | |
* **description**
```text
The context validation function did not take care of the IT[7:0] bit field of the PSR.  Add a code block that validates this processor state.
```

* **summary**
```text
ARM: Validate IT[7:0] bit field in PSR on Thumb 2 targets
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3093#comment:1|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/3093#comment:1|In a95d909/rtems: arm: Validate IT[7:0] bit field of PSR Update #3093.|Thu, 10 Aug 2017 06:19:09 GMT|Ticket|
|https://devel.rtems.org/ticket/3093#comment:2|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/3093#comment:2|In 0daa8ab/rtems: arm: Use ARM code on Thumb 1 targets Update #3093.|Thu, 10 Aug 2017 07:04:55 GMT|Ticket|
|https://devel.rtems.org/ticket/3093#comment:3|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/3093#comment:3|status changed from assigned to closed resolution set to fixed In 7d097c5/rtems: arm: Validate IT[7:0] bit field of PSR Close #3093.|Thu, 10 Aug 2017 07:25:32 GMT|Ticket|
## [3162](https://devel.rtems.org/ticket/3162)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|score|fixed| |3162| |4.11.3|Sebastian Huber|defect| | |
* **description**
```text
The RTEMS_MILLISECONDS_TO_TICKS() macro doesn't round up. Do not use it to calculate the program timeout in ticks.  Check program done condition after the timeout check to account for pre-emptions.
```

* **summary**
```text
I2C EEPROM driver uses incorrect program timeout handling
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3162#comment:1|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/3162#comment:1|In 9c063df/rtems: i2c: Fix EEPROM driver program timeout handling The RTEMS_MILLISECONDS_TO_TICKS() macro doesn't round up. Do not use it to calculate the program timeout in ticks. Check program done condition after the timeout check to account for pre-emptions. Update #3162.|Mon, 02 Oct 2017 11:41:28 GMT|Ticket|
|https://devel.rtems.org/ticket/3162#comment:2|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/3162#comment:2|status changed from assigned to closed resolution set to fixed In 1a21831/rtems: i2c: Fix EEPROM driver program timeout handling The RTEMS_MILLISECONDS_TO_TICKS() macro doesn't round up. Do not use it to calculate the program timeout in ticks. Check program done condition after the timeout check to account for pre-emptions. Close #3162.|Mon, 02 Oct 2017 11:47:06 GMT|Ticket|
## [2747](https://devel.rtems.org/ticket/2747)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|lib/dl|fixed| |2747|Ryan Slabaugh|4.11.3|Patrick Gauvin|defect|3298| |
* **description**
```text
Expected behavior of dlerror:
- The error is cleared after each invocation
- `NULL` is returned when no error is set
- Return value is `char *`, not `const char *`
http://pubs.opengroup.org/onlinepubs/9699919799/functions/dlerror.html

I've attached patches that address these issues, please critique them and I will submit to the development mailing list. They should also apply to master, but they were generated against 4.11.

Development Environment:
- '''RTEMS Version:''' 4.11 (Branch "4.11", commit 3f72dda6ee518d3ea04341ad4df079ecb1895ef7)
- '''System Type:''' ARM Cortex-A9, xilinx_zynq_a9_qemu BSP
- '''GCC Version:'''

  arm-rtems4.11-gcc (GCC) 4.9.3 20150626 (RTEMS 4.11, RSB 1675a733536d1aec2020011e5e522497a442561a (HEAD, origin/4.11, 4.11), Newlib 2.2.0.20150423)
- '''RTEMS Configure Options:'''

  ../rtems/configure --target=arm-rtems4.11 --enable-rtemsbsp="xilinx_zynq_a9_qemu xilinx_zynq_zedboard xilinx_zynq_csp_cots xilinx_zynq_csp_hybrid" --enable-tests=samples --enable-posix --prefix=$HOME/development/rtems/4.11 --disable-networking

```

* **summary**
```text
dlerror non-conformance
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2747#comment:1|Chris Johns|milestone set|https://devel.rtems.org/ticket/2747#comment:1|milestone set to 4.11.3|Mon, 14 Aug 2017 00:12:35 GMT|Ticket|
|https://devel.rtems.org/ticket/2747#comment:2|Chris Johns|status changed|https://devel.rtems.org/ticket/2747#comment:2|status changed from new to accepted|Mon, 05 Feb 2018 04:41:10 GMT|Ticket|
|https://devel.rtems.org/ticket/2747#comment:3|Chris Johns|blocking set|https://devel.rtems.org/ticket/2747#comment:3|blocking set to 3298|Thu, 08 Feb 2018 03:37:08 GMT|Ticket|
|https://devel.rtems.org/ticket/2747#comment:4|Chris Johns <chrisj@…>| |https://devel.rtems.org/ticket/2747#comment:4|In 7093cb5e/rtems: libtest/dl01: Add dlerror tests. Update #2747|Thu, 08 Feb 2018 22:32:42 GMT|Ticket|
|https://devel.rtems.org/ticket/2747#comment:5|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2747#comment:5|status changed from accepted to closed resolution set to fixed|Thu, 08 Feb 2018 22:34:06 GMT|Ticket|
|https://devel.rtems.org/ticket/2747#comment:6|Chris Johns <chrisj@…>| |https://devel.rtems.org/ticket/2747#comment:6|In 7093cb5e/rtems: libtest/dl01: Add dlerror tests. Update #2747|Fri, 16 Feb 2018 02:16:46 GMT|Ticket|
### attachments
|guid|creator|title|link|description|attachment_link|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2747|Patrick Gauvin|attachment set|https://devel.rtems.org/ticket/2747|attachment set to 0001-libdl-Clear-error-between-dlerror-invocations.patch|https://devel.rtems.org/attachment/ticket/2747/0001-libdl-Clear-error-between-dlerror-invocations.patch|Sun, 26 Jun 2016 17:36:02 GMT|Ticket|
|https://devel.rtems.org/ticket/2747|Patrick Gauvin|attachment set|https://devel.rtems.org/ticket/2747|attachment set to 0002-libdl-dlerror-return-NULL-when-no-error.patch|https://devel.rtems.org/attachment/ticket/2747/0002-libdl-dlerror-return-NULL-when-no-error.patch|Sun, 26 Jun 2016 17:36:13 GMT|Ticket|
|https://devel.rtems.org/ticket/2747|Patrick Gauvin|attachment set|https://devel.rtems.org/ticket/2747|attachment set to 0003-libdl-Fix-dlerror-return-type.patch|https://devel.rtems.org/attachment/ticket/2747/0003-libdl-Fix-dlerror-return-type.patch|Sun, 26 Jun 2016 17:36:22 GMT|Ticket|
|https://devel.rtems.org/ticket/2747|Patrick Gauvin|attachment set|https://devel.rtems.org/ticket/2747|attachment set to 0004-Update-dlerror-usage.patch|https://devel.rtems.org/attachment/ticket/2747/0004-Update-dlerror-usage.patch|Sun, 26 Jun 2016 17:36:41 GMT|Ticket|
## [2538](https://devel.rtems.org/ticket/2538)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|blocker|Chris Johns|high|closed|tool/rsb|worksforme| |2538| |4.11.3|Joel Sherrill|defect| | |
* **description**
```text
From the log building arm-rtems4.11 target. It is in rtems-tools and the ln only has one argument. Looks like I can expect all targets to fail.

+ /bin/rm -rf rtems-tools-4.11
+ ln -s /data/home/joel/rtems-4.11-work/rtems-source-builder/rtems/sources/git/rtems-tools.git
+ cd rtems-tools-4.11
/data/home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/rtems-tools-4.11-1/doit: line 85: cd: rtems-tools-4.11: No such file or directory
shell cmd failed: /bin/sh -ex  /data/home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/rtems-tools-4.11-1/doit
error: building rtems-tools-4.11-1



```

* **summary**
```text
4.11 tools on RSB 4.11 branch fail to build
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2538#comment:1|Chris Johns|status changed|https://devel.rtems.org/ticket/2538#comment:1|status changed from new to accepted|Wed, 20 Jan 2016 00:14:27 GMT|Ticket|
|https://devel.rtems.org/ticket/2538#comment:2|Mario Gruber| |https://devel.rtems.org/ticket/2538#comment:2|Duplicate of #2495|Mon, 25 Jan 2016 16:53:59 GMT|Ticket|
|https://devel.rtems.org/ticket/2538#comment:3|Chris Johns| |https://devel.rtems.org/ticket/2538#comment:3|I suspect the issue is the git command in the config file attempts to change to the 4.11 branch before a pull and if you have a repo in your sources directory that was cloned before the 4.11 branch was added it fails. I have changed the pull to be before the branch.|Fri, 19 Feb 2016 03:11:25 GMT|Ticket|
|https://devel.rtems.org/ticket/2538#comment:4|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2538#comment:4|milestone changed from 4.11.1 to 4.11.2|Thu, 26 Jan 2017 07:16:00 GMT|Ticket|
|https://devel.rtems.org/ticket/2538#comment:5|Chris Johns| |https://devel.rtems.org/ticket/2538#comment:5|I just built 4.11/rtems-arm with out error. I cannot reproduce this on FreeBSD. Can you please provide some more information?|Tue, 21 Mar 2017 03:12:16 GMT|Ticket|
|https://devel.rtems.org/ticket/2538#comment:6|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2538#comment:6|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2538#comment:7|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2538#comment:7|status changed from accepted to closed resolution set to worksforme I cannot repeat this and the related code looks OK so without further details I cannot do much with this but report.|Wed, 07 Feb 2018 05:15:39 GMT|Ticket|
## [3257](https://devel.rtems.org/ticket/3257)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| |normal|Sebastian Huber|normal|closed|fs/fat|fixed| |3257| |4.11.3|Sebastian Huber|defect| | |
* **description**
```text
Take care that a file in the root directory with the same name as the
volume name can be found.
```

* **summary**
```text
fat: Support files in the root directoy with the same name as the volume label
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3257#comment:1|Christian Mauderer <Christian.Mauderer@…>| |https://devel.rtems.org/ticket/3257#comment:1|In ca835e56/rtems: dosfs: Fix files with same name as volume name. Take care that a file in the root directory with the same name as the volume name can be found. Update #3257.|Tue, 05 Dec 2017 07:01:08 GMT|Ticket|
|https://devel.rtems.org/ticket/3257#comment:2|Christian Mauderer <Christian.Mauderer@…>|status changed; resolution set|https://devel.rtems.org/ticket/3257#comment:2|status changed from assigned to closed resolution set to fixed In 004a63e/rtems: dosfs: Fix files with same name as volume name. Take care that a file in the root directory with the same name as the volume name can be found. Close #3257.|Tue, 05 Dec 2017 07:03:36 GMT|Ticket|
## [2639](https://devel.rtems.org/ticket/2639)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|high|closed|tool/rsb|duplicate|RSB 4.11.0-RC2|2639| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Long path support on Windows requires the use of Unicode paths. The current path is not Unicode and some paths in C++ can be longer than 255 character when building the release candidates using the standard paths in the releases.

The solution is to change paths.py so it's host call returns a Unicode string. The also requires changes to the macro key logic to convert any unicode string to an ascii string, all macro keys are ascii. Also the execute module needs to better manage Unicode strings.
```

* **summary**
```text
RSB long path support on Windows is still broken.
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2639#comment:1|Chris Johns|status changed|https://devel.rtems.org/ticket/2639#comment:1|status changed from new to accepted|Mon, 14 Mar 2016 04:26:04 GMT|Ticket|
|https://devel.rtems.org/ticket/2639#comment:2|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2639#comment:2|milestone changed from 4.11 to 4.11.2|Thu, 26 Jan 2017 07:05:05 GMT|Ticket|
|https://devel.rtems.org/ticket/2639#comment:3|Chris Johns| |https://devel.rtems.org/ticket/2639#comment:3|This is a major change and I do not think it is suitable for a release branch. This change should only happen on master.|Tue, 21 Mar 2017 03:15:23 GMT|Ticket|
|https://devel.rtems.org/ticket/2639#comment:4|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2639#comment:4|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2639#comment:5|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2639#comment:5|status changed from accepted to closed resolution set to duplicate Closing this ticket as #2992 has more details.|Sat, 22 Apr 2017 22:25:30 GMT|Ticket|
## [2944](https://devel.rtems.org/ticket/2944)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|fs/fat|fixed| |2944| |4.11.3|Sebastian Huber|defect| | |
* **description**
```text
https://lists.rtems.org/pipermail/users/2017-March/031101.html

In msdos_shut_down ( msdos_fsunmount.c ) there is a call to fat_file_close( .. ) which attempts to close a file
descriptor and write a range of metadata to that file's director entry located in another cluster:

* fat_file_write_first_cluster_num
* fat_file_write_file_size
* fat_file_write_time_and_date

The problem is that this is the root node, and of course doesn't have a corresponding parent directory entry. 

In addition, the "parent directory entry" cluster number is initialised to 0x1 (FAT_ROOTDIR_CLUSTER_NUM) 
which is not working according to the FAT specification (cluster numbering starts at 2).
This actually creates a critical bug that overwrites random data to above sectors, because 2 is subtracted from 1
to calculate the sector number of the cluster -> through a series of function calls -> leads to a sector number at
the end of FAT2 (just below the start of the cluster region). The driver believes this is a FAT region (in fat_buf_release),
writes the sector to what it "thinks" is FAT1, proceeds to copy the changes to FAT2 -> adds FAT_LENGTH (8161) to sector,
leading to a write well into the cluster region, randomly overwriting files. 

The three function calls above lead to fsck complaining about disk structure:

#######

fsck from util-linux 2.27.1
fsck.fat 3.0.28 (2015-05-16)
0x41: Dirty bit is set. Fs was not properly unmounted and some data may be corrupt.
1) Remove dirty bit
2) No action
? 2
There are differences between boot sector and its backup.
This is mostly harmless. Differences: (offset:original/backup)
  65:01/00
1) Copy original to backup
2) Copy backup to original
3) No action
? 3
/  and
/APPLICAT.ION
  share clusters.
  Truncating second to 0 bytes because first is FAT32 root dir.
/APPLICAT.ION
  File size is 4096 bytes, cluster chain length is 0 bytes.
  Truncating file to 0 bytes.
Perform changes ? (y/n) n
/dev/sdm1: 14 files, 1600/1044483 clusters

########

In particular the "shared cluster" problem is caused by fat_file_write_first_cluster_num, which adds a directory
entry to the root directory cluster pointing at itself; e.g. there is a directory entry in cluster 2 pointing to
a file in cluster 2. (Note: this occurs because we have fixed the "point to cluster # 1 issue" by reading the relative
location of the root cluster node from the FAT volume info strcture). 

Removing the function call in msdos_shut_down ( .. ) to close the root file descriptor solves the problem perfectly
(clean fsck). However, we're a bit unsure about the intent behind closing the root directory. 


```

* **summary**
```text
FAT data corruption during unmount()
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2944#comment:1|Chris Johns| |https://devel.rtems.org/ticket/2944#comment:1|Replying to Sebastian Huber: Removing the function call in msdos_shut_down ( .. ) to close the root file descriptor solves the problem perfectly (clean fsck). I assume you mean fat_file_close? However, we're a bit unsure about the intent behind closing the root directory. There is memory allocated in fat_file_open which you would leak. I see the fat_file_close calls fat_buf_release and if the fs_info cache is not empty it is holding a bdbuf buffer so this would cause a leak of buffers. What about the fat_file_close calls in the msdos init call on error? Would they also cause the same problem?|Mon, 20 Mar 2017 21:21:33 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:2|slemstick| |https://devel.rtems.org/ticket/2944#comment:2|Replying to Chris Johns: Replying to Sebastian Huber: Removing the function call in msdos_shut_down ( .. ) to close the root file descriptor solves the problem perfectly (clean fsck). I assume you mean fat_file_close? Yes. However, we're a bit unsure about the intent behind closing the root directory. There is memory allocated in fat_file_open which you would leak. We fixed this issue by creating a special "root file close" function, by removing the call to fat_file_update() in fat_file_close() (which caused the corruption). I see the fat_file_close calls fat_buf_release and if the fs_info cache is not empty it is holding a bdbuf buffer so this would cause a leak of buffers. What about the fat_file_close calls in the msdos init call on error? Would they also cause the same problem? Yes, these will cause the same issues. To update / summarise this ticket a bit here: We originally attempted a fix to this problem by setting the hard-coded root directory cluster number to 2, as well as the above (remove corruption caused by fat_file_update() in fat_file_close() on unmount). However, our attempt to fix the broken root cluster numbering breaks a hashing mechanism in fat_file_open(..). This mechanism indexes open file descriptors based on 1) parent directory cluster number and 2) offset into that directory structure. The issue is that the root directory, and the file pointed to by the first directory entry in the root directory, may construct their hashes based on the same indexes: Root directory: cluster number 2, offset 0 First file in root directory: cluster number 2, offset 0 Before, this was not a problem of course, as the root directory had the hard-coded cluster number of 1, and the keys were therefore always unique. But this can actually cause a number of new issues. The fix to this problem is to set the hard-coded root cluster directory number back to 1, instead of drastically changing the key hashing method function calls and data structures, and trusting that removing calls to fat_file_update(on_root_node) are sufficient to avoid the data corruption issue described above. However, there are two other places in msdos_misc.c where the hardcoded root directory cluster number - FAT_ROOTDIR_CLUSTER_NUM - is used: msdos_get_name_node() msdos_get_dotdot_dir_info_cluster_num() Like this: if ( (MSDOS_EXTRACT_CLUSTER_NUM(dotdot_node)) == 0) { /* we handle root dir for all FAT types in the same way with the ordinary directories ( through fat_file_* calls ) */ fat_dir_pos_init(dir_pos); dir_pos->sname.cln = FAT_ROOTDIR_CLUSTER_NUM; } Which, to my understanding, will never occur as you should never have a cluster number below 2 in a compliant (msdos) FAT file system. Does anyone know the intent behind this?|Tue, 28 Mar 2017 08:15:10 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:3|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2944#comment:3|milestone changed from 4.12 to 4.12.0|Thu, 11 May 2017 07:31:02 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:4|Chris Johns|version changed|https://devel.rtems.org/ticket/2944#comment:4|version changed from 4.11 to 4.12|Mon, 14 Aug 2017 00:21:48 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:5|Sebastian Huber|owner, status changed|https://devel.rtems.org/ticket/2944#comment:5|owner changed from chrisj@… to Sebastian Huber status changed from new to assigned|Thu, 24 Aug 2017 09:56:36 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:6|Sebastian Huber|version, milestone changed|https://devel.rtems.org/ticket/2944#comment:6|version changed from 4.12 to 4.11 milestone changed from 4.12.0 to 4.11.3|Wed, 06 Sep 2017 12:39:26 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:7|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/2944#comment:7|In 4d495cf/rtems: dosfs: Fix fat_file_update() Do not update the non-existant meta-data of the root directory. Update #2944.|Wed, 06 Sep 2017 12:40:16 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:8|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/2944#comment:8|status changed from assigned to closed resolution set to fixed In a3199d91/rtems: dosfs: Fix fat_file_update() Do not update the non-existant meta-data of the root directory. Close #2944.|Wed, 06 Sep 2017 12:41:05 GMT|Ticket|
|https://devel.rtems.org/ticket/2944#comment:9|Sebastian Huber|component changed|https://devel.rtems.org/ticket/2944#comment:9|component changed from fs to fs/fat|Tue, 10 Oct 2017 06:50:58 GMT|Ticket|
## [3297](https://devel.rtems.org/ticket/3297)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|build|fixed| |3297| |4.11.3|Chris Johns|defect| | |
* **description**
```text
A check of the 4.11 branch shows:
{{{
$ grep "EXEEXT =" `find sparc-rtems4.11/c/erc32/testsuites/ -name Makefile`
  [removed some lines]
sparc-rtems4.11/c/erc32/testsuites/psxtmtests/psxtmcond05/Makefile:EXEEXT = .exe
sparc-rtems4.11/c/erc32/testsuites/psxtmtests/psxtmkey02/Makefile:EXEEXT = .exe
sparc-rtems4.11/c/erc32/testsuites/Makefile:EXEEXT = .exe
sparc-rtems4.11/c/erc32/testsuites/libtests/block16/Makefile:EXEEXT = 
sparc-rtems4.11/c/erc32/testsuites/libtests/heapwalk/Makefile:EXEEXT = 
  [removed some lines]
}}}
```

* **summary**
```text
4.11: libtests in the testsuite does not set EXEEXT to .exe
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3297#comment:1|Chris Johns|status changed; owner set|https://devel.rtems.org/ticket/3297#comment:1|owner set to Chris Johns status changed from new to accepted|Thu, 08 Feb 2018 03:27:07 GMT|Ticket|
|https://devel.rtems.org/ticket/3297#comment:2|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3297#comment:2|status changed from accepted to closed resolution set to fixed ​http://git.rtems.org/rtems/commit/?id=1a304307a2f0527023b912595c70d0c7fb17a2d0|Thu, 08 Feb 2018 22:34:45 GMT|Ticket|
## [3004](https://devel.rtems.org/ticket/3004)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|doc|fixed| |3004|chrisj@…|4.11.3|Linda Huxley|defect| | |
* **description**
```text
There are a couple of apparent typos in section "5.2 Releases" in the Note box near the bottom of the section.  The following switch is mentioned twice:

--with-rtemsbsp

However, I can't find that switch anywhere in the RSB source code.  Should that read:

--with-rtems-bsp

Thare are a couple of typos in section "5.2.1. RTEMS Tools and Kernel":

$ mv rtems-source-builder-4.11.0 4.110
$ cd 4.11.0

That should read:

$ mv rtems-source-builder-4.11.0 4.11.0
$ cd 4.11.0/rtems

```

* **summary**
```text
Typos in RTEMS User Manual 4.11.99
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3004#comment:1|Chris Johns|milestone changed|https://devel.rtems.org/ticket/3004#comment:1|milestone changed from 4.11.2 to 4.11.3|Tue, 11 Jul 2017 00:34:08 GMT|Ticket|
|https://devel.rtems.org/ticket/3004#comment:2|Sebastian Huber|component changed|https://devel.rtems.org/ticket/3004#comment:2|component changed from Documentation to doc|Tue, 10 Oct 2017 06:06:29 GMT|Ticket|
|https://devel.rtems.org/ticket/3004#comment:3|Chris Johns|owner, status changed|https://devel.rtems.org/ticket/3004#comment:3|owner changed from chrisj@… to Chris Johns status changed from new to accepted|Mon, 05 Feb 2018 03:38:30 GMT|Ticket|
|https://devel.rtems.org/ticket/3004#comment:4|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3004#comment:4|status changed from accepted to closed resolution set to fixed ​https://git.rtems.org/rtems-docs/commit/?h=4.11&id=0319856bca6a0655e453a5faa20344d97ff78c64|Mon, 05 Feb 2018 23:23:36 GMT|Ticket|
## [3066](https://devel.rtems.org/ticket/3066)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal| |normal|closed|tool/gcc|wontfix| |3066| |4.11.3|Chris Johns|defect| | |
* **description**
```text
C++ sample does not build:
{{{
Making all in iostream
gmake[6]: Entering directory '/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/lm32-rtems4.11-kernel-4.11.2-1/lm32-rtems4.11-kernel-4.11.2-1-4.11.2/build/lm32-rtems4.11/c/lm32_evr/testsuites/samples/iostream'
lm32-rtems4.11-g++ -B../../../../../lm32_evr/lib/ -specs bsp_specs -qrtems -DHAVE_CONFIG_H -I. -I../../../../../../../rtems-4.11.2/c/src/../../testsuites/samples/iostream -I..     -O0 -g -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs -MT init.o -MD -MP -MF .deps/init.Tpo -c -o init.o ../../../../../../../rtems-4.11.2/c/src/../../testsuites/samples/iostream/init.cc
cc1plus: warning: command line option '-Wmissing-prototypes' is valid for C/ObjC but not for C++
cc1plus: warning: command line option '-Wimplicit-function-declaration' is valid for C/ObjC but not for C++
cc1plus: warning: command line option '-Wstrict-prototypes' is valid for C/ObjC but not for C++
cc1plus: warning: command line option '-Wnested-externs' is valid for C/ObjC but not for C++
mv -f .deps/init.Tpo .deps/init.Po
lm32-rtems4.11-g++ -B../../../../../lm32_evr/lib/ -specs bsp_specs -qrtems -O0 -g -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs       -o cxx_iostream.exe init.o
`.gcc_except_table._ZN9__gnu_cxx7__mutexD2Ev' referenced in section `.rodata.cst4' of /build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-lm32.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/lm32-rtems4.11/4.9.3/libstdc++.a(eh_terminate.o): defined in discarded section `.gcc_except_table._ZN9__gnu_cxx7__mutexD2Ev[_ZN9__gnu_cxx7__mutexD5Ev]' of /build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-lm32.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/lm32-rtems4.11/4.9.3/libstdc++.a(eh_terminate.o)
`.gcc_except_table._ZN9__gnu_cxx7__mutexD2Ev' referenced in section `.rodata.cst4' of /build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-lm32.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/lm32-rtems4.11/4.9.3/libstdc++.a(new_handler.o): defined in discarded section `.gcc_except_table._ZN9__gnu_cxx7__mutexD2Ev[_ZN9__gnu_cxx7__mutexD5Ev]' of /build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-lm32.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/lm32-rtems4.11/4.9.3/libstdc++.a(new_handler.o)
}}}
```

* **summary**
```text
RTEMS 4.11.2 LM32 build fails
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3066#comment:1|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3066#comment:1|status changed from new to closed resolution set to wontfix If you want LM32 support use master.|Mon, 05 Feb 2018 05:41:55 GMT|Ticket|
|https://devel.rtems.org/ticket/3066#comment:2|Chris Johns|component changed|https://devel.rtems.org/ticket/3066#comment:2|component changed from unspecified to tool/gcc|Mon, 12 Feb 2018 03:57:34 GMT|Ticket|
## [3279](https://devel.rtems.org/ticket/3279)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool/rsb|fixed| |3279| |4.11.3|Chris Johns|defect| | |
* **description**
```text
The Darwin configuration expects the tool to be in `/usr/local/bin` however the `xz` is not part of the Xcode command line tools and may be built to a different path. Make the configuration path base.
```

* **summary**
```text
Make the XZ executable path based on the Darwin (MacOS) host.
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3279#comment:1|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/3279#comment:1|status changed from assigned to closed resolution set to fixed In 892b416/rtems-source-builder: darwin: Make the xz executable path based. The xz tool is not provided in Xcode command line tools and needs to built or obtained somehow. This path can be any where so relax the need for an absolute path. Close #3279|Mon, 29 Jan 2018 03:26:00 GMT|Ticket|
## [3274](https://devel.rtems.org/ticket/3274)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal| |normal|closed|tool/rsb|fixed| |3274| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Remove and clean up the configuration files that are not used on the branch.
```

* **summary**
```text
RSB remove unused tool configuration files.
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3274#comment:1|Chris Johns <chrisj@…>| |https://devel.rtems.org/ticket/3274#comment:1|In efa1677/rtems-source-builder: rtems: Update all MPC version to use GNU's FTP site. Update #3274|Fri, 19 Jan 2018 00:41:42 GMT|Ticket|
|https://devel.rtems.org/ticket/3274#comment:2|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3274#comment:2|status changed from assigned to closed resolution set to fixed|Fri, 19 Jan 2018 02:19:17 GMT|Ticket|
## [3065](https://devel.rtems.org/ticket/3065)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|chrisj@…|normal|closed|build|invalid| |3065| |4.11.3|Chris Johns|defect| | |
* **description**
```text
{{{
checking for scandir... no
../../../../../rtems-4.11.2/c/src/../../cpukit/configure: 5249: Syntax error: Bad fd number
configure: error: /bin/sh '../../../../../rtems-4.11.2/c/src/../../cpukit/configure' failed for ../../cpukit
}}}
```

* **summary**
```text
RTEMS 4.11.2 avr build fails
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3065#comment:1|Sebastian Huber|component changed|https://devel.rtems.org/ticket/3065#comment:1|component changed from Autoconf to build|Tue, 10 Oct 2017 06:00:29 GMT|Ticket|
|https://devel.rtems.org/ticket/3065#comment:2|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3065#comment:2|status changed from new to closed resolution set to invalid I cannot repeat this building the 4.11 branch tools and then RTEMS on FreeBSD 11.1. As a result I will close this PR. Note, the AVR BSP does not build as GCC fails with: /opt/work/chris/rtems/kernel/rtems.git/c/src/../../cpukit/libfs/src/dosfs/msdos_misc.c: In function 'msdos_find_node_by_cluster_num_in_fat_file': /opt/work/chris/rtems/kernel/rtems.git/c/src/../../cpukit/libfs/src/dosfs/msdos_misc.c:2069:1: error: unable to find a register to spill in class 'POINTER_REGS' } ^ /opt/work/chris/rtems/kernel/rtems.git/c/src/../../cpukit/libfs/src/dosfs/msdos_misc.c:2069:1: error: this is the insn: (insn 144 143 145 17 (set (reg:HI 26 r26) (reg/v/f:HI 96 [ dir_entry ])) /opt/work/chris/rtems/kernel/rtems.git/c/src/../../cpukit/libfs/src/dosfs/msdos_misc.c:2061 83 {*movhi} (expr_list:REG_DEAD (reg/v/f:HI 96 [ dir_entry ]) (nil))) /opt/work/chris/rtems/kernel/rtems.git/c/src/../../cpukit/libfs/src/dosfs/msdos_misc.c:2069: confused by earlier errors, bailing out|Mon, 05 Feb 2018 05:29:27 GMT|Ticket|
## [2964](https://devel.rtems.org/ticket/2964)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Sebastian Huber|normal|closed|fs/fat|fixed| |2964| |4.11.3|slemstick|defect| | |
* **description**
```text
We have a volume that has a lot of free'd up directory entries, one of which looks like this:

 * 1-> old LFN end entry n
 * 2-> old LFN end entry n - 1
 * 3-> old SHORT entry freed with byte[0] = 0xe5

and one remaining file, named slemstick.tar.gz, which resides AFTER this in the directory structure (and is NOT deleted). The old, deleted LFN above (consisting of three consequtive directory entries) earlier contained slemstick.tar.gz, such that the old filename still exist in the old LFN entries 1 and 2 above - but the SHORT entry (3) has been freed by setting byte[0] to 0xe5. 

The problem is that, when the filename search algorithm in msdos_find_file_in_directory(..) encounters the LFN entries 1 and 2, it starts parsing them as normal LFN entries. When it encounters the SHORT entry 3) above, the variable entry_empty is set and the algorithm continues to parse the remaining directory entries by skipping entry 3). As a consequence, it never finds the actual file in the directory entries below. 

A working fix to our problem is to add this clause in side the "else if(entry_empty)" if check around line ~1400 in msdos_misc.c:

https://pastebin.com/guW5JPfT

Which resets the search algorithm, if a short directory entry that has been freed is found while searching for a long file name. 

Can anyone comment on this patch?

```

* **summary**
```text
fat: msdos_find_file_in_directory(..) doesn't reset LFN search appropriately
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2964#comment:1|Sebastian Huber| |https://devel.rtems.org/ticket/2964#comment:1|Could you please provide a patch against the current Git master of RTEMS. Please also provide a self-contained test case, e.g. in ​https://git.rtems.org/rtems/tree/testsuites/fstests/fsdosfsname01/init.c|Fri, 31 Mar 2017 12:24:33 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:2|Sebastian Huber| |https://devel.rtems.org/ticket/2964#comment:2|Please create two patches with the git format-patch command. The first patch should add a test case for this issue to ​https://git.rtems.org/rtems/tree/testsuites/fstests/fsdosfsname01/init.c which fails. The second patch should fix the problem and let the test case pass.|Mon, 03 Apr 2017 06:12:40 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:3|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2964#comment:3|milestone changed from 4.12 to 4.12.0|Thu, 11 May 2017 07:31:02 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:4|Chris Johns|version changed|https://devel.rtems.org/ticket/2964#comment:4|version changed from 4.11 to 4.12|Mon, 14 Aug 2017 00:22:25 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:5|Sebastian Huber|status changed; owner set|https://devel.rtems.org/ticket/2964#comment:5|owner set to Sebastian Huber status changed from new to assigned|Thu, 24 Aug 2017 09:56:36 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:6|Sebastian Huber|component, summary changed|https://devel.rtems.org/ticket/2964#comment:6|component changed from General to filesystem summary changed from msdos_find_file_in_directory(..) doesn't reset LFN search appropriately to fat: msdos_find_file_in_directory(..) doesn't reset LFN search appropriately|Thu, 24 Aug 2017 10:02:52 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:7|Sebastian Huber| |https://devel.rtems.org/ticket/2964#comment:7|It looks like a bug, but I am not able to write a test case for this. The msdos_set_first_char4file_name() sets the first byte of each directory entry to 0xe5. How did you end up with 1-> old LFN end entry n 2-> old LFN end entry n - 1 3-> old SHORT entry freed with byte[0] = 0xe5 ? Do you use a removable media and delete the file with another operating system or via the short file name?|Wed, 06 Sep 2017 10:01:51 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:8|Sebastian Huber <sebastian.huber@…>| |https://devel.rtems.org/ticket/2964#comment:8|In a2c204eb/rtems: dosfs: Fix find name next entry preparation Update #2964.|Wed, 06 Sep 2017 12:08:46 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:9|Sebastian Huber|version, milestone changed|https://devel.rtems.org/ticket/2964#comment:9|version changed from 4.12 to 4.11 milestone changed from 4.12.0 to 4.11.3|Wed, 06 Sep 2017 12:09:49 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:10|Sebastian Huber <sebastian.huber@…>|status changed; resolution set|https://devel.rtems.org/ticket/2964#comment:10|status changed from assigned to closed resolution set to fixed In a76c31e1/rtems: dosfs: Fix find name next entry preparation Close #2964.|Wed, 06 Sep 2017 12:10:08 GMT|Ticket|
|https://devel.rtems.org/ticket/2964#comment:11|Sebastian Huber|component changed|https://devel.rtems.org/ticket/2964#comment:11|component changed from fs to fs/fat|Tue, 10 Oct 2017 06:50:58 GMT|Ticket|
### attachments
|guid|creator|title|link|description|attachment_link|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2964|slemstick|attachment set|https://devel.rtems.org/ticket/2964|attachment set to l4n_find.patch Patch file agains master|https://devel.rtems.org/attachment/ticket/2964/l4n_find.patch|Mon, 03 Apr 2017 06:06:49 GMT|Ticket|
## [2362](https://devel.rtems.org/ticket/2362)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|lib/block|wontfix| |2362| |4.11.3|mw|defect| | |
* **description**
```text
If CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS is set too large, the initialization of the block device buffer can fail without any notice, causing problems downstream that are seemingly unrelated (such as trying to read from the device) and with misleading error codes.

Tested on pc386 BSP

Ran testsuites/samples/fileio/fileio.exe fine, initializing partition /dev/hda with result = 0

Modified testsuites/samples/fileio/system.h, setting CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS to 32 (rather than 2).

Re-ran, and initializing partition /dev/hda fails with result = 3 (Invalid Name).
```

* **summary**
```text
ramdisk_initialize() returns an error code and driver initialization error code is ignored in general
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/2362#comment:1|Gedare|status changed; owner, milestone set|https://devel.rtems.org/ticket/2362#comment:1|owner set to Chris Johns status changed from new to assigned milestone set to 4.11.1|Tue, 09 Jun 2015 15:49:59 GMT|Ticket|
|https://devel.rtems.org/ticket/2362#comment:2|Sebastian Huber|summary changed|https://devel.rtems.org/ticket/2362#comment:2|summary changed from Configuration/initialization of block device buffer fails silently to ramdisk_initialize() returns an error code and driver initialization error code is ignored in general The rtems_bdbuf_init() doesn't fail silently. It returns an error code. We even have a test case for this libtests/block17. The real problem is that ramdisk_initialize() returns an error code which nobody evaluates. This is a device driver API flaw.|Tue, 09 Jun 2015 19:38:43 GMT|Ticket|
|https://devel.rtems.org/ticket/2362#comment:3|Sebastian Huber|milestone changed|https://devel.rtems.org/ticket/2362#comment:3|milestone changed from 4.11.1 to 4.11.2|Thu, 26 Jan 2017 07:16:00 GMT|Ticket|
|https://devel.rtems.org/ticket/2362#comment:4|Chris Johns|milestone changed|https://devel.rtems.org/ticket/2362#comment:4|milestone changed from 4.11.2 to 4.11.3 The 4.11.2 milestone is closing.|Thu, 23 Mar 2017 01:03:28 GMT|Ticket|
|https://devel.rtems.org/ticket/2362#comment:5|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/2362#comment:5|status changed from assigned to closed resolution set to wontfix|Mon, 05 Feb 2018 05:50:27 GMT|Ticket|
|https://devel.rtems.org/ticket/2362#comment:6|Chris Johns|component changed|https://devel.rtems.org/ticket/2362#comment:6|component changed from unspecified to lib/block|Mon, 12 Feb 2018 03:56:35 GMT|Ticket|
## [3258](https://devel.rtems.org/ticket/3258)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| |normal|Sebastian Huber|normal|closed|fs/fat|fixed| |3258| |4.11.3|Sebastian Huber|defect| | |
* **description**
```text
If there is already a file with a long file name it isn't possible to
create a second file which has a name that ends on the first files name
(for example ets.beam and sets.beam).
```

* **summary**
```text
fat: Fix creation of files with a similar name to existing files in the directory
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3258#comment:1|Christian Mauderer <Christian.Mauderer@…>| |https://devel.rtems.org/ticket/3258#comment:1|In 2fe3687/rtems: dosfs: Allow creating a file with similar name. If there is already a file with a long file name it isn't possible to create a second file which has a name that ends on the first files name (for example ets.beam and sets.beam). This patch fixes that. Update #3258.|Thu, 07 Dec 2017 07:03:44 GMT|Ticket|
|https://devel.rtems.org/ticket/3258#comment:2|Christian Mauderer <Christian.Mauderer@…>|status changed; resolution set|https://devel.rtems.org/ticket/3258#comment:2|status changed from assigned to closed resolution set to fixed In d438427/rtems: dosfs: Allow creating a file with similar name. If there is already a file with a long file name it isn't possible to create a second file which has a name that ends on the first files name (for example ets.beam and sets.beam). This patch fixes that. Close #3258.|Thu, 07 Dec 2017 07:04:31 GMT|Ticket|
## [3295](https://devel.rtems.org/ticket/3295)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool/rsb|fixed| |3295| |4.11.3|Chris Johns|defect| | |
* **description**
```text
The option expansion is missing `--with-download'.
```

* **summary**
```text
4.11: RSB `--source-only-download` does not download the source
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3295#comment:1|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/3295#comment:1|status changed from assigned to closed resolution set to fixed In 4671017/rtems-source-builder: sb: Option --source-only-download does not download the source. The option expansion is missing `--with-download'. Close #3295|Wed, 07 Feb 2018 22:14:41 GMT|Ticket|
|https://devel.rtems.org/ticket/3295#comment:2|Chris Johns <chrisj@…>| |https://devel.rtems.org/ticket/3295#comment:2|In 4671017/rtems-source-builder: sb: Option --source-only-download does not download the source. The option expansion is missing `--with-download'. Close #3295|Fri, 16 Feb 2018 02:16:28 GMT|Ticket|
## [3104](https://devel.rtems.org/ticket/3104)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|shell|fixed| |3104| |4.11.3|Chris Johns|enhancement| | |
* **description**
```text
This is back port of the patch on development. See #3096.
```

* **summary**
```text
Shell internal commands should be public.
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3104#comment:1|Chris Johns|status changed|https://devel.rtems.org/ticket/3104#comment:1|status changed from assigned to accepted|Mon, 05 Feb 2018 05:50:58 GMT|Ticket|
|https://devel.rtems.org/ticket/3104#comment:2|Chris Johns|component changed|https://devel.rtems.org/ticket/3104#comment:2|component changed from unspecified to shell|Mon, 05 Feb 2018 05:51:09 GMT|Ticket|
|https://devel.rtems.org/ticket/3104#comment:3|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3104#comment:3|status changed from accepted to closed resolution set to fixed ​https://git.rtems.org/rtems/commit/?h=4.11&id=89fd08eae6d3801a917daccc992b0ac5b32cf4d6|Mon, 05 Feb 2018 23:24:48 GMT|Ticket|
## [3271](https://devel.rtems.org/ticket/3271)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|blocker|Chris Johns|normal|closed|tool/rsb|fixed| |3271| |4.11.3|mholm|defect| | |
* **description**
```text
The multiprocessor.org website is used to download e.g. mpc in many of the GCC build descriptions. Recently the website underwent some changes and re-organised the download directories which have broken at least the 4.11 branch of RSB, but probably many other branches.

Having discussed this with Andreas Enge (maintainer of MPC), he suggests that the gnu mirror is used instead:

''I see, thank you for the info. Actually, I reorganised the web site, so
the tool is permanently broken. They should not use multiprecision.org,
but instead the official GNU ftp site:''
   https://ftp.gnu.org/gnu/mpc/

It would probably be good to use the GNU mirror also for MPFR and GMP and others if they aren't already.
```

* **summary**
```text
Avoid using multiprocessor.org in rtems source builder
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3271#comment:1|Gedare|status, severity changed; owner, version, milestone set|https://devel.rtems.org/ticket/3271#comment:1|owner set to Chris Johns status changed from new to assigned version set to 4.10 severity changed from critical to blocker milestone set to 5.1|Sat, 13 Jan 2018 14:21:57 GMT|Ticket|
|https://devel.rtems.org/ticket/3271#comment:2|Gedare|version changed|https://devel.rtems.org/ticket/3271#comment:2|version changed from 4.10 to 5 Fix should be applied to 4.11, 4.10, and master branches of RSB, please.|Sat, 13 Jan 2018 14:23:10 GMT|Ticket|
|https://devel.rtems.org/ticket/3271#comment:3|Chris Johns|status changed|https://devel.rtems.org/ticket/3271#comment:3|status changed from assigned to accepted|Mon, 15 Jan 2018 22:00:57 GMT|Ticket|
|https://devel.rtems.org/ticket/3271#comment:4|Chris Johns|version, milestone changed|https://devel.rtems.org/ticket/3271#comment:4|version changed from 5 to 4.11 milestone changed from 5.1 to 4.11.3 RTEMS 5 is already using the GNU FTP site (1). I have moved this ticket to 4.11 and a 4.11.3 milestone. Note, for 4.10 we need a separate ticket with a suitable 4.10 milestone, a ticket cannot cover more than one release and milestone. That ticket could reference this ticket and depend on it however by default Trac does not support any ticket dependency and I think we may need something (2) if we want to be able to do this. (1) ​https://git.rtems.org/rtems-source-builder/tree/source-builder/config/gcc-7-1.cfg#n21 (2) ​https://trac-hacks.org/wiki/MasterTicketsPlugin|Mon, 15 Jan 2018 22:25:37 GMT|Ticket|
|https://devel.rtems.org/ticket/3271#comment:5|mholm| |https://devel.rtems.org/ticket/3271#comment:5|I added ​https://devel.rtems.org/ticket/3272 for the 4.10 branch.|Tue, 16 Jan 2018 07:09:03 GMT|Ticket|
|https://devel.rtems.org/ticket/3271#comment:6|Chris Johns| |https://devel.rtems.org/ticket/3271#comment:6|Replying to mholm: I added ​https://devel.rtems.org/ticket/3272 for the 4.10 branch. Thank you. I have a patch for that branch so I will update the ticket details and post it soon.|Tue, 16 Jan 2018 08:01:24 GMT|Ticket|
|https://devel.rtems.org/ticket/3271#comment:7|Chris Johns <chrisj@…>| |https://devel.rtems.org/ticket/3271#comment:7|In f7c729e/rtems-source-builder: gcc: Update MPC verison to one hosted on GNU's FTP site. Update #3271|Thu, 18 Jan 2018 03:19:40 GMT|Ticket|
|https://devel.rtems.org/ticket/3271#comment:8|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3271#comment:8|status changed from accepted to closed resolution set to fixed Check the 4.11 branch and it is now using the GNU ftp site: package: arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.1-1 download: https://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz -> sources/mpc-1.0.3.tar.gz downloading: sources/mpc-1.0.3.tar.gz - 654.2kB of 654.2kB (100%)|Wed, 07 Feb 2018 22:12:41 GMT|Ticket|
## [3275](https://devel.rtems.org/ticket/3275)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns <chrisj@…>|normal|closed|tool/rsb|fixed| |3275| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Do not build the RTEMS kernel by default when released.
```

* **summary**
```text
RSB do not build the kernel when released.
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3275#comment:1|Chris Johns <chrisj@…>|status changed; owner, resolution set|https://devel.rtems.org/ticket/3275#comment:1|owner set to Chris Johns <chrisj@…> status changed from new to closed resolution set to fixed In 49033ff/rtems-source-builder: kernel: Do not build the RTEMS kernel by default when released. Close #3275|Fri, 19 Jan 2018 02:44:20 GMT|Ticket|
|https://devel.rtems.org/ticket/3275#comment:2|Chris Johns <chrisj@…>| |https://devel.rtems.org/ticket/3275#comment:2|In db86923/rtems-docs: RSB does not build a kernel by default. Update #3275.|Sun, 25 Mar 2018 23:13:30 GMT|Ticket|
## [3193](https://devel.rtems.org/ticket/3193)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool/rsb|fixed| |3193| |4.11.3|Ben|project| | |
* **description**
```text
Download 4-11.2
Running resource builder gives for each call to
sb-check, sb-set-builder : a first line NOT RELEASED.
This suggest a not released package which may be trusted but not guaranteed
```

* **summary**
```text
NOT released from source builder
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3193#comment:1|Chris Johns|status changed; owner set|https://devel.rtems.org/ticket/3193#comment:1|owner set to Chris Johns status changed from new to accepted|Mon, 05 Feb 2018 04:36:33 GMT|Ticket|
|https://devel.rtems.org/ticket/3193#comment:2|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3193#comment:2|status changed from accepted to closed resolution set to fixed I download ​rtems-source-builder-4.11.2.tar.xz and the sb-check shows: $ ./source-builder/sb-check RTEMS Source Builder - Check, 4.11.not_released Environment is ok which matches the output in this ticket. I copied the VERSION file from this version to the 4.11 branch version and got: $ ./source-builder/sb-check RTEMS Source Builder - Check, 4.11.2 I believe this issue is fixed on the branch.|Wed, 07 Feb 2018 02:59:44 GMT|Ticket|
## [3108](https://devel.rtems.org/ticket/3108)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal|Chris Johns|normal|closed|tool/rsb|fixed| |3108| |4.11.3|Chris Johns|defect| | |
* **description**
```text
Move the patches in the ARM buildste file.
```

* **summary**
```text
Remove RSB ARM specific config file rtems-arm-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg
```

### comments
|guid|author|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3108#comment:1|Chris Johns <chrisj@…>|status changed; resolution set|https://devel.rtems.org/ticket/3108#comment:1|status changed from assigned to closed resolution set to fixed In 4a87913/rtems-source-builder: Remove RSB ARM specific config file rtems-arm-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg Closes #3108.|Wed, 23 Aug 2017 01:11:13 GMT|Ticket|
## [3196](https://devel.rtems.org/ticket/3196)
### meta
|version|severity|owner|priority|status|component|resolution|keywords|id|cc|milestone|reporter|type|blocking|blockedby|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|4.11|normal| |normal|closed|tool/rsb|wontfix| |3196| |4.11.3|Ben|defect| | |
* **description**
```text
4-11.2 source building fails during gdb generation on Linux Mint 17.1
"checking for python2.7" is followed by
"python missing are unusable"

this is due to an #include "Python.h" that fails 

NOTE: the source building package of 4-11.2 that is used, generates a NOT RELEASED message at the start; a ticket has been raised for this
```

* **summary**
```text
4-11.2 gdb generation fails
```

### comments
|guid|creator|title|link|description|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3196#comment:1|Ben| |https://devel.rtems.org/ticket/3196#comment:1|The problem has been resolved The message sequence "checking python2.7" and result "python missing" are not related In between is a check for Python.h which was not installed. Installation has resolved the generation issue Hence a recommendation is left for sb-check to test on Python.h (as well to check for ncurses and termcap)|Mon, 23 Oct 2017 08:38:46 GMT|Ticket|
|https://devel.rtems.org/ticket/3196#comment:2|Chris Johns|status changed; resolution set|https://devel.rtems.org/ticket/3196#comment:2|status changed from new to closed resolution set to wontfix This will not be fixed on this branch. Checking for a header is not simple to implement. Where do you check for python.h because the location can vary from host to host. For example on MacOS and Xcode it is /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/Python.h.|Mon, 05 Feb 2018 04:47:05 GMT|Ticket|
### attachments
|guid|creator|title|link|description|attachment_link|pubDate|category|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|https://devel.rtems.org/ticket/3196|Ben|attachment set|https://devel.rtems.org/ticket/3196|attachment set to config.log config.log in ..../rtems-source-builder-4.11.2/rtems/build/m68k-rtems4.11-gdb-7.9-i686-linux-gnu-1/build/gdb|https://devel.rtems.org/attachment/ticket/3196/config.log|Tue, 17 Oct 2017 05:09:27 GMT|Ticket|
