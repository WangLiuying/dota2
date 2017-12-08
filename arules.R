##arules

library(arules)
library(data.table)
library(Matrix)
library(arulesViz)

trainset = fread('dota2trainNew.csv', encoding="UTF-8")
str(trainset)

#先考虑组合问题
radient = trainset[win==1, -c(1:5)]
radient = as.matrix(radient);radient = (ifelse(radient>0,1,0))

dire = trainset[win==-1, -c(1:5)]
dire = as.matrix(dire);dire = (ifelse(dire>0,1,0))

combine = rbind(radient,dire)
rm(radient,dire)
combine_class = as(combine, 'transactions')

saveAsGraph(rules,'rules.graphml')
#查看支持度
sort(itemFrequency(combine_class),decreasing = T)[1:10]
itemFrequencyPlot(combine_class, topN=20)

rules = apriori(combine_class,
                parameter = list(support = 0.001, confidence=0.1, 
                                 target = 'rules',minlen=2))

rules_1 = apriori(combine_class,
                parameter = list(support = 0.001, confidence=0.1, 
                                 target = 'frequent itemsets',minlen=1))
rules_1
summary(rules)
#查看提升度较高项
inspect(sort(subset(rules,subset = lift>1),by = 'lift')[1:20])

rules_lift = subset(rules, subset = lift>1.1)
plot(rules_lift, method='graph',main='')
plot(rules_lift, method='grouped')
plot(rules_lift, method='paracoord')



plotly_arules(rules)
plotly_arules(rules,'matrix')
#htmlwidgets::saveWidget(p, "arules.html", selfcontained = FALSE)
#browseURL("arules.html")

##克制关系

##
trainset = fread('trainset.csv', encoding='UTF-8')
str(trainset)
##胜负方所选英雄的差异
win = trainset[win==1,6:117]>0
lose = trainset[win==-1,6:117]>0
winHeroes = names(sort(apply(win,2,sum),decreasing = T)[1:20])
loseHeroes = names(sort(apply(lose,2,sum),decreasing = T)[1:20])
winHeroes %in% loseHeroes

##胜负方队伍阵容属性的差异
win = trainset[win==1,118:159]
lose = trainset[win==-1,118:159]
win-lose


#yansuan
train = fread('dota2trainNew.csv', encoding='UTF-8')
compute = train[斧王==1&敌法师==-1,]
(sum(compute$win)+dim(compute)[1])/(2*dim(compute)[1])
