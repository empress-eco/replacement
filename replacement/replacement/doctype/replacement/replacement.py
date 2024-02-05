# Copyright (c) 2024, ERPGulf and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class Replacement(Document):
# 	pass

import frappe
@frappe.whitelist(allow_guest=True)
def create_replacement_doc():
    workspace = frappe.get_doc({
        "doctype":"Workspace",
        'title': 'Replacement',
        'sequence_id': 25,
        'parent_page':'Home' ,
        'module': 'Replacement',
        'icon': 'change',
        'restrict_to_domain': None,
        'hide_custom': False,
        'public': True,
        'label': 'Replacement',
    })
    workspace.insert(ignore_permissions=True)
    workspace.submit()