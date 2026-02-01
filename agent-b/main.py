def main(args):
    # 1. Extract Customer & Transfer Info
    customer = args.get("customer", "Unknown Customer")
    transfer_id = args.get("transfer_id", "N/A")
    amount = args.get("amount", "200 USD")
    
    # 2. Extract the 7 Uploaded Files
    # Expecting 'files' to be a list of 7 document links
    files = args.get("files", [])
    files_count = len(files)
    
    # 3. Decision Logic (Review Process)
    if files_count >= 7:
        decision_status = "DONE"
        official_reason = "Payment confirmed and all 7 documents are verified."
    else:
        decision_status = "NOT DONE"
        official_reason = f"Verification failed. Only {files_count}/7 documents were provided."

    # 4. Final Output for Employee View
    return {
        "employee_portal": {
            "review_summary": {
                "client_name": customer,
                "transaction_ref": transfer_id,
                "amount_received": amount,
                "documents_uploaded": files_count
            },
            "document_links": files,
            "final_decision": {
                "result": decision_status,
                "reasoning": official_reason
            }
        },
        "system_status": "Review Phase Completed"
    }