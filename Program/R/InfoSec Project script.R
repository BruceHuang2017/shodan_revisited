#CS-7193 Security Economics
#Philipe Bled, Bruce Huang, and Jenna Baccus
#Project: Shodan 

#install.packages('plyr')
library(plyr)

#Set the working directory to whatever directory you saved the Shodan queries
setwd("C:/Users/philb/College/CS 7143 Security Economics/Project/Shodan_Queries")

A850_Telemetry_Gateway = read.csv('A850+Telemetry+Gateway.csv', header = TRUE)
A850_Telemetry_Gateway$Query <- "A850_Telemetry_Gateway"
A850_Telemetry_Gateway$Category <- "Telemetry"

ABB_Webmodule = read.csv('ABB+Webmodule.csv', header = TRUE)
ABB_Webmodule$Query <- "ABB_Webmodule"
ABB_Webmodule$Category <- "Embedded Web Server"

Allen_Bradley = read.csv('Allen-Bradley.csv', header = TRUE)
Allen_Bradley$Query <- "Allen_Bradley"
Allen_Bradley$Category <- "PAC"

BroadWeb = read.csv('BroadWeb.csv', header = TRUE)
BroadWeb$Query <-"BroadWeb"
BroadWeb$Category <-"HMI"

Cimetrics_Eplus_Web_Server = read.csv('Cimetrics+Eplus+Web+Server.csv', header = TRUE)
Cimetrics_Eplus_Web_Server$Query <-"Cimetrics_Eplus_Web_Server"
Cimetrics_Eplus_Web_Server$Category <-"Embedded Web Server"

CIMPLICITY = read.csv('CIMPLICITY.csv', header = TRUE)
CIMPLICITY$Query <- 'CIMPLICITY'
CIMPLICITY$Category <- 'HMI'

EIG_Embedded_Web_Server = read.csv('EIG+Embedded+Web+Server.csv', header = TRUE)
EIG_Embedded_Web_Server$Query <- "EIG_Embedded_Web_Server"
EIG_Embedded_Web_Server$Category <- "Embedded Web Server"

eiPortal = read.csv('eiPortal.csv', header = TRUE)
eiPortal$Query <- "eiPortal"
eiPortal$Category <- "Historian"

EnergyICT = read.csv('EnergyICT.csv', header = TRUE)
EnergyICT$Query <-"EnergyICT"
EnergyICT$Category <-"RTU"

HMS_AnyBus_S_WebServer = read.csv('HMS+AnyBus-S+WebServer.csv', header = TRUE)
HMS_AnyBus_S_WebServer$Query <- "HMS_AnyBus_S_WebServer"
HMS_AnyBus_S_WebServer$Category <- "Embedded Web Server"

i.LON = read.csv('i.LON.csv', header = TRUE)
i.LON$Query <- "i.LON"
i.LON$Category <- "BMS"

ioLogik = read.csv('ioLogik.csv', header = TRUE)
ioLogik$Query <- "ioLogik"
ioLogik$Category <- "PLC"

Modbus_Bridge = read.csv('Modbus+Bridge.csv', header = TRUE)
Modbus_Bridge$Query <- "Modbus_Bridge"
Modbus_Bridge$Category <- "Protocol Bridge"

ModbusGW = read.csv('ModbusGW.csv', header = TRUE)
ModbusGW$Query <- "ModbusGW"
ModbusGW$Category <- "Protocol Bridge"

Modicon_M340_CPU = read.csv('Modicon+M340+CPU.csv', header = TRUE)
Modicon_M340_CPU$Query <- "Modicon_M340_CPU"
Modicon_M340_CPU$Category <- "Protocol Bridge"

Niagara_Web_Server = read.csv('Niagara+Web+Server.csv', header = TRUE)
Niagara_Web_Server$Query <- "Niagara_Web_Server"
Niagara_Web_Server$Category <- "HAN/BMS"

Powerlink = read.csv('Powerlink.csv', header = TRUE)
Powerlink$Query <-"Powerlink"
Powerlink$Category <-"HAN/BMS"

Reliance_4_Control_Server = read.csv('Reliance+4+Control+Server.csv', header = TRUE)
Reliance_4_Control_Server$Query <- "Reliance_4_Control_Server"
Reliance_4_Control_Server$Category <- "SCADA"

RTS_Scada = read.csv('RTS+Scada.csv', header = TRUE)
RTS_Scada$Query <- "RTS_Scada"
RTS_Scada$Category <- "SCADA"

RTU560 = read.csv('RTU560.csv', header = TRUE)
RTU560$Query <- "RTU560"
RTU560$Category <- "RTU"

SIMATIC_NET = read.csv('SIMATIC+NET.csv', header = TRUE)
SIMATIC_NET$Query <- "SIMATIC_NET"
SIMATIC_NET$Category <- "HMI"

Simatic_S7 = read.csv('Simatic+S7.csv', header = TRUE)
Simatic_S7$Query <- "Simatic_S7"
Simatic_S7$Category <- "PLC"

SoftPLC= read.csv('SoftPLC.csv', header = TRUE)
SoftPLC$Query <- "SoftPLC"
SoftPLC$Category <- "PAC"

WAGO= read.csv('WAGO.csv', header = TRUE)
WAGO$Query <- "WAGO"
WAGO$Category <- "Telemetry"

data <- rbind(A850_Telemetry_Gateway,
              ABB_Webmodule,
              Allen_Bradley,
              BroadWeb,
              Cimetrics_Eplus_Web_Server,
              CIMPLICITY,
              EIG_Embedded_Web_Server,
              eiPortal,
              EnergyICT,
              HMS_AnyBus_S_WebServer,
              i.LON,
              ioLogik,
              Modbus_Bridge,
              ModbusGW,
              Modicon_M340_CPU,
              Niagara_Web_Server,
              Powerlink,
              Reliance_4_Control_Server,
              RTS_Scada,
              RTU560,
              SIMATIC_NET,
              SoftPLC,
              Simatic_S7,
              WAGO
              )

summary(data)
head(data)
length(data$Query)
#write.csv(data, file = "C:/Users/philb/College/CS 7143 Security Economics/Project/MyData.csv")

#######################################################################################################################
# OS 
#length(data$Operating.System)
length(data$Operating.System & !is.na(data$Operating.System))
summary((data$Operating.System))

#This doesn't work: ostype  <- data$Operating.System[data$Operating.System !=" " && !is.na(data$Operating.System)]
os <- data$Operating.System[!is.na(data$Operating.System)]
ostype <- os[os !=""]
length(ostype)

newos <-subset(data, !is.na(data$Operating.System))

#Count frequency of each OS
osfreq <- count(ostype)
class(osfreq)
head(osfreq)
sum(osfreq$freq)

#We combined this results from the OS column with the info extracted from the banner.
allOS <- read.csv("C:/Users/philb/College/CS 7143 Security Economics/Project/OS/OS_From_Banner_And_OS_cloumn.csv", header = TRUE)

sum(allOS$freq)

allOS <- allOS[order(- allOS$freq),]
#?barplot
OSbarplot<-barplot(allOS$freq
        #, names=allOS$os
        , ylim = c(0,1800)
        , ylab="Connections"
        , col = topo.colors(15)
        , main = "Number of Connections per OS Type"
        , horiz=FALSE
        )
text(x=OSbarplot[,1], y=-1, adj=c(1, 1), allOS$os, cex=0.8, srt=45, xpd=TRUE)

#LOG10
allOS$logfreq <- log10(allOS$freq)

logOSbarplot<-barplot(allOS$logfreq
                   #, names=allOS$os
                   , ylim = c(0,3.5)
                   , ylab="Log10 of Number of Connections"
                   , col = topo.colors(15)
                   , main = "Number of Connections per OS Type in Log10 scale"
                   , horiz=FALSE
)
text(x=logOSbarplot[,1], y=-.2, adj=c(1, 1), allOS$os, cex=0.8, srt=45, xpd=TRUE)

#####################################################################################################################
#Cateories
categ <- count(data, "Category")
categ <- categ[order(-categ$freq),]
head(categ)

catbp17 <- barplot(categ$freq
                      , space = .5
                      #, names=categ$x
                      , main = "Connections per System Type in 2017"
                      #, xlab = "System Type"
                      , ylim = c(0,12000)
                      , ylab="Connections"
                      , col = topo.colors(12)
                      , horiz=FALSE
                      )
text(x=catbp17[,1], y=-1, adj=c(1, 1), categ$Category, cex=0.8, srt=45, xpd=TRUE)


#_____________________________________________________________________________________________________________________
cats <- read.csv( "C:/Users/philb/College/CS 7143 Security Economics/Project/Categories.csv" , header=TRUE)
type <- read.csv( "C:/Users/philb/College/CS 7143 Security Economics/Project/cattype.csv" , header=TRUE)

cat11bp <- barplot(cats$old
                   , space = .5
                   #, names=categ$x
                   , main = "Connections per System and Device Type in 2011"
                   #, xlab = "System Type"
                   , ylim = c(0,3500)
                   , ylab="Connections"
                   , col = topo.colors(12)
                   , horiz=FALSE
)
text(x=cat11bp[,1], y=-1, adj=c(1, 1), categ$Category, cex=0.8, srt=45, xpd=TRUE)

cat17bp <- barplot(cats$new
                   , space = .5
                   #, names=categ$x
                   , main = "Connections per System and Device Type in 2011"
                   #, xlab = "System Type"
                   , ylim = c(0,30000)
                   , ylab="Connections"
                   , col = topo.colors(12)
                   , horiz=FALSE
)
text(x=cat17bp[,1], y=-1, adj=c(1, 1), categ$Category, cex=0.8, srt=45, xpd=TRUE)


#_____________________________________________________________________________________________________
tab <- as.table(cats)
tab<-(as.table(as.matrix(cats)))
class(tab)
table1$old <- tab$old
table1$new <-tab$new


count <- rbind(cats$old, cats$new)

mp <- barplot(count
              , beside = TRUE
              , ylim = c(0, 30000)
              , names.arg = cats$Category
              , col = topo.colors(2)
              , main = "Connections per System and Device Type in 2011 and 2017 "
              )

logcount <- log10(count)
mp <- barplot(logcount
              , beside = TRUE
              , ylim = c(0, 5)
              , names.arg = cats$Category
              , col = topo.colors(2)
              , main = "Log bas 10 of Connections per System and Device Type in 2011 and 2017 "
              , legend.text = c(2011, 2017)
              )


cats$diff <-  cats$new-cats$old
barplot(cats$diff
     , names.arg = cats$Category
     )

prop.table(table(tab[,2], tab[,3]))
chisq.test(table(tab[,2], tab[,3]))

mosaicplot(tab[,2], tab[,3])
hisq.test(tab )


#____________________________________________________________________________________________________
#Count Organizations and their frequencies
orgs_freq <- count(data, 'Organization')
class(orgs_freq)
orgs_freq <- orgs_freq[order(-orgs_freq$freq),]
head(orgs_freq)

top10 <- orgs_freq[1:10,]

bp<-barplot(top10$freq
        , space = 1
        #, names= top10$Organization
        , main="Number of Connections Top 10 Organizations"
        #, xlab="Organization"
        , ylab="Connections" 
        , col = topo.colors(10)
        , horiz=FALSE
        , ylim=c(0,2000)
        )
text(x=bp[,1], y=-1, adj=c(1, 1), top10$Organization, cex=0.8, srt=45, xpd=TRUE)

#TOP20
top20 <- orgs_freq[1:20,]

bp<-barplot(top20$freq
            , space = 1
            #, names= top10$Organization
            , main="Number of Connections Top 20 Organizations"
            #, xlab="Organization"
            , ylab="Connections" 
            , col = topo.colors(20)  #Other colors:rainbow, topo.colors, heat.colors
            , horiz=FALSE
            , ylim=c(0,2000)
)
text(x=bp[,1], y=-1, adj=c(1, 1), top20$Organization, cex=0.8, srt=45, xpd=TRUE)

#TOP50
top50 <- orgs_freq[1:50,]

bp<-barplot(top50$freq
            , space = 1
            #, names= top10$Organization
            , main="Number of Connections of Top 50 Organizations"
            #, xlab="Organization"
            , ylab="Connections" 
            , col = topo.colors(50)
            , horiz = FALSE
            , ylim=c(0,2000)
)
text(x=bp[,1], y=-1, adj=c(1, 1), top50$Organization, cex=0.8, srt=45, xpd=TRUE)


#_________________________________________________________________________________________________________________
country <- count(data, "Country")
country <- country[order(-country$freq),]
t20countries <- country[1:20,]
head(country)

t20countries_barplot <- barplot(country$freq
                      , space = .5
                      #, names=categ$x
                      , main = "Connections per System Type"
                      #, xlab = "System Type"
                      , ylim = c(0,12000)
                      , ylab="Connections"
                      , col = topo.colors(12)
                      , horiz=FALSE
                      )

text(x=catbarplot[,1], y=-1, adj=c(1, 1), country$Category, cex=0.8, srt=45, xpd=TRUE)

#______________________________________________________________________________________________________________________
#Country stuff
countdata <- read.csv("C:/Users/philb/College/CS 7143 Security Economics/Project/newandoldCountry.csv", header = TRUE)
head(countdata)
names(countdata)[1]<-paste("country")
countdata$oldcount <- as.numeric(as.character(countdata$oldcount))
countdata$newcount <- as.numeric(as.character(countdata$newcount))

#Sort by count Top10 and cut the table

cntold <- countdata[order( -countdata$oldcount),]
head(cntold)

cntold20 <- cntold[1:20,]
oldbp <- barplot(cntold20$oldcount
                 , space = .5
                 , main = "Connections in Top 20 Countries in 2011"
                 , ylim = c(0,4000)
                 , ylab="Connections"
                 , col = topo.colors(20)
                 , horiz=FALSE
)
text(x=oldbp[,1], y=-1, adj=c(1, 1), cntold20$country, cex=0.8, srt=45, xpd=TRUE)

cntnew <- countdata[order(-countdata$newcount),]
head(cntnew)
cntnew20 <- cntnew[1:20,]
newbp <- barplot(cntnew20$newcount
                 , space = .5
                 , main = "Connections in Top 20 Countries in 2017"
                 , ylim = c(0,25000)
                 , ylab="Connections"
                 , col = topo.colors(20)
                 , horiz=FALSE
)
text(x=newbp[,1], y=-1, adj=c(1, 1), cntnew20$country, cex=0.8, srt=45, xpd=TRUE)

#Same plots in base log10
cntold20$oldlog <- log10(cntold20$oldcount)
cntnew20$newlog <- log10(cntnew20$newcount)

log_oldbp <- barplot(cntold20$oldlog
                 , space = .5
                 , main = "Connections per Country in 2011 base log 10"
                 , ylim = c(0,4)
                 , ylab="log10(Connections)"
                 , col = topo.colors(20)
                 , horiz=FALSE
)
text(x=log_oldbp[,1], y=-.1, adj=c(1, 1), cntold20$country, cex=0.8, srt=45, xpd=TRUE)


log_newbp <- barplot(cntnew20$newlog
                 , space = .5
                 , main = "Connections per Country in 2017 base log 10"
                 , ylim = c(0,5)
                 , ylab="log10(Connections)"
                 , col = topo.colors(20)
                 , horiz=FALSE
)
text(x=log_newbp[,1], y=-.1, adj=c(1, 1), cntnew20$country, cex=0.8, srt=45, xpd=TRUE)


#
cntnew20$newlog <- log10(cntnew20$newcount)
cntnew20$oldlog <- log10(cntnew20$oldcount)
cntnew20

num <- rbind(cntnew20$oldlog , cntnew20$newlog)

op <- par(mar = c(10,4,4,2) + 0.1)
num_mp <- barplot(num
              , beside = TRUE
              , ylim = c(0, 5)
              , names.arg = cntnew20$country
              , col = topo.colors(2)
              , main = "Connections per Country from 2011 to 2017 in log base "
              , legend.text = c(2011, 2017)
              , las = 2
              )
abline(h=0)
num2 <- rbind(cntold20$oldcount , cntold20$newcount)

op <- par(mar = c(10,4,4,2) + 0.1)
num2_mp <- barplot(num2
                  , beside = TRUE
                  , ylim = c(0, 25000)
                  , names.arg = cntold20$country
                  , col = topo.colors(2)
                  , main = "Connections per Country from 2011 to 2017"
                  , legend.text = c(2011, 2017)
                  , las = 2
                  )


#######################################################################################################################
# MAPS
library(rworldmap)
#To see documentaion of this package run this line: vignette('rworldmap')

countrylist <- read.csv("C:/Users/philb/College/CS 7143 Security Economics/Project/mycountrylist.csv", header = TRUE)
countrylist$oldcount <- as.numeric(as.character(countrylist$oldcount))
countrylist$new_l10count <- log10( countrylist$newcount) 

head(countrylist)

sPDF <- joinCountryData2Map( countrylist, joinCode = "ISO2", nameJoinColumn = "code")

#par(mai=c(0,0,0.2,0),xaxs="i",yaxs="i")
#mapCountryData( sPDF, nameColumnToPlot="l10count" )
#COLORS = white2Black black2White palette heat topo terrain rainbow negpos8 negpos9 
mapParams <- mapCountryData( sPDF
                             , catMethod = "pretty" #for numeric data : "pretty", "fixedWidth", "diverging", "logFixedWidth", "quantiles"
                             , numCats = 5
                             , colourPalette=  c('lightgreen','yellow','orange','red', 'darkred') #c('lightgreen','green','yellow','orange','darkorange', 'red', 'darkred')
                             , nameColumnToPlot="new_l10count" 
                             , addLegend=TRUE
                             , oceanCol=  "lightblue"
                             , missingCountryCol  = "lightgrey"
                             ,  mapTitle = "Log 10 of Number of Connections per Country in 2017"
)
#do.call( addMapLegend, c(mapParams, legendWidth=1, legendMar = .1))


countrylist$old_l10count <- log10( countrylist$oldcount) 

countrylist<-countrylist[order(-countrylist$oldcount),]
head(countrylist)

sPDF2 <- joinCountryData2Map( countrylist, joinCode = "ISO2", nameJoinColumn = "code")


#COLORS = white2Black black2White palette heat topo terrain rainbow negpos8 negpos9 
mapParams <- mapCountryData( sPDF2
                             , catMethod = "pretty" #for numeric data : "pretty", "fixedWidth", "diverging", "logFixedWidth", "quantiles"
                             , numCats = 5
                             , colourPalette=  c('lightgreen','yellow','orange','red')
                             , nameColumnToPlot="old_l10count" 
                             , addLegend=TRUE
                             , oceanCol=  "lightblue"
                             , missingCountryCol  = "lightgrey"
                             ,  mapTitle = "Log 10 of Number of Connections per Country in 2011"
)
#do.call( addMapLegend, c(mapParams, legendWidth=1, legendMar = .1))

#_____________________________________________________________________________________________________
#This maps the difference
countrylist$diff <- countrylist$newcount - countrylist$oldcount
head(countrylist)
#countrylist$log10_diff <- log10( countrylist$diff) 
sPDF3 <- joinCountryData2Map( countrylist, joinCode = "ISO2", nameJoinColumn = "code")


mapParams <- mapCountryData( sPDF3
                             , catMethod = "fixedWidth" 
                             , colourPalette=  "topo" #c('lightgreen','green','yellow','orange','darkorange', 'red', 'darkred')
                             , nameColumnToPlot="diff" 
                             , addLegend=TRUE
                             , oceanCol=  "lightblue"
                             , missingCountryCol  = "lightgrey"
                             ,mapTitle = "Difference Number of Connections per Country from 2011 to 2017"
)

top20_diff <- countrylist[1:20,]

diff_bp <- barplot(top20_diff$diff
                     , space = .5
                     , main = "Connections per Country in 2017 base log 10"
                     , ylim = c(-100,20000)
                     , ylab="log10(Connections)"
                     , col = topo.colors(20)
                     , horiz=FALSE
)
abline(h=0, lty=1)
text(x=diff_bp[,1], y=-.1, adj=c(1, 1), top20_diff$name, cex=0.8, srt=45, xpd=TRUE)

#Only Finland, Greece and Slovenia diminish from 2011 to 2017

#Percentage of difference 
countrylist$percentdiff <- (countrylist$diff *100) / countrylist$oldcount
head(countrylist)
class(countrylist$precentdiff)

#Map the difference
sPDF4 <- joinCountryData2Map( countrylist, joinCode = "ISO2", nameJoinColumn = "code")

percentdiffmap <- mapCountryData( sPDF4
                             , catMethod = "pretty" #for numeric data : "pretty", "fixedWidth", "diverging", "logFixedWidth", "quantiles"
                             , numCats = 6
                             , colourPalette=  c('blue','lightgreen','yellow','orange','red','dark red')#c('lightgreen','green','yellow','orange','darkorange', 'red', 'darkred')
                             , nameColumnToPlot="percentdiff" 
                             , addLegend=TRUE
                             , oceanCol=  "lightblue"
                             , missingCountryCol  = "lightgrey"
                             , mapTitle = "Percentage Change in Connections per Country frm 2011 to 2017"
                             )

#_____________________________________________________________________________________________________________
sum(countrylist$newcount)

#Order my difference
countrylist<-countrylist[order(-countrylist$diff),]
head(countrylist)
countrylist<-countrylist[order(-countrylist$percentdiff),]
head(countrylist)
