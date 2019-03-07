// UNIVERSITY OF COLORADO, BOULDER
//
// Author: Gautham KA and Kiran Hegde
// Date: 11/11/2018
//
// Lambda function which sends messages to SQS queue
//

const QUEUE_URL = "https://sqs.us-west-2.amazonaws.com/305186948671/project3_q.fifo";
const LAST_QUEUE = "https://sqs.us-west-2.amazonaws.com/305186948671/LastQueue.fifo";
var AWS = require('aws-sdk');


exports.handler = (event, context, callback) =>
{
    var sqs = new AWS.SQS({ region : 'us-west-2' });
    var eventText = JSON.stringify(event, null, 2);
    console.log(eventText);
    if(event.Temperature == "None")
    {
        console.log("Error_None\n");
    }
    else
    {
        var cur_time = event.ts;
        var cur_Temp= Number(event.Temperature);
        var cur_Hum=Number(event.Humidity);
        console.log("Point1\n");

        var result="";

        var last_params =
        {
            QueueUrl: LAST_QUEUE,
            MaxNumberOfMessages: 1
        };

        sqs.receiveMessage(last_params, function(err, data)
        {
            if (err)
            {
                console.log("Error_LastQueue_Receive", err);
            }
            else
            {
                // default 100,0,0,100,0,0,0
                result= data.Messages[0].Body;
                var handle = data.Messages[0].ReceiptHandle;

                var deleteParams =
                {
                    QueueUrl: LAST_QUEUE,
                    ReceiptHandle: handle
                };
                sqs.deleteMessage(deleteParams, function(err, data)
                {
                    if (err)
                    {
                        console.log("Delete Error", err);
                    }
                    else
                    {
                        console.log("Message Deleted", data);
                    }
                }); // end of deleteMessage


                console.log("Succed ", data);
                console.log("Got last Q",result);
                var array = result.split(",");
                console.log("Array ",array);
                        // get minimum
                var minTemp;
                if(cur_Temp<Number(array[0])) minTemp=cur_Temp;
                else minTemp=Number(array[0]);

                var maxTemp;
                if(cur_Temp>Number(array[2])) maxTemp=cur_Temp;
                else maxTemp=Number(array[2]);

                var minHum;
                if(cur_Hum<Number(array[3])) minHum=cur_Hum;
                else minHum=Number(array[3]);

                var maxHum;
                if(cur_Hum>Number(array[5])) maxHum=cur_Hum;
                else maxHum=Number(array[5]);

                //get averages by increasing the count from the last value queue
                //and averaging the current value with it
                var lastCount=Number(array[6]);
                var count=Number(array[6])+1;
                var avgTemp= ((lastCount*Number(array[1]))+cur_Temp)/count;
                var avgHum=((lastCount*Number(array[4]))+cur_Hum)/count;

                var lastQmessage = minTemp+","+avgTemp+","+maxTemp+","+minHum+","+avgHum+","+maxHum+","+count;
                var curQmessage = cur_time+","+ cur_Temp+","+minTemp+","+avgTemp+","+maxTemp+","+cur_Hum+","+minHum+","+avgHum+","+maxHum;
                    // Write the string to the console
                console.log("last Queue ",lastQmessage);
                console.log("End result ",curQmessage);

                var lastQparams =
                {
                    MessageBody: lastQmessage,
                    QueueUrl: LAST_QUEUE,
                    MessageGroupId: "MessageGroup1"
                };

                sqs.sendMessage(lastQparams, function(err, data)
                {
                    if (err)
                    {
                        console.log("Error_SendLastQueue", err);
                    }
                    else
                    {
                        console.log("Success", data.MessageId);
                    }
                });

                var curQparams =
                {
                    MessageBody: curQmessage,
                    QueueUrl: QUEUE_URL,
                    MessageGroupId: "MessageGroup2"
                };

                sqs.sendMessage(curQparams, function(err, data)
                {
                    if (err)
                    {
                        console.log("Error_Queue", err);
                    }
                    else
                    {
                        console.log("Success", data.MessageID);
                    }
                });
            }
        });
    }
    //const response = {
    //    statusCode: 200,
    //    body: JSON.stringify('Hello from Lambda!'),
    //};
    //return response;
};