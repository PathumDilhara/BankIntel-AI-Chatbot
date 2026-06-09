response_templates = {

    "card": {
        "message": "I can help with your card. What would you like to do?",
        "options": [
            {"label": "Block Card", "action": "block_card"},
            {"label": "Report Issue", "action": "card_support"},
            {"label": "Order New Card", "action": "new_card"}
        ]
    },

    "transfer": {
        "message": "Let's sort out your transfer. Choose an option below.",
        "options": [
            {"label": "Check Status", "action": "check_transfer"},
            {"label": "Cancel Transfer", "action": "cancel_transfer"},
            {"label": "Report Missing", "action": "missing_transfer"}
        ]
    },

    "topup": {
        "message": "Need help with a top-up?",
        "options": [
            {"label": "Top-up Failed", "action": "topup_failed"},
            {"label": "Top-up Limits", "action": "topup_limits"}
        ]
    },

    "balance": {
        "message": "I can help with your balance or recent transactions.",
        "options": [
            {"label": "Check Balance", "action": "check_balance"},
            {"label": "Transaction Issue", "action": "txn_issue"}
        ]
    },

    "payment": {
        "message": "Let's take a look at your payment issue.",
        "options": [
            {"label": "Dispute Payment", "action": "dispute_payment"},
            {"label": "Check Charges", "action": "check_charges"}
        ]
    },

    "verification": {
        "message": "I can help with account verification",
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