import frappe

# frappe.init(site="husna.erpgulf.com")
# frappe.connect()

@frappe.whitelist(allow_guest=True)
def search_items_and_replacements(item_name, all_replacements=None):
    if all_replacements is None:
        all_replacements = set()

    replacements = frappe.get_all('Replacement', filters={'item': item_name}, fields=['replacement_item'])
    replacements = {replacement.get('replacement_item') for replacement in replacements}

    for replacement in replacements:
        if replacement not in all_replacements:
            all_replacements.add(replacement)
            search_items_and_replacements(replacement, all_replacements)

    return {
        'combined_list':(all_replacements - {item_name})  # Exclude the initial search item
    }
