import sys
sys.path.insert(1, "../../source")

from utility.loggers import (
	TextLoggingKind, JsonLoggingKind, EmailLoggingKind
)

current = "email"

if current == "text":
	print(TextLoggingKind("/home/admin/Robot-Informant/tests/logging/logs.txt").logData("segmentation fault", "stack overflow"))

elif current == "text_json":
	print(JsonLoggingKind("./logs.json").logData({
		"name": "Grigory",
		"password": "1234567"
	},
	{
		"name": "Matvey",
		"password": "67676"
	}))
	
elif current == "email":
	print(EmailLoggingKind("therobotadolf@gmail.com", "egorhacker05@gmail.com").logData("Segmentation fault", "Stack overflow"))
