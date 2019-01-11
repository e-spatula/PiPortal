# PiPortal Error Codes

As there are several points where an error can occur when requesting and receiving information over the Internet and from the interaction of software and hardware it can be sometimes unclear where a problem originates. I hope to minimise this problem in my projects through the use of integer error codes and flashing LEDs. As this project is only a software project at this stage I will only include the error codes for the software components and not the LED colours which will indicate them in the physical world. However, as and when they are decided upon the LED colours will be added here. 

Integer error codes have been chosen for this project as it involves the interaction of several different systems and languages, across which integers are infinitely portable. Boolean alternatively could have been used, however it doesn't provide the same level of nuance.

Using integers for error codes is also practical for interaction with Arduinos as it enables the use of switching statements which can take the returned integer value of a function and flash an LED of the colour which pertains to the error code returned.

It is hoped that this document will evolve into something of a handbook for diagnosing errors with this system.

## Error Codes

 `1`
 > The request has been completed successfully and the user has the stated permission

` 0 `

>The request has completed successfully and the user does not have the stated permission

` -1 `

>The UID supplied is not the correct length or format to be processed. For example it may be 9 characters long.  
