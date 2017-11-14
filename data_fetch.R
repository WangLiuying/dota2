#get heros' attributes

library(rvest)
library(stringr)



#取出所有英雄的链接
url = 'http://www.dota2.com.cn/heroes/index.htm'
page = read_html(url)
linkpage = html_nodes(page,xpath="//ul[@class='hero_list']/li/a") %>% html_attr('href')

herosAttributes = data.frame()
for (url_link in linkpage)
{
##fetch data from a hero

page = read_html(url_link)

#英雄名字
name = html_nodes(page,xpath = "//div[@class='top_hero_card']//p") %>% html_text() %>% 
  str_extract(pattern = "[a-z|A-Z|]+.+") %>% str_replace_all(pattern = '[\\\t]',replacement = "")
name_ch = html_nodes(page,xpath = "//div[@class='top_hero_card']//p") %>% html_text() %>% 
  str_extract(pattern = ".+[a-z|A-Z|]") %>% str_replace_all(pattern = '[a-z|A-Z]',replacement = "")
jpg = html_nodes(page,xpath = "//div[@class='top_hero_card']//img") %>% html_attr('src')
#攻击类型
AttackType = html_node(page,xpath = "//p[@class='info_p']") %>% html_text() %>%
  str_replace_all(pattern = '[\\\t|\\\n]',replacement = "")

#定位&评分
type = html_nodes(page,xpath = "//p[@id='lastEm']//span[@class='_btn_type']") %>% 
  html_attr("type")
typeStars = html_nodes(page,xpath = "//p[@id='lastEm']//span[@class='_btn_type']") %>% 
  html_attr("star") %>% as.numeric()
names(typeStars) = type

type = rep(0,9)
names(type) = c('核心','控制','先手','打野','辅助','耐久','高爆发','推进','逃生')
type[names(typeStars)] = typeStars

#阵营
camp = html_nodes(page,xpath = "//p[@class='info_p zhengying_p']") %>% html_text() %>%
  str_replace_all(pattern = '[:space:]',replacement = "") 

#属性
pro6 = html_node(page,xpath = "//ul[@class='pro6_box']")
##力量
protext = html_node(pro6,xpath = "li[1]") %>% html_text() %>%
  str_replace_all(pattern = '[:space:]',replacement = "") 
strength = str_extract(protext, pattern = "[0-9|.]+\\+") %>% str_replace(pattern = '\\+',replacement = "") %>% as.numeric()
strength_growth = str_extract(protext, pattern = "\\+[0-9|.]+") %>% str_replace(pattern = '\\+',replacement = "") %>% as.numeric()
##敏捷
protext = html_node(pro6,xpath = "li[2]") %>% html_text() %>%
  str_replace_all(pattern = '[:space:]',replacement = "") 
agility = str_extract(protext, pattern = "[0-9|.]+\\+") %>% str_replace(pattern = '\\+',replacement = "") %>% as.numeric()
agility_growth = str_extract(protext, pattern = "\\+[0-9|.]+") %>% str_replace(pattern = '\\+',replacement = "") %>% as.numeric()
##智慧
protext = html_node(pro6,xpath = "li[3]") %>% html_text() %>%
  str_replace_all(pattern = '[:space:]',replacement = "") 
wisdom = str_extract(protext, pattern = "[0-9|.]+\\+") %>% str_replace(pattern = '\\+',replacement = "") %>% as.numeric()
wisdom_growth = str_extract(protext, pattern = "\\+[0-9|.]+") %>% str_replace(pattern = '\\+',replacement = "") %>% as.numeric()
##攻击
protext = html_node(pro6,xpath = "li[4]") %>% html_text() %>%
  str_replace_all(pattern = '[:space:]',replacement = "") 
attackSpeed = str_extract(protext, pattern = "攻击速度：\\d+") %>% str_replace_all(pattern="\\D",replacement = "") %>% as.numeric()
attackValue = str_extract(protext,pattern = "^\\d+") %>% as.numeric()
attackDistance = str_extract(protext,pattern = "攻击距离：\\d+") %>% str_replace_all(pattern = "\\D",replacement = "") %>% as.numeric()
##护甲
protext = html_node(pro6,xpath = "li[5]") %>% html_text() %>%
  str_replace_all(pattern = '[:space:]',replacement = "") 
defence = str_extract(protext, pattern = "^\\d+") %>% as.numeric()
pDef = str_extract(protext,pattern = "物理伤害抗性：\\d+") %>% str_replace_all(pattern = "\\D",replacement = "")%>% as.numeric()
mDef = str_extract(protext,pattern = "魔法伤害抗性：\\d+") %>% str_replace_all(pattern = "\\D",replacement = "") %>% as.numeric()
##移动
movement = html_node(pro6,xpath = "li[6]") %>% html_text() %>%
  str_replace_all(pattern = '[:space:]',replacement = "") %>% as.numeric()
##范围
areatext = html_node(page,xpath = "//div[@class='area_box']/table")%>% html_text()
sight_day = str_extract(areatext, pattern = "视野范围：[:space:]+\\d+") %>%
  str_replace_all(pattern = "\\D",replacement = "") %>% as.numeric()
sight_night = str_extract(areatext, pattern = "\\d+[:space:]+攻击范围") %>%
  str_replace_all(pattern = "\\D",replacement = "") %>% as.numeric()
ballisticVelocity = str_extract(areatext, pattern = "弹道速度：\\D+\\d+\\D") %>%
  str_replace_all(pattern = "\\D",replacement = "") %>% as.numeric()

df = data.frame(
  name = name, name_ch = name_ch, camp = camp,
  AttackType = AttackType,
  core = type[1], control = type[2], initiating = type[3],
  jungle = type[4], support = type[5], durable = type[6],
  explosive = type[7], push = type[8], survive = type[9],
  strength = strength, strength_growth = strength_growth,
  agility = agility, agility_growth = agility_growth,
  wisdom = wisdom, wisdom_growth = wisdom_growth,
  atttackValue = attackValue, attackSpeed = attackSpeed, attackDistance = attackDistance,
  defence = defence, pDef = pDef, mDef = mDef,
  movement = movement, ballisticVelocity =ballisticVelocity,
  sight_day = sight_day, sight_night = sight_night,
  picture = jpg
  )
herosAttributes = rbind(herosAttributes,df)
Sys.sleep(runif(n = 1,min = 1,max=7))
}
rownames(herosAttributes)=herosAttributes$name_ch

write.csv(herosAttributes,file= 'heroAttributes.csv',fileEncoding = "UTF-8")
