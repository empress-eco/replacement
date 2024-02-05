frappe.ui.form.on('Replacement', {
    before_save: function(frm) {
        frappe.call({
            method: 'replacement.replacement.test.create_reverse_replacement_doc',
            args: {
                item: frm.doc.item,
                replacement_item: frm.doc.replacement_item
            },
            callback: function(r) {
                if (!r.exc) {
                    // Handle the response if needed
                }
            }
        });
    },
    
    refresh: function(frm) {
        // Add custom button to the toolbar
        frm.add_custom_button(__('Search Item'), function() {
            frappe.prompt([
                {
                    'fieldname': 'item',
                    'fieldtype': 'Link',
                    'label': __('Item'),
                    'options': 'Item',
                    'reqd': 1,
                },
            ], function(values){
                frappe.call({
                    method: 'replacement.replacement.button.search_items_and_replacements',
                    args: {
                        item_name: values.item // Ensure the correct argument name
                    },
                    callback: function(r) {
                        if (!r.exc) {
                            // Create a table to display search results
                            var table = '<table class="table table-bordered">';
                            table += '<thead><tr><th>Replacements</th></tr></thead>';
                            table += '<tbody>';
                            
                            // Add a row for the searched item
                            table += '<tr><td>';
                            
                            // Iterate through replacements and add a row for each
                            r.message.combined_list.forEach(function(replacement) {
                                table += replacement + '<br>';
                            });
                            
                            table += '</td></tr>';
                            
                            table += '</tbody></table>';
                            
                            // Display the table in a dialog
                            frappe.msgprint({
                                message: table,
                                title: __('Search Results'),
                                wide: true
                            });
                        }
                    }
                });
            }, __('Search Item'), 'View');
        });
    }
});




