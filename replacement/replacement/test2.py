import frappe
# frappe.init(site="husna.erpgulf.com")
# frappe.connect()

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
    workspace.save()

    #     create_workspace_shortcut('Replacement Shortcut', 1, 'Replacement', 'Replacement', workspace.name, 'Workspace')
    #     create_workspace_shortcut('Search Item Button Shortcut', 2, 'Search Item Button', 'Replacement',workspace.name, 'Workspace')
    #     create_workspace_shortcut('Item Shortcut', 3, 'Item', 'Item', workspace.name, 'Workspace')

    # except frappe.exceptions.UniqueValidationError:
    #     print('Replacement Doc "{0}" already exists.'.format(workspace.name))
    # except frappe.exceptions.ValidationError as e:
    #     print('Validation Error: {0}'.format(str(e)))

# def create_workspace_shortcut(title, idx, label, link_to, parent, parenttype):
#     shortcut_doc = frappe.new_doc('Workspace Shortcut')
#     shortcut_doc.update({
#         'title': title,
#         'idx': idx,
#         'label': label,
#         'link_to': link_to,
#         'parent': parent,
#         'parenttype': parenttype,
#     })

#     try:
#         shortcut_doc.insert(ignore_permissions=True)
#         print('Workspace Shortcut "{0}" created successfully.'.format(shortcut_doc.name))
#     except frappe.exceptions.UniqueValidationError:
#         print('Workspace Shortcut "{0}" already exists.'.format(shortcut_doc.name))
#     except frappe.exceptions.ValidationError as e:
#         print('Validation Error: {0}'.format(str(e)))



