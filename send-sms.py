from sinch import SinchClient

sinch_client = SinchClient(
    key_id="7e13066c-5498-4434-beb9-65e6c815dc87",
    key_secret="67Nnjs9XalfOBTGXx_EBnXUDuQ",
    project_id="9c4d9afd-f7b2-4f27-99da-f0ee939e3962"
)

send_batch_response = sinch_client.sms.batches.send(
    body="Internet Gas Gauge in AZ report delivered to email",
    to=["19282509248"],
    from_="12085813506",
    delivery_report="none"
)

print(send_batch_response)
