from sinch import SinchClient

sinch_client = SinchClient(
    key_id="YOUR_key_id",
    key_secret="YOUR_key_secret",
    project_id="YOUR_project_id"
)

send_batch_response = sinch_client.sms.batches.send(
    body="Internet Gas Gauge in AZ report delivered to email",
    to=["19282509248"],
    from_="12085813506",
    delivery_report="none"
)

print(send_batch_response)
