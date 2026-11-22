"""JSON-LD for <script type="application/ld+json"> blocks."""

import json

from django.utils.safestring import mark_safe

# Escape characters that could close the <script> tag early.
_ESCAPES = {ord("<"): "\\u003C", ord(">"): "\\u003E", ord("&"): "\\u0026"}


def json_ld(data):
    return mark_safe(json.dumps(data, ensure_ascii=False).translate(_ESCAPES))
