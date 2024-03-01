from openai import OpenAI

client = OpenAI(api_key="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")

user_input = input("Enter the incident: ")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Work as a assistant for a victim who has experienced a crime. Refer to the numbers in the table below, the user will tell you their complaint and you have to suggest the best number the user should call for their situation. You have to take the user's complaint and suggest the best number to call to get help. Give the output in the following format, Department Name: Phone number. Don't print anything else. ((PCR, 112), (Eyes and Ears, 14547), (Women in distress, 1091), (Special Cell (North-Eastern States), 1093), (Missing Persons, (1094, 23241210)), (Traffic, (1095, 25844444)), (Vigilance (Anti Corruption Helpline), 1064), (For uploading Audio and Video Clips, 9910641064), (Railways, 1512), (Senior Citizen, 1291), (Cyber Complaints, 1930))"},
        {"role": "user", "content": f"Please provide the number of the concerned department'{user_input}'"},
    ]
)

res = response.choices[0].message.content

print(res)