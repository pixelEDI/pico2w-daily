//        _          _          _ _
//  _ __ (_)_  _____| | ___  __| (_)
// | '_ \| \ \/ / _ \ |/ _ \/ _` | |
// | |_) | |>  <  __/ |  __/ (_| | |
// | .__/|_/_/\_\___|_|\___|\__,_|_|
// |_|
// https://links.pixeledi.eu
// Pico 2 W - RP2350 | 02.2026 - Arduino C++

// Buttons
const int button1 = 21;  // Einfahren
const int button2 = 22;  // Ausfahren

// L298N Motor Driver
const int in1 = 19;
const int in2 = 18;

void motor_stop() {
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
}

void setup() {
    // Buttons als INPUT mit Pull-Down
    pinMode(button1, INPUT_PULLDOWN);
    pinMode(button2, INPUT_PULLDOWN);
    
    // Motor Pins als OUTPUT
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    
    motor_stop();
}

void loop() {
    if (digitalRead(button1) == HIGH) {
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
        delay(500);  // 0.5 Sekunde ausfahren
        motor_stop();
        delay(300);  // Entprellung
    }
    else if (digitalRead(button2) == HIGH) {
        digitalWrite(in2, HIGH);
        digitalWrite(in1, LOW);
        delay(500);  // 0.5 Sekunde einfahren
        motor_stop();
        delay(300);  // Entprellung
    }
    
    delay(100);
}
