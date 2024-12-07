########################################################################
# demo: https://bilene.shinyapps.io/starwars/
# This is the UI:
library(shiny)
library(datasets)
library(dplyr)
data(starwars)

# Define UI 
ui <- shinyUI(fluidPage(
  
  # Application title
  titlePanel("Height-Mass Exploration of Star Wars Characters"),
  
  # Sidebar with checkboxes
  sidebarLayout(
    sidebarPanel(
      checkboxInput("female", "Include female", value = TRUE),
      checkboxInput("male", "Include male", value = TRUE),
      # insert some help text:
      checkboxInput("outlier", "Include Jabba the Hut", value = F),
      helpText('Filter Star Wars characters, fit a linear regression of height on mass. Use the checkboxes above!'),
      # slider value:
      sliderInput("height", "Your height in cm", value = 170, min = 40, max = 274, 1)),
    # Show the plot
    mainPanel(
      plotOutput("distPlot", width = "100%")
    )
  )
))

########################################################################
# This is the server (where calculations happen)
server <- function(input, output) {
  step1  <- reactive({
    sw <- data.frame(starwars)
    # remove outlier, if unselected
    if(input$outlier == FALSE){
      sw <- sw[-16,]
    }
    # remove male, if unselected
    if(input$male == FALSE){
      sw <- filter(sw, sex != 'male') 
    } 
    # remove female, if unselected
    if(input$female == FALSE){
      sw <- filter(sw, sex != 'female') 
    }
    # if none chosen, return null
    if(input$female == FALSE && input$male == FALSE && input$outlier == FALSE){
      return(NULL)
    }
    return(sw)
  })
  
  step2  <- reactive({
    # this is your height
    yh <- input$height
    return(yh)
  })
  
  output$distPlot <- renderPlot({
    sw <- step1() # call the first function
    if(!is.null(sw)) { # if not null,
      model1 <- lm(sw$height ~ sw$mass) # fit a model to get mean pred for weight
      b = summary(model1)$coefficients[1, 1]
      m = summary(model1)$coefficients[2, 1]
      pred <- (step2() - b) / m
      # scatterplot
      plot(sw$mass,sw$height, xlab = "Mass",
           ylab = "Height", bty = "n", pch = 19)
      abline(model1, col = "red", lwd = 4)
      text(sw$mass, sw$height,  sw$name,
           cex=0.88, pos=3, col="black") 
      mtext(paste('Slope ', round(summary(model1)$coefficients[2, 1],2)), side=3) # print slope
      mtext(paste('Intercept ', round(summary(model1)$coefficients[1, 1],2)), side=1, line = -2)
      mtext(paste('Your alter ego star wars character has a mass (weight on earth) of ', round(pred,1), ' kgs'), side=1, line =4.0, col = 'red', cex=1.3) # note pred will be printed
      
    }
  }, height = 650, width = 950 )
}

shinyApp(ui = ui, server = server)
