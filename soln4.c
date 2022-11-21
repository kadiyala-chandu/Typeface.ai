#include <LiquidCrystal.h>


LiquidCrystal lcd(12, 11, 5, 4, 3, 2);


void setup()
{
  lcd.begin(16, 2); // Set up the number of columns and rows on the LCD.

  // Print a message to the LCD.
  lcd.print("Ambulance is approaching!");
}

void loop()
{
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting
  // begins with 0):
  lcd.setCursor(0,1);
  
  // Print a message to the LCD.
  lcd.print("Time:");

  for (int seconds = 60; seconds > 0; --seconds){
    lcd.setCursor(6,1);
    lcd.print(seconds-1);
    delay(1000);
    
  }
}
