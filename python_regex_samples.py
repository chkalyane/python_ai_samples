import re

sampletext = "Please contact our sales team at 123-456-7890 or support at 987-654-3210. For international inquiries, try +1-555-123-4567. You can also reach John Doe at 1112223333 or Jane Smith at 4445556666. Our main office number is 9998887777, and for after-hours support, dial 1002003004. If you have any further questions, please call us at 0102030405. Alternatively, you can contact a different support line at 5678901234 or a sales representative at 6789012345."

# find phone numbers

pattern = '\d{10}'
result = re.findall(pattern, sampletext)
print(result)