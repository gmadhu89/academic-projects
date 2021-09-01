

#clear workspace
rm(list=ls())

library(dplyr)#library for dataframe manipulation
library(caret)#library will be used for dummy variable encoding

dataM = read.table("mental-heath-in-tech-2016_20161114.csv", sep=",", header=T,
                   stringsAsFactors = F)

#filter data
dataFiltered = dataM %>% 
  rename(provide.coverage = Does.your.employer.provide.mental.health.benefits.as.part.of.healthcare.coverage.) %>%
  rename(US.territory = What.US.state.or.territory.do.you.live.in.) %>%
  rename(treatment = Have.you.ever.sought.treatment.for.a.mental.health.issue.from.a.mental.health.professional.) %>%
  rename(illness = Have.you.been.diagnosed.with.a.mental.health.condition.by.a.medical.professional.) %>%
  rename(discussionEmployer = Do.you.think.that.discussing.a.mental.health.disorder.with.your.employer.would.have.negative.consequences.) %>%
  rename(discussionCoworker = Would.you.feel.comfortable.discussing.a.mental.health.disorder.with.your.coworkers.) %>%
  rename(discussionSupervisor = Would.you.feel.comfortable.discussing.a.mental.health.disorder.with.your.direct.supervisor.s..) %>%
  rename(seriousness = Do.you.feel.that.your.employer.takes.mental.health.as.seriously.as.physical.health.) %>%
  filter(discussionEmployer != '' | discussionCoworker != '' | discussionSupervisor != '' | seriousness != '') %>%
  mutate(negativeSentimentWork= ifelse(discussionEmployer== 'Yes' |
                                         discussionCoworker == 'No' |
                                         discussionSupervisor == 'No' |
                                         seriousness == 'No', 1, 0))%>%
  filter(What.country.do.you.work.in. != '') %>%
  mutate(isInUS = ifelse(What.country.do.you.work.in. == 'United States of America', 1 ,0)) %>%
  mutate(isInUK = ifelse(What.country.do.you.work.in. == 'United Kingdom', 1 ,0)) %>%
  mutate(isInCA = ifelse(What.country.do.you.work.in. == 'Canada', 1 ,0)) %>%
  mutate(isInDE = ifelse(What.country.do.you.work.in. == 'Germany', 1 ,0)) %>%
  mutate(isInNL = ifelse(What.country.do.you.work.in. == 'Netherlands', 1 ,0)) %>%
  mutate(illness = ifelse(illness == 'Yes', 1, 0))
  
nrow(dataFiltered)

#287 rows omitted for negative sentiment work variable

  dataFiltered %>% count(discussionEmployer)
  dataFiltered %>% count(discussionCoworker)
  dataFiltered %>% count(discussionSupervisor)
  dataFiltered %>% count(seriousness)



#aggregate data to get count values
dataPois = dataFiltered %>%
  group_by(negativeSentimentWork, isInUS, isInUK, isInCA, isInDE, isInNL) %>%
  summarize(Y_illness = sum(illness), .groups="keep")

dataFiltered %>% count(negativeSentimentWork)
nrow(dataFiltered)

#fit a poisson model
poisIllness = glm(Y_illness~., dataPois, family=poisson())
summary(poisIllness)
drop1(poisIllness, test="F")

model2 = glm(Y_illness~.-isInUK, dataPois, family=poisson())
summary(model2)
drop1(model2, test="F")

#check for multicollinearity
library(car)
vif(model2) #all less than 5 so no multicollinearity

dp = sum( residuals(model2, type="pearson")^2) / model2$df.res
dp #underdispersion 0.30

#add interaction terms
model3 = glm(Y_illness~negativeSentimentWork + isInUS + isInCA + isInNL + isInDE
             +negativeSentimentWork*isInUS + negativeSentimentWork*isInCA +
               negativeSentimentWork*isInNL + negativeSentimentWork*isInDE, dataPois,
             family=poisson())
drop1(model3, test="F") #no statistically significant interactions


#test out effect of coverage
dataFilteredCov = dataM %>% 
  rename(provide.coverage = Does.your.employer.provide.mental.health.benefits.as.part.of.healthcare.coverage.) %>%
  rename(treatment = Have.you.ever.sought.treatment.for.a.mental.health.issue.from.a.mental.health.professional.) %>%
  filter(provide.coverage =='Yes' | provide.coverage == 'No') %>%
  filter(What.country.do.you.work.in. != '') %>%
  mutate(offersCoverage = ifelse(provide.coverage == 'Yes', 1, 0)) %>%
  mutate(isInUS = ifelse(What.country.do.you.work.in. == 'United States of America', 1 ,0)) %>%
  mutate(isInUK = ifelse(What.country.do.you.work.in. == 'United Kingdom', 1 ,0)) %>%
  mutate(isInCA = ifelse(What.country.do.you.work.in. == 'Canada', 1 ,0)) %>%
  mutate(isInDE = ifelse(What.country.do.you.work.in. == 'Germany', 1 ,0)) %>%
  mutate(isInNL = ifelse(What.country.do.you.work.in. == 'Netherlands', 1 ,0))


dataFilteredCov %>% count(provide.coverage)
dataFilteredCov %>% count(treatment)

nrow(dataM) - nrow(dataFilteredCov) #689 rows ommitted when controlling for coverage


#aggregate data to get count values
dataPoisCov = dataFilteredCov %>%
  group_by(offersCoverage, isInUS, isInUK, isInCA, isInDE, isInNL) %>%
  summarize(Y_treatment = sum(treatment), .groups="keep")

poisTreatment = glm(Y_treatment~., dataPoisCov, family=poisson())
summary(poisTreatment)
drop1(poisTreatment, test="F")

model2Cov = glm(Y_treatment~.-isInUK, dataPoisCov, family=poisson())
drop1(model2Cov, test="F")

model3Cov = glm(Y_treatment~.-isInUK-isInCA, dataPoisCov, family=poisson())
drop1(model3Cov, test="F")

model4Cov = glm(Y_treatment~.-isInUK-isInCA-isInDE, dataPoisCov, family=poisson())
drop1(model4Cov, test="F")

model5Cov = glm(Y_treatment~.-isInUK-isInCA-isInDE-isInNL, dataPoisCov, family=poisson())
drop1(model5Cov, test="F")

#add some interaction terms
model6Cov = glm(Y_treatment~isInUS+offersCoverage + isInUS*offersCoverage, dataPoisCov, family=poisson())
drop1(model6Cov, test="F") #interaction is statistically significant
summary(model6Cov)

#check for dispersion
dpCov = sum( residuals(model6Cov, type="pearson")^2) / model6Cov$df.res
dpCov #4.308 has overdispersion


#can correct for it 
summary(model6Cov, dpCov)


