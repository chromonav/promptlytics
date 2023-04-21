import frappe

# API mehtod: api/method/promptlytics.api.track
@frappe.whitelist()
def track(**kwargs):
    try:
        kwargs.pop('api_key')
        kwargs.pop('cmd')
        prompt = kwargs
        response = kwargs.get('request_response')
        doc = frappe.new_doc('Prompt Log')
        doc.prompt = prompt
        doc.response = response
        doc.insert()
        return "Success"
    except Exception as e:
        print(e)
        return "Error"

# API mehtod: api/method/promptlytics.api.library_get_prompt_template
@frappe.whitelist() 
def library_get_prompt_template(**kwargs):
    pass


# API mehtod: api/method/promptlytics.api.library_publish_prompt_template
@frappe.whitelist() 
def library_publish_prompt_template(**kwargs):
    pass


# API mehtod: api/method/promptlytics.api.library_track_prompt
@frappe.whitelist() 
def library_track_prompt(**kwargs):
    pass


# API mehtod: api/method/promptlytics.api.library_track_metadata
@frappe.whitelist() 
def library_track_metadata(**kwargs):
    pass


# API mehtod: api/method/promptlytics.api.library_track_score
@frappe.whitelist() 
def library_track_score(**kwargs):
    pass
