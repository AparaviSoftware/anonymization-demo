from IPython.display import display, Markdown
import json, re

def _fix_mojibake(s: str) -> str:
    # Best fix for â–ˆ → █ (bytes E2 96 88 mis-decoded as cp1252)
    for enc in ("cp1252", "latin-1"):
        try:
            return s.encode(enc).decode("utf-8")
        except Exception:
            pass
    return re.sub(r"â[–-]ˆ", "█", s)

def _extract_objects(res):
    if isinstance(res, list):
        objs = []
        for item in res:
            objs.extend(_extract_objects(item))
        return objs
    if isinstance(res, dict):
        if "objects" in res and isinstance(res["objects"], dict):
            return list(res["objects"].values())
        if "data" in res:
            return _extract_objects(res["data"])
        if "text" in res or (isinstance(res.get("data"), dict) and "text" in res["data"]):
            return [res]
    return []

def render_aparavi_result(res, show_raw=False, max_chars=100000):
    objs = _extract_objects(res)
    if not objs:
        display(Markdown("**No objects to display.**"))
        if show_raw:
            display(Markdown(f"```json\n{json.dumps(res, indent=2)[:max_chars]}\n```"))
        return

    for i, obj in enumerate(objs, 1):
        name = obj.get("name") or f"Object {i}"
        path = obj.get("path", "")
        display(Markdown(f"### {i}. {name}"))
        if path:
            display(Markdown(f"`{path}`"))

        texts = obj.get("text") or (obj.get("data", {}) or {}).get("text")
        if texts:
            if isinstance(texts, list):
                content = "\n\n".join(_fix_mojibake(t) for t in texts)
            else:
                content = _fix_mojibake(str(texts))
            display(Markdown(content))
        else:
            display(Markdown("_No text content available._"))

        if show_raw:
            display(Markdown("<details><summary>Raw object</summary>"))
            display(Markdown(f"```json\n{json.dumps(obj, indent=2)[:max_chars]}\n```"))
            display(Markdown("</details>"))