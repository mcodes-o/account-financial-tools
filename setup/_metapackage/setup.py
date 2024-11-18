import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-account-financial-tools",
    description="Meta package for oca-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_asset_batch_compute',
        'odoo12-addon-account_asset_management',
        'odoo12-addon-account_balance_line',
        'odoo12-addon-account_bank_statement_chatter',
        'odoo12-addon-account_cash_basis_group_base_line',
        'odoo12-addon-account_chart_update',
        'odoo12-addon-account_check_deposit',
        'odoo12-addon-account_clearance_plan',
        'odoo12-addon-account_coa_menu',
        'odoo12-addon-account_cost_center',
        'odoo12-addon-account_document_reversal',
        'odoo12-addon-account_fiscal_month',
        'odoo12-addon-account_fiscal_position_vat_check',
        'odoo12-addon-account_fiscal_year',
        'odoo12-addon-account_fiscal_year_auto_create',
        'odoo12-addon-account_group_menu',
        'odoo12-addon-account_invoice_constraint_chronology',
        'odoo12-addon-account_invoice_currency',
        'odoo12-addon-account_journal_lock_date',
        'odoo12-addon-account_loan',
        'odoo12-addon-account_lock_date_update',
        'odoo12-addon-account_lock_to_date',
        'odoo12-addon-account_menu',
        'odoo12-addon-account_move_batch_validate',
        'odoo12-addon-account_move_budget',
        'odoo12-addon-account_move_chatter',
        'odoo12-addon-account_move_fiscal_month',
        'odoo12-addon-account_move_fiscal_year',
        'odoo12-addon-account_move_line_drilldown',
        'odoo12-addon-account_move_line_partner_country',
        'odoo12-addon-account_move_line_purchase_info',
        'odoo12-addon-account_move_line_tax_editable',
        'odoo12-addon-account_move_post_date_user',
        'odoo12-addon-account_move_template',
        'odoo12-addon-account_netting',
        'odoo12-addon-account_partner_required',
        'odoo12-addon-account_payment_netting',
        'odoo12-addon-account_permanent_lock_move',
        'odoo12-addon-account_renumber',
        'odoo12-addon-account_spread_cost_revenue',
        'odoo12-addon-account_subsequence_fiscal_year',
        'odoo12-addon-account_tag_menu',
        'odoo12-addon-account_template_active',
        'odoo12-addon-account_type_menu',
        'odoo12-addon-account_voucher_print',
        'odoo12-addon-base_vat_optional_vies',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
