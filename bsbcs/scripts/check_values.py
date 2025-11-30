import os, django, json, re
os.environ.setdefault('DJANGO_SETTINGS_MODULE','bsbcs.settings')
django.setup()
from website.models import OrganizationalValue
vals = OrganizationalValue.objects.filter(value_type='value').order_by('order')
values_items = []
if vals.count() > 1:
    for v in vals:
        text = v.title or (v.description or '').strip()
        if text:
            values_items.append(text)
elif vals.count() == 1:
    single = vals.first()
    desc = (single.description or '').strip()
    if desc:
        parts = [p.strip() for p in re.split(r'[\r\n]+', desc) if p.strip()]
        if len(parts) == 1:
            parts = [p.strip() for p in re.split(r'[;\u2022,]+', desc) if p.strip()]
        values_items = parts
    else:
        if single.title:
            values_items = [single.title]
print(json.dumps({'count': len(vals), 'values_items': values_items}, ensure_ascii=False, indent=2))
