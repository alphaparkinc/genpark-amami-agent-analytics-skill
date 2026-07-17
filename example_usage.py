from client import AmamiAgentAnalyticsClient
client = AmamiAgentAnalyticsClient()
print(client.evaluate_session(2500, 1200, True))