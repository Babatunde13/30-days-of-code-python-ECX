import re


def email_validator(string):
  '''this function is to validate an email input
  input is a string containing a said email
  process is a regex function testing for all conditions
  output is a valid or invalid response to whether the mail is correct or not
  '''
  pattern= r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
  if(re.search(pattern,email)):  
      return "Valid Email" 
  else:  
      return "Invalid Email"
  

email=input('input email')
email_validator(email)
