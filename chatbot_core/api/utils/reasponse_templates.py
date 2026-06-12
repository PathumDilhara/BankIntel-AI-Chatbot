response_templates = {

    # ---------------- CARD ----------------
    "card": {
        "message": "I can help you with your card. What would you like to do?",
        "options": [
            {"label": "Activate Card", "action": "activate_card"},
            {"label": "Order New Card", "action": "order_card"},
            {"label": "Card Delivery Info", "action": "card_delivery"}
        ]
    },

    # ---------------- CARD ISSUES ----------------
    "card_issue": {
        "message": "It looks like you're having an issue with your card. Let's fix it.",
        "options": [
            {"label": "Block Card", "action": "block_card"},
            {"label": "Report Lost/Stolen", "action": "lost_card"},
            {"label": "Card Not Working", "action": "card_not_working"}
        ]
    },

    # ---------------- TRANSFER ----------------
    "transfer": {
        "message": "I can help with your transfer. What do you need?",
        "options": [
            {"label": "Send Money", "action": "send_money"},
            {"label": "Check Status", "action": "check_transfer"},
            {"label": "Transfer History", "action": "transfer_history"}
        ]
    },

    # ---------------- TRANSFER ISSUES ----------------
    "transfer_issue": {
        "message": "I understand you're having a transfer issue. Let's sort it out.",
        "options": [
            {"label": "Failed Transfer", "action": "failed_transfer"},
            {"label": "Not Received", "action": "missing_transfer"},
            {"label": "Cancel Transfer", "action": "cancel_transfer"}
        ]
    },

    # ---------------- TOPUP ----------------
    "topup": {
        "message": "I can help you add money to your account.",
        "options": [
            {"label": "Top Up Now", "action": "topup_now"},
            {"label": "Top Up Methods", "action": "topup_methods"}
        ]
    },

    # ---------------- TOPUP ISSUES ----------------
    "topup_issue": {
        "message": "Your top-up didn't go through. Let's check what happened.",
        "options": [
            {"label": "Failed Top Up", "action": "topup_failed"},
            {"label": "Top Up Limits", "action": "topup_limits"},
            {"label": "Refund Status", "action": "topup_refund"}
        ]
    },

    # ---------------- BALANCE ----------------
    "balance": {
        "message": "I can help you with your balance and transactions.",
        "options": [
            {"label": "Check Balance", "action": "check_balance"},
            {"label": "Recent Transactions", "action": "transactions"},
            {"label": "Balance Not Updated", "action": "balance_issue"}
        ]
    },

    # ---------------- PAYMENT ----------------
    "payment": {
        "message": "Let's look into your payment issue.",
        "options": [
            {"label": "Dispute Payment", "action": "dispute_payment"},
            {"label": "Check Charges", "action": "check_charges"},
            {"label": "Payment History", "action": "payment_history"}
        ]
    },

    # ---------------- SECURITY ----------------
    "security": {
        "message": "I noticed a security-related request. I can help.",
        "options": [
            {"label": "Change PIN", "action": "change_pin"},
            {"label": "Blocked Card Help", "action": "blocked_card"},
            {"label": "Contactless Issue", "action": "contactless_issue"}
        ]
    },

    # ---------------- VERIFICATION ----------------
    "verification": {
        "message": "I can help you with identity verification.",
        "options": [
            {"label": "Verify Identity", "action": "verify_identity"},
            {"label": "Why Required?", "action": "why_verify"},
            {"label": "Source of Funds", "action": "verify_funds"}
        ]
    },

    # ---------------- ACCOUNT ----------------
    "account": {
        "message": "I can help you manage your account settings.",
        "options": [
            {"label": "Update Details", "action": "edit_details"},
            {"label": "Forgot PIN", "action": "forgot_pin"},
            {"label": "Close Account", "action": "close_account"}
        ]
    },

    # ---------------- CASH / ATM ----------------
    "cash": {
        "message": "I can help with ATM and cash withdrawal issues.",
        "options": [
            {"label": "ATM Issue", "action": "atm_issue"},
            {"label": "Withdrawal Problem", "action": "withdrawal_issue"}
        ]
    },

    # ---------------- EXCHANGE ----------------
    "exchange": {
        "message": "I can help with currency exchange services.",
        "options": [
            {"label": "Check Rates", "action": "exchange_rate"},
            {"label": "Exchange Charges", "action": "exchange_fee"}
        ]
    },

    # ---------------- LIMITS ----------------
    "limits": {
        "message": "I can help you understand your account limits.",
        "options": [
            {"label": "Top Up Limit", "action": "topup_limits"},
            {"label": "Card Limit", "action": "card_limits"}
        ]
    },

    # ---------------- INFO ----------------
    "info": {
        "message": "Here’s some information you might need.",
        "options": [
            {"label": "Supported Cards", "action": "supported_cards"},
            {"label": "Country Support", "action": "country_support"}
        ]
    },

    # ---------------- DEFAULT ----------------
    "default": {
        "message": "I’m here to help. What do you need assistance with?",
        "options": [
            {"label": "Talk to Support", "action": "support"}
        ]
    }
}