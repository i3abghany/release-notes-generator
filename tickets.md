# Overall Progress
|total|closed|in_progress|new|assigned|percentage|
|:---:|:---:|:---:|:---:|:---:|:---:|
|47|47|0|0|0|100%|
# By Category
## owner
|owner|closed|total|progress|
|:---:|:---:|:---:|:---:|
|chrisj@…|2|2|2/2|
|Chris Johns|22|22|22/22|
| |6|6|6/6|
|Joel Sherrill|2|2|2/2|
|Sebastian Huber|13|13|13/13|
|Amar Takhar|1|1|1/1|
|Chris Johns <chrisj@<br />…>|1|1|1/1|
## type
|type|closed|total|progress|
|:---:|:---:|:---:|:---:|
|defect|42|42|42/42|
|infra|1|1|1/1|
|enhancement|3|3|3/3|
|project|1|1|1/1|
## priority
|priority|closed|total|progress|
|:---:|:---:|:---:|:---:|
|highest|3|3|3/3|
|high|3|3|3/3|
|normal|40|40|40/40|
|low|1|1|1/1|
## component
|component|closed|total|progress|
|:---:|:---:|:---:|:---:|
|doc|6|6|6/6|
|tool/gcc|5|5|5/5|
|tool/rsb|13|13|13/13|
|tool|3|3|3/3|
|lib/block|1|1|1/1|
|arch/arm|2|2|2/2|
|build|3|3|3/3|
|lib/dl|2|2|2/2|
|fs/fat|5|5|5/5|
|score|5|5|5/5|
|shell|1|1|1/1|
|config|1|1|1/1|
## severity
|severity|closed|total|progress|
|:---:|:---:|:---:|:---:|
|critical|1|1|1/1|
|blocker|6|6|6/6|
|normal|39|39|39/39|
|minor|1|1|1/1|
## reporter
|reporter|closed|total|progress|
|:---:|:---:|:---:|:---:|
|Chris Johns|21|21|21/21|
|Joel Sherrill|3|3|3/3|
|Mario Gruber|1|1|1/1|
|mw|1|1|1/1|
|Adit|1|1|1/1|
|Patrick Gauvin|1|1|1/1|
|Sebastian Huber|10|10|10/10|
|slemstick|2|2|2/2|
|Linda Huxley|1|1|1/1|
|Pavel|1|1|1/1|
|Steen Palm|1|1|1/1|
|Ben|2|2|2/2|
|mholm|1|1|1/1|
|Jeffrey Hill|1|1|1/1|
## version
|version|closed|total|progress|
|:---:|:---:|:---:|:---:|
|4.11|44|44|44/44|
| |3|3|3/3|
# Tickets
## [2988](https://devel.rtems.org/ticket/2988)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2988|Chris Johns|chrisj@…|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|highest|4.11.3|doc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|critical|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The link on docs.rtems.org to the latest release is broken. I suspect an issue  
 in the catalogue Javascript code.
```

* **summary**
```text
Documentation link to the 4.11 release is broken.
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Tue, 11 Jul 2017 00:<br />38:21 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2988#comm<br />ent:1|
|Chris Johns|Mon, 04 Sep 2017 03:<br />40:17 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2988#comm<br />ent:2|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />06:29 GMT|component changed|https://devel.rtems.<br />org/ticket/2988#comm<br />ent:3|
|Danxue Huang|Tue, 29 May 2018 03:<br />47:12 GMT| |https://devel.rtems.<br />org/ticket/2988#comm<br />ent:4|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2988#comm<br />ent:1|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />Moved to 4.11.3 and <br />will fix once #3031 <br />is fixed.|Ticket|
|https://devel.rtems.<br />org/ticket/2988#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed Fixed. ​https://g<br />it.rtems.org/chrisj/<br />rtems-admin.git/comm<br />it/?id=7eed3cecc3d6f<br />729550468d973641d13e<br />9ce7956|Ticket|
|https://devel.rtems.<br />org/ticket/2988#comm<br />ent:3|component changed fr<br />om Documentation to <br />doc|Ticket|
|https://devel.rtems.<br />org/ticket/2988#comm<br />ent:4|This is for test pur<br />pose. NVM :D|Ticket|


## [3107](https://devel.rtems.org/ticket/3107)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3107|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|highest|4.11.3|tool/gcc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|blocker|fixed|GCC FreeBSD|

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Building GCC breaks on FreeBDS 11.1. See https://bugs.freebsd.org/bugzilla/sho  
w_bug.cgi?id=212465 for details.
```

* **summary**
```text
Building gcc-4.9.3 is broken on FreeBSD 11.1
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Wed, 23 Aug 2017 01:<br />08:53 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3107#comm<br />ent:1|
|Sebastian Huber|Tue, 10 Oct 2017 05:<br />58:26 GMT|component changed|https://devel.rtems.<br />org/ticket/3107#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3107#comm<br />ent:1|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In bb43afd/rtems-<br />source-builder: Buil<br />ding gcc-4.9.3 is br<br />oken on FreeBSD 11.1<br /> Reference the patch<br /> for the FreeBSD por<br />t. See ticket: ​http<br />s://bugs.freebsd.org<br />/bugzilla/show_bug.c<br />gi?id=212465 Closes <br />#3107.|Ticket|
|https://devel.rtems.<br />org/ticket/3107#comm<br />ent:2|component changed fr<br />om GCC to tool/gcc|Ticket|


## [3119](https://devel.rtems.org/ticket/3119)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3119|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|highest|4.11.3|doc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|blocker|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Back port the master (4.12) fix.
```

* **summary**
```text
Docs failed to build PDF with the latest Sphinx.
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Sun, 03 Sep 2017 05:<br />40:24 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3119#comm<br />ent:1|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />06:29 GMT|component changed|https://devel.rtems.<br />org/ticket/3119#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3119#comm<br />ent:1|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In ba143e0/rtems-<br />docs: pdf: Update th<br />e RTEMS style to wor<br />k recent Sphinx vers<br />ions. Closes #3119.|Ticket|
|https://devel.rtems.<br />org/ticket/3119#comm<br />ent:2|component changed fr<br />om Documentation to <br />doc|Ticket|


## [2538](https://devel.rtems.org/ticket/2538)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2538|Joel Sherrill|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|high|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|blocker|worksforme| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
From the log building arm-rtems4.11 target. It is in rtems-tools and the ln on  
ly has one argument. Looks like I can expect all targets to fail.

+ /bin/rm  
 -rf rtems-tools-4.11
+ ln -s /data/home/joel/rtems-4.11-work/rtems-source-bu  
ilder/rtems/sources/git/rtems-tools.git
+ cd rtems-tools-4.11
/data/home/joe  
l/rtems-4.11-work/rtems-source-builder/rtems/build/rtems-tools-4.11-1/doit: li  
ne 85: cd: rtems-tools-4.11: No such file or directory
shell cmd failed: /bin  
/sh -ex  /data/home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/rtem  
s-tools-4.11-1/doit
error: building rtems-tools-4.11-1



```

* **summary**
```text
4.11 tools on RSB 4.11 branch fail to build
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Wed, 20 Jan 2016 00:<br />14:27 GMT|status changed|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:1|
|Mario Gruber|Mon, 25 Jan 2016 16:<br />53:59 GMT| |https://devel.rtems.<br />org/ticket/2538#comm<br />ent:2|
|Chris Johns|Fri, 19 Feb 2016 03:<br />11:25 GMT| |https://devel.rtems.<br />org/ticket/2538#comm<br />ent:3|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />16:00 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:4|
|Chris Johns|Tue, 21 Mar 2017 03:<br />12:16 GMT| |https://devel.rtems.<br />org/ticket/2538#comm<br />ent:5|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:6|
|Chris Johns|Wed, 07 Feb 2018 05:<br />15:39 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:7|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:1|status changed from <br />new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:2|Duplicate of #2495|Ticket|
|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:3|I suspect the issue <br />is the git command i<br />n the config file at<br />tempts to change to <br />the 4.11 branch befo<br />re a pull and if you<br /> have a repo in your<br /> sources directory t<br />hat was cloned befor<br />e the 4.11 branch wa<br />s added it fails. I <br />have changed the pul<br />l to be before the b<br />ranch.|Ticket|
|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:4|milestone changed fr<br />om 4.11.1 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:5|I just built 4.11/rt<br />ems-arm with out err<br />or. I cannot reprodu<br />ce this on FreeBSD. <br />Can you please provi<br />de some more informa<br />tion?|Ticket|
|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:6|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2538#comm<br />ent:7|status changed from <br />accepted to closed r<br />esolution set to wor<br />ksforme I cannot rep<br />eat this and the rel<br />ated code looks OK s<br />o without further de<br />tails I cannot do mu<br />ch with this but rep<br />ort.|Ticket|


## [2578](https://devel.rtems.org/ticket/2578)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2578|Mario Gruber|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|high|4.11.3|tool|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|blocker|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Building rtems-tools for Cxc builds:

{{{
git checkout -b 4.11 origin/4.11   
\
 && source-builder/sb-check \
 && cd rtems \
 && ../source-builder/sb-set  
-builder \
 --log=rsb-powerpc-rtems4.11-mingw.txt \
 --prefix=/opt/powerpc-r  
tems4.11-mingw \
 --host=i686-w64-mingw32 \
 --bset-tar-files \
 4.11/rtems  
-powerpc
}}}

dies at configuring package rtems-tools-4.11-1:

{{{
confi  
g: tools/rtems-tools-4.11-1.cfg
package: rtems-tools-4.11-1
...
+ echo ==>   
%build:
==> %build:
+ pwd
+ build_top=/tmp/rtems-source-builder/rtems/build  
/rtems-tools-4.11-1
+ test x86_64-linux-gnu != i686-w64-mingw32
+ RT_HOST=-h  
ost=i686-w64-mingw32
+ cd rtems-tools-4.11
+ ./waf configure -host=i686-w64-  
mingw32 
+ --prefix=/opt/powerpc-rtems4.11-mingw
waf [commands] [options]

  

Main commands (example: ./waf build -j4)
  build    : executes the build
    
clean    : cleans the project
...
+ ./waf
The project was not configured: r  
un "waf configure" first!
shell cmd failed: /bin/sh -ex  /tmp/rtems-source-bu  
ilder/rtems/build/rtems-tools-4.11-1/doit
error: building rtems-tools-4.11-1
  

  See error report: rsb-report-rtems-tools-4.11-1.txt
}}}

This is due to   
the -host command line argument, which is missing a hyphen.

I sent a patch   
to the mailing list:

https://lists.rtems.org/pipermail/devel/2016-January/0  
13348.html
```

* **summary**
```text
rtems-tools configure fails for Cxc builds
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Mario Gruber|Thu, 18 Feb 2016 08:<br />36:58 GMT|status changed; owne<br />r set|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:1|
|Chris Johns|Sun, 27 Mar 2016 00:<br />48:40 GMT|owner changed|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:2|
|Chris Johns|Sun, 27 Mar 2016 00:<br />51:58 GMT|priority, milestone <br />changed|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:3|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />05:05 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:4|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:5|
|Chris Johns|Tue, 23 Jan 2018 21:<br />37:54 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:6|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:1|owner set to Sebasti<br />an Huber status chan<br />ged from new to assi<br />gned|Ticket|
|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:2|owner changed from S<br />ebastian Huber to Ch<br />ris Johns|Ticket|
|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:3|priority changed fro<br />m normal to high mil<br />estone changed from <br />4.11.1 to 4.11|Ticket|
|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:4|milestone changed fr<br />om 4.11 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:5|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2578#comm<br />ent:6|status changed from <br />assigned to closed r<br />esolution set to won<br />tfix I am going to c<br />lose this ticket. We<br /> are now building Wi<br />ndows tools on Windo<br />ws so the need for C<br />xc build is not as i<br />mportant as it was. <br />Building on Windows <br />ensures we have the <br />correct DLL set for <br />the tools.|Ticket|


## [2639](https://devel.rtems.org/ticket/2639)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2639|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|high|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|duplicate|RSB 4.11.0-RC2|

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Long path support on Windows requires the use of Unicode paths. The current pa  
th is not Unicode and some paths in C++ can be longer than 255 character when   
building the release candidates using the standard paths in the releases.

T  
he solution is to change paths.py so it's host call returns a Unicode string.   
The also requires changes to the macro key logic to convert any unicode string  
 to an ascii string, all macro keys are ascii. Also the execute module needs t  
o better manage Unicode strings.
```

* **summary**
```text
RSB long path support on Windows is still broken.
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 14 Mar 2016 04:<br />26:04 GMT|status changed|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:1|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />05:05 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:2|
|Chris Johns|Tue, 21 Mar 2017 03:<br />15:23 GMT| |https://devel.rtems.<br />org/ticket/2639#comm<br />ent:3|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:4|
|Chris Johns|Sat, 22 Apr 2017 22:<br />25:30 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:5|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:1|status changed from <br />new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:2|milestone changed fr<br />om 4.11 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:3|This is a major chan<br />ge and I do not thin<br />k it is suitable for<br /> a release branch. T<br />his change should on<br />ly happen on master.|Ticket|
|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:4|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2639#comm<br />ent:5|status changed from <br />accepted to closed r<br />esolution set to dup<br />licate Closing this <br />ticket as #2992 has <br />more details.|Ticket|


## [2362](https://devel.rtems.org/ticket/2362)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2362|mw|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|lib/block|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
If CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS is set too large, the initialization   
of the block device buffer can fail without any notice, causing problems downs  
tream that are seemingly unrelated (such as trying to read from the device) an  
d with misleading error codes.

Tested on pc386 BSP

Ran testsuites/sample  
s/fileio/fileio.exe fine, initializing partition /dev/hda with result = 0

M  
odified testsuites/samples/fileio/system.h, setting CONFIGURE_BDBUF_MAX_READ_A  
HEAD_BLOCKS to 32 (rather than 2).

Re-ran, and initializing partition /dev/  
hda fails with result = 3 (Invalid Name).
```

* **summary**
```text
ramdisk_initialize() returns an error code and driver initialization error cod  
e is ignored in general
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Gedare|Tue, 09 Jun 2015 15:<br />49:59 GMT|status changed; owne<br />r, milestone set|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:1|
|Sebastian Huber|Tue, 09 Jun 2015 19:<br />38:43 GMT|summary changed|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:2|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />16:00 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:3|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:4|
|Chris Johns|Mon, 05 Feb 2018 05:<br />50:27 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:5|
|Chris Johns|Mon, 12 Feb 2018 03:<br />56:35 GMT|component changed|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:6|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:1|owner set to Chris J<br />ohns status changed <br />from new to assigned<br /> milestone set to 4.<br />11.1|Ticket|
|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:2|summary changed from<br /> Configuration/initi<br />alization of block d<br />evice buffer fails s<br />ilently to ramdisk_i<br />nitialize() returns <br />an error code and dr<br />iver initialization <br />error code is ignore<br />d in general The rte<br />ms_bdbuf_init() does<br />n't fail silently. I<br />t returns an error c<br />ode. We even have a <br />test case for this l<br />ibtests/block17. The<br /> real problem is tha<br />t ramdisk_initialize<br />() returns an error <br />code which nobody ev<br />aluates. This is a d<br />evice driver API fla<br />w.|Ticket|
|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:3|milestone changed fr<br />om 4.11.1 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:4|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:5|status changed from <br />assigned to closed r<br />esolution set to won<br />tfix|Ticket|
|https://devel.rtems.<br />org/ticket/2362#comm<br />ent:6|component changed fr<br />om unspecified to li<br />b/block|Ticket|


## [2439](https://devel.rtems.org/ticket/2439)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2439|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/gcc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | |3262|


* **description**
```text
Building 4.11/rtems-arm with the RSB fails with (error report attached):

{{  
{
/Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/arm-rte  
ms4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/build/./gcc  
/xgcc -B/Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/ar  
m-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/build/  
./gcc/ -nostdinc -B/Users/chris/development/rtems/rsb/rtems-source-builder/rte  
ms/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0  
.0-1/build/arm-rtems4.11/newlib/ -isystem /Users/chris/development/rtems/rsb/r  
tems-source-builder/rtems/build/arm-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-  
x86_64-apple-darwin15.0.0-1/build/arm-rtems4.11/newlib/targ-include -isystem /  
Users/chris/development/rtems/rsb/rtems-source-builder/rtems/build/arm-rtems4.  
11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-apple-darwin15.0.0-1/gcc-4.9.3/newli  
b/libc/include -B/Users/chris/development/rtems/4.11/arm-rtems4.11/bin/ -B/Use  
rs/chris/development/rtems/4.11/arm-rtems4.11/lib/ -isystem /Users/chris/devel  
opment/rtems/4.11/arm-rtems4.11/include -isystem /Users/chris/development/rtem  
s/4.11/arm-rtems4.11/sys-include    -g -O2 -mthumb -O2 -I../../../../gcc-4.9.3  
/libgcc/../newlib/libc/sys/rtems/include -g -O2 -DIN_GCC  -DCROSS_DIRECTORY_ST  
RUCTURE  -W -Wall -Wno-narrowing -Wwrite-strings -Wcast-qual -Wstrict-prototyp  
es -Wmissing-prototypes -Wold-style-definition  -isystem ./include   -fno-inli  
ne -g -DIN_LIBGCC2 -fbuilding-libgcc -fno-stack-protector -Dinhibit_libc  -fno  
-inline -I. -I. -I../../.././gcc -I../../../../gcc-4.9.3/libgcc -I../../../../  
gcc-4.9.3/libgcc/. -I../../../../gcc-4.9.3/libgcc/../gcc -I../../../../gcc-4.9  
.3/libgcc/../include  -DHAVE_CC_TLS  -o _arm_unorddf2_s.o -MT _arm_unorddf2_s.  
o -MD -MP -MF _arm_unorddf2_s.dep -DSHARED -DL_arm_unorddf2 -xassembler-with-c  
pp -c ../../../../gcc-4.9.3/libgcc/config/arm/lib1funcs.S
../../../../gcc-4.9  
.3/libgcc/config/arm/ieee754-df.S: Assembler messages:
../../../../gcc-4.9.3/  
libgcc/config/arm/ieee754-df.S:567: Error: invalid constant (ff) after fixup
  
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:673: Error: invalid const  
ant (ff) after fixup
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:689  
: Error: invalid constant (fd) after fixup
../../../../gcc-4.9.3/libgcc/confi  
g/arm/ieee754-df.S:875: Error: invalid constant (ff) after fixup
../../../../  
gcc-4.9.3/libgcc/config/arm/ieee754-df.S:912: Error: invalid constant (fd) aft  
er fixup
../../../../gcc-4.9.3/libgcc/config/arm/ieee754-df.S:985: Error: inv  
alid constant (fd) after fixup
}}}
```

* **summary**
```text
GCC 4.9.3 ARM build fails on OS X 10.11 (El Capitan)
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 02 Nov 2015 00:<br />06:00 GMT|summary changed|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:1|
|Amar Takhar|Mon, 02 Nov 2015 02:<br />47:10 GMT|summary changed|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:2|
|Chris Johns|Wed, 04 Nov 2015 23:<br />31:42 GMT| |https://devel.rtems.<br />org/ticket/2439#comm<br />ent:3|
|Joel Sherrill|Thu, 05 Nov 2015 00:<br />59:15 GMT| |https://devel.rtems.<br />org/ticket/2439#comm<br />ent:4|
|Chris Johns|Wed, 11 Nov 2015 00:<br />11:22 GMT| |https://devel.rtems.<br />org/ticket/2439#comm<br />ent:5|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />16:00 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:6|
|Chris Johns|Thu, 23 Mar 2017 01:<br />04:45 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:7|
|Sebastian Huber|Tue, 10 Oct 2017 05:<br />58:26 GMT|component changed|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:8|
|Chris Johns|Tue, 23 Jan 2018 03:<br />03:54 GMT|blocking set|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:9|
|Chris Johns|Tue, 23 Jan 2018 05:<br />10:15 GMT| |https://devel.rtems.<br />org/ticket/2439#comm<br />ent:10|
|Chris Johns|Thu, 25 Jan 2018 05:<br />51:43 GMT|status changed; owne<br />r set|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:11|
|Chris Johns|Wed, 07 Feb 2018 05:<br />12:32 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:12|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:1|summary changed from<br /> ARM build fails on <br />OS X 10.11 (Ll Capit<br />an) to GCC 4.9.3 ARM<br /> build fails on OS X<br /> 10.11 (Ll Capitan)|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:2|summary changed from<br /> GCC 4.9.3 ARM build<br /> fails on OS X 10.11<br /> (Ll Capitan) to GCC<br /> 4.9.3 ARM build fai<br />ls on OS X 10.11 (El<br /> Capitan)|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:3|The ARM target does <br />not build on Yosemit<br />e or El Capitan with<br /> Xcode 7.1 command l<br />ine tools and the pr<br />oblem still exists i<br />n El Capitan with Xc<br />ode 7.1 and the 7.2 <br />beta command line to<br />ols. It appears to b<br />e a bug in clang in <br />Xcode building tc-ar<br />m.c in binutils. I h<br />ave raise a bug repo<br />rt with Apple with a<br /> small test case.|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:4|Did you ask about th<br />is on the binutils a<br />nd clang lists? It m<br />ight actually get mo<br />re traction on the p<br />ublic side.|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:5|I raised a bug repor<br />t and it has been fi<br />xed in binutils and <br />should be released i<br />n 2.26.|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:6|milestone changed fr<br />om 4.11.1 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:7|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:8|component changed fr<br />om GCC to tool/gcc|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:9|blocking set to 3262|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:10|Testing the latest R<br />SB for this ticket w<br />ith the latest MacOS<br /> (High Sierra) with <br />the latest Xcode (9.<br />2) and it's command <br />line tools fails wit<br />h: /usr/bin/c++ -O2 <br />-pipe -fbracket-dept<br />h=1024 -I/opt/work/c<br />hris/rtems/rsb/rtems<br />-source-builder.git/<br />rtems/build/tmp/sb-c<br />hris/4.11/rtems-arm.<br />bset/opt/work/rtems/<br />4.11/include -c -DIN<br />_GCC_FRONTEND -g -O2<br /> -DIN_GCC -DCROSS_DI<br />RECTORY_STRUCTURE -f<br />no-exceptions -fno-r<br />tti -fasynchronous-u<br />nwind-tables -W -Wal<br />l -Wno-narrowing -Ww<br />rite-strings -Wcast-<br />qual -Wmissing-forma<br />t-attribute -pedanti<br />c -Wno-long-long -Wn<br />o-variadic-m acros -<br />Wno-overlength-strin<br />gs -DHAVE_CONFIG_H -<br />I. -Ic -I../../gcc-4<br />.9.3/gcc -I../../gcc<br />-4.9.3/gcc/c -I../..<br />/gcc-4.9.3/gcc/../in<br />clude -I../../gcc-4.<br />9.3/gcc/../libcpp/in<br />clude -I/opt/work/ch<br />ris/rtems/rsb/rtems-<br />source-builder.git/r<br />tems/build/arm-rtems<br />4.11-gcc-4.9.3-newli<br />b-2.2.0.20150423-x86<br />_64-apple-darwin17.3<br />.0-1/build/./gmp -I/<br />opt/work/chris/rtems<br />/rsb/rtems-source-bu<br />ilder.git/rtems/buil<br />d/arm-rtems4.11-gcc-<br />4.9 .3-newlib-2.2.0.<br />20150423-x86_64-appl<br />e-darwin17.3.0-1/gcc<br />-4.9.3/gmp -I/opt/wo<br />rk/chris/rtems/rsb/r<br />tems-source-builder.<br />git/rtems/build/arm-<br />rtems4.11-gcc-4.9.3-<br />newlib-2.2.0.2015042<br />3-x86_64-apple-darwi<br />n17.3.0-1/build/./mp<br />fr -I/opt/work/chris<br />/rtems/rsb/rtems-sou<br />rce-builder.git/rtem<br />s/build/arm-rtems4.1<br />1-gcc-4.9.3-newlib-2<br />.2.0.20150423-x86_64<br />-apple-darwin17.3.0-<br />1/gcc-4.9.3/mpfr -I/<br />opt/work/chris/rtems<br />/rsb/rtems-sourc e-b<br />uilder.git/rtems/bui<br />ld/arm-rtems4.11-gcc<br />-4.9.3-newlib-2.2.0.<br />20150423-x86_64-appl<br />e-darwin17.3.0-1/gcc<br />-4.9.3/mpc/src -I../<br />../gcc-4.9.3/gcc/../<br />libdecnumber -I../..<br />/gcc-4.9.3/gcc/../li<br />bdecnumber/dpd -I../<br />libdecnumber -I../..<br />/gcc-4.9.3/gcc/../li<br />bbacktrace -o c/c-ob<br />jc-common.o -MT c/c-<br />objc-common.o -MMD -<br />MP -MF c/.deps/c-obj<br />c-common.TPo ../../g<br />cc-4.9.3/gcc/c/c-obj<br />c-common.c clang: wa<br />rning: treating 'c' <br />input as 'c++' when <br />in C++ mode, this be<br />havior is deprecated<br /> [-Wdeprecated] In f<br />ile included from ..<br />/../gcc-4.9.3/gcc/c/<br />c-objc-common.c:33: <br />In file included fro<br />m /Applications/Xcod<br />e.app/Contents/Devel<br />oper/Toolchains/Xcod<br />eDefault.xctoolchain<br />/usr/include/c++/v1/<br />new:89: /Application<br />s/Xcode.app/Contents<br />/Developer/Toolchain<br />s/XcodeDefault.xctoo<br />lchain/usr/include/c<br />++/v1/exception:173:<br />5: error: no member <br />named 'fancy_abort' <br />in namespace 'std::_<br />_1'; did you mean si<br />mply 'fancy_abort'? <br />_VSTD::abort(); ^~~~<br />~~~ /Applications/Xc<br />ode.app/Contents/Dev<br />eloper/Toolchains/Xc<br />odeDefault.xctoolcha<br />in/usr/include/c++/v<br />1/__config:392:15: n<br />ote: expanded from m<br />acro '_VSTD' #define<br /> _VSTD std::_LIBCPP_<br />NAMESPACE ^ ../../gc<br />c-4.9.3/gcc/system.h<br />:685:13: note: 'fanc<br />y_abort' declared he<br />re extern void fancy<br />_abort (const char *<br />, int, const char *)<br /> ATTRIBUTE_NORETURN;<br /> ^ 1 error generated<br />.|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:11|owner set to Chris J<br />ohns status changed <br />from new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/2439#comm<br />ent:12|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed ARM is building o<br />n MacOS: ​https://li<br />sts.rtems.org/piperm<br />ail/build/2018-Febru<br />ary/000447.html|Ticket|


### attachments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 02 Nov 2015 00:<br />05:09 GMT|attachment set|https://devel.rtems.<br />org/ticket/2439|
|Chris Johns|Tue, 23 Jan 2018 22:<br />09:36 GMT|attachment set|https://devel.rtems.<br />org/ticket/2439|

|guid|description|category|attachment_link|
|:---:|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2439|attachment set to rs<br />b-report-arm-rtems4.<br />11-gcc-4.9.3-newlib-<br />2.2.0.20150423-x86_6<br />4-apple-darwin15.0.0<br />-1.txt RSB report.|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2439/rsb-report-ar<br />m-rtems4.11-gcc-4.9.<br />3-newlib-2.2.0.20150<br />423-x86_64-apple-dar<br />win15.0.0-1.txt|
|https://devel.rtems.<br />org/ticket/2439|attachment set to gc<br />c-4.9.3-macos-xcode9<br />.diff Fixes for MacO<br />S (High Sierra) and <br />Xocde 9.2 command li<br />ne tools.|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2439/gcc-4.9.3-mac<br />os-xcode9.diff|


## [2460](https://devel.rtems.org/ticket/2460)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2460|Adit| |defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|arch/arm|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|duplicate| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
This bug pertains to the ARM Generic Interrupt Controller (GIC) register utili  
ty functions in 

{{{c/src/lib/libbsp/arm/shared/include/arm-gic.h}}}

The  
 following routines all use the macro {{{GIC_ID_TO_TWO_BITS_REG_OFFSET(id)}}}:  


{{{
gic_id_get_handling_mode
gic_id_set_handling_mode
gic_id_get_trigge  
r_mode
gic_id_set_trigger_mode
}}}

These routines set the {{{GIC_ICFGRn}}  
} set of registers. These registers have 2-bit bit fields. Let's take the trig  
ger mode routines as an example of the bug, but it applies to the handling mod  
e as well. The GIC specification from ARM states that for a particular interru  
pt ID ''m'' the register ''n'' and bit field ''F'' is found by:

''n = m DIV  
 16''
''F = m MOD 16''

And the bit location in register ''n'' is defined a  
s ''[2F+1:2F]''. However, the macro  {{{GIC_ID_TO_TWO_BITS_REG_OFFSET(id)}}} a  
nd the routines that use it, set bits ''[F+1:F]''.

I have tested this by us  
ing the set_trigger_mode routine to set an interrupt to be edge triggered, but  
 the correct bit does not get set, and the interrupt still behaves in a level   
triggered fashion. When I adjust the macro to have a {{{<< 1}}} it works corre  
ctly.

If someone can verify my logic at least, then I can submit a tested p  
atch.
```

* **summary**
```text
arm-gic.h - GIC_ID_TO_TWO_BITS_REG_OFFSET(id) incorrectly defined
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber|Tue, 10 Nov 2015 07:<br />16:01 GMT| |https://devel.rtems.<br />org/ticket/2460#comm<br />ent:1|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />16:00 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:2|
|Chris Johns|Thu, 23 Mar 2017 01:<br />04:45 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:3|
|Chris Johns|Mon, 05 Feb 2018 04:<br />40:23 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:4|
|Sebastian Huber|Mon, 05 Feb 2018 07:<br />48:15 GMT|status, milestone ch<br />anged; resolution se<br />t|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:5|
|Sebastian Huber|Mon, 05 Feb 2018 07:<br />59:59 GMT|component changed|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:6|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:1|Yes, please send a p<br />atch to devel(at)rte<br />ms.org and add "Clos<br />e #2460." to the com<br />mit message.|Ticket|
|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:2|milestone changed fr<br />om 4.11.1 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:3|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:4|milestone changed fr<br />om 4.11.3 to Indefin<br />ite Requires funding<br />.|Ticket|
|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:5|status changed from <br />new to closed resolu<br />tion set to duplicat<br />e milestone changed <br />from Indefinite to 4<br />.11.3 Duplicate of #<br />3002.|Ticket|
|https://devel.rtems.<br />org/ticket/2460#comm<br />ent:6|component changed fr<br />om bsps to arch/arm|Ticket|


### attachments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Adit|Wed, 11 Nov 2015 04:<br />42:44 GMT|attachment set|https://devel.rtems.<br />org/ticket/2460|

|guid|description|category|attachment_link|
|:---:|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2460|attachment set to 00<br />01-Fixes-GIC_ID_TO_T<br />WO_BITS_REG_OFFSET-m<br />acro-in-arm-gic.patc<br />h|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2460/0001-Fixes-GI<br />C_ID_TO_TWO_BITS_REG<br />_OFFSET-macro-in-arm<br />-gic.patch|


## [2610](https://devel.rtems.org/ticket/2610)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2610|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Building unhex.c on Windows gives the following error:

{{{
gcc -DHAVE_CONF  
IG_H -I. -I/c/opt/rtems/kernel/rtems.git/tools/build     -g -O2 -MT rtems-bin2  
c.o -MD -MP -MF .deps/rtems-bin2c.Tpo -c -o rtems-bin2c.o /c/opt/rtems/kernel/  
rtems.git/tools/build/rtems-bin2c.c
In file included from C:/opt/rtems/kernel  
/rtems.git/tools/build/unhex.c:36:0:
C:/opt/rtems/kernel/rtems.git/tools/buil  
d/unhex.c: In function 'error':
C:/opt/rtems/kernel/rtems.git/tools/build/unh  
ex.c:687:16: warning: '_errno' redeclared without dllimport attribute: previou  
s dllimport ignored [-Wattributes]
     extern int errno;
                ^
  

}}}
```

* **summary**
```text
unhex.c does not build on MSYS2
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Tue, 23 Feb 2016 05:<br />22:17 GMT| |https://devel.rtems.<br />org/ticket/2610#comm<br />ent:1|
|Chris Johns|Tue, 23 Feb 2016 05:<br />22:50 GMT|priority, severity, <br />milestone changed|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:2|
|Chris Johns|Wed, 24 Feb 2016 03:<br />15:50 GMT|status changed|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:3|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />16:00 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:4|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:5|
|Chris Johns|Wed, 07 Feb 2018 03:<br />00:35 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:6|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:1|This is a warning an<br />d not fatal. I think<br /> it should still be <br />cleaned up.|Ticket|
|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:2|priority changed fro<br />m highest to normal <br />severity changed fro<br />m critical to normal<br /> milestone changed f<br />rom 4.11 to 4.11.1|Ticket|
|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:3|status changed from <br />new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:4|milestone changed fr<br />om 4.11.1 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:5|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2610#comm<br />ent:6|status changed from <br />accepted to closed r<br />esolution set to won<br />tfix I am closing th<br />is ticket. The tool <br />can be fixed on mast<br />er.|Ticket|


## [2671](https://devel.rtems.org/ticket/2671)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2671|Joel Sherrill|Joel Sherrill|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
I recall needing to sync the binutils and gcc. Checking an old install for 4.1  
1, I noticed that the gcc seems to match what is configured but the binutils i  
s older (2.25).

[joel@rtbf64c ~]$ ~/rtems-4.11-work/tools/4.11/bin/moxie-rt  
ems4.11-as --version
GNU assembler (GNU Binutils) 2.25
Copyright (C) 2014 Fr  
ee Software Foundation, Inc.
This program is free software; you may redistrib  
ute it under the terms of
the GNU General Public License version 3 or later.
  

This program has absolutely no warranty.
This assembler was configured for a  
 target of `moxie-rtems4.11'.
[joel@rtbf64c ~]$ ~/rtems-4.11-work/tools/4.11/  
bin/moxie-rtems4.11-gcc --version
moxie-rtems4.11-gcc (GCC) 4.9.3 20150626 (R  
TEMS 4.11, RSB 075ed1c8e2363ec7fcfcaec6b648222597009f20, Newlib 2.2.0.20150423  
)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; s  
ee the source for copying conditions.  There is NO
warranty; not even for MER  
CHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.



Error below:

/home  
/joel/rtems-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9  
.3-newlib-2.2.0.20150423-x86_64-linux-gnu-1/build/./gcc/xgcc -B/home/joel/rtem  
s-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-  
2.2.0.20150423-x86_64-linux-gnu-1/build/./gcc/ -nostdinc -B/home/joel/rtems-4.  
11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-newlib-2.2.  
0.20150423-x86_64-linux-gnu-1/build/moxie-rtems4.11/newlib/ -isystem /home/joe  
l/rtems-4.11-work/rtems-source-builder/rtems/build/moxie-rtems4.11-gcc-4.9.3-n  
ewlib-2.2.0.20150423-x86_64-linux-gnu-1/build/moxie-rtems4.11/newlib/targ-incl  
ude -isystem /home/joel/rtems-4.11-work/rtems-source-builder/rtems/build/moxie  
-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-linux-gnu-1/gcc-4.9.3/newlib  
/libc/include -B/home/joel/rtems-4.11-work/tools/4.11/moxie-rtems4.11/bin/ -B/  
home/joel/rtems-4.11-work/tools/4.11/moxie-rtems4.11/lib/ -isystem /home/joel/  
rtems-4.11-work/tools/4.11/moxie-rtems4.11/include -isystem /home/joel/rtems-4  
.11-work/tools/4.11/moxie-rtems4.11/sys-include    -g -O2 -mel -O2 -I../../../  
../gcc-4.9.3/libgcc/../newlib/libc/sys/rtems/include -g -O2 -DIN_GCC  -DCROSS_  
DIRECTORY_STRUCTURE  -W -Wall -Wno-narrowing -Wwrite-strings -Wcast-qual -Wstr  
ict-prototypes -Wmissing-prototypes -Wold-style-definition  -isystem ./include  
   -g -DIN_LIBGCC2 -fbuilding-libgcc -fno-stack-protector -Dinhibit_libc  -I.   
-I. -I../../.././gcc -I../../../../gcc-4.9.3/libgcc -I../../../../gcc-4.9.3/li  
bgcc/. -I../../../../gcc-4.9.3/libgcc/../gcc -I../../../../gcc-4.9.3/libgcc/..  
/include  -DHAVE_CC_TLS -DUSE_EMUTLS -o _ashldi3.o -MT _ashldi3.o -MD -MP -MF   
_ashldi3.dep -DL_ashldi3 -c ../../../../gcc-4.9.3/libgcc/libgcc2.c -fvisibilit  
y=hidden -DHIDE_EXPORTS
/tmp/cctmIP4r.s: Assembler messages:
/tmp/cctmIP4r.s  
:26: Error: unknown opcode sub.l $r1,$r2
Makefile:463: recipe for target '_ne  
gdi2.o' failed
make[4]: *** [_negdi2.o] Error 1
make[4]: *** Waiting for unf  
inished jobs....
/tmp/ccaQiOcs.s: /tmp/ccWFtIrs.s: Assembler messages:
Assem  
bler messages:
/tmp/ccaQiOcs.s:22: Error: unknown opcode sub.l $r3,$r2
/tmp/  
ccWFtIrs.s:44: Error: unknown opcode mul.l $r12,$r6
/tmp/ccWFtIrs.s:46: Error  
: unknown opcode mul.l $r4,$r1
/tmp/ccWFtIrs.s:49: Error: unknown opcode mul.  
l $r8,$r1
/tmp/ccWFtIrs.s:52: Error: unknown opcode mul.l $r3,$r6
/tmp/ccWFt  
Irs.s:56: Error: unknown opcode add.l $r6,$r3
/tmp/ccWFtIrs.s:61: Error: unkn  
own opcode add.l $r3,$r6
/tmp/ccWFtIrs.s:68: Error: unknown opcode add.l $r1,  
$r4
/tmp/ccWFtIrs.s:75: Error: unknown opcode add.l $r1,$r4
/tmp/ccWFtIrs.s:  
89: Error: unknown opcode mul.l $r0,$r4
/tmp/ccWFtIrs.s:93: Error: unknown op  
code mul.l $r2,$r4
/tmp/ccWFtIrs.s:95: Error: unknown opcode add.l $r0,$r2
/  
tmp/ccWFtIrs.s:99: Error: unknown opcode add.l $r0,$r12
/tmp/ccWFtIrs.s:100:   
Error: unknown opcode add.l $r1,$r2
Makefile:463: recipe for target '_muldi3.  
o' failed
make[4]: *** [_muldi3.o] Error 1
make[4]: *** [_lshrdi3.o] Error 1  


```

* **summary**
```text
moxie tools fail to build on 4.11
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Joel Sherrill|Mon, 21 Mar 2016 14:<br />54:34 GMT| |https://devel.rtems.<br />org/ticket/2671#comm<br />ent:1|
|Joel Sherrill|Mon, 21 Mar 2016 15:<br />27:18 GMT| |https://devel.rtems.<br />org/ticket/2671#comm<br />ent:2|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />05:37 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:3|
|Chris Johns|Tue, 21 Mar 2017 04:<br />07:24 GMT|owner, status change<br />d|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:4|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:5|
|Chris Johns|Mon, 05 Feb 2018 05:<br />45:16 GMT| |https://devel.rtems.<br />org/ticket/2671#comm<br />ent:6|
|Chris Johns|Mon, 05 Feb 2018 05:<br />45:26 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:7|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:1|The following is suf<br />ficient to get a too<br />lset built. diff --g<br />it a/rtems/config/4.<br />11/rtems-moxie.bset <br />b/rtems/config/4.11/<br />rtems-moxie.bset ind<br />ex 0473f02..c8f764e <br />100644 --- a/rtems/c<br />onfig/4.11/rtems-mox<br />ie.bset +++ b/rtems/<br />config/4.11/rtems-mo<br />xie.bset @@ -22,7 +2<br />2,7 @@ 4.11/rtems-au<br />totools devel/expat-<br />2.1.0-1 devel/dtc-1.<br />4.1-1 -tools/rtems-b<br />inutils-2.26-1 +tool<br />s/rtems-binutils-2.2<br />5-1 tools/rtems-gcc-<br />4.9.3-newlib-2.2.0-2<br />0150423-1 tools/rtem<br />s-gdb-7.9-1 tools/rt<br />ems-tools-4.11-1|Ticket|
|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:2|moxie/moxiesim built<br /> but didn't run: Sta<br />rting program: /home<br />/joel/rtems-4.11-wor<br />k/rtems-testing/rtem<br />s/ticker-executables<br />/moxie-moxiesim-tick<br />er.ralf sim-core.c:4<br />76: assertion failed<br /> - (addr & (nr_bytes<br /> - 1)) == 0 Aborted <br />(core dumped) But at<br /> least the tools bui<br />ld. I will confirm s<br />tatus on the master <br />once I get time.|Ticket|
|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:3|milestone changed fr<br />om 4.11 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:4|owner changed from C<br />hris Johns to Joel S<br />herrill status chang<br />ed from new to assig<br />ned I suggest you cr<br />eate a patch and app<br />ly to the RSB to res<br />olve this. Please cl<br />ose the ticket in th<br />e commit. Thanks.|Ticket|
|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:5|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:6|If you want Moxie su<br />pport use master.|Ticket|
|https://devel.rtems.<br />org/ticket/2671#comm<br />ent:7|status changed from <br />assigned to closed r<br />esolution set to won<br />tfix|Ticket|


## [2677](https://devel.rtems.org/ticket/2677)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2677|Chris Johns|Joel Sherrill|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|build|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Any host, such as OX S, with a case insensitive file system does not build. PC  
I.c includes PCI.h. There must be a pci.h somewhere now.
```

* **summary**
```text
PowerPC BSP score603e PCI.c is broken on case insensitive file system
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Joel Sherrill|Mon, 28 Mar 2016 03:<br />15:56 GMT|status changed; owne<br />r set|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:1|
|Chris Johns|Mon, 28 Mar 2016 04:<br />03:39 GMT| |https://devel.rtems.<br />org/ticket/2677#comm<br />ent:2|
|Joel Sherrill|Mon, 28 Mar 2016 19:<br />08:15 GMT| |https://devel.rtems.<br />org/ticket/2677#comm<br />ent:3|
|Sebastian Huber|Thu, 26 Jan 2017 07:<br />16:00 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:4|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:5|
|Joel Sherrill|Thu, 13 Jul 2017 13:<br />42:18 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:6|
|Chris Johns|Mon, 12 Feb 2018 03:<br />57:08 GMT|component changed|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:7|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:1|owner set to Joel Sh<br />errill status change<br />d from new to assign<br />ed I will try to fix<br /> this but the BSP sh<br />ould have been remov<br />ed on master. Should<br /> I look for other fi<br />les with upper case <br />letters in their nam<br />e?|Ticket|
|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:2|Replying to joel.she<br />rrill: I will try to<br /> fix this but the BS<br />P should have been r<br />emoved on master. To<br />o late for 4.11. Sho<br />uld I look for other<br /> files with upper ca<br />se letters in their <br />name? Not 4.11. For <br />4.11 any simple hack<br /> to avoid this would<br /> be good.|Ticket|
|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:3|The file is installe<br />d as bsp/PCI.h and t<br />he shared infrastruc<br />ture is installed as<br /> bsp/pci.h. It is us<br />ed just enough where<br /> reworking code to a<br />void it for a deprec<br />ated BSP isn't worth<br /> it. I am testing a <br />patch now to rename <br />it to bsp/pciimpl.h.<br /> But at the moment, <br />I am going back to r<br />elax and enjoy my te<br />am with honey, lemon<br /> and fresh mint. I c<br />aught something from<br /> someone last week a<br />nd passed it along t<br />o Michele. :(|Ticket|
|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:4|milestone changed fr<br />om 4.11.1 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:5|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:6|status changed from <br />assigned to closed r<br />esolution set to won<br />tfix This BSP has be<br />en removed from the <br />RTEMS source tree.|Ticket|
|https://devel.rtems.<br />org/ticket/2677#comm<br />ent:7|component changed fr<br />om unspecified to bu<br />ild|Ticket|


## [2747](https://devel.rtems.org/ticket/2747)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2747|Patrick Gauvin|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|lib/dl|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
|Ryan Slabaugh| |3298|


* **description**
```text
Expected behavior of dlerror:
- The error is cleared after each invocation
-  
 `NULL` is returned when no error is set
- Return value is `char *`, not `con  
st char *`
http://pubs.opengroup.org/onlinepubs/9699919799/functions/dlerror.  
html

I've attached patches that address these issues, please critique them   
and I will submit to the development mailing list. They should also apply to m  
aster, but they were generated against 4.11.

Development Environment:
- ''  
'RTEMS Version:''' 4.11 (Branch "4.11", commit 3f72dda6ee518d3ea04341ad4df079e  
cb1895ef7)
- '''System Type:''' ARM Cortex-A9, xilinx_zynq_a9_qemu BSP
- '''  
GCC Version:'''

  arm-rtems4.11-gcc (GCC) 4.9.3 20150626 (RTEMS 4.11, RSB 1  
675a733536d1aec2020011e5e522497a442561a (HEAD, origin/4.11, 4.11), Newlib 2.2.  
0.20150423)
- '''RTEMS Configure Options:'''

  ../rtems/configure --target  
=arm-rtems4.11 --enable-rtemsbsp="xilinx_zynq_a9_qemu xilinx_zynq_zedboard xil  
inx_zynq_csp_cots xilinx_zynq_csp_hybrid" --enable-tests=samples --enable-posi  
x --prefix=$HOME/development/rtems/4.11 --disable-networking

```

* **summary**
```text
dlerror non-conformance
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 14 Aug 2017 00:<br />12:35 GMT|milestone set|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:1|
|Chris Johns|Mon, 05 Feb 2018 04:<br />41:10 GMT|status changed|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:2|
|Chris Johns|Thu, 08 Feb 2018 03:<br />37:08 GMT|blocking set|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:3|
|Chris Johns <chrisj@<br />…>|Thu, 08 Feb 2018 22:<br />32:42 GMT| |https://devel.rtems.<br />org/ticket/2747#comm<br />ent:4|
|Chris Johns|Thu, 08 Feb 2018 22:<br />34:06 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:5|
|Chris Johns <chrisj@<br />…>|Fri, 16 Feb 2018 02:<br />16:46 GMT| |https://devel.rtems.<br />org/ticket/2747#comm<br />ent:6|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:1|milestone set to 4.1<br />1.3|Ticket|
|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:2|status changed from <br />new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:3|blocking set to 3298|Ticket|
|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:4|In 7093cb5e/rtems: l<br />ibtest/dl01: Add dle<br />rror tests. Update #<br />2747|Ticket|
|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:5|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed|Ticket|
|https://devel.rtems.<br />org/ticket/2747#comm<br />ent:6|In 7093cb5e/rtems: l<br />ibtest/dl01: Add dle<br />rror tests. Update #<br />2747|Ticket|


### attachments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Patrick Gauvin|Sun, 26 Jun 2016 17:<br />36:02 GMT|attachment set|https://devel.rtems.<br />org/ticket/2747|
|Patrick Gauvin|Sun, 26 Jun 2016 17:<br />36:13 GMT|attachment set|https://devel.rtems.<br />org/ticket/2747|
|Patrick Gauvin|Sun, 26 Jun 2016 17:<br />36:22 GMT|attachment set|https://devel.rtems.<br />org/ticket/2747|
|Patrick Gauvin|Sun, 26 Jun 2016 17:<br />36:41 GMT|attachment set|https://devel.rtems.<br />org/ticket/2747|

|guid|description|category|attachment_link|
|:---:|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2747|attachment set to 00<br />01-libdl-Clear-error<br />-between-dlerror-inv<br />ocations.patch|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2747/0001-libdl-Cl<br />ear-error-between-dl<br />error-invocations.pa<br />tch|
|https://devel.rtems.<br />org/ticket/2747|attachment set to 00<br />02-libdl-dlerror-ret<br />urn-NULL-when-no-err<br />or.patch|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2747/0002-libdl-dl<br />error-return-NULL-wh<br />en-no-error.patch|
|https://devel.rtems.<br />org/ticket/2747|attachment set to 00<br />03-libdl-Fix-dlerror<br />-return-type.patch|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2747/0003-libdl-Fi<br />x-dlerror-return-typ<br />e.patch|
|https://devel.rtems.<br />org/ticket/2747|attachment set to 00<br />04-Update-dlerror-us<br />age.patch|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2747/0004-Update-d<br />lerror-usage.patch|


## [2910](https://devel.rtems.org/ticket/2910)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2910|Joel Sherrill|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|doc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text

This section of the RSB has "+sb_check+" which I assume is supposed to be it  
alics or bold.

https://docs.rtems.org/branches/master/rsb/hosts.html#maveri  
cks

Also the formatting of the sentence on xz in the same section is odd.
```

* **summary**
```text
RSB docs for Mavericks has Incorrect Formatting Markup
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber|Wed, 15 Feb 2017 13:<br />44:44 GMT|owner, status, miles<br />tone changed|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:1|
|Joel Sherrill|Wed, 15 Feb 2017 14:<br />05:49 GMT|owner, milestone cha<br />nged|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:2|
|Chris Johns|Thu, 23 Mar 2017 01:<br />03:28 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:3|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />06:29 GMT|component changed|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:4|
|Chris Johns|Mon, 05 Feb 2018 04:<br />54:44 GMT|status changed|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:5|
|Chris Johns <chrisj@<br />…>|Mon, 05 Feb 2018 23:<br />22:15 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:6|
|Chris Johns <chrisj@<br />…>|Fri, 16 Feb 2018 02:<br />17:18 GMT| |https://devel.rtems.<br />org/ticket/2910#comm<br />ent:7|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:1|owner changed from C<br />hris Johns to Needs <br />Funding status chang<br />ed from new to assig<br />ned milestone change<br />d from 4.11.2 to Ind<br />efinite|Ticket|
|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:2|owner changed from N<br />eeds Funding to Chri<br />s Johns milestone ch<br />anged from Indefinit<br />e to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:3|milestone changed fr<br />om 4.11.2 to 4.11.3 <br />The 4.11.2 milestone<br /> is closing.|Ticket|
|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:4|component changed fr<br />om Documentation to <br />doc|Ticket|
|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:5|status changed from <br />assigned to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:6|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed In 739e0f9/rtems-<br />docs: rsb: Minor fix<br />es. Close #2910|Ticket|
|https://devel.rtems.<br />org/ticket/2910#comm<br />ent:7|In 739e0f9/rtems-doc<br />s: rsb: Minor fixes.<br /> Close #2910|Ticket|


## [2944](https://devel.rtems.org/ticket/2944)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2944|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|fs/fat|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
https://lists.rtems.org/pipermail/users/2017-March/031101.html

In msdos_shu  
t_down ( msdos_fsunmount.c ) there is a call to fat_file_close( .. ) which att  
empts to close a file
descriptor and write a range of metadata to that file's  
 director entry located in another cluster:

* fat_file_write_first_cluster_  
num
* fat_file_write_file_size
* fat_file_write_time_and_date

The problem  
 is that this is the root node, and of course doesn't have a corresponding par  
ent directory entry. 

In addition, the "parent directory entry" cluster num  
ber is initialised to 0x1 (FAT_ROOTDIR_CLUSTER_NUM) 
which is not working acc  
ording to the FAT specification (cluster numbering starts at 2).
This actuall  
y creates a critical bug that overwrites random data to above sectors, because  
 2 is subtracted from 1
to calculate the sector number of the cluster -> thro  
ugh a series of function calls -> leads to a sector number at
the end of FAT2  
 (just below the start of the cluster region). The driver believes this is a F  
AT region (in fat_buf_release),
writes the sector to what it "thinks" is FAT1  
, proceeds to copy the changes to FAT2 -> adds FAT_LENGTH (8161) to sector,
l  
eading to a write well into the cluster region, randomly overwriting files. 
  

The three function calls above lead to fsck complaining about disk structure  
:

#######

fsck from util-linux 2.27.1
fsck.fat 3.0.28 (2015-05-16)
0x4  
1: Dirty bit is set. Fs was not properly unmounted and some data may be corrup  
t.
1) Remove dirty bit
2) No action
? 2
There are differences between boot  
 sector and its backup.
This is mostly harmless. Differences: (offset:origina  
l/backup)
  65:01/00
1) Copy original to backup
2) Copy backup to original
  

3) No action
? 3
/  and
/APPLICAT.ION
  share clusters.
  Truncating sec  
ond to 0 bytes because first is FAT32 root dir.
/APPLICAT.ION
  File size is  
 4096 bytes, cluster chain length is 0 bytes.
  Truncating file to 0 bytes.
  
Perform changes ? (y/n) n
/dev/sdm1: 14 files, 1600/1044483 clusters

#####  
###

In particular the "shared cluster" problem is caused by fat_file_write_  
first_cluster_num, which adds a directory
entry to the root directory cluster  
 pointing at itself; e.g. there is a directory entry in cluster 2 pointing to
  

a file in cluster 2. (Note: this occurs because we have fixed the "point to c  
luster # 1 issue" by reading the relative
location of the root cluster node f  
rom the FAT volume info strcture). 

Removing the function call in msdos_shu  
t_down ( .. ) to close the root file descriptor solves the problem perfectly
  
(clean fsck). However, we're a bit unsure about the intent behind closing the   
root directory. 


```

* **summary**
```text
FAT data corruption during unmount()
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 20 Mar 2017 21:<br />21:33 GMT| |https://devel.rtems.<br />org/ticket/2944#comm<br />ent:1|
|slemstick|Tue, 28 Mar 2017 08:<br />15:10 GMT| |https://devel.rtems.<br />org/ticket/2944#comm<br />ent:2|
|Sebastian Huber|Thu, 11 May 2017 07:<br />31:02 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:3|
|Chris Johns|Mon, 14 Aug 2017 00:<br />21:48 GMT|version changed|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:4|
|Sebastian Huber|Thu, 24 Aug 2017 09:<br />56:36 GMT|owner, status change<br />d|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:5|
|Sebastian Huber|Wed, 06 Sep 2017 12:<br />39:26 GMT|version, milestone c<br />hanged|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:6|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 06 Sep 2017 12:<br />40:16 GMT| |https://devel.rtems.<br />org/ticket/2944#comm<br />ent:7|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 06 Sep 2017 12:<br />41:05 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:8|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />50:58 GMT|component changed|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:9|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:1|Replying to Sebastia<br />n Huber: Removing th<br />e function call in m<br />sdos_shut_down ( .. <br />) to close the root <br />file descriptor solv<br />es the problem perfe<br />ctly (clean fsck). I<br /> assume you mean fat<br />_file_close? However<br />, we're a bit unsure<br /> about the intent be<br />hind closing the roo<br />t directory. There i<br />s memory allocated i<br />n fat_file_open whic<br />h you would leak. I <br />see the fat_file_clo<br />se calls fat_buf_rel<br />ease and if the fs_i<br />nfo cache is not emp<br />ty it is holding a b<br />dbuf buffer so this <br />would cause a leak o<br />f buffers. What abou<br />t the fat_file_close<br /> calls in the msdos <br />init call on error? <br />Would they also caus<br />e the same problem?|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:2|Replying to Chris Jo<br />hns: Replying to Seb<br />astian Huber: Removi<br />ng the function call<br /> in msdos_shut_down <br />( .. ) to close the <br />root file descriptor<br /> solves the problem <br />perfectly (clean fsc<br />k). I assume you mea<br />n fat_file_close? Ye<br />s. However, we're a <br />bit unsure about the<br /> intent behind closi<br />ng the root director<br />y. There is memory a<br />llocated in fat_file<br />_open which you woul<br />d leak. We fixed thi<br />s issue by creating <br />a special "root file<br /> close" function, by<br /> removing the call t<br />o fat_file_update() <br />in fat_file_close() <br />(which caused the co<br />rruption). I see the<br /> fat_file_close call<br />s fat_buf_release an<br />d if the fs_info cac<br />he is not empty it i<br />s holding a bdbuf bu<br />ffer so this would c<br />ause a leak of buffe<br />rs. What about the f<br />at_file_close calls <br />in the msdos init ca<br />ll on error? Would t<br />hey also cause the s<br />ame problem? Yes, th<br />ese will cause the s<br />ame issues. To updat<br />e / summarise this t<br />icket a bit here: We<br /> originally attempte<br />d a fix to this prob<br />lem by setting the h<br />ard-coded root direc<br />tory cluster number <br />to 2, as well as the<br /> above (remove corru<br />ption caused by fat_<br />file_update() in fat<br />_file_close() on unm<br />ount). However, our <br />attempt to fix the b<br />roken root cluster n<br />umbering breaks a ha<br />shing mechanism in f<br />at_file_open(..). Th<br />is mechanism indexes<br /> open file descripto<br />rs based on 1) paren<br />t directory cluster <br />number and 2) offset<br /> into that directory<br /> structure. The issu<br />e is that the root d<br />irectory, and the fi<br />le pointed to by the<br /> first directory ent<br />ry in the root direc<br />tory, may construct <br />their hashes based o<br />n the same indexes: <br />Root directory: clus<br />ter number 2, offset<br /> 0 First file in roo<br />t directory: cluster<br /> number 2, offset 0 <br />Before, this was not<br /> a problem of course<br />, as the root direct<br />ory had the hard-cod<br />ed cluster number of<br /> 1, and the keys wer<br />e therefore always u<br />nique. But this can <br />actually cause a num<br />ber of new issues. T<br />he fix to this probl<br />em is to set the har<br />d-coded root cluster<br /> directory number ba<br />ck to 1, instead of <br />drastically changing<br /> the key hashing met<br />hod function calls a<br />nd data structures, <br />and trusting that re<br />moving calls to fat_<br />file_update(on_root_<br />node) are sufficient<br /> to avoid the data c<br />orruption issue desc<br />ribed above. However<br />, there are two othe<br />r places in msdos_mi<br />sc.c where the hardc<br />oded root directory <br />cluster number - FAT<br />_ROOTDIR_CLUSTER_NUM<br /> - is used: msdos_ge<br />t_name_node() msdos_<br />get_dotdot_dir_info_<br />cluster_num() Like t<br />his: if ( (MSDOS_EXT<br />RACT_CLUSTER_NUM(dot<br />dot_node)) == 0) { /<br />* we handle root dir<br /> for all FAT types i<br />n the same way with <br />the ordinary directo<br />ries ( through fat_f<br />ile_* calls ) */ fat<br />_dir_pos_init(dir_po<br />s); dir_pos->sname.c<br />ln = FAT_ROOTDIR_CLU<br />STER_NUM; } Which, t<br />o my understanding, <br />will never occur as <br />you should never hav<br />e a cluster number b<br />elow 2 in a complian<br />t (msdos) FAT file s<br />ystem. Does anyone k<br />now the intent behin<br />d this?|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:3|milestone changed fr<br />om 4.12 to 4.12.0|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:4|version changed from<br /> 4.11 to 4.12|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:5|owner changed from c<br />hrisj@… to Sebastian<br /> Huber status change<br />d from new to assign<br />ed|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:6|version changed from<br /> 4.12 to 4.11 milest<br />one changed from 4.1<br />2.0 to 4.11.3|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:7|In 4d495cf/rtems: do<br />sfs: Fix fat_file_up<br />date() Do not update<br /> the non-existant me<br />ta-data of the root <br />directory. Update #2<br />944.|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:8|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In a3199d91/rtems<br />: dosfs: Fix fat_fil<br />e_update() Do not up<br />date the non-existan<br />t meta-data of the r<br />oot directory. Close<br /> #2944.|Ticket|
|https://devel.rtems.<br />org/ticket/2944#comm<br />ent:9|component changed fr<br />om fs to fs/fat|Ticket|


## [2964](https://devel.rtems.org/ticket/2964)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2964|slemstick|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|fs/fat|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
We have a volume that has a lot of free'd up directory entries, one of which l  
ooks like this:

 * 1-> old LFN end entry n
 * 2-> old LFN end entry n - 1
  

 * 3-> old SHORT entry freed with byte[0] = 0xe5

and one remaining file, n  
amed slemstick.tar.gz, which resides AFTER this in the directory structure (an  
d is NOT deleted). The old, deleted LFN above (consisting of three consequtive  
 directory entries) earlier contained slemstick.tar.gz, such that the old file  
name still exist in the old LFN entries 1 and 2 above - but the SHORT entry (3  
) has been freed by setting byte[0] to 0xe5. 

The problem is that, when the  
 filename search algorithm in msdos_find_file_in_directory(..) encounters the   
LFN entries 1 and 2, it starts parsing them as normal LFN entries. When it enc  
ounters the SHORT entry 3) above, the variable entry_empty is set and the algo  
rithm continues to parse the remaining directory entries by skipping entry 3).  
 As a consequence, it never finds the actual file in the directory entries bel  
ow. 

A working fix to our problem is to add this clause in side the "else i  
f(entry_empty)" if check around line ~1400 in msdos_misc.c:

https://pastebi  
n.com/guW5JPfT

Which resets the search algorithm, if a short directory entr  
y that has been freed is found while searching for a long file name. 

Can a  
nyone comment on this patch?

```

* **summary**
```text
fat: msdos_find_file_in_directory(..) doesn't reset LFN search appropriately
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber|Fri, 31 Mar 2017 12:<br />24:33 GMT| |https://devel.rtems.<br />org/ticket/2964#comm<br />ent:1|
|Sebastian Huber|Mon, 03 Apr 2017 06:<br />12:40 GMT| |https://devel.rtems.<br />org/ticket/2964#comm<br />ent:2|
|Sebastian Huber|Thu, 11 May 2017 07:<br />31:02 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:3|
|Chris Johns|Mon, 14 Aug 2017 00:<br />22:25 GMT|version changed|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:4|
|Sebastian Huber|Thu, 24 Aug 2017 09:<br />56:36 GMT|status changed; owne<br />r set|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:5|
|Sebastian Huber|Thu, 24 Aug 2017 10:<br />02:52 GMT|component, summary c<br />hanged|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:6|
|Sebastian Huber|Wed, 06 Sep 2017 10:<br />01:51 GMT| |https://devel.rtems.<br />org/ticket/2964#comm<br />ent:7|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 06 Sep 2017 12:<br />08:46 GMT| |https://devel.rtems.<br />org/ticket/2964#comm<br />ent:8|
|Sebastian Huber|Wed, 06 Sep 2017 12:<br />09:49 GMT|version, milestone c<br />hanged|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:9|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 06 Sep 2017 12:<br />10:08 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:10|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />50:58 GMT|component changed|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:11|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:1|Could you please pro<br />vide a patch against<br /> the current Git mas<br />ter of RTEMS. Please<br /> also provide a self<br />-contained test case<br />, e.g. in ​https://g<br />it.rtems.org/rtems/t<br />ree/testsuites/fstes<br />ts/fsdosfsname01/ini<br />t.c|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:2|Please create two pa<br />tches with the git f<br />ormat-patch command.<br /> The first patch sho<br />uld add a test case <br />for this issue to ​h<br />ttps://git.rtems.org<br />/rtems/tree/testsuit<br />es/fstests/fsdosfsna<br />me01/init.c which fa<br />ils. The second patc<br />h should fix the pro<br />blem and let the tes<br />t case pass.|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:3|milestone changed fr<br />om 4.12 to 4.12.0|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:4|version changed from<br /> 4.11 to 4.12|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:5|owner set to Sebasti<br />an Huber status chan<br />ged from new to assi<br />gned|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:6|component changed fr<br />om General to filesy<br />stem summary changed<br /> from msdos_find_fil<br />e_in_directory(..) d<br />oesn't reset LFN sea<br />rch appropriately to<br /> fat: msdos_find_fil<br />e_in_directory(..) d<br />oesn't reset LFN sea<br />rch appropriately|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:7|It looks like a bug,<br /> but I am not able t<br />o write a test case <br />for this. The msdos_<br />set_first_char4file_<br />name() sets the firs<br />t byte of each direc<br />tory entry to 0xe5. <br />How did you end up w<br />ith 1-> old LFN end <br />entry n 2-> old LFN <br />end entry n - 1 3-> <br />old SHORT entry free<br />d with byte[0] = 0xe<br />5 ? Do you use a rem<br />ovable media and del<br />ete the file with an<br />other operating syst<br />em or via the short <br />file name?|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:8|In a2c204eb/rtems: d<br />osfs: Fix find name <br />next entry preparati<br />on Update #2964.|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:9|version changed from<br /> 4.12 to 4.11 milest<br />one changed from 4.1<br />2.0 to 4.11.3|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:10|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In a76c31e1/rtems<br />: dosfs: Fix find na<br />me next entry prepar<br />ation Close #2964.|Ticket|
|https://devel.rtems.<br />org/ticket/2964#comm<br />ent:11|component changed fr<br />om fs to fs/fat|Ticket|


### attachments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|slemstick|Mon, 03 Apr 2017 06:<br />06:49 GMT|attachment set|https://devel.rtems.<br />org/ticket/2964|

|guid|description|category|attachment_link|
|:---:|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2964|attachment set to l4<br />n_find.patch Patch f<br />ile agains master|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2964/l4n_find.patc<br />h|


## [2987](https://devel.rtems.org/ticket/2987)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|2987|slemstick|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|fs/fat|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
msdos_dir_read(..) uses a conversion function, convert_handler->utf16_to_utf8,  
 to convert LFN directory entry names in utf16 format to utf8. 

However, th  
e conversion handler sets the string length of the output utf8 string as well.  
 That variable: **string_size** in msdos_dir_read(..) is never re-initialised   
in the search algorithm. When the volume becomes sufficiently fragmented, de-a  
llocated LFN directory entry checksums will cause the filename search algorith  
m to fail, effectively breaking the current attempt to concatenate directory e  
ntry filename chunks, but the output string size is now much shorter (10 chara  
cters, where it should be **sizeof(tmp_dirent.d_name)**). Consequently, msdos_  
dir_read(..) will continue to parse directory entries with a much smaller outp  
ut string size. 

The end result is that attempts to read file names from a   
directory will output truncated file names (for example, readdir() will "work"  
 as normal but the output filenames are too short). Any attempt to open these   
truncated file names will, of course, fail. 
```

* **summary**
```text
fat: msdos_dir_read(..) doesn't reset conversion output string length
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Gedare|Tue, 11 Apr 2017 00:<br />43:35 GMT| |https://devel.rtems.<br />org/ticket/2987#comm<br />ent:1|
|Sebastian Huber|Thu, 11 May 2017 07:<br />31:02 GMT|milestone changed|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:2|
|Sebastian Huber|Mon, 12 Jun 2017 07:<br />32:58 GMT| |https://devel.rtems.<br />org/ticket/2987#comm<br />ent:3|
|Sebastian Huber|Thu, 24 Aug 2017 09:<br />56:36 GMT|status changed; owne<br />r set|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:4|
|Sebastian Huber|Thu, 24 Aug 2017 10:<br />03:56 GMT|component, summary c<br />hanged|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:5|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 06 Sep 2017 11:<br />22:03 GMT| |https://devel.rtems.<br />org/ticket/2987#comm<br />ent:6|
|Sebastian Huber|Wed, 06 Sep 2017 11:<br />24:30 GMT|version, milestone c<br />hanged|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:7|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 06 Sep 2017 11:<br />24:52 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:8|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />50:58 GMT|component changed|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:9|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:1|Please remove the sp<br />urious whitespace ch<br />anges, add "Closes #<br />2987." Into the comm<br />it message, and form<br />at a friendly short <br />commit message that <br />specifies the rtems <br />subsystem first, e.g<br />. "libfs/dosfs: ..."<br /> Please see Develope<br />r/Git|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:2|milestone changed fr<br />om 4.12 to 4.12.0|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:3|Without a real name <br />I cannot apply this <br />patch.|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:4|owner set to Sebasti<br />an Huber status chan<br />ged from new to assi<br />gned|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:5|component changed fr<br />om General to filesy<br />stem summary changed<br /> from msdos_dir_read<br />(..) doesn't reset c<br />onversion output str<br />ing length to fat: m<br />sdos_dir_read(..) do<br />esn't reset conversi<br />on output string len<br />gth|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:6|In 34dda604/rtems: d<br />osfs: Fix msdos_dir_<br />read() Set a proper <br />name buffer length f<br />or each converter in<br />vocation. Update #29<br />87.|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:7|version changed from<br /> 4.12 to 4.11 milest<br />one changed from 4.1<br />2.0 to 4.11.3|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:8|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In e1c3dc09/rtems<br />: dosfs: Fix msdos_d<br />ir_read() Set a prop<br />er name buffer lengt<br />h for each converter<br /> invocation. Close #<br />2987.|Ticket|
|https://devel.rtems.<br />org/ticket/2987#comm<br />ent:9|component changed fr<br />om fs to fs/fat|Ticket|


### attachments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|slemstick|Sun, 09 Apr 2017 10:<br />33:41 GMT|attachment set|https://devel.rtems.<br />org/ticket/2987|

|guid|description|category|attachment_link|
|:---:|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/2987|attachment set to 00<br />01-Fix-issue-that-ms<br />dos_dir_read-didn-t-<br />reset-an-output.patc<br />h|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/2987/0001-Fix-issu<br />e-that-msdos_dir_rea<br />d-didn-t-reset-an-ou<br />tput.patch|


## [3004](https://devel.rtems.org/ticket/3004)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3004|Linda Huxley|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|doc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
|chrisj@…| | |


* **description**
```text
There are a couple of apparent typos in section "5.2 Releases" in the Note box  
 near the bottom of the section.  The following switch is mentioned twice:

  
--with-rtemsbsp

However, I can't find that switch anywhere in the RSB sourc  
e code.  Should that read:

--with-rtems-bsp

Thare are a couple of typos   
in section "5.2.1. RTEMS Tools and Kernel":

$ mv rtems-source-builder-4.11.  
0 4.110
$ cd 4.11.0

That should read:

$ mv rtems-source-builder-4.11.0   
4.11.0
$ cd 4.11.0/rtems

```

* **summary**
```text
Typos in RTEMS User Manual 4.11.99
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Tue, 11 Jul 2017 00:<br />34:08 GMT|milestone changed|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:1|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />06:29 GMT|component changed|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:2|
|Chris Johns|Mon, 05 Feb 2018 03:<br />38:30 GMT|owner, status change<br />d|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:3|
|Chris Johns|Mon, 05 Feb 2018 23:<br />23:36 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:4|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:1|milestone changed fr<br />om 4.11.2 to 4.11.3|Ticket|
|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:2|component changed fr<br />om Documentation to <br />doc|Ticket|
|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:3|owner changed from c<br />hrisj@… to Chris Joh<br />ns status changed fr<br />om new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/3004#comm<br />ent:4|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed ​https://git.rtem<br />s.org/rtems-docs/com<br />mit/?h=4.11&id=03198<br />56bca6a0655e453a5faa<br />20344d97ff78c64|Ticket|


## [3024](https://devel.rtems.org/ticket/3024)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3024|Pavel|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|lib/dl|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed|dl04, dl05, depcomp,<br /> CXXDEPMOD|

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Building rtems-4.11.2-rc4 with "--enable-tests" option fails with error from d  
epcomp:
"depcomp: Variables source, object and depmode must be set"

The re  
ason (in my opinion) is empty CXXDEPMODE variable in Makefiles generated for d  
l04 and dl05.

I changed it to depmode=gcc for dl04 and depmode=gcc3 for dl0  
5 just to check, it helped.

But I don't know the right value for this varia  
ble.

target  - i386-rtems4.11
bsp     - pc486
version - rtems-4.11.2-rc4   
(version downloaded by rtems-source-builder-4.11.2-rc4)
```

* **summary**
```text
dl04, dl05 build failes
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Joel Sherrill|Tue, 23 May 2017 15:<br />47:28 GMT|owner, status change<br />d|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:1|
|Chris Johns|Wed, 24 May 2017 00:<br />06:42 GMT|milestone changed|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:2|
|Chris Johns|Tue, 11 Jul 2017 00:<br />37:09 GMT|milestone changed|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:3|
|Chris Johns <chrisj@<br />…>|Tue, 22 Aug 2017 23:<br />49:20 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:4|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />46:55 GMT|component changed|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:5|
|Chris Johns|Mon, 12 Feb 2018 03:<br />54:22 GMT|component changed|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:6|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:1|owner changed from j<br />oel.sherrill@… to Ch<br />ris Johns status cha<br />nged from new to ass<br />igned Changing own t<br />o chrisj since he ow<br />ns the dl tests and <br />has been hacking on <br />the Makefiles lately<br />. The script depcomp<br /> is at the top of a <br />bootstrapped source <br />tree and is document<br />ed as part of automa<br />ke. Hopefully the do<br />cumentation pointers<br /> saved someone some <br />time.|Ticket|
|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:2|milestone changed fr<br />om 4.11.3 to 4.11.2|Ticket|
|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:3|milestone changed fr<br />om 4.11.2 to 4.11.3|Ticket|
|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:4|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 2ed53cb9/rtems<br />: testsuite/dl: Add <br />C++ by default for D<br />L tests which use C+<br />+. Add AM C++ suppor<br />t to the testsuite c<br />onfigure.ac script. <br />Fix the dependences <br />in the DL tests. Clo<br />ses #3024.|Ticket|
|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:5|component changed fr<br />om testing to unspec<br />ified|Ticket|
|https://devel.rtems.<br />org/ticket/3024#comm<br />ent:6|component changed fr<br />om unspecified to li<br />b/dl|Ticket|


## [3031](https://devel.rtems.org/ticket/3031)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3031|Chris Johns|Amar Takhar|infra|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|doc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|blocker|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
|Joel@…| | |


* **description**
```text
Giving jails such as docs and sync access to an area of the TrueNAS storage wo  
uld make building and moving of the docs from sync to the docs website much si  
mpler.

Currently I build the docs on a server in Sydney, copy them to the R  
TEMS FTP server using an ssh key and docs.rtems.org picks up the copy. I like   
to make the whole process local to the RTEMS servers and not rely on gear here  
 with my dodgy connection and me needing to monitor it.
```

* **summary**
```text
Give docs.rtems.org and sync.rtems.org jails access to the TrueNAS storage.
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Joel Sherrill|Wed, 07 Jun 2017 06:<br />58:09 GMT|cc set|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:1|
|Amar Takhar|Wed, 07 Jun 2017 11:<br />45:10 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:2|
|Chris Johns|Thu, 15 Jun 2017 02:<br />27:38 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:3|
|Amar Takhar|Thu, 15 Jun 2017 02:<br />34:32 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:4|
|Chris Johns|Thu, 15 Jun 2017 02:<br />35:56 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:5|
|Amar Takhar|Mon, 19 Jun 2017 19:<br />00:38 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:6|
|Chris Johns|Tue, 11 Jul 2017 00:<br />35:11 GMT|severity, milestone <br />changed|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:7|
|Chris Johns|Tue, 11 Jul 2017 00:<br />35:41 GMT|owner, status change<br />d|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:8|
|Amar Takhar|Tue, 11 Jul 2017 02:<br />23:30 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:9|
|Amar Takhar|Tue, 11 Jul 2017 02:<br />24:07 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:10|
|Amar Takhar|Tue, 11 Jul 2017 12:<br />30:19 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:11|
|Chris Johns|Tue, 11 Jul 2017 23:<br />43:30 GMT| |https://devel.rtems.<br />org/ticket/3031#comm<br />ent:12|
|Chris Johns|Sun, 03 Sep 2017 05:<br />37:17 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:13|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />06:29 GMT|component changed|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:14|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:1|cc Joel@… added|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:2|OK I will look into <br />this Tonight or Frid<br />ay (2017-06-09). I'l<br />l try to get it done<br /> quickly tonight but<br /> that will depend on<br /> what time I get hom<br />e.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:3|How is this going?|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:4|Sigh, thanks for the<br /> reminder. I need to<br /> setup auto-reminder<br />s for trac to harass<br /> me. I need to fix s<br />omething in the swit<br />ch to give this mach<br />ine access to the VL<br />AN I am away tomorro<br />w (2016-06-15) but I<br /> will be back Friday<br /> (2016-06-16). I wil<br />l take care of this <br />then and have entere<br />d it into my calenda<br />r.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:5|Hey no problem, and <br />thanks. Let me know <br />how it goes.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:6|FYI an update I'm al<br />most done this just <br />took some time to cl<br />ean up a few VLANs o<br />n the switch.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:7|severity changed fro<br />m major to blocker m<br />ilestone changed fro<br />m 4.11.2 to 4.11.3 I<br /> cannot wait any lon<br />ger and will release<br /> RTEMS 4.11.2. Movin<br />g this to 4.11.3 and<br /> making it a blocker<br /> issue.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:8|owner changed from c<br />hrisj@… to Amar Takh<br />ar status changed fr<br />om new to assigned A<br />ssign to Amar.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:9|Huh, I thought I did<br /> this already I will<br /> look at it in the m<br />orning. Sorry.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:10|I think all I need t<br />o do is attach the s<br />hare, it's late here<br /> I will do it in the<br /> morning.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:11|This is done please <br />check to make sure i<br />t works.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:12|Replying to Amar Tak<br />har: This is done pl<br />ease check to make s<br />ure it works. Thank <br />you. I will take a l<br />ook over this week.|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:13|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed|Ticket|
|https://devel.rtems.<br />org/ticket/3031#comm<br />ent:14|component changed fr<br />om Documentation to <br />doc|Ticket|


## [3065](https://devel.rtems.org/ticket/3065)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3065|Chris Johns|chrisj@…|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|build|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|invalid| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
{{{
checking for scandir... no
../../../../../rtems-4.11.2/c/src/../../cpuki  
t/configure: 5249: Syntax error: Bad fd number
configure: error: /bin/sh '../  
../../../../rtems-4.11.2/c/src/../../cpukit/configure' failed for ../../cpukit  

}}}
```

* **summary**
```text
RTEMS 4.11.2 avr build fails
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />00:29 GMT|component changed|https://devel.rtems.<br />org/ticket/3065#comm<br />ent:1|
|Chris Johns|Mon, 05 Feb 2018 05:<br />29:27 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3065#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3065#comm<br />ent:1|component changed fr<br />om Autoconf to build|Ticket|
|https://devel.rtems.<br />org/ticket/3065#comm<br />ent:2|status changed from <br />new to closed resolu<br />tion set to invalid <br />I cannot repeat this<br /> building the 4.11 b<br />ranch tools and then<br /> RTEMS on FreeBSD 11<br />.1. As a result I wi<br />ll close this PR. No<br />te, the AVR BSP does<br /> not build as GCC fa<br />ils with: /opt/work/<br />chris/rtems/kernel/r<br />tems.git/c/src/../..<br />/cpukit/libfs/src/do<br />sfs/msdos_misc.c: In<br /> function 'msdos_fin<br />d_node_by_cluster_nu<br />m_in_fat_file': /opt<br />/work/chris/rtems/ke<br />rnel/rtems.git/c/src<br />/../../cpukit/libfs/<br />src/dosfs/msdos_misc<br />.c:2069:1: error: un<br />able to find a regis<br />ter to spill in clas<br />s 'POINTER_REGS' } ^<br /> /opt/work/chris/rte<br />ms/kernel/rtems.git/<br />c/src/../../cpukit/l<br />ibfs/src/dosfs/msdos<br />_misc.c:2069:1: erro<br />r: this is the insn:<br /> (insn 144 143 145 1<br />7 (set (reg:HI 26 r2<br />6) (reg/v/f:HI 96 [ <br />dir_entry ])) /opt/w<br />ork/chris/rtems/kern<br />el/rtems.git/c/src/.<br />./../cpukit/libfs/sr<br />c/dosfs/msdos_misc.c<br />:2061 83 {*movhi} (e<br />xpr_list:REG_DEAD (r<br />eg/v/f:HI 96 [ dir_e<br />ntry ]) (nil))) /opt<br />/work/chris/rtems/ke<br />rnel/rtems.git/c/src<br />/../../cpukit/libfs/<br />src/dosfs/msdos_misc<br />.c:2069: confused by<br /> earlier errors, bai<br />ling out|Ticket|


## [3066](https://devel.rtems.org/ticket/3066)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3066|Chris Johns| |defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/gcc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
C++ sample does not build:
{{{
Making all in iostream
gmake[6]: Entering di  
rectory '/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/  
build/lm32-rtems4.11-kernel-4.11.2-1/lm32-rtems4.11-kernel-4.11.2-1-4.11.2/bui  
ld/lm32-rtems4.11/c/lm32_evr/testsuites/samples/iostream'
lm32-rtems4.11-g++   
-B../../../../../lm32_evr/lib/ -specs bsp_specs -qrtems -DHAVE_CONFIG_H -I. -I  
../../../../../../../rtems-4.11.2/c/src/../../testsuites/samples/iostream -I..  
     -O0 -g -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstric  
t-prototypes -Wnested-externs -MT init.o -MD -MP -MF .deps/init.Tpo -c -o init  
.o ../../../../../../../rtems-4.11.2/c/src/../../testsuites/samples/iostream/i  
nit.cc
cc1plus: warning: command line option '-Wmissing-prototypes' is valid   
for C/ObjC but not for C++
cc1plus: warning: command line option '-Wimplicit-  
function-declaration' is valid for C/ObjC but not for C++
cc1plus: warning: c  
ommand line option '-Wstrict-prototypes' is valid for C/ObjC but not for C++
  
cc1plus: warning: command line option '-Wnested-externs' is valid for C/ObjC b  
ut not for C++
mv -f .deps/init.Tpo .deps/init.Po
lm32-rtems4.11-g++ -B../..  
/../../../lm32_evr/lib/ -specs bsp_specs -qrtems -O0 -g -Wall -Wmissing-protot  
ypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs       
  -o cxx_iostream.exe init.o
`.gcc_except_table._ZN9__gnu_cxx7__mutexD2Ev' re  
ferenced in section `.rodata.cst4' of /build/rtems/releases/build/4.11.2/rtems  
-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-lm32.bset/build/rte  
ms/releases/4.11.2/bin/../lib/gcc/lm32-rtems4.11/4.9.3/libstdc++.a(eh_terminat  
e.o): defined in discarded section `.gcc_except_table._ZN9__gnu_cxx7__mutexD2E  
v[_ZN9__gnu_cxx7__mutexD5Ev]' of /build/rtems/releases/build/4.11.2/rtems-sour  
ce-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-lm32.bset/build/rtems/re  
leases/4.11.2/bin/../lib/gcc/lm32-rtems4.11/4.9.3/libstdc++.a(eh_terminate.o)
  

`.gcc_except_table._ZN9__gnu_cxx7__mutexD2Ev' referenced in section `.rodata.  
cst4' of /build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/  
build/tmp/sb-chris/4.11/rtems-lm32.bset/build/rtems/releases/4.11.2/bin/../lib  
/gcc/lm32-rtems4.11/4.9.3/libstdc++.a(new_handler.o): defined in discarded sec  
tion `.gcc_except_table._ZN9__gnu_cxx7__mutexD2Ev[_ZN9__gnu_cxx7__mutexD5Ev]'   
of /build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/  
tmp/sb-chris/4.11/rtems-lm32.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/l  
m32-rtems4.11/4.9.3/libstdc++.a(new_handler.o)
}}}
```

* **summary**
```text
RTEMS 4.11.2 LM32 build fails
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 05 Feb 2018 05:<br />41:55 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3066#comm<br />ent:1|
|Chris Johns|Mon, 12 Feb 2018 03:<br />57:34 GMT|component changed|https://devel.rtems.<br />org/ticket/3066#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3066#comm<br />ent:1|status changed from <br />new to closed resolu<br />tion set to wontfix <br />If you want LM32 sup<br />port use master.|Ticket|
|https://devel.rtems.<br />org/ticket/3066#comm<br />ent:2|component changed fr<br />om unspecified to to<br />ol/gcc|Ticket|


## [3067](https://devel.rtems.org/ticket/3067)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3067|Chris Johns| |defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/gcc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
CPU Top does not build:
{{{
m32c-rtems4.11-gcc --pipe -DHAVE_CONFIG_H   -I..  
 -I../../cpukit/../../../m32csim/lib/include   -g -O0 -MT monitor/mon-queue.o   
-MD -MP -MF $depbase.Tpo -c -o monitor/mon-queue.o ../../../../../../rtems-4.1  
1.2/c/src/../../cpukit/libmisc/monitor/mon-queue.c &&\
mv -f $depbase.Tpo $de  
pbase.Po
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpu  
usagetop.c: In function 'print_memsize':
../../../../../../rtems-4.11.2/c/src  
/../../cpukit/libmisc/cpuuse/cpuusagetop.c:159:20: warning: integer overflow i  
n expression [-Woverflow]
   if (size > (1024 * 1024))
                    ^  

../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop  
.c:161:40: warning: integer overflow in expression [-Woverflow]
               
              size / (1024 * 1024), label);
                                   
       ^
../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpu  
usagetop.c:161:32: warning: division by zero [-Wdiv-by-zero]
                  
           size / (1024 * 1024), label);
                                ^
.  
./../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:  
 In function 'rtems_cpuusage_top_thread':
../../../../../../rtems-4.11.2/c/sr  
c/../../cpukit/libmisc/cpuuse/cpuusagetop.c:309:33: warning: cast to pointer f  
rom integer of different size [-Wint-to-pointer-cast]
   rtems_cpu_usage_data  
*  data = (rtems_cpu_usage_data*) arg;
                                 ^
..  
/../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:   
In function 'rtems_cpu_usage_top_with_plugin':
../../../../../../rtems-4.11.2  
/c/src/../../cpukit/libmisc/cpuuse/cpuusagetop.c:617:36: warning: cast from po  
inter to integer of different size [-Wpointer-to-int-cast]
     id, rtems_cpu  
usage_top_thread, (rtems_task_argument) &data
                                 
     ^
depbase=`echo monitor/mon-driver.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`  
;\
m32c-rtems4.11-gcc --pipe -DHAVE_CONFIG_H   -I.. -I../../cpukit/../../../m  
32csim/lib/include   -g -O0 -MT monitor/mon-driver.o -MD -MP -MF $depbase.Tpo   
-c -o monitor/mon-driver.o ../../../../../../rtems-4.11.2/c/src/../../cpukit/l  
ibmisc/monitor/mon-driver.c &&\
mv -f $depbase.Tpo $depbase.Po
depbase=`echo  
 monitor/mon-itask.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
m32c-rtems4.11-gcc  
 --pipe -DHAVE_CONFIG_H   -I.. -I../../cpukit/../../../m32csim/lib/include   -  
g -O0 -MT monitor/mon-itask.o -MD -MP -MF $depbase.Tpo -c -o monitor/mon-itask  
.o ../../../../../../rtems-4.11.2/c/src/../../cpukit/libmisc/monitor/mon-itask  
.c &&\
mv -f $depbase.Tpo $depbase.Po
In file included from ../../../../../.  
./rtems-4.11.2/c/src/../../cpukit/libmisc/dummy/default-configuration.c:113:0:  

../../cpukit/../../../m32csim/lib/include/rtems/confdefs.h: At top level:
.  
./../cpukit/../../../m32csim/lib/include/rtems/confdefs.h:1483:46: warning: ca  
st from pointer to integer of different size [-Wpointer-to-int-cast]
   #defi  
ne CONFIGURE_INIT_TASK_ARGUMENTS     ((rtems_task_argument) &bsp_boot_cmdline)  

                                              ^
../../cpukit/../../../m32cs  
im/lib/include/rtems/confdefs.h:1514:7: note: in expansion of macro 'CONFIGURE  
_INIT_TASK_ARGUMENTS'
       CONFIGURE_INIT_TASK_ARGUMENTS
       ^
../../c  
pukit/../../../m32csim/lib/include/rtems/confdefs.h:1515:5: error: initializer  
 element is not constant
     }
     ^
../../cpukit/../../../m32csim/lib/in  
clude/rtems/confdefs.h:1515:5: error: (near initialization for 'Initialization  
_tasks[0].argument')
}}}
```

* **summary**
```text
RTEMS 4.11.2 M32C build fails
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 05 Feb 2018 05:<br />42:28 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3067#comm<br />ent:1|
|Chris Johns|Mon, 12 Feb 2018 03:<br />57:48 GMT|component changed|https://devel.rtems.<br />org/ticket/3067#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3067#comm<br />ent:1|status changed from <br />new to closed resolu<br />tion set to wontfix <br />If you want M32C sup<br />port use master.|Ticket|
|https://devel.rtems.<br />org/ticket/3067#comm<br />ent:2|component changed fr<br />om unspecified to to<br />ol/gcc|Ticket|


## [3068](https://devel.rtems.org/ticket/3068)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3068|Chris Johns| |defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/gcc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
C++ sample fails to build:
{{{
moxie-rtems4.11-g++ -B../../../../../moxiesim  
/lib/ -specs bsp_specs -qrtems -Os -g -ffunction-sections -fdata-sections -Wal  
l -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wn  
ested-externs  -Wl,--gc-sections     -o cxx_iostream.exe init.o
init.o: In fu  
nction `__static_initialization_and_destruction_0':
/build/rtems/releases/bui  
ld/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxi  
e.bset/build/rtems/releases/4.11.2/lib/gcc/moxie-rtems4.11/4.9.3/include/c++/i  
ostream:74: undefined reference to `__dso_handle'
/build/rtems/releases/build  
/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.  
bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/libstdc+  
+.a(atomicity.o): In function `get_atomic_mutex':
/build/rtems/releases/build  
/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-gcc-4.9.3-newl  
ib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/libstdc++-v3/src/  
c++98/atomicity.cc:33: undefined reference to `__dso_handle'
/build/rtems/rel  
eases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/r  
tems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9  
.3/libstdc++.a(locale.o): In function `get_locale_cache_mutex':
/build/rtems/  
releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-  
gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/lib  
stdc++-v3/src/c++98/../../../../../gcc-4.9.3/libstdc++-v3/src/c++98/locale.cc:  
36: undefined reference to `__dso_handle'
/build/rtems/releases/build/4.11.2/  
rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/bui  
ld/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/libstdc++.a(syst  
em_error.o): In function `__static_initialization_and_destruction_0':
/build/  
rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtem  
s4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.  
11/libstdc++-v3/src/c++11/../../../../../gcc-4.9.3/libstdc++-v3/src/c++11/syst  
em_error.cc:65: undefined reference to `__dso_handle'
gmake[6]: Leaving direc  
tory '/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/bui  
ld/moxie-rtems4.11-kernel-4.11.2-1/moxie-rtems4.11-kernel-4.11.2-1-4.11.2/buil  
d/moxie-rtems4.11/c/moxiesim/testsuites/samples/iostream'
/build/rtems/releas  
es/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-gcc-4.  
9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/moxie-rtems4.11/libstdc++  
-v3/src/c++11/../../../../../gcc-4.9.3/libstdc++-v3/src/c++11/system_error.cc:  
66: undefined reference to `__dso_handle'
gmake[5]: Leaving directory '/build  
/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rte  
ms4.11-kernel-4.11.2-1/moxie-rtems4.11-kernel-4.11.2-1-4.11.2/build/moxie-rtem  
s4.11/c/moxiesim/testsuites/samples'
/build/rtems/releases/build/4.11.2/rtems  
-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rt  
ems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11/4.9.3/libstdc++.a(eh_alloc.  
o):/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/  
moxie-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd11.0-1/build/mox  
ie-rtems4.11/libstdc++-v3/libsupc++/../../../../gcc-4.9.3/libstdc++-v3/libsupc  
++/eh_alloc.cc:96: more undefined references to `__dso_handle' follow
gmake[4  
]: Leaving directory '/build/rtems/releases/build/4.11.2/rtems-source-builder-  
4.11.2/rtems/build/moxie-rtems4.11-kernel-4.11.2-1/moxie-rtems4.11-kernel-4.11  
.2-1-4.11.2/build/moxie-rtems4.11/c/moxiesim/testsuites/samples'
/build/rtems  
/releases/build/4.11.2/rtems-source-builder-4.11.2/rtems/build/tmp/sb-chris/4.  
11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/../lib/gcc/moxie-rtems4.11  
/4.9.3/../../../../moxie-rtems4.11/bin/ld: cxx_iostream.exe: hidden symbol `__  
dso_handle' isn't defined
gmake[3]: Leaving directory '/build/rtems/releases/  
build/4.11.2/rtems-source-builder-4.11.2/rtems/build/moxie-rtems4.11-kernel-4.  
11.2-1/moxie-rtems4.11-kernel-4.11.2-1-4.11.2/build/moxie-rtems4.11/c/moxiesim  
/testsuites'
/build/rtems/releases/build/4.11.2/rtems-source-builder-4.11.2/r  
tems/build/tmp/sb-chris/4.11/rtems-moxie.bset/build/rtems/releases/4.11.2/bin/  
../lib/gcc/moxie-rtems4.11/4.9.3/../../../../moxie-rtems4.11/bin/ld: final lin  
k failed: Bad value
}}}
```

* **summary**
```text
RTEMS 4.11.2 Moxie build fails
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 05 Feb 2018 05:<br />42:57 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3068#comm<br />ent:1|
|Chris Johns|Mon, 12 Feb 2018 03:<br />58:04 GMT|component changed|https://devel.rtems.<br />org/ticket/3068#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3068#comm<br />ent:1|status changed from <br />new to closed resolu<br />tion set to wontfix <br />If you want Moxie su<br />pport use master.|Ticket|
|https://devel.rtems.<br />org/ticket/3068#comm<br />ent:2|component changed fr<br />om unspecified to to<br />ol/gcc|Ticket|


## [3074](https://devel.rtems.org/ticket/3074)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3074|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
RTEMS 4.11.2 Released Tools version is wrong:
{{{
$ /opt/work/rtems/4.11/bin  
/arm-rtems4.11-gcc --version
arm-rtems4.11-gcc (GCC) 4.9.3 20150626 (RTEMS 4.  
11, RSB no-repo, Newlib 2.2.0.20150423)
Copyright (C) 2015 Free Software Foun  
dation, Inc.
This is free software; see the source for copying conditions.  T  
here is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR  
 PURPOSE.
}}}

The RSB field should be `4.11.2`.
```

* **summary**
```text
gcc version report for released tools is wrong.
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Wed, 07 Feb 2018 21:<br />54:15 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3074#comm<br />ent:1|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3074#comm<br />ent:1|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 3822803/rtems-<br />source-builder: gcc:<br /> Use the RSB release<br /> for released tools.<br /> Using the RSB relea<br />se version for the g<br />cc version string me<br />ans the tools have a<br /> version string that<br /> matches the release<br />. Close #3074|Ticket|


## [3092](https://devel.rtems.org/ticket/3092)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3092|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|score|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **summary**
```text
ARM: Test spcontext01 fails on Cortex-R4
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber|Thu, 10 Aug 2017 06:<br />10:33 GMT|summary changed|https://devel.rtems.<br />org/ticket/3092#comm<br />ent:1|
|Sebastian Huber|Thu, 10 Aug 2017 06:<br />21:47 GMT|summary changed|https://devel.rtems.<br />org/ticket/3092#comm<br />ent:2|
|Sebastian Huber <seb<br />astian.huber@…>|Thu, 10 Aug 2017 06:<br />24:11 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3092#comm<br />ent:3|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3092#comm<br />ent:1|summary changed from<br /> Test spcontext01 fa<br />ils on Cortex-R5 to <br />ARM: Test spcontext0<br />1 fails on Cortex-R5|Ticket|
|https://devel.rtems.<br />org/ticket/3092#comm<br />ent:2|summary changed from<br /> ARM: Test spcontext<br />01 fails on Cortex-R<br />5 to ARM: Test spcon<br />text01 fails on Cort<br />ex-R4|Ticket|
|https://devel.rtems.<br />org/ticket/3092#comm<br />ent:3|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 5cc276e/rtems:<br /> arm: Fix CPU contex<br />t validation for Cor<br />tex-R4 Do not touch <br />the FPSCR[QC] bit si<br />nce this is DNM/RAZ <br />on Cortex-R4. Close <br />#3092.|Ticket|


## [3093](https://devel.rtems.org/ticket/3093)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3093|Sebastian Huber|Sebastian Huber|enhancement|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|score|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
| |normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The context validation function did not take care of the IT[7:0] bit field of   
the PSR.  Add a code block that validates this processor state.
```

* **summary**
```text
ARM: Validate IT[7:0] bit field in PSR on Thumb 2 targets
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber <seb<br />astian.huber@…>|Thu, 10 Aug 2017 06:<br />19:09 GMT| |https://devel.rtems.<br />org/ticket/3093#comm<br />ent:1|
|Sebastian Huber <seb<br />astian.huber@…>|Thu, 10 Aug 2017 07:<br />04:55 GMT| |https://devel.rtems.<br />org/ticket/3093#comm<br />ent:2|
|Sebastian Huber <seb<br />astian.huber@…>|Thu, 10 Aug 2017 07:<br />25:32 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3093#comm<br />ent:3|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3093#comm<br />ent:1|In a95d909/rtems: ar<br />m: Validate IT[7:0] <br />bit field of PSR Upd<br />ate #3093.|Ticket|
|https://devel.rtems.<br />org/ticket/3093#comm<br />ent:2|In 0daa8ab/rtems: ar<br />m: Use ARM code on T<br />humb 1 targets Updat<br />e #3093.|Ticket|
|https://devel.rtems.<br />org/ticket/3093#comm<br />ent:3|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 7d097c5/rtems:<br /> arm: Validate IT[7:<br />0] bit field of PSR <br />Close #3093.|Ticket|


## [3094](https://devel.rtems.org/ticket/3094)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3094|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Some architectures like ARM encode the short enum option state in the object f  
ile and the linker checks that this option is consistent for all objects of an  
 executable.  In case applications use -fno-short-enums, then this leads to li  
nker warnings.  Use the enum __packed attribute for the relevant enums to avoi  
d the -fshort-enums compiler option.  This attribute is at least available on   
GCC, LLVM/clang and the Intel compiler.
```

* **summary**
```text
ARM: Back port Newlib patch to avoid warnings with -fno-short-enums
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber <seb<br />astian.huber@…>|Fri, 11 Aug 2017 05:<br />16:41 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3094#comm<br />ent:1|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3094#comm<br />ent:1|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 50908d2/rtems-<br />source-builder: ARM:<br /> Avoid warnings with<br /> -fno-short-enums Cl<br />ose #3094.|Ticket|


## [3104](https://devel.rtems.org/ticket/3104)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3104|Chris Johns|Chris Johns|enhancement|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|shell|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
This is back port of the patch on development. See #3096.
```

* **summary**
```text
Shell internal commands should be public.
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 05 Feb 2018 05:<br />50:58 GMT|status changed|https://devel.rtems.<br />org/ticket/3104#comm<br />ent:1|
|Chris Johns|Mon, 05 Feb 2018 05:<br />51:09 GMT|component changed|https://devel.rtems.<br />org/ticket/3104#comm<br />ent:2|
|Chris Johns|Mon, 05 Feb 2018 23:<br />24:48 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3104#comm<br />ent:3|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3104#comm<br />ent:1|status changed from <br />assigned to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/3104#comm<br />ent:2|component changed fr<br />om unspecified to sh<br />ell|Ticket|
|https://devel.rtems.<br />org/ticket/3104#comm<br />ent:3|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed ​https://git.rtem<br />s.org/rtems/commit/?<br />h=4.11&id=89fd08eae6<br />d3801a917daccc992b0a<br />c5b32cf4d6|Ticket|


## [3105](https://devel.rtems.org/ticket/3105)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3105|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|config|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The unlimited objects option is available for POSIX key value pairs. This flag  
 must be removed for the memory size configuration.
```

* **summary**
```text
Invalid memory size configuration for POSIX keys
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber <seb<br />astian.huber@…>|Tue, 22 Aug 2017 06:<br />02:41 GMT| |https://devel.rtems.<br />org/ticket/3105#comm<br />ent:1|
|Sebastian Huber <seb<br />astian.huber@…>|Tue, 22 Aug 2017 14:<br />13:58 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3105#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3105#comm<br />ent:1|In e0660391/rtems: c<br />onfdefs: Fix POSIX k<br />eys configuration Re<br />move the OBJECTS_UNL<br />IMITED_OBJECTS flag <br />for the memory size <br />configuration. Updat<br />e #3105.|Ticket|
|https://devel.rtems.<br />org/ticket/3105#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 492c95e/rtems:<br /> confdefs: Fix POSIX<br /> keys configuration <br />Remove the OBJECTS_U<br />NLIMITED_OBJECTS fla<br />g for the memory siz<br />e configuration. Clo<br />se #3105.|Ticket|


## [3108](https://devel.rtems.org/ticket/3108)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3108|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Move the patches in the ARM buildste file.
```

* **summary**
```text
Remove RSB ARM specific config file rtems-arm-gcc-4.9.3-newlib-2.2.0-20150423-  
1.cfg
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Wed, 23 Aug 2017 01:<br />11:13 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3108#comm<br />ent:1|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3108#comm<br />ent:1|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 4a87913/rtems-<br />source-builder: Remo<br />ve RSB ARM specific <br />config file rtems-ar<br />m-gcc-4.9.3-newlib-2<br />.2.0-20150423-1.cfg <br />Closes #3108.|Ticket|


## [3161](https://devel.rtems.org/ticket/3161)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3161|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|score|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The I2C EEPROM driver must send the MSB of the address bytes first.
```

* **summary**
```text
I2C EEPROM driver uses incorrect address format
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber <seb<br />astian.huber@…>|Mon, 02 Oct 2017 11:<br />41:17 GMT| |https://devel.rtems.<br />org/ticket/3161#comm<br />ent:1|
|Sebastian Huber|Mon, 02 Oct 2017 11:<br />47:47 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3161#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3161#comm<br />ent:1|In 2e1d595/rtems: i2<br />c: Send MSB of addre<br />ss first for EEPROMs<br /> Update #3161.|Ticket|
|https://devel.rtems.<br />org/ticket/3161#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed [8ca15e26ba98f172<br />ee1396f34269ca664925<br />427d/rtems]|Ticket|


## [3162](https://devel.rtems.org/ticket/3162)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3162|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|score|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The RTEMS_MILLISECONDS_TO_TICKS() macro doesn't round up. Do not use it to cal  
culate the program timeout in ticks.  Check program done condition after the t  
imeout check to account for pre-emptions.
```

* **summary**
```text
I2C EEPROM driver uses incorrect program timeout handling
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber <seb<br />astian.huber@…>|Mon, 02 Oct 2017 11:<br />41:28 GMT| |https://devel.rtems.<br />org/ticket/3162#comm<br />ent:1|
|Sebastian Huber <seb<br />astian.huber@…>|Mon, 02 Oct 2017 11:<br />47:06 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3162#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3162#comm<br />ent:1|In 9c063df/rtems: i2<br />c: Fix EEPROM driver<br /> program timeout han<br />dling The RTEMS_MILL<br />ISECONDS_TO_TICKS() <br />macro doesn't round <br />up. Do not use it to<br /> calculate the progr<br />am timeout in ticks.<br /> Check program done <br />condition after the <br />timeout check to acc<br />ount for pre-emption<br />s. Update #3162.|Ticket|
|https://devel.rtems.<br />org/ticket/3162#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 1a21831/rtems:<br /> i2c: Fix EEPROM dri<br />ver program timeout <br />handling The RTEMS_M<br />ILLISECONDS_TO_TICKS<br />() macro doesn't rou<br />nd up. Do not use it<br /> to calculate the pr<br />ogram timeout in tic<br />ks. Check program do<br />ne condition after t<br />he timeout check to <br />account for pre-empt<br />ions. Close #3162.|Ticket|


## [3164](https://devel.rtems.org/ticket/3164)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3164|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|score|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **summary**
```text
aio_cancel() does not destroy the corresponding condition variables
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 04 Oct 2017 07:<br />25:50 GMT| |https://devel.rtems.<br />org/ticket/3164#comm<br />ent:1|
|Sebastian Huber <seb<br />astian.huber@…>|Wed, 04 Oct 2017 07:<br />26:55 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3164#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3164#comm<br />ent:1|In dcdd329/rtems: po<br />six: Fix aio_cancel(<br />) Update #3164.|Ticket|
|https://devel.rtems.<br />org/ticket/3164#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In c139a70/rtems:<br /> posix: Fix aio_canc<br />el() Close #3164.|Ticket|


## [3183](https://devel.rtems.org/ticket/3183)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3183|Steen Palm|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|arch/arm|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed|build|

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
I have built release 4.11.2 of RTEMS for ERC32, and it can successfully run th  
e hello example using the SPARC gdb.

I'm now trying to build RTEMS for ARM   
using RSB 4.11.2, but RSB fails after it has built the kernel, while it is mak  
ing a hello example test. The strange thing is that RSB is attempting to use a  
 file that is part of the RTEMS built for ERC32 - a file that does not exist.   
 The prefix for the ERC32 RTEMS is /home/smile/dev/rtems/4.11/erc32 and /home/  
smile/dev/rtems/4.11/arm for the ARM RTEMS.

Used build command:  ../source-  
builder/sb-set-builder --prefix=$HOME/dev/rtems/4.11/arm 4.11/rtems-arm

Ext  
ract from the log file rsb-report-arm-rtems4.11-kernel-4.11.2-1.txt:
...
mak  
e  all-am
make[5]: Entering directory '/home/smile/dev/rtems/4.11/rtems-sourc  
e-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kerne  
l-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites/samples'
BSP Testsuite  
 Data: all tests
Making all in hello
make[6]: Entering directory '/home/smil  
e/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-  
4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsu  
ites/samples/hello'
arm-rtems4.11-gcc -B../../../../../nds/lib/ -specs bsp_sp  
ecs -qrtems -DHAVE_CONFIG_H -I. -I../../../../../../../rtems-4.11.2/c/src/../.  
./testsuites/samples/hello -I..     -mcpu=arm9tdmi -O2 -Wall -Wmissing-prototy  
pes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs -MT i  
nit.o -MD -MP -MF .deps/init.Tpo -c -o init.o ../../../../../../../rtems-4.11.  
2/c/src/../../testsuites/samples/hello/init.c
mv -f .deps/init.Tpo .deps/init  
.Po
arm-rtems4.11-gcc -B../../../../../nds/lib/ -specs bsp_specs -qrtems -mcp  
u=arm9tdmi -O2 -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wst  
rict-prototypes -Wnested-externs    -mcpu=arm9tdmi   -o hello.exe init.o 
arm  
-rtems4.11-nm -g -n hello.exe > hello.num arm-rtems4.11-size hello.exe
   tex  
t	   data	    bss	    dec	    hex	filename
 145504	   2384	4043392	4191280	 3  
ff430	hello.exe
arm-rtems4.11-objcopy -O binary hello.exe hello.bin ../../../  
../../nds/build-tools/ndstool -c hello.nds -9 hello.bin -7 /home/smile/dev/rte  
ms/4.11/erc32/sparc-rtems4.11/erc32/lib/coproc.bin
Cannot open file '/home/sm  
ile/dev/rtems/4.11/erc32/sparc-rtems4.11/erc32/lib/coproc.bin'.
Nintendo DS r  
om tool compiled for rtems - Oct 10 2017 by Rafael Vuijk, Dave Murphy, Alexei   
Karpenko
Makefile:626: recipe for target 'hello.exe' failed
make[6]: Leaving  
 directory '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build  
/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-  
rtems4.11/c/nds/testsuites/samples/hello'
make[6]: *** [hello.exe] Error 1
m  
ake[5]: *** [all-local] Error 1
make[4]: *** [all] Error 2
make[3]: *** [all  
-recursive] Error 1
make[2]: *** [all-recursive] Error 1
Makefile:583: recip  
e for target 'all-local' failed
make[5]: Leaving directory '/home/smile/dev/r  
tems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-  
1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites/sa  
mples'
Makefile:245: recipe for target 'all' failed
make[4]: Leaving directo  
ry '/home/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rte  
ms4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.1  
1/c/nds/testsuites/samples'
Makefile:313: recipe for target 'all-recursive' f  
ailed
make[3]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-bui  
lder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.1  
1.2-1-4.11.2/build/arm-rtems4.11/c/nds/testsuites'
Makefile:424: recipe for t  
arget 'all-recursive' failed
make[2]: Leaving directory '/home/smile/dev/rtem  
s/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/a  
rm-rtems4.11-kernel-4.11.2-1-4.11.2/build/arm-rtems4.11/c/nds'
make[1]: *** [  
all-recursive] Error 1
Makefile:286: recipe for target 'all-recursive' failed  

make[1]: Leaving directory '/home/smile/dev/rtems/4.11/rtems-source-builder-  
4.11.2/rtems/build/arm-rtems4.11-kernel-4.11.2-1/arm-rtems4.11-kernel-4.11.2-1  
-4.11.2/build/arm-rtems4.11/c'
make: *** [all-recursive] Error 1
Makefile:41  
0: recipe for target 'all-recursive' failed shell cmd failed: /bin/sh -ex  /ho  
me/smile/dev/rtems/4.11/rtems-source-builder-4.11.2/rtems/build/arm-rtems4.11-  
kernel-4.11.2-1/doit
error: building arm-rtems4.11-kernel-4.11.2-1

```

* **summary**
```text
Build of RTEMS 4.11.2 using RSB fails for ARM
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Steen Palm|Thu, 12 Oct 2017 08:<br />00:23 GMT| |https://devel.rtems.<br />org/ticket/3183#comm<br />ent:1|
|Chris Johns|Thu, 12 Oct 2017 15:<br />52:03 GMT| |https://devel.rtems.<br />org/ticket/3183#comm<br />ent:2|
|Chris Johns|Tue, 06 Feb 2018 00:<br />41:37 GMT|status, component ch<br />anged; owner, milest<br />one set|https://devel.rtems.<br />org/ticket/3183#comm<br />ent:3|
|Chris Johns|Wed, 07 Feb 2018 03:<br />12:28 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3183#comm<br />ent:4|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3183#comm<br />ent:1|I forgot to mention <br />that the platform is<br /> Debian 8.|Ticket|
|https://devel.rtems.<br />org/ticket/3183#comm<br />ent:2|As a work around ple<br />ase add --without-rt<br />ems as an option to <br />the RSB set builder <br />command. You will th<br />en need to build RTE<br />MS yourself and you <br />can select the speci<br />fic BSP you are inte<br />rested in.|Ticket|
|https://devel.rtems.<br />org/ticket/3183#comm<br />ent:3|owner set to Chris J<br />ohns status changed <br />from new to assigned<br /> component changed f<br />rom admin to arch/ar<br />m milestone set to 4<br />.11.3|Ticket|
|https://devel.rtems.<br />org/ticket/3183#comm<br />ent:4|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed This fix resolves<br /> the RSB side of thi<br />ngs, the kernel is n<br />ow not build by defa<br />ult with the followi<br />ng change so this er<br />ror is avoided: ​htt<br />ps://git.rtems.org/r<br />tems-source-builder/<br />commit/?h=4.11&id=49<br />033ffc66f75d10ba47df<br />166be77827d0069b56 T<br />he underlying bug in<br /> the BSP is still pr<br />esent and if it is a<br /> problem a new ticke<br />t can be created.|Ticket|


## [3193](https://devel.rtems.org/ticket/3193)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3193|Ben|Chris Johns|project|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Download 4-11.2
Running resource builder gives for each call to
sb-check, sb  
-set-builder : a first line NOT RELEASED.
This suggest a not released package  
 which may be trusted but not guaranteed
```

* **summary**
```text
NOT released from source builder
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 05 Feb 2018 04:<br />36:33 GMT|status changed; owne<br />r set|https://devel.rtems.<br />org/ticket/3193#comm<br />ent:1|
|Chris Johns|Wed, 07 Feb 2018 02:<br />59:44 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3193#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3193#comm<br />ent:1|owner set to Chris J<br />ohns status changed <br />from new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/3193#comm<br />ent:2|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed I download ​rtems<br />-source-builder-4.11<br />.2.tar.xz and the sb<br />-check shows: $ ./so<br />urce-builder/sb-chec<br />k RTEMS Source Build<br />er - Check, 4.11.not<br />_released Environmen<br />t is ok which matche<br />s the output in this<br /> ticket. I copied th<br />e VERSION file from <br />this version to the <br />4.11 branch version <br />and got: $ ./source-<br />builder/sb-check RTE<br />MS Source Builder - <br />Check, 4.11.2 I beli<br />eve this issue is fi<br />xed on the branch.|Ticket|


## [3196](https://devel.rtems.org/ticket/3196)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3196|Ben| |defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|wontfix| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
4-11.2 source building fails during gdb generation on Linux Mint 17.1
"checki  
ng for python2.7" is followed by
"python missing are unusable"

this is due  
 to an #include "Python.h" that fails 

NOTE: the source building package of  
 4-11.2 that is used, generates a NOT RELEASED message at the start; a ticket   
has been raised for this
```

* **summary**
```text
4-11.2 gdb generation fails
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Ben|Mon, 23 Oct 2017 08:<br />38:46 GMT| |https://devel.rtems.<br />org/ticket/3196#comm<br />ent:1|
|Chris Johns|Mon, 05 Feb 2018 04:<br />47:05 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3196#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3196#comm<br />ent:1|The problem has been<br /> resolved The messag<br />e sequence "checking<br /> python2.7" and resu<br />lt "python missing" <br />are not related In b<br />etween is a check fo<br />r Python.h which was<br /> not installed. Inst<br />allation has resolve<br />d the generation iss<br />ue Hence a recommend<br />ation is left for sb<br />-check to test on Py<br />thon.h (as well to c<br />heck for ncurses and<br /> termcap)|Ticket|
|https://devel.rtems.<br />org/ticket/3196#comm<br />ent:2|status changed from <br />new to closed resolu<br />tion set to wontfix <br />This will not be fix<br />ed on this branch. C<br />hecking for a header<br /> is not simple to im<br />plement. Where do yo<br />u check for python.h<br /> because the locatio<br />n can vary from host<br /> to host. For exampl<br />e on MacOS and Xcode<br /> it is /Applications<br />/Xcode.app/Contents/<br />Developer/Platforms/<br />MacOSX.platform/Deve<br />loper/SDKs/MacOSX.sd<br />k/System/Library/Fra<br />meworks/Python.frame<br />work/Versions/2.7/in<br />clude/python2.7/Pyth<br />on.h.|Ticket|


### attachments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Ben|Tue, 17 Oct 2017 05:<br />09:27 GMT|attachment set|https://devel.rtems.<br />org/ticket/3196|

|guid|description|category|attachment_link|
|:---:|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3196|attachment set to co<br />nfig.log config.log <br />in ..../rtems-source<br />-builder-4.11.2/rtem<br />s/build/m68k-rtems4.<br />11-gdb-7.9-i686-linu<br />x-gnu-1/build/gdb|Ticket|https://devel.rtems.<br />org/attachment/ticke<br />t/3196/config.log|


## [3257](https://devel.rtems.org/ticket/3257)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3257|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|fs/fat|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
| |normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Take care that a file in the root directory with the same name as the
volume   
name can be found.
```

* **summary**
```text
fat: Support files in the root directoy with the same name as the volume label
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Christian Mauderer <<br />Christian.Mauderer@…<br />>|Tue, 05 Dec 2017 07:<br />01:08 GMT| |https://devel.rtems.<br />org/ticket/3257#comm<br />ent:1|
|Christian Mauderer <<br />Christian.Mauderer@…<br />>|Tue, 05 Dec 2017 07:<br />03:36 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3257#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3257#comm<br />ent:1|In ca835e56/rtems: d<br />osfs: Fix files with<br /> same name as volume<br /> name. Take care tha<br />t a file in the root<br /> directory with the <br />same name as the vol<br />ume name can be foun<br />d. Update #3257.|Ticket|
|https://devel.rtems.<br />org/ticket/3257#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 004a63e/rtems:<br /> dosfs: Fix files wi<br />th same name as volu<br />me name. Take care t<br />hat a file in the ro<br />ot directory with th<br />e same name as the v<br />olume name can be fo<br />und. Close #3257.|Ticket|


## [3258](https://devel.rtems.org/ticket/3258)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3258|Sebastian Huber|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|fs/fat|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
| |normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
If there is already a file with a long file name it isn't possible to
create   
a second file which has a name that ends on the first files name
(for example  
 ets.beam and sets.beam).
```

* **summary**
```text
fat: Fix creation of files with a similar name to existing files in the direct  
ory
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Christian Mauderer <<br />Christian.Mauderer@…<br />>|Thu, 07 Dec 2017 07:<br />03:44 GMT| |https://devel.rtems.<br />org/ticket/3258#comm<br />ent:1|
|Christian Mauderer <<br />Christian.Mauderer@…<br />>|Thu, 07 Dec 2017 07:<br />04:31 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3258#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3258#comm<br />ent:1|In 2fe3687/rtems: do<br />sfs: Allow creating <br />a file with similar <br />name. If there is al<br />ready a file with a <br />long file name it is<br />n't possible to crea<br />te a second file whi<br />ch has a name that e<br />nds on the first fil<br />es name (for example<br /> ets.beam and sets.b<br />eam). This patch fix<br />es that. Update #325<br />8.|Ticket|
|https://devel.rtems.<br />org/ticket/3258#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In d438427/rtems:<br /> dosfs: Allow creati<br />ng a file with simil<br />ar name. If there is<br /> already a file with<br /> a long file name it<br /> isn't possible to c<br />reate a second file <br />which has a name tha<br />t ends on the first <br />files name (for exam<br />ple ets.beam and set<br />s.beam). This patch <br />fixes that. Close #3<br />258.|Ticket|


## [3271](https://devel.rtems.org/ticket/3271)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3271|mholm|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|blocker|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The multiprocessor.org website is used to download e.g. mpc in many of the GCC  
 build descriptions. Recently the website underwent some changes and re-organi  
sed the download directories which have broken at least the 4.11 branch of RSB  
, but probably many other branches.

Having discussed this with Andreas Enge  
 (maintainer of MPC), he suggests that the gnu mirror is used instead:

''I   
see, thank you for the info. Actually, I reorganised the web site, so
the too  
l is permanently broken. They should not use multiprecision.org,
but instead   
the official GNU ftp site:''
   https://ftp.gnu.org/gnu/mpc/

It would prob  
ably be good to use the GNU mirror also for MPFR and GMP and others if they ar  
en't already.
```

* **summary**
```text
Avoid using multiprocessor.org in rtems source builder
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Gedare|Sat, 13 Jan 2018 14:<br />21:57 GMT|status, severity cha<br />nged; owner, version<br />, milestone set|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:1|
|Gedare|Sat, 13 Jan 2018 14:<br />23:10 GMT|version changed|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:2|
|Chris Johns|Mon, 15 Jan 2018 22:<br />00:57 GMT|status changed|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:3|
|Chris Johns|Mon, 15 Jan 2018 22:<br />25:37 GMT|version, milestone c<br />hanged|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:4|
|mholm|Tue, 16 Jan 2018 07:<br />09:03 GMT| |https://devel.rtems.<br />org/ticket/3271#comm<br />ent:5|
|Chris Johns|Tue, 16 Jan 2018 08:<br />01:24 GMT| |https://devel.rtems.<br />org/ticket/3271#comm<br />ent:6|
|Chris Johns <chrisj@<br />…>|Thu, 18 Jan 2018 03:<br />19:40 GMT| |https://devel.rtems.<br />org/ticket/3271#comm<br />ent:7|
|Chris Johns|Wed, 07 Feb 2018 22:<br />12:41 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:8|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:1|owner set to Chris J<br />ohns status changed <br />from new to assigned<br /> version set to 4.10<br /> severity changed fr<br />om critical to block<br />er milestone set to <br />5.1|Ticket|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:2|version changed from<br /> 4.10 to 5 Fix shoul<br />d be applied to 4.11<br />, 4.10, and master b<br />ranches of RSB, plea<br />se.|Ticket|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:3|status changed from <br />assigned to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:4|version changed from<br /> 5 to 4.11 milestone<br /> changed from 5.1 to<br /> 4.11.3 RTEMS 5 is a<br />lready using the GNU<br /> FTP site (1). I hav<br />e moved this ticket <br />to 4.11 and a 4.11.3<br /> milestone. Note, fo<br />r 4.10 we need a sep<br />arate ticket with a <br />suitable 4.10 milest<br />one, a ticket cannot<br /> cover more than one<br /> release and milesto<br />ne. That ticket coul<br />d reference this tic<br />ket and depend on it<br /> however by default <br />Trac does not suppor<br />t any ticket depende<br />ncy and I think we m<br />ay need something (2<br />) if we want to be a<br />ble to do this. (1) <br />​https://git.rtems.o<br />rg/rtems-source-buil<br />der/tree/source-buil<br />der/config/gcc-7-1.c<br />fg#n21 (2) ​https://<br />trac-hacks.org/wiki/<br />MasterTicketsPlugin|Ticket|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:5|I added ​https://dev<br />el.rtems.org/ticket/<br />3272 for the 4.10 br<br />anch.|Ticket|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:6|Replying to mholm: I<br /> added ​https://deve<br />l.rtems.org/ticket/3<br />272 for the 4.10 bra<br />nch. Thank you. I ha<br />ve a patch for that <br />branch so I will upd<br />ate the ticket detai<br />ls and post it soon.|Ticket|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:7|In f7c729e/rtems-sou<br />rce-builder: gcc: Up<br />date MPC verison to <br />one hosted on GNU's <br />FTP site. Update #32<br />71|Ticket|
|https://devel.rtems.<br />org/ticket/3271#comm<br />ent:8|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed Check the 4.11 br<br />anch and it is now u<br />sing the GNU ftp sit<br />e: package: arm-rtem<br />s4.11-gcc-4.9.3-newl<br />ib-2.2.0.20150423-x8<br />6_64-freebsd11.1-1 d<br />ownload: https://ftp<br />.gnu.org/gnu/mpc/mpc<br />-1.0.3.tar.gz -> sou<br />rces/mpc-1.0.3.tar.g<br />z downloading: sourc<br />es/mpc-1.0.3.tar.gz <br />- 654.2kB of 654.2kB<br /> (100%)|Ticket|


## [3274](https://devel.rtems.org/ticket/3274)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3274|Chris Johns| |defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Remove and clean up the configuration files that are not used on the branch.
```

* **summary**
```text
RSB remove unused tool configuration files.
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Fri, 19 Jan 2018 00:<br />41:42 GMT| |https://devel.rtems.<br />org/ticket/3274#comm<br />ent:1|
|Chris Johns|Fri, 19 Jan 2018 02:<br />19:17 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3274#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3274#comm<br />ent:1|In efa1677/rtems-sou<br />rce-builder: rtems: <br />Update all MPC versi<br />on to use GNU's FTP <br />site. Update #3274|Ticket|
|https://devel.rtems.<br />org/ticket/3274#comm<br />ent:2|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed|Ticket|


## [3275](https://devel.rtems.org/ticket/3275)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3275|Chris Johns|Chris Johns <chrisj@<br />…>|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
Do not build the RTEMS kernel by default when released.
```

* **summary**
```text
RSB do not build the kernel when released.
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Fri, 19 Jan 2018 02:<br />44:20 GMT|status changed; owne<br />r, resolution set|https://devel.rtems.<br />org/ticket/3275#comm<br />ent:1|
|Chris Johns <chrisj@<br />…>|Sun, 25 Mar 2018 23:<br />13:30 GMT| |https://devel.rtems.<br />org/ticket/3275#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3275#comm<br />ent:1|owner set to Chris J<br />ohns <chrisj@…> stat<br />us changed from new <br />to closed resolution<br /> set to fixed In 490<br />33ff/rtems-source-bu<br />ilder: kernel: Do no<br />t build the RTEMS ke<br />rnel by default when<br /> released. Close #32<br />75|Ticket|
|https://devel.rtems.<br />org/ticket/3275#comm<br />ent:2|In db86923/rtems-doc<br />s: RSB does not buil<br />d a kernel by defaul<br />t. Update #3275.|Ticket|


## [3279](https://devel.rtems.org/ticket/3279)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3279|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The Darwin configuration expects the tool to be in `/usr/local/bin` however th  
e `xz` is not part of the Xcode command line tools and may be built to a diffe  
rent path. Make the configuration path base.
```

* **summary**
```text
Make the XZ executable path based on the Darwin (MacOS) host.
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Mon, 29 Jan 2018 03:<br />26:00 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3279#comm<br />ent:1|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3279#comm<br />ent:1|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 892b416/rtems-<br />source-builder: darw<br />in: Make the xz exec<br />utable path based. T<br />he xz tool is not pr<br />ovided in Xcode comm<br />and line tools and n<br />eeds to built or obt<br />ained somehow. This <br />path can be any wher<br />e so relax the need <br />for an absolute path<br />. Close #3279|Ticket|


## [3289](https://devel.rtems.org/ticket/3289)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3289|Chris Johns|Chris Johns|enhancement|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
To help the long term support of the 4.11 branch back port the RSB changes to   
support mailing list posting of builds.
```

* **summary**
```text
RSB backport changes to support mailing list posting of builds.
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Mon, 05 Feb 2018 04:<br />33:55 GMT|status changed|https://devel.rtems.<br />org/ticket/3289#comm<br />ent:1|
|Chris Johns|Mon, 05 Feb 2018 23:<br />17:12 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3289#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3289#comm<br />ent:1|status changed from <br />assigned to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/3289#comm<br />ent:2|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed|Ticket|


## [3295](https://devel.rtems.org/ticket/3295)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3295|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|tool/rsb|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
The option expansion is missing `--with-download'.
```

* **summary**
```text
4.11: RSB `--source-only-download` does not download the source
```

### comments
|author|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns <chrisj@<br />…>|Wed, 07 Feb 2018 22:<br />14:41 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3295#comm<br />ent:1|
|Chris Johns <chrisj@<br />…>|Fri, 16 Feb 2018 02:<br />16:28 GMT| |https://devel.rtems.<br />org/ticket/3295#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3295#comm<br />ent:1|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In 4671017/rtems-<br />source-builder: sb: <br />Option --source-only<br />-download does not d<br />ownload the source. <br />The option expansion<br /> is missing `--with-<br />download'. Close #32<br />95|Ticket|
|https://devel.rtems.<br />org/ticket/3295#comm<br />ent:2|In 4671017/rtems-sou<br />rce-builder: sb: Opt<br />ion --source-only-do<br />wnload does not down<br />load the source. The<br /> option expansion is<br /> missing `--with-dow<br />nload'. Close #3295|Ticket|


## [3297](https://devel.rtems.org/ticket/3297)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3297|Chris Johns|Chris Johns|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|normal|4.11.3|build|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|normal|fixed| |

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text
A check of the 4.11 branch shows:
{{{
$ grep "EXEEXT =" `find sparc-rtems4.1  
1/c/erc32/testsuites/ -name Makefile`
  [removed some lines]
sparc-rtems4.11  
/c/erc32/testsuites/psxtmtests/psxtmcond05/Makefile:EXEEXT = .exe
sparc-rtems  
4.11/c/erc32/testsuites/psxtmtests/psxtmkey02/Makefile:EXEEXT = .exe
sparc-rt  
ems4.11/c/erc32/testsuites/Makefile:EXEEXT = .exe
sparc-rtems4.11/c/erc32/tes  
tsuites/libtests/block16/Makefile:EXEEXT = 
sparc-rtems4.11/c/erc32/testsuite  
s/libtests/heapwalk/Makefile:EXEEXT = 
  [removed some lines]
}}}
```

* **summary**
```text
4.11: libtests in the testsuite does not set EXEEXT to .exe
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Chris Johns|Thu, 08 Feb 2018 03:<br />27:07 GMT|status changed; owne<br />r set|https://devel.rtems.<br />org/ticket/3297#comm<br />ent:1|
|Chris Johns|Thu, 08 Feb 2018 22:<br />34:45 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3297#comm<br />ent:2|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3297#comm<br />ent:1|owner set to Chris J<br />ohns status changed <br />from new to accepted|Ticket|
|https://devel.rtems.<br />org/ticket/3297#comm<br />ent:2|status changed from <br />accepted to closed r<br />esolution set to fix<br />ed ​http://git.rtems<br />.org/rtems/commit/?i<br />d=1a304307a2f0527023<br />b912595c70d0c7fb17a2<br />d0|Ticket|


## [3075](https://devel.rtems.org/ticket/3075)
### meta
|id|reporter|owner|type|
|:---:|:---:|:---:|:---:|
|3075|Jeffrey Hill|Sebastian Huber|defect|

|status|priority|milestone|component|
|:---:|:---:|:---:|:---:|
|closed|low|4.11.3|doc|

|version|severity|resolution|keywords|
|:---:|:---:|:---:|:---:|
|4.11|minor|fixed|interrupt lock acqui<br />re|

|cc|blockedby|blocking|
|:---:|:---:|:---:|
| | | |


* **description**
```text

I suspect that in this section it should indicate that the second argument i  
s "rtems_interrupt_level * level" instead of "rtems_interrupt_level level". Fu  
rthermore, perhaps it should state that the function is caching some type of o  
paque context inside of "level" to be restored when the lock is released. Also  
, perhaps a better argument name would be "pPrvCtx"? The documentation might a  
lso divulge additional _functional_ details about what occurs on an SMP system  
. Does it prevent interrupts from running on all CPUs simultaneously when the   
lock is acquired? It does say something about an SMP lock, but that perhaps is  
 an implementation detail, and not a functional description of what the functi  
on does.

{{{
7.4.8 INTERRUPT_LOCK_ACQUIRE - Acquire an ISR Lock
CALLING S  
EQUENCE:

void rtems_interrupt_lock_acquire(
  rtems_interrupt_lock *lock,
  

  rtems_interrupt_level level
);
}}}

```

* **summary**
```text
rtems_interrupt_lock_acquire interface documentation issue in the "RTEMS C Use  
rs Guide"
```

### comments
|creator|pubDate|title|link|
|:---:|:---:|:---:|:---:|
|Gedare|Thu, 13 Jul 2017 22:<br />10:43 GMT|owner, status change<br />d|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:1|
|Sebastian Huber <seb<br />astian.huber@…>|Fri, 14 Jul 2017 05:<br />53:00 GMT| |https://devel.rtems.<br />org/ticket/3075#comm<br />ent:2|
|Sebastian Huber|Fri, 14 Jul 2017 05:<br />53:23 GMT|milestone set|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:3|
|Sebastian Huber <seb<br />astian.huber@…>|Fri, 14 Jul 2017 05:<br />55:52 GMT|status changed; reso<br />lution set|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:4|
|Sebastian Huber|Fri, 14 Jul 2017 06:<br />00:17 GMT| |https://devel.rtems.<br />org/ticket/3075#comm<br />ent:5|
|Sebastian Huber|Tue, 10 Oct 2017 06:<br />06:29 GMT|component changed|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:6|

|guid|description|category|
|:---:|:---:|:---:|
|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:1|owner changed from c<br />hrisj@… to Sebastian<br /> Huber status change<br />d from new to assign<br />ed|Ticket|
|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:2|In f776fe6/rtems-doc<br />s: c-user: Fix inter<br />rupt lock documentat<br />ion Update #3075.|Ticket|
|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:3|milestone set to 4.1<br />1.3|Ticket|
|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:4|status changed from <br />assigned to closed r<br />esolution set to fix<br />ed In eecec5f/rtems-<br />docs: c-user: Fix in<br />terrupt lock documen<br />tation Close #3075.|Ticket|
|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:5|If it is still uncle<br />ar, then please re-o<br />pen the ticket.|Ticket|
|https://devel.rtems.<br />org/ticket/3075#comm<br />ent:6|component changed fr<br />om Documentation to <br />doc|Ticket|
