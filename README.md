# Weight-scales-alert-message-on-whatsapp-project

The idea is to detect the weight by a sensor connected to the Arduino. When exceeding a certain weight, it is necessary for the user to be notified on WhatsApp about this event and to be informed of the respective value

It uses a weight sensor, attached to a 24-bit read module, HX711. It is connected by a clock wire and a data wire to the Arduino, transmitting data at about 3 seconds.

When the if condition is met, the Python program is used, placed on a nice Raspberry PI to retrieve the value and send it, via the API to Twilio, and further on as a message on WhatsApp.
