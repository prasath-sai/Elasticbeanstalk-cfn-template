# Elasticbeanstalk-cfn-template
template for elasticbeanstalk application creation
-- template.yaml creates infrastructure for all the required resources
-- ecc-app folders helps to run flaskapp application in beanstalk environment
---------------------------------------------------------------------------
-- load folder will just help helps us to stress the application
  -- provided hyperlinks to test the load also with load and aws cli commands for reference 
----------------------------------------------------------------------------
How it Works:
  -- As per the documentation templates provision EB, ASG, ELB with all the specified requirements, when stress is high for 5 mins ASG will add another instance similarly scale-out works as per policy.
      we can check the configuration after provisiong the resouces.
--------------------------------------------------------------------------
Tested:
  -- I have tested it working as per requirement.
