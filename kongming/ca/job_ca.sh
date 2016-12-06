#bin
data=data/ca
bin=bin/ca

#cat ${data}/ca.ls |
#./${bin}/xparser/testparser.1126 ${bin}/xparser/jconf "http://www.caipr.com/1" > ${data}/ca.testparser.1126

cat ${data}/ca.testparser.1126 |
./${bin}/html.py | # 过滤html中的转义字符等
./${bin}/1raw.raw.py | #去掉空行
./${bin}/2raw.raw.py | #一个字段合并为一行

./${bin}/ca.pn.py |  #整理PN，并移到最后，每个专利元组以PN结尾
./${bin}/ca.an.py |  #在AN前添加CA国代码
./${bin}/ca.ti.py |  #选择TI
./${bin}/ca.ab.py |  #选择AB 
./${bin}/ca.ipcr.py | #格式化IPCR
./${bin}/ca.au.py | #格式化AU
./${bin}/ca.pa.py | #缺失PA，用GA代替
./${bin}/ca.ga.py | #格式化GA
./${bin}/ca.agc.py | #格式化AGC
./${bin}/ca.pd.ipnn.ipnd.ipn.py | #无PD用IPND代替，无IPND用PD代替
./${bin}/ca.ad.ianc.iann.iand.ian.py | #无AD用IAND代替，无IAND用AD代替，IANC由IANN得出，合并IAN
./${bin}/ca.pctf.py | #格式化PCTF
./${bin}/ca.prc.py "${data}/dict.country" | #用字典替换国家
./${bin}/ca.prn.py | #格式化PRN
./${bin}/ca.prd.py | #格式化PRD
./${bin}/ca.pr.py | #合并PR
./${bin}/ca.other.py |  #过滤掉无用的字段
./${bin}/ca.pn2top.py | #将PN移动到前面，并且添加AC
./${bin}/pn2.3.py | #每行添加PN,由2列变成3列

./${bin}/final.py | #去除首末空格，空值等，包括多值中的值
./${bin}/db.py > ${data}/ca.db #生成入库数据
