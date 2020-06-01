
MQTT client("test.mosquitto.org", 1883, callback);



void callback(char* topic, byte* payload, unsigned int length) 
{
    
    char p[length + 1];
    memcpy(p, payload, length);
    p[length] = NULL;
    Particle.publish(p);
    
    if (!strcmp(p, "-atypical-on")){
        Particle.publish("atypical");
        digitalWrite(D2, HIGH);};
        
    if (!strcmp(p,"-altered-carbon-on")){
        Particle.publish("alteredcarbon");
        digitalWrite(D3, HIGH);};
        
    if (!strcmp(p, "-kettle-on")){
        Particle.publish("kettle");
        digitalWrite(D4, HIGH);};
        
    if (!strcmp(p, "-study-light-on")){
        Particle.publish("study");
        digitalWrite(D5, HIGH);}
        
    if (!strcmp(p, "-loung-light-on")){
        Particle.publish("lounge");
        digitalWrite(D6, HIGH);};
    
     if (!strcmp(p, "-all-off")){
        Particle.publish("off");
        
        digitalWrite(D2, LOW);
        digitalWrite(D3, LOW);
        digitalWrite(D4, LOW);
        digitalWrite(D5, LOW);
        digitalWrite(D6, LOW);};
}

void setup() 
{
  
    client.connect("WELCOME_HOME_CONTROL");
    client.subscribe("WELCOME_HOME");
  
    pinMode(D2, OUTPUT);
    pinMode(D3, OUTPUT);
    pinMode(D4, OUTPUT);
    pinMode(D5, OUTPUT);
    pinMode(D6, OUTPUT);
}


void loop() 
{
    if (client.isConnected()){client.loop();}

  
}