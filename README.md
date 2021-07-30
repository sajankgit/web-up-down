# web-up-down

### Problem

I have a web application hosted in AWS. The server is behind AWS application load balancer.

It needs to run only during office hours and other times it should redirect me to another static page showing good night.

### Solution

Create two lamda functions.

- goodnight.py
    
    This script will modify the loadbalancer listener to the target group where static page is part of.
    
- goodmorning.py

    This script will modify the loadbalancer listener to web applicaion target group.
    
    
Schedule goodnight.py lamda script to run when office hour ends ( eg: 9PM ). So static page will be shown from 9PM.
Schedule goodmorining.py lamda script to execute when office hour starts (eg 9AM). So people will see your webapplication when they reach to office.

Additionaly you can schedule your autoscaling to shut down webapplication during off hours to save some bucks
