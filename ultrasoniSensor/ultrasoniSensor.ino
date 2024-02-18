#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

bool flags = false;
String data = "";

void setup(){
  lcd.init();
  lcd.backlight();
  lcd.setCursor(4,0);
  lcd.print("WELCOME");
  lcd.setCursor(5,1);
  lcd.print("USERS");

  Serial.begin(38400);
  delay(3000);

  Serial.write("INIT");
  lcd.clear();
  lcd.setCursor(0, 1);
  lcd.print("Status :");
}

void loop(){
  lcd.setCursor(9, 1);
  lcd.print(flags ? "ON " : "OFF");

  if(Serial.available()>0){
    data = Serial.readStringUntil('\n');
    if(data == "check"){
      Serial.write(flags ? "ON" : "OFF");
    } else if(data == "ON-IN"){
      flags = true;
    } else if(data == "OFF-IN"){
      flags = false;
    }
  }
}