library(shiny)
library(quadprog)
library(bootstrap)
library(linprog)
library(data.table)
library(tidyverse)
library(lubridate)
library(dplyr)
library(tidyr)
library(readr)
library(ggplot2)
Korea_stocks <- read_csv("data/Korea_stocks.csv")
# Define UI for app that draws a histogram ----
ui <- fluidPage(
  
  # App title ----
  titlePanel("MBTI Stock Recommendation"),
  fluidRow(h3("  "),
           h3("Instruction for MSR"),
           helpText("Note:This app is made for people who want to get recommendation about Korean stock based on their personaluty,", 
                    "Please put the dates of stocks which will be searched, your MBTI personality, 
                    and how much you will invest in the recommended portfolio. If you don't know your MBTI please copy and paste this link and get the result",
                    a("https://www.16personalities.com/ko/%EB%AC%B4%EB%A3%8C-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC"))
    
    
   
),



  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    # Sidebar panel for inputs ----
    sidebarPanel(
     
      sliderInput("pf_percent", h3("Percent of your portfolio (%)"),
                  min = 0, max = 100, value = 50,
      ),
      sliderInput("bond_rate", h3("Government bond interest rate(0.1%)"),
                  min = 0, max = 100, value = 50,
      ),
      
      selectInput("mbti", h3("Select your MBTI"), 
                  choices = list("ISFJ" = 1, "ISFP" = 2,
                                 "ISTJ" = 3,"ISTP" = 4, "INFJ" = 5,
                                 "INFP" = 6,"INTJ" = 9, "INTP" = 10,
                                 "ESFJ" = 7,"ESFP" = 8, "ENFJ" = 11,
                                 "ENFP" = 12,"ESTJ" = 13,"ESTP" = 14, "ENTJ" = 15,
                                 "ENTP" = 16), selected = 1),
      
      selectInput("prospect", h3("Economic Prospect"), 
                  choices = list("Positive" = 1, "Negative" = 2
                                 ), selected = 1),
      
      
    ),
    # Main panel for displaying outputs ----
    mainPanel(
      # Output: Histogram ----
      plotOutput(outputId = "distPlot"),
      textOutput(outputId = "selected_var")
  
    )
  )
)


# Define server logic required to draw a histogram ----
server <- function(input, output) {
  mufree <- 0.05
  
  output$distPlot <- renderPlot({
    attach(Korea_stocks)
    beta <- c(
      coef(lm(KOSPI200~Samsung_elec))['Samsung_elec'],
      coef(lm(KOSPI200~SK_hynix))['SK_hynix'],
      coef(lm(KOSPI200~Naver))['Naver'],
      coef(lm(KOSPI200~LG_chemical))['LG_chemical'],
      coef(lm(KOSPI200~Kakao))['Kakao'],
      coef(lm(KOSPI200~Samsung_bio))['Samsung_bio'],
      coef(lm(KOSPI200~Hyundai))['Hyundai'],
      coef(lm(KOSPI200~Samsung_SDI))['Samsung_SDI'],
      coef(lm(KOSPI200~Celltrion))['Celltrion'],
      coef(lm(KOSPI200~KIA))['KIA'],
      coef(lm(KOSPI200~POSCO))['POSCO'],
      coef(lm(KOSPI200~Hyundai_Mobis))['Hyundai_Mobis']
    )
    
    
    h <- as.data.frame(beta)[1:length(beta),]
    s <- c(rep(0,3))
    
    if(input$prospect == 1){
      k <- as.data.frame(sort(beta))[(length(beta)-2):length(beta),]
     }else {
      k <- as.data.frame(sort(beta))[1:3,]
     }
    
    for( i in 1:3){
      for( j in 1: length(beta)){
        if(k[i] == h[j]){
          s[i] = j
        } 
      }
    }
    R = Korea_stocks[s+2]
    R
    mean_vect = apply(R,2,mean)
    mean_vect
    cov_mat = cov(R)
    sd_vect = sqrt(diag(cov_mat))
    sd_vect
    Amat = cbind(rep(1,3),mean_vect)  # set the constraints matrix
    muP = seq(.05,2.0,length=500) 
    sdP = muP
    
    weights = matrix(0,nrow=500,ncol=3) # storage for portfolio weights
    for (i in 1:length(muP))  # find the optimal portfolios for each target expected return
    {
      bvec = c(1,muP[i])  # constraint vector
      result =
        solve.QP(Dmat=2*cov_mat,dvec=rep(0,3),Amat=Amat,bvec=bvec,meq=2)
      sdP[i] = sqrt(result$value)
      weights[i,] = result$solution
    }
    
    plot(sdP,muP,lty=3, lwd = .5)+
      lines(c(0,2),mufree+c(0,2)*(muP[ind]-mufree)/sdP[ind],lwd=4,lty=1, col = "blue")#  plot
    # the efficient frontier (and inefficient portfolios
    # below the min var portfolio)
    mufree = input$bond_rate/1000
    points(0,mufree,cex=4,pch="*")  # show risk-free asset
    sharpe =( muP-mufree)/sdP # compute Sharpe's ratios
    ind = (sharpe == max(sharpe)) # Find maximum Sharpe's ratio
    options(digits=3)
    weights[ind,] #  print the weights of the tangency portfolio
    # show line of optimal portfolios
    points(sdP[ind],muP[ind],cex=4,pch="*") # show tangency portfolio
    ind2 = (sdP == min(sdP)) # find the minimum variance portfolio
    ind3 = (muP > muP[ind2])
    lines(sdP[ind3],muP[ind3],type="l",xlim=c(0,.25),
          ylim=c(0,.3),lwd=3, col = "red")  #  plot the efficient frontier
    legend("topleft", c("CML", "efficient frontier","tangency portfolio"),
           col = c("blue","red","purple","black"),
           lty = c(1,1,1,NA), lwd = c(4,3,3,NA), pch = c(NA,NA,NA,"*"), pt.cex = c(1,1,1,4)  )
    
    a <- (which(ind == T) - min(which(ind3 == T)))
    t <- c(rep(0,3))
    if(input$mbti < 3){
      t = weights[which(ind == T),]
    }else if(input$mbti >=3 && input$mbti <7){
      t = weights[which(ind == T)+3+round(50/a),]
    }else if(input$mbti >= 7 && input$mbti <15 ){
      t = weights[which(ind == T)+9+round(50/a),]
    }else if(input$mbti >= 15) {
      t = weights[which(ind == T)+12+round(50/a),]
    }
    
    final_w <- t*input$pf_percent
    name <- names(Korea_stocks[s+2])
    
    
    
    output$selected_var <- renderText({
      paste("The MSR result is ", name[1],"is", final_w[1],"%" 
            , name[2],"is", final_w[2],"%" 
            , name[3],"is", final_w[3],"%")})
    
    
    
      
    })
  
  
}
shinyApp(ui = ui, server = server)



