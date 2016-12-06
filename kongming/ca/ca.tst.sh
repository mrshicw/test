#bin
#cat ca/ca.ls |
#./ca/xparser/testparser.1126 ca/xparser/jconf "http://www.caipr.com/1" > ca/ca.testparser.1126

cat ca/ca.testparser.1126 |

./html.py |
./ca/1raw.raw.py | #去掉空行
./ca/2raw.raw.py | #一个字段合并为一行

./ca/ca.pn.py |  #整理PN，并移到最后
./ca/ca.an.py |  #在AN前添加CA
./ca/ca.ti.py |  #选择TI
./ca/ca.ab.py |  #选择AB 
./ca/ca.ipcr.py | #格式化IPCR
./ca/ca.au.py | #格式化AU
./ca/ca.pa.py | #缺失PA，用GA代替
./ca/ca.ga.py | #格式化GA
./ca/ca.agc.py | #格式化AGC
./ca/ca.pd.ipnn.ipnd.ipn..tst.py | #无PD用IPND代替，无IPND用PD代替
./ca/ca.ad.ianc.iann.iand.ian.py | #无AD用IAND代替，无IAND用AD代替，IANC由IANN得出，合并IAN
./ca/ca.pctf.py | #格式化PCTF
./ca/ca.prc.py | #用字典替换国家
./ca/ca.prn.py | #格式化PRN
./ca/ca.prd.py | #格式化PRD
./ca/ca.pr.py | #合并PR

./ca/ca.other.py |  #过滤掉无用的字段
./ca/ca.pn2top.py | #将PN移动到前面，添加AC
./pn2.3.py | #每行添加PN
./final.py > ca/ca.final.20141126.tst
