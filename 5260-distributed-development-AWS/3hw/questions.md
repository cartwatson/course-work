# Step 8 - Questions

## Question 1

*Why is possible that Update and Delete Widget Requests may fail, even when you were running just one Consumer?*

It's possible that the requests are failing because of data propagation issues, it's possible that something is staged to be created on the AWS side and the delete request is processed before the data is actually propagated.

## Question 2

*How would this possible behavior impact the design of distributed applications that use queues?*

This could be an issue for distributed applications more so than just one consumer.  This is because the create request for an object may come before a delete request but the first machine gets the create and the second machine processes the delete request before the create request is through.  This would fail the delete request and create an object that isn't supposed to be there.
