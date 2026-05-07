from demo_records import demo_contracts
from services.groq_service import analyze_contract_safe

print("Running demo analysis...\n")

for idx, contract in enumerate(demo_contracts, start=1):

    print(f"Record {idx}")

    result = analyze_contract_safe(contract["text"])

    print(result)
    print("-" * 50)

print("All demo records processed successfully")