from twilio.rest import Client
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_msg():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hey Raushan, you are best!!!',
        to='whatsapp:+919882552098'
    )
    print(message.sid)
    # target_numbers = [9635056109,9748223207,9882552098]
    # for target_number in target_numbers:
    #     if target_number == 9635056109:
    #         message = client.messages.create(
    #             from_='whatsapp:+14155238886',
    #             body='This is from Raushan, kya be Buddha Gandu!!!',
    #             to='whatsapp:+91' + str(target_number)
    #         )
    #         print(message.sid)
    #     elif target_number == 9748223207:
    #         message = client.messages.create(
    #             from_='whatsapp:+14155238886',
    #             body='This is from Raushan, kya be wazid Gandu!!!',
    #             to='whatsapp:+91' + str(target_number)
    #         )
    #         print(message.sid)
    #     elif target_number == 9882552098:
    #         message = client.messages.create(
    #             from_='whatsapp:+14155238886',
    #             body='Hey Raushan, you are best!!!',
    #             to='whatsapp:+91' + str(target_number)
    #         )
    #         print(message.sid)



if __name__ == '__main__':
    send_msg()
