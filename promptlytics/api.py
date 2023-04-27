import json
import frappe

# API method: api/method/promptlytics.api.track
@frappe.whitelist()
def track(**kwargs):
    try:
        kwargs.pop('api_key')
        kwargs.pop('cmd')
        doc = frappe.new_doc('Prompt Log')
        doc.function_name = kwargs.get("function_name")
        doc.provider_type = kwargs.get("provider_type")
        model_kwargs = kwargs.get("kwargs")
        doc.model = model_kwargs.get("model")
        doc.request_timeout = model_kwargs.get("request_timeout")
        doc.max_tokens = model_kwargs.get("max_tokens")
        doc.stream = model_kwargs.get("stream")
        doc.temperature = model_kwargs.get("temperature")
        doc.group = kwargs.get("tags")
        doc.prompt = json.dumps(kwargs, indent=4)
        doc.response = json.dumps(kwargs.get('request_response'), indent=4)
        doc.insert()
        return "Success"
    except Exception as e:
        print(e)
        return "Error"

# API method: api/method/promptlytics.api.library_get_prompt_template
@frappe.whitelist() 
def library_get_prompt_template(**kwargs):
    prompt_name = kwargs.get('prompt_name')
    prompt = frappe.get_doc('Prompt', prompt_name)
    return {"prompt_name":prompt_name, "prompt_template": prompt.content}


# API method: api/method/promptlytics.api.library_publish_prompt_template
@frappe.whitelist() 
def library_publish_prompt_template(**kwargs):
    try:
        prompt_name = kwargs.get('prompt_name')
        doc = frappe.new_doc('Prompt')
        doc.title = prompt_name
        doc.content = kwargs.get('prompt_template')
        doc.insert()
        return "Success"
    except Exception as e:
        print(e)
        return "Error"


# API method: api/method/promptlytics.api.library_track_prompt
@frappe.whitelist() 
def library_track_prompt(**kwargs):
    pass


# API method: api/method/promptlytics.api.library_track_metadata
@frappe.whitelist() 
def library_track_metadata(**kwargs):
    pass


# API method: api/method/promptlytics.api.library_track_score
@frappe.whitelist() 
def library_track_score(**kwargs):
    pass
