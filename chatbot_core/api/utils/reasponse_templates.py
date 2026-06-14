response_templates = {

    # ---------------- CARD ----------------
    "card": [
            {"label": "Activate Card", "action": "activate_card"},
            {"label": "Order New Card", "action": "order_card"},
            {"label": "Card Delivery Info", "action": "card_delivery"}
        ],

    # ---------------- CARD ISSUES ----------------
    "card_issue": [
            {"label": "Block Card", "action": "block_card"},
            {"label": "Report Lost/Stolen", "action": "lost_card"},
            {"label": "Card Not Working", "action": "card_not_working"}
        ],

    # ---------------- TRANSFER ----------------
    "transfer": [
            {"label": "Send Money", "action": "send_money"},
            {"label": "Check Status", "action": "check_transfer"},
            {"label": "Transfer History", "action": "transfer_history"}
        ],

    # ---------------- TRANSFER ISSUES ----------------
    "transfer_issue": [
            {"label": "Failed Transfer", "action": "failed_transfer"},
            {"label": "Not Received", "action": "missing_transfer"},
            {"label": "Cancel Transfer", "action": "cancel_transfer"}
        ],

    # ---------------- TOPUP ----------------
    "topup": [
            {"label": "Top Up Now", "action": "topup_now"},
            {"label": "Top Up Methods", "action": "topup_methods"}
        ],

    # ---------------- TOPUP ISSUES ----------------
    "topup_issue": [
            {"label": "Failed Top Up", "action": "topup_failed"},
            {"label": "Top Up Limits", "action": "topup_limits"},
            {"label": "Refund Status", "action": "topup_refund"}
        ],

    # ---------------- BALANCE ----------------
    "balance": [
            {"label": "Check Balance", "action": "check_balance"},
            {"label": "Recent Transactions", "action": "transactions"},
            {"label": "Balance Not Updated", "action": "balance_issue"}
        ],

    # ---------------- PAYMENT ----------------
    "payment": [
            {"label": "Dispute Payment", "action": "dispute_payment"},
            {"label": "Check Charges", "action": "check_charges"},
            {"label": "Payment History", "action": "payment_history"}
        ],

    # ---------------- SECURITY ----------------
    "security": [
            {"label": "Change PIN", "action": "change_pin"},
            {"label": "Blocked Card Help", "action": "blocked_card"},
            {"label": "Contactless Issue", "action": "contactless_issue"}
        ],

    # ---------------- VERIFICATION ----------------
    "verification": [
            {"label": "Verify Identity", "action": "verify_identity"},
            {"label": "Why Required?", "action": "why_verify"},
            {"label": "Source of Funds", "action": "verify_funds"}
        ],

    # ---------------- ACCOUNT ----------------
    "account": [
            {"label": "Update Details", "action": "edit_details"},
            {"label": "Forgot PIN", "action": "forgot_pin"},
            {"label": "Close Account", "action": "close_account"}
        ],

    # ---------------- CASH / ATM ----------------
    "cash": [
            {"label": "ATM Issue", "action": "atm_issue"},
            {"label": "Withdrawal Problem", "action": "withdrawal_issue"}
        ],

    # ---------------- EXCHANGE ----------------
    "exchange": [
            {"label": "Check Rates", "action": "exchange_rate"},
            {"label": "Exchange Charges", "action": "exchange_fee"}
        ],

    # ---------------- LIMITS ----------------
    "limits": [
            {"label": "Top Up Limit", "action": "topup_limits"},
            {"label": "Card Limit", "action": "card_limits"}
        ],

    # ---------------- INFO ----------------
    "info": [
            {"label": "Supported Cards", "action": "supported_cards"},
            {"label": "Country Support", "action": "country_support"}
        ],

    # ---------------- DEFAULT ----------------
    "unknown":  []
}