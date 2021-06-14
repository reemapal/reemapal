| | | |
|-|-|-|
|lscpu - display information about the CPU architecture| | |
|S NO.|COLUMNS|EXPLANATION|
|1|CPU |The logical CPU number of a CPU as used by the Linux kernel.|
| | | |
|2|CORE |The logical core number. A core can contain several CPUs.|
| | | |
|3|SOCKET| The logical socket number. A socket can contain several cores.|
| | | |
|4|BOOK |The logical book number. A book can contain several sockets.|
| | | |
|5|NODE| The logical NUMA node number. A node may contain several books.|
| | | |
|6|CACHE| Information about how caches are shared between CPUs.|
| | | |
|7|ADDRESS|The physical address of a CPU.|
| | | |
|8|ONLINE| Indicator that shows whether the Linux instance currently makes use of the CPU.|
| | | |
|9|CONFIGURED|Indicator that shows if the hypervisor has allocated the CPU to the virtual hardware on which the Linux instance runs.                                                                                                                                                                                                                                        CPUs that are configured can be set online by the Linux instance. This column contains data only if your hardware system and hyper-visor support dynamic CPU resource allocation.|
| | | |
|10|POLARIZATION|This column contains data for Linux instances that run on virtual hardware with a hypervisor that can switch the CPU dispatch-ing mode (polarization). The polarization can be:|
| | | |
|11|horizontal |The workload is spread across all available CPUs.|
| | | |
|12|vertical |The workload is concentrated on few CPUs.|
