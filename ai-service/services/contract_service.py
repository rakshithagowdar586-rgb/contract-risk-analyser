from services.ai_service_client import AiServiceClient
import threading

class ContractService:

    def __init__(self):
        self.ai_client = AiServiceClient()

    # MAIN CREATE METHOD
    def create_contract(self, contract_data):

        # 1. Save contract (mock or DB later)
        contract = {
            "id": 1,
            "description": contract_data["description"],
            "aiAnalysis": None
        }

        # 2. Run AI in background
        thread = threading.Thread(
            target=self.process_ai,
            args=(contract,)
        )
        thread.start()

        return contract

    # ASYNC AI PROCESS
    def process_ai(self, contract):

        result = self.ai_client.analyze_contract(
            contract["description"]
        )

        # 3. SAFE HANDLING
        if result is None:
            contract["aiAnalysis"] = "AI failed or unavailable"
        else:
            contract["aiAnalysis"] = result

        print("AI Updated Contract:", contract)