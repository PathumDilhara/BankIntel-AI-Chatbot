response_templates = {

    "card": {
        "message": "This is a card-related issue. What would you like to do?",
        "options": [
            {"label": "Block Card", "action": "block_card"},
            {"label": "Report Issue", "action": "card_support"},
            {"label": "Order New Card", "action": "new_card"}
        ]
    },

    "transfer": {
        "message": "Transfer issue detected. Choose an option:",
        "options": [
            {"label": "Check Status", "action": "check_transfer"},
            {"label": "Cancel Transfer", "action": "cancel_transfer"},
            {"label": "Report Missing", "action": "missing_transfer"}
        ]
    },

    "topup": {
        "message": "Top-up related help options:",
        "options": [
            {"label": "Top-up Failed", "action": "topup_failed"},
            {"label": "Top-up Limits", "action": "topup_limits"}
        ]
    },

    "balance": {
        "message": "Balance issue detected. What do you need?",
        "options": [
            {"label": "Check Balance", "action": "check_balance"},
            {"label": "Transaction Issue", "action": "txn_issue"}
        ]
    },

    "payment": {
        "message": "Payment-related issue. Choose one:",
        "options": [
            {"label": "Dispute Payment", "action": "dispute_payment"},
            {"label": "Check Charges", "action": "check_charges"}
        ]
    },

    "verification": {
        "message": "Identity verification help:",
        "options": [
            {"label": "Verify Identity", "action": "verify_identity"},
            {"label": "Why Needed?", "action": "why_verify"}
        ]
    },

    "default": {
        "message": "How can I help you today?",
        "options": [
            {"label": "Talk to Support", "action": "support"}
        ]
    }
}