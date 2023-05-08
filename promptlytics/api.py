import json
import frappe
from datetime import datetime

# API method: api/method/promptlytics.api.track
@frappe.whitelist()
def track(**kwargs):
    try:
        kwargs.pop('cmd')
        doc = frappe.new_doc('Prompt Log')
        doc.function_name = kwargs.get("function_name")
        doc.provider_type = kwargs.get("provider_type")
        args = kwargs.get('args')
        doc.prompt_role = args[0].get("role")
        doc.prompt_content = args[0].get("content")
        model_kwargs = kwargs.get("kwargs")
        doc.model = model_kwargs.get("model")
        doc.request_timeout = model_kwargs.get("request_timeout")
        doc.max_tokens = model_kwargs.get("max_tokens")
        doc.stream = model_kwargs.get("stream")
        doc.temperature = model_kwargs.get("temperature")
        doc.group = kwargs.get("tags")
        doc.prompt = json.dumps(kwargs, indent=4)
        response = kwargs.get('request_response')
        doc.response = json.dumps(response, indent=4)
        doc.response_role = response[0].get("role")
        doc.response_content = response[0].get("content")

        request_start_time = float(kwargs["request_start_time"])
        request_end_time = float(kwargs["request_end_time"])
        doc.request_start_time = datetime.fromtimestamp(request_start_time)
        doc.request_end_time = datetime.fromtimestamp(request_end_time)
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
