import json, re

display_fix = {
    "hai mươi xăng-ti-mét": "20cm",
    "bảy sắc cầu vồng": "7 sắc cầu vồng",
    "vài xăng-ti-mét": "vài cm",
    "chín ngàn chín trăm chín mươi chín": "9.999",
    "một ngàn năm trăm": "1.500",
    "chín trăm chín mươi chín": "999",
    "ba phần ngàn giây": "0,003s",
    "mười ngàn bốn trăm g": "10.400g",
    "hai mươi hai ly": "22 ly",
    "một phần mười giây": "0,1s",
    "ba mươi lần": "30 lần",
    "tám mươi lăm": "85",
    "mười sáu loại": "16 loại",
    "chín g": "9g",
    "một ngàn lần": "1.000 lần",
    "bốn ngàn bảy trăm độ C": "4.700°C",
    "tháng tư năm 1998": "tháng 4 năm 1998",
    "mười xăng-ti-mét": "10cm",
    "sáu mi-li-mét": "6mm",
    "ba loại": "3 loại",
    "ba trăm sáu mươi độ": "360°",
    "ba chiều": "3D",
    "Mơn-ti-xơ": "Mantis",
    "S-cu-la-rút": "Scyllarus",
    "Bu-li-găng": "Bouligand",
    "Cáp-vi-tây-sơn": "Cavitation",
    "Xô-nô-lu-mi-nét-xen": "Sonoluminescence",
    "A-T-K": "ATK",
    "S-P-D": "SPD",
    "D-E-F": "DEF",
    "U-V": "UV"
}

def script_tokens(text: str, display: dict) -> list[str]:
    text = re.sub(r"\[[a-zA-Z0-9_\-]+\]", " ", text)
    for k in sorted(display.keys(), key=len, reverse=True):
        if " " in k or "-" in k:
            text = text.replace(k, display[k])
    out = []
    for t in text.split():
        core = t.strip(".,!?:;\"'()")
        if core in display:
            t = t.replace(core, display[core])
        out.append(t)
    return out

ep = json.load(open('projects/tap-07-tom-tit/episode.json', encoding='utf-8'))
for sc in ep['longform']['scenes']:
    txt = " ".join(sc['parts'])
    toks = script_tokens(txt, display_fix)
    print(f"{sc['id']}: {len(toks)} tokens")
    # check for remaining spelled out words
    for bad in ["hai mươi", "xăng-ti-mét", "chín ngàn", "bốn ngàn bảy trăm", "mười ngàn"]:
        if any(bad in t for t in toks):
            print("  FOUND BAD:", bad)
print("Tokens preview scene02:", [t for t in script_tokens(" ".join(ep['longform']['scenes'][1]['parts']), display_fix) if any(c.isdigit() or c in "ATKSPDDEF" for c in t)])
