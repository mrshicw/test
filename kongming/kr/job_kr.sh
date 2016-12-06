#bin
data=data/kr
bin=bin/kr

# 从html提取数据
#cat ${data}/kr1.ls | ${bin}/xparser/testparser.unrecode ${bin}/xparser/jconf "http://www.kripr.com/1" > ${data}/kr1.testparser.unrecode
#cat ${data}/kr2.ls | ${bin}/xparser/testparser.unrecode ${bin}/xparser/jconf "http://www.kripr.com/2" > ${data}/kr2.testparser.unrecode
#cat ${data}/kr3.ls | ${bin}/xparser/testparser.unrecode ${bin}/xparser/jconf "http://www.kripr.com/3" > ${data}/kr3.testparser.unrecode
#cat ${data}/kr4.ls | ${bin}/xparser/testparser.unrecode ${bin}/xparser/jconf "http://www.kripr.com/4" > ${data}/kr4.testparser.unrecode
#cat ${data}/kr5.ls | ${bin}/xparser/testparser.unrecode ${bin}/xparser/jconf "http://www.kripr.com/5" > ${data}/kr5.testparser.unrecode
#cat ${data}/kr7.ls | ${bin}/xparser/testparser.unrecode ${bin}/xparser/jconf "http://www.kripr.com/7" > ${data}/kr7.testparser.unrecode


# 分别格式化数据
#cat ${data}/kr1.testparser.unrecode | ./${bin}/kr1.1.sh > ${data}/kr1.tmp
#cat ${data}/kr1.tmp                 | ./${bin}/kr1.2.sh > ${data}/kr1.dat
#cat ${data}/kr2.testparser.unrecode | ./${bin}/kr2.sh > ${data}/kr2.dat
#cat ${data}/kr3.testparser.unrecode | ./${bin}/kr3.sh > ${data}/kr3.dat
#cat ${data}/kr4.testparser.unrecode | ./${bin}/kr4.sh > ${data}/kr4.dat
#cat ${data}/kr5.testparser.unrecode | ./${bin}/kr5.sh > ${data}/kr5.dat
#cat ${data}/kr7.testparser.unrecode | ./${bin}/kr7.sh > ${data}/kr7.dat

# 生成AN:PN字典
#cat ${data}/kr1.tmp | ./${bin}/kr1.dict.py > ${data}/kr.dict 
#rm ${data}/kr1.tmp

# 根据AN:PN字典，替换相应的PN
cat ${data}/kr*.dat | 
./${bin}/kr.dict.65u.py "${data}/kr.dict" |
./${bin}/final.py |
./${bin}/db.py > ${data}/65u.kr.db

# 根据AN:PN字典，替换相应的PN
cat ${data}/kr*.dat | 
./${bin}/kr.dict.11p.py "${data}/kr.dict" |
./${bin}/final.py |
./${bin}/db.py > ${data}/11p.kr.db
