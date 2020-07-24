# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Arelux",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "sale",
        "account",
        "mail",
        "survey",
        "crm_claim"
    ],
    "data": [
        "views/account_invoice_view.xml",
        "views/resources.xml",
    ],
    "installable": True
}