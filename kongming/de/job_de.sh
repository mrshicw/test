#bin

data=data/de
bin=bin/de

#cat ${data}/de.ls | 
#./${bin}/xparser/testparser.nl ${bin}/xparser/jconf "http://www.deipr.com/1" > ${data}/de.testparser.nl

cat ${data}/de.testparser.nl |
./${bin}/html.py |

./${bin}/de.1raw.raw.py | 
./${bin}/de.2raw.raw.py | 
./${bin}/de.field.py |

./${bin}/de.ti.ab.py | 
./${bin}/de.au.py | 
./${bin}/de.ad.py | 
./${bin}/de.ac.py |
./${bin}/de.an.py | 
./${bin}/de.pd.py | 
./${bin}/de.pr.py | 
./${bin}/de.ipc.py |
./${bin}/de.ctd.py |
./${bin}/de.ctn.pro.py |
./${bin}/de.ctn.py |
./${bin}/de.ctn.end.py |
./${bin}/de.final.py |

./${bin}/pr.py |
./${bin}/ipc.py |
./${bin}/pn2.3.py |
./${bin}/final.py |
./${bin}/db.py > ${data}/de.db
